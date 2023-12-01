import re

input = open("input.txt", "r").read()
regex = re.findall("[A-Z]{2}|\d{1,2}", input)

print(input)
print(regex)

class valve:
  def __init__(self, name, flowrate, *tunnels):
    self.name = name
    self.tunnels = tunnels
    self.flowrate = flowrate

