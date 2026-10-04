import numpy as np # type: ignore

subjects = np.array(['maths','physics','social','chemistry'])

marks = np.array([44,55,66,99])

total = (np.sum(marks))
highest = (np.max(marks))
lowest = (np.min(marks))
average = (np.mean(marks))
std = (np.std(marks))
highest_index = (np .argmax(marks))
highest_subject = subjects[highest_index]
above_average = marks[marks>average]
if average >90:
    print("super performers")
elif average > 60:
    print("good performers")
elif average >50:
    print("average performers")
elif average >40:
    print("duller performers")
else :
    print ("fail")
print("___Student Marks Analyzer")
print("total marks:" ,total)
print("Highest subject:",highest_subject)
print("lowest marks:",lowest)
print("average marks:",average)
print("standard deviation:",std)
print("above average marks:",above_average)
print("grade:",average) 