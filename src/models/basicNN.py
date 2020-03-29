import numpy as np
import pandas as pd

import torch
import torch.nn as nn
from torch.autograd import grad
from torch.autograd import Variable

class AN(nn.Module):

    def __init__(self, in_size, hidden_sizes, out_size):

        super(AN, self).__init__()

        #Input layer
        self.input = nn.Linear(in_size, hidden_sizes[0])

        #Hidden layers
        self.hidden = nn.ModuleList()
        for k in range(len(hidden_sizes)-1):
            self.hidden.append(nn.Linear(hidden_sizes[k], hidden_sizes[k+1]))

        #Output layer
        self.output = nn.Linear(hidden_sizes[-1], out_size)

    def forward(self, input):

        #activation function after input layer
        input = torch.tanh(self.input(input))

        #going through each hidden layer
        for layer in self.hidden:
            input = torch.tanh(layer(input))

        #after output layer
        output = self.output(input)
        output = torch.sigmoid(output)

        return output

model = AN(7, [8, 8], 1)
csv_file = 'updated_data.csv'
dataframe = pd.read_csv(csv_file)
dataframe = dataframe.drop(dataframe.columns[0:2], axis=1)

training_data = np.array(dataframe)
testing_data = training_data[-100:]
training_data = training_data[:-100]

age_train = training_data[:,0]
age_test = testing_data[:,0]
death_train = training_data[:,1]
death_test = testing_data[:,1]
male_train = training_data[:,2]
male_test = testing_data[:,2]
female_train = training_data[:,3]
female_test = testing_data[:,3]
days_train = training_data[:,4]
days_test = testing_data[:,4]
rate_train = training_data[:,5]
rate_test = testing_data[:,5]
density_train = training_data[:,6]
density_test = testing_data[:,6]
risk_train = training_data[:,7]
risk_test = testing_data[:,7]

age_train = torch.Tensor(np.reshape(age_train, (age_train.size, 1)))
age_test = torch.Tensor(np.reshape(age_test, (age_test.size, 1)))
death_train = torch.Tensor(np.reshape(death_train, (death_train.size, 1)))
death_test = torch.Tensor(np.reshape(death_test, (death_test.size, 1)))
male_train = torch.Tensor(np.reshape(male_train, (male_train.size, 1)))
male_test = torch.Tensor(np.reshape(male_test, (male_test.size, 1)))
female_train = torch.Tensor(np.reshape(female_train, (female_train.size, 1)))
female_test = torch.Tensor(np.reshape(female_test, (female_test.size, 1)))
days_train = torch.Tensor(np.reshape(days_train, (days_train.size, 1)))
days_test = torch.Tensor(np.reshape(days_test, (days_test.size, 1)))
rate_train = torch.Tensor(np.reshape(rate_train, (rate_train.size, 1)))
rate_test = torch.Tensor(np.reshape(rate_test, (rate_test.size, 1)))
density_train = torch.Tensor(np.reshape(density_train, (density_train.size, 1)))
density_test = torch.Tensor(np.reshape(density_test, (density_test.size, 1)))
risk_train = torch.Tensor(np.reshape(risk_train, (risk_train.size, 1)))
risk_test = torch.Tensor(np.reshape(risk_test, (risk_test.size, 1)))

training_data = torch.cat((age_train, male_train, female_train, days_train, rate_train, density_train, risk_train), 1)
testing_data = torch.cat((age_test, male_test, female_test, days_test, rate_test, density_test, risk_test), 1)

#Parameters
num_of_epochs = int(100000)
learning_rate = 0.0005
error_threshold = 0.001
display_step = int(1000)

#defining loss function and optimizer for back propagation
MSE = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), learning_rate)

for epoch in range(num_of_epochs):

    cost1 = MSE(model(training_data), death_train)

    #Backward propagation and optimize
    optimizer.zero_grad()
    cost1.backward()
    optimizer.step()

    if cost1 < error_threshold:
        print(cost1)

    if epoch % display_step == 0:
        print('Epoch [{}/{}], Loss: {:.4f}'.format(epoch, num_of_epochs, cost1))

result = model(testing_data)

error = result - death_test
mean_absolute_error = ((result-death_test)).mean()
mean_squared_error = ((result-death_test)**2).mean()
error = list(error)
result = list(result)
count = 0
for i in range(len(result)):
    if result[i] > 0.9:
        result[i] = 1
    else:
        result[i] = 0
for i in range(len(result)):
    if result[i] != death_test[i]:
        count+=1
missed = 1 - (count/len(error))
print('Accuracy: {:.4f}'.format(missed))
print('Mean Absolute Error: {:.4f}'.format(mean_absolute_error))
print('Mean Squared Error: {:.4f}'.format(mean_squared_error))
torch.save(model.state_dict(), 'ANN.pkl')