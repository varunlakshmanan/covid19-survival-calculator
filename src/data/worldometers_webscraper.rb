#!/usr/bin/ruby

require "httparty"
require "nokogiri"


url = "https://www.worldometers.info/coronavirus/country/us/"

response = HTTParty.get(url)
unless response.code == 200
  puts "HTTP #{response.code} Error"
end
document = Nokogiri::HTML.parse(response.body.to_s)

states = document.css("tr > td:first-child")[0...-3].map do |x|
  x.text.strip
end
cases = document.css("tr > td:nth-child(2)")[0...-3].map do |x|
  x.text.strip.gsub(",", "").to_i
end
deaths = document.css("tr > td:nth-child(4)")[0...-3].map do |x|
  x.text.strip.gsub(",", "").to_i
end

puts "{\"state\": #{states}, \"cases\": #{cases}, \"deaths\": #{deaths}}"
