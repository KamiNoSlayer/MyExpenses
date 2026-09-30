#################################################
#Author : Hussler Clement
#Date of creation : 30/09/2026
#Last_update : 30/09/2026

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
'''
def write_data(Name,Ammount,Date,Type,Additional_note,datapath):
    with open(datapath,'w') as file :
        

def read_data(Name,Ammount,Date,Type,Additional_note,datapath):
'''

try :
    Name = input('What is the expense name ? ')
    Amount = int(input('What is the amount of the expense ? '))
    Type = input('What is the type of the expense ? ')
    Additional_note = input('Any additional note regarding the expense ? ')
except ValueError :
    print('Data type is not correct please enter the correct one')
