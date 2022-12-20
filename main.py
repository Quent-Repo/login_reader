""""
Made to read .csv logins from firefox
"""

import csv
with open('logins.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if(row['username'] == ""):
            print(row['url']+", ", "***No User Name ***, ", row['password']+", ")
        else:
            print(row['url']+", ", row['username']+", ", row['password']+", ")
        print('___')
