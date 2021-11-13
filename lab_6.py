# -*- coding: utf-8 -*-
"""Lab 6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19ZOvthGZs1fCeEV2uKNYK4TPup3yZQ3p
"""

#Problem 1

scoreList = []
newScoreList = []

for i in range(5):
  scores = float(input("Enter a test score: "))
  scoreList.append(scores)

print("All scores: ", scoreList)

newScoreList = scoreList[:]

for i in range(5):
  if newScoreList[i] < 60:
    newScoreList[i] += 10

print("Students who scored below 60 get 10 extra points.")
print("All scores: ", newScoreList)

for i in range(5):
  if newScoreList[i] != scoreList[i]:
    print("Old score:", scoreList[i], "New score:", newScoreList[i])

#Problem 2

intList = []

enterNum = int(input("Enter an integer from 1 to 10: "))
intList.append(enterNum)
yesNoQuestion = str(input("Enter another integer? [y/n] ").lower())

while yesNoQuestion == "y":
  enterNum = int(input("Enter an integer from 1 to 10: "))
  intList.append(enterNum)
  yesNoQuestion = str(input("Enter another integer? [y/n] ").lower())

averageList = sum(intList)/len(intList)

print("Number List:", intList)
print("Largest element:", max(intList))
print("Smallest element:", min(intList))
print("Sum of all element:", sum(intList))
print("Length of list:", len(intList))
print("Average:", averageList)

intList.reverse()
print("List reversed:", intList)

lastToFront = intList.insert(0, intList.pop())
print("Last element moved to front:", intList)

#Problem 3

print("First Sequence:")
for i in range(5, 25, 4):
  print(i)

print("Second Sequence:")
for i in range(26, -2, -7):
  print(i)

#Problem 4

strEntry = input("Enter a string: ").upper()
strEntry = strEntry.replace(",", "")
strEntry = strEntry.replace(" ", "")

print('')

def freq_finder(strFinder):
  dict = {}
  for i in strFinder:
    keys = dict.keys()
    if i in keys:
      dict[i] += 1
    else:
      dict[i] = 1
  return dict

newDic = freq_finder(strEntry)

print(newDic)

newLetter = input("Choose a letter: ").upper()

if newLetter in newDic:
  print("Frequency count of that letter", newDic[newLetter])
  newDic.pop(newLetter)
  print("Dictinary after that letter removed:", newDic)
else:
  print("Letter not in dictionary")

sortedDic = sorted(newDic)
print(sortedDic)