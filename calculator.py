import socket
import sys
import csv
import numpy as np
from scipy.optimize import minimize

# In case two few/many arguments
def usage():
    print( """
    Usage:
        python calculator.py [csv_file]

    """)
def ryans_an_ass(x, data):
    f1 = 0
    f2 = 0
    l = []

    for game in data:
        f1 =0 
        f1 += x[1]*game[1 - 1]
        f1 += x[2]*game[2 - 1]
        f1 += x[3]*game[3 - 1]
        f1 += x[4]*game[4 - 1]
        f1 += x[5]*game[5 - 1]
        f1 += x[6]*game[6 - 1]
        f1 += x[7]*game[7 - 1]
        f1 += x[8]*game[8 - 1]
        f1 += x[9]*game[9 - 1]
        f1 += x[10]*game[10 - 1]
        f1 += x[11]*game[11 - 1]
        f1 += x[12]*game[12 - 1]
        f1 += x[13]*game[13 - 1]
        
        f2  = 0
        f2 += x[1]*game[2*1 - 1]
        f2 += x[2]*game[2*2 - 1]
        f2 += x[3]*game[2*3 - 1]
        f2 += x[4]*game[2*4 - 1]
        f2 += x[5]*game[2*5 - 1]
        f2 += x[6]*game[2*6 - 1]
        f2 += x[7]*game[2*7 - 1]
        f2 += x[8]*game[2*8 - 1]
        f2 += x[9]*game[2*9 - 1]
        f2 += x[10]*game[2*10 - 1]
        f2 += x[11]*game[2*11 - 1]
        f2 += x[12]*game[2*12 - 1]
        f2 += x[13]*game[2*13 - 1]
           
        real = ( game[26] - game[27] ) / float( game[26] + game[27] )

        l.append(abs((f1/f2 - real)))

    return sum(l)/ float(len(l))

def constraint_function(x, data):
    print x
    return 0
    f1 = 0
    f2 = 0
    l = []

    for game in data:
        f1 = 0
        f1 += x[1]*game[1 - 1]
        f1 += x[2]*game[2 - 1]
        f1 += x[3]*game[3 - 1]
        f1 += x[4]*game[4 - 1]
        f1 += x[5]*game[5 - 1]
        f1 += x[6]*game[6 - 1]
        f1 += x[7]*game[7 - 1]
        f1 += x[8]*game[8 - 1]
        f1 += x[9]*game[9 - 1]
        f1 += x[10]*game[10 - 1]
        f1 += x[11]*game[11 - 1]
        f1 += x[12]*game[12 - 1]
        f1 += x[13]*game[13 - 1]
        
        f2  = 0
        f2 += x[1]*game[2*1 - 1]
        f2 += x[2]*game[2*2 - 1]
        f2 += x[3]*game[2*3 - 1]
        f2 += x[4]*game[2*4 - 1]
        f2 += x[5]*game[2*5 - 1]
        f2 += x[6]*game[2*6 - 1]
        f2 += x[7]*game[2*7 - 1]
        f2 += x[8]*game[2*8 - 1]
        f2 += x[9]*game[2*9 - 1]
        f2 += x[10]*game[2*10 - 1]
        f2 += x[11]*game[2*11 - 1]
        f2 += x[12]*game[2*12 - 1]
        f2 += x[13]*game[2*13 - 1]

        real = ( game[26] - game[27] ) / float( game[26] + game[27] )

        l.append(np.sign(f1)*np.sign(real) - 1)
    
    percent_wrong = sum(l) / len(l)
    cutoff = 0.5

    if (percent_wrong > cutoff):
        return 1
    else:   
        return 0

def load_data(fileName):
    fileHandle = open(fileName, 'rU')
    fileReader = csv.DictReader(fileHandle)

    data = []
    for line in fileReader:
        data.append(read_line(line))

    return data

def read_line(row):
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
    "ThreePointersAttempted",
    "Points"
    ]

    for name in headings:
        homeStat, awayStat = get_value(row, name)
        data.append(homeStat)
        data.append(awayStat)
    return data

def get_value(row, statName):
    homeStat = int(row.get(statName))
    # The opponent values all start with "O.""
    awayStat = int(row.get("O." + statName))
    return (homeStat, awayStat)

# Sets up and runs the code
if __name__ == '__main__':
    if len(sys.argv)!=2:
        usage()
        sys.exit(2)
    data = load_data(sys.argv[1])

    coefficients = [1]*14
    # res = minimize(ryans_an_ass, coefficients, args=data, method="SLSQP", options={'ftol': 1e-6, 'disp': True})
    res = minimize(ryans_an_ass, coefficients, args=data, method="SLSQP", tol=1e-6, options={'disp': True}, constraints=({'type': 'eq', 'fun': lambda coefficients: constraint_function(coefficients, data)}))
    print(res.coefficients)