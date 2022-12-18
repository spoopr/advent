input = repr(open("input.txt", "r").read())
score = input.count("X") + (input.count("Y")*2) + (input.count("Z")*3) + ((input.count("A X") + input.count("B Y") +input.count("C Z"))*3) + ((input.count("C X") + input.count("A Y") + input.count("B Z"))*6)
print(score)

better_input = [pair.split(" ") for pair in input.replace("'","").split(r"\n")]
print(better_input)
score = 0
cases = {"X":{"A":3,"B":1,"C":2}, "Y":{"A":4,"B":5,"C":6}, "Z":{"A":8,"B":9,"C":7}}
for round in better_input:
  score += cases[round[1]][round[0]]
print(score)
