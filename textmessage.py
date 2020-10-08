#Notes: You must manually clean excel sheet, format numbers to XXXXXXXXXX, remove dublicates, make sure to test before sending texts, make sure all rows are correct.
from twilio.rest import Client

import csv

filename = "rush_responses.csv"
# initializing the titles and rows list
fields = [] #Subjects on the spread sheet
rows = [] #The rows
names = [] #First names of rushees
numbers = [] #phone numbers of rushees

# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting field names through first row
    #fields = csvreader.next()

    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)

    # get total number of rows
    print("Total no. of rows: %d"%(csvreader.line_num))
    # printing the field names
print('Field names are:' + ', '.join(field for field in fields))

#  printing first 5 rows
#rowCount = 0
print('\nThe rows are:\n')
for row in rows[:]:
    print(row)
    print('Name: ', row[1]) #The rushee name
    first_name = row[1].split() #split the names so that only first name is attained
    names.append(first_name[0])#[rowCount] = row[1]
    print('Number: ', row[2]) #The rushee number
    numbers.append(row[2])#[rowCount] = row[2]
    #rowCount = rowCount + 1
    print('\n')

#Print names and numbers
rowCount = 0
for nameNumber in names:
    print('NUMBER: ' + str(rowCount))
    print('Rushee Name: ' + names[rowCount])
    print('Rushee Number: '+ numbers[rowCount])
    rowCount = rowCount + 1

account_sid = 'AC6c5eacd663494ce1bbfb04ca09c5c5bf' #<get this from Twilio account>
auth_token = 'e65e82a3bcf2e110f7b52778d43a849b' #<get this from Twilio account>
client = Client(account_sid, auth_token)
nameCount = 1
for number in numbers:
    message = client.messages \
                    .create(
                        body="",
                        from_= '+14052536450', #<Get this from twilio>,
                        to = number
                     )
    nameCount = nameCount + 1

print(message.sid)
