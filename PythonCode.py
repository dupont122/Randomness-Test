import random

lotteryNumbers = []

for numRange in range (0,10):
  numbers = random.randint(1,50)
  while number in lotteryNumbers:
    number = random.randint(1,50)
  lotteryNumbers.append(number)

lotteryNumbers.sort()

print(lotteryNumbers)
