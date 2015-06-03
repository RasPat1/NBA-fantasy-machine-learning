"""
V = (v1 - v2) / (v1 + v2)
Transofrm the values as above
v1 being stats for home
v2 beign stats for away

Calucate rDiff for each game store in single column
rDiff = (home - away ) / (home + away)

linear regression on xV = rDiff
where x is matrix of coefficient 
V is transformed values
rDiff is the actual diff
"""
import sys
import csv
from sklearn import linear_model
import matplotlib.pyplot as plt

def read(fileName):
    fileHandle = open(fileName, 'rU') 
    reader = csv.DictReader(fileHandle)
    values = []
    for line in reader:
        values.append(readLine(line))

    stats = [row[:-1] for row in values]
    rDiff = [row[-1] for row in values]

    traingSetSize = 300
    sizeShortHand = -1 * traingSetSize

    trainStats = stats[:sizeShortHand]
    trainrDiff = rDiff[:sizeShortHand]

    testStats = stats[sizeShortHand:]
    testrDiff = rDiff[sizeShortHand:]

    coefs = []
    for game in values:
        clf.fit(trainStats, trainrDiff)



    // clf = linear_model.LinearRegression()
    clf.fit (trainStats, trainrDiff)
    print "linearRegression" 
    print clf.coef_
    print clf.score(testStats, testrDiff)

    ridge = linear_model.Ridge (alpha = .5)
    ridge.fit (trainStats, trainrDiff)
    print "ridgeLinearRegression"
    print ridge.coef_
    print ridge.score(testStats, testrDiff)


def plot(x, y, model):
    plt.scatter(x, y, color='black')
    plt.plot(x, model.predict(x), color='blue',
             linewidth=3)

    plt.xticks(())
    plt.yticks(())

    plt.show()
   
def readLine(row):
    data = []
    headings = [
    "Assists",
    "Blocks",
    "Steals",
    "Turnovers",
    "FreeThrowsAttempted",
    "FreeThrowsMade",
    "ThreePointersMade",
    "OffensiveRebounds",
    "DefensiveRebounds",
    "Fouls",
    "TwoPointersAttempted",
    "TwoPointersMade",
    "ThreePointersAttempted"
    ]
    for name in headings:
        data.append(getValue(row, name))

    real = getValue(row, "Points")
    data.append(real)
    return data

def getValue(row, statName):
    homeStat = int(row.get(statName))
    # The opponent values all start with "O.""
    awayStat = int(row.get("O." + statName))
    return getNormalizedValue(homeStat, awayStat)

def getNormalizedValue(homeStat, awayStat):
    numer = homeStat - awayStat
    denom = homeStat + awayStat
    if (denom == 0 or numer == 0):
        return 0
    else:
        return numer / float(denom)

if __name__ == '__main__':
    read(sys.argv[1])


