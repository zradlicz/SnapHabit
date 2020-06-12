import ics #ics parsing library
from ics import Calendar, Event
from datetime import datetime
import arrow

    
def findStart (cal):
    start = arrow.get('9999-12-30')
    for event in cal.events:
        date = event.begin
        if date < start:
            start = date
    return start
    


def changeStartDate(file,date): #function takes old startdate (old), and new startdate (new), old calendar ics file, and the new calendar ics file.
    filename = file
    CalFile = open(filename,'r',encoding='utf8')
    c = Calendar(CalFile.read())    
    
    
    
    startdate = arrow.get(date) #convert to datetime/arrow object
    firstdate = findStart(c)
    delta = startdate-firstdate #the amount of time between old start date and new start date
    
    for event in c.events: #iterates through every event in the calendar and changes the start and end date by 'delta' amount of time
        event.end=event.end+delta
        event.begin=event.begin+delta
        s = event.begin
        e = event.end
        
        print(s.datetime)
        print(e.datetime)

    with open('Edited'+file,'w') as f: #writes to new file
        f.writelines(c)
        
changeStartDate('JusticeJune.ics','2020-06-15')
   
        





