import os
import csv

curpath = os.path.dirname(os.path.abspath(__file__))

ippath = curpath + '/data/yelp_academic_dataset_checkin.csv'
oppath = curpath + '/data/checkins.csv'
 
def readCSVFile(url):
    infile = csv.DictReader(open(url,'rb'), delimiter=',')
    return infile
 
def writeCSVFile(url):
    fieldnames = ['business_id','type','checkins']
    infile = csv.DictWriter(open(url,'wb'), fieldnames=fieldnames)
    return infile
 
def checkAttribute(attr):
    check = ['type', 'business_id']
    if attr in check: return True
    return False

def formatString(val):
    length = len(str(val).strip())
    if length > 0 : return val
    return 0

reader = readCSVFile(ippath)
writer = writeCSVFile(oppath)
 
writer.writeheader()
 
for row in reader:
    obj = {}
    count = 0   
    for key in row:
      valid = checkAttribute (key)
      if valid:
         obj[key] = row[key]

      else:
        count = count + int(formatString(row[key]))
    obj['checkins'] = str(count)
    writer.writerow(obj)

    #writer.writerow({'Salary': row['Salary'], 'ExpYear': str(year), 'Ht': str(result), 'MP': row['MP'], 'FG': row['FG'], 'PTS': row['PTS']})
       
