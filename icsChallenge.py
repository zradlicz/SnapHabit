import ics #ics parsing library
from ics import Calendar, Event
from datetime import datetime
import arrow

    
def ChangeStartDate(old,new,oldfile,newfile): #function takes old startdate (old), and new startdate (new), old calendar ics file, and the new calendar ics file.
    filename = oldfile
    file = open(filename,'r',encoding='utf8')
    c = Calendar(file.read())    
    
    startdate = arrow.get(new) #convert to datetime/arrow object
    firstdate = arrow.get(old)
    delta = startdate-firstdate #the amount of time between old start date and new start date
    
    for event in c.events: #iterates through every event in the calendar and changes the start and end date by 'delta' amount of time
        event.end=event.end+delta
        event.begin=event.begin+delta
        s = event.begin
        e = event.end
        
        print(s.datetime)
        print(e.datetime)

    with open(newfile,'w') as f: #writes to new file
        f.writelines(c)
        
ChangeStartDate('2020-06-04','2020-06-15','JusticeJune.ics','JusticeJuneJumped.ics')
    
        





