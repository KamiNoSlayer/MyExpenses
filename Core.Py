#################################################
#Author : Hussler Clement
#Date of creation : 30/09/2026
#Last_update : 01/10/2026

#All copyright belongs to the original author
################################################

#Libraries import
import os
import csv
import datetime

#Variables
datapath = '' # path to file for data location
date = datetime.datetime.now() # date of the day

Name = ''
Amount = 0
Day = date.strftime('%d')
Type = ''
Additional_note = ''

#Main
def write_data(Name,Amount,date,Type,Additional_note,datapath):
    with open(datapath, 'w', newline = '') as file :
        data_line = csv.writer(file)
        
        data_line.writerow(['Expense'] + ['Amount'] + ['Type'] + ['Date_of_expense'] + ['Additional note'])
        data_line.writerow([Name] + [str(Amount)] + [Type] + [str(date)] + [Additional_note])

'''
def read_data(Name,Ammount,Date,Type,Additional_note,datapath):
'''

try :
    Name = input('What is the expense name ? ')
    Amount = int(input('What is the amount of the expense ? '))
    Type = input('What is the type of the expense ? ')
    Additional_note = input('Any additional note regarding the expense ? ')
except ValueError :
    print('Data type is not correct please enter the correct one')

write_data(Name,Amount,date,Type,Additional_note,datapath)