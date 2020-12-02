from xmlrpc.client import ServerProxy
import configparser
from datetime import datetime, timedelta
from dateutil import rrule
from isoweek import Week
import getpass

import numpy as np #pip install numpy
import matplotlib.pyplot as plt #pip install matplotlib
from matplotlib.backends.backend_pdf import PdfPages
from collections import OrderedDict
import pprint

'''
Setup time related stuff
'''
period = 90 #90 day period

#see https://gist.github.com/dogsbody/8dce2429da2bddae2c31b67e0471b683
def get_holidays(a, b):
    rs = rrule.rruleset()
    # Include all potential holidays
    rs.rrule(rrule.rrule(rrule.YEARLY, dtstart=a, until=b, bymonth= 1, bymonthday= 1))                     # New Years Day
    rs.rrule(rrule.rrule(rrule.YEARLY, dtstart=a, until=b, bymonth= 1, bymonthday= 2, byweekday=rrule.MO)) # New Years Day
    rs.rrule(rrule.rrule(rrule.YEARLY, dtstart=a, until=b, bymonth= 1, bymonthday= 3, byweekday=rrule.MO)) # New Years Day
    rs.rrule(rrule.rrule(rrule.YEARLY, dtstart=a, until=b, byeaster= -2))                                  # Good Friday
    rs.rrule(rrule.rrule(rrule.YEARLY, dtstart=a, until=b, byeaster= 1))                                   # Easter Monday
    rs.rrule(rrule.rrule(rrule.YEARLY, dtstart=a, until=b, bymonth= 5, byweekday=rrule.MO, bysetpos=1))    # May Day
    rs.rrule(rrule.rrule(rrule.YEARLY, dtstart=a, until=b, bymonth= 5, byweekday=rrule.MO, bysetpos=-1))   # Spring Bank Holiday
    rs.rrule(rrule.rrule(rrule.YEARLY, dtstart=a, until=b, bymonth= 8, byweekday=rrule.MO, bysetpos=-1))   # Late Summer Bank Holiday
    rs.rrule(rrule.rrule(rrule.YEARLY, dtstart=a, until=b, bymonth=12, bymonthday=25))                     # Christmas
    rs.rrule(rrule.rrule(rrule.YEARLY, dtstart=a, until=b, bymonth=12, bymonthday=26, byweekday=rrule.MO)) # Christmas
    rs.rrule(rrule.rrule(rrule.YEARLY, dtstart=a, until=b, bymonth=12, bymonthday=27, byweekday=rrule.MO)) # Christmas
    rs.rrule(rrule.rrule(rrule.YEARLY, dtstart=a, until=b, bymonth=12, bymonthday=26))                     # Boxing Day
    rs.rrule(rrule.rrule(rrule.YEARLY, dtstart=a, until=b, bymonth=12, bymonthday=27, byweekday=rrule.MO)) # Boxing Day
    rs.rrule(rrule.rrule(rrule.YEARLY, dtstart=a, until=b, bymonth=12, bymonthday=27, byweekday=rrule.TU)) # Boxing Day
    rs.rrule(rrule.rrule(rrule.YEARLY, dtstart=a, until=b, bymonth=12, bymonthday=28, byweekday=rrule.MO)) # Boxing Day
    rs.rrule(rrule.rrule(rrule.YEARLY, dtstart=a, until=b, bymonth=12, bymonthday=28, byweekday=rrule.TU)) # Boxing Day
    # Exclude potential holidays that fall on weekends
    rs.exrule(rrule.rrule(rrule.WEEKLY, dtstart=a, until=b, byweekday=(rrule.SA,rrule.SU)))
    return rs

def get_working_days(a, b):
    rs = rrule.rruleset()
    rs.rrule(rrule.rrule(rrule.DAILY, dtstart=a, until=b))                         # Get all days between a and b
    rs.exrule(rrule.rrule(rrule.WEEKLY, dtstart=a, byweekday=(rrule.SA,rrule.SU))) # Exclude weekends
    rs.exrule(get_holidays(a,b))                                                   # Exclude holidays
    return rs

#get start date of week
#see https://stackoverflow.com/questions/5882405/get-date-from-iso-week-number-in-python
startdate = (datetime.today()+timedelta(days=-period)).isocalendar()
weekstart = Week(startdate[0],startdate[1]).monday()
startweek = int(weekstart.strftime("%Y%m%d"))

enddate = datetime.today().isocalendar()
endweek = int(Week(enddate[0],enddate[1]).monday().strftime("%Y%m%d"))
#print("endweek:")
#print(endweek)

j=0
weeks=[]
weeks.append(str(startweek))
step=0

while j<endweek:
    i=(datetime.today()+timedelta(days=(-period+step))).isocalendar()
    j=int(Week(i[0],i[1]).monday().strftime("%Y%m%d"))
    #pprint.pprint(j)
    weeks.append(str(j))
    step+=7

'''Data structure
each is a dictionary with team/totals as the key, and a tuple containing another dictionary (key=weeknum, value=throughput for that wek) and 2 lista (leadtimes and cycle times):
    {({},[],[])}
'''

Teams={}
Totals={}

uname = raw_input("Trac username:")
pwd = getpass.getpass("Trac (windows) password:")

p = ServerProxy("https://"+uname + ":" + pwd +"@trac.psenterprise.com/login/rpc")
#print(p.system.getAPIVersion())

Config = configparser.ConfigParser()
Config.read("trac.ini")

def ConfigSectionMap(section):
    dict1={}
    options = Config.options(section)
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
        except:
            print("Exception on %s!" % option)
            disct1[option] = None
    #print(dict1)
    return dict1
        
def setup(team, options):
    #Teams[team]=({}.fromkeys(range(startweek,endweek+1)),[],[])
    Teams[team]=({}.fromkeys(weeks),[],[])
    
    #print(weeks)
    for week in weeks:
        Teams[team][0][week]=0
    
    if not "Totals" in Totals:
        Totals["Totals"]=({}.fromkeys(weeks),[],[])
        for week in weeks:
            Totals["Totals"][0][week]=0

def cleanDate(datestr):

    string=datestr.split('T')[0]
    date=datetime.strptime(string,'%Y%m%d')

    #print(date)

    return date

def storeData(created,closed,started,team,options):

    startedstr=""
    started_date=0

    created_date = cleanDate(created)

    #print(closed)
    closed_date = cleanDate(closed)
    #print(closed_date)

    isocal = datetime.date(closed_date).isocalendar()
    #print(isocal)
    closedweek=Week(isocal[0],isocal[1]).monday()
    #print(closedweek)
    weeknum=closedweek.strftime("%Y%m%d")

    #throughput
    #print(weeknum)
    Teams[team][0][weeknum]+=1
    #only add up stuff from projects, not teams, otherwise there'd be dupes
    if options[0]=="project":
        Totals["Totals"][0][weeknum]+=1

    #leadtime
    leadtime=len(list(get_working_days(created_date, closed_date)))
    Teams[team][1].append(leadtime)
    if options[0]=="project":
        Totals["Totals"][1].append(leadtime)

    #cycletime is approximatio from assigned date as point at which work started. This is not always true.
    if str(started) != "0":
        started_date = cleanDate(started)
        cycletime = len(list(get_working_days(started_date,closed_date)))
        Teams[team][2].append(cycletime)
        if options[0]=="project":
            Totals["Totals"][2].append(cycletime)

def getData(area,options,tickets):

    startdate="0"
    createddate=0
    closeddate=0
    print("Number of tickets:")
    print(len(tickets))
    for ticket in tickets:
        skip=False
        print(ticket)
        changes = p.ticket.changeLog(ticket)
        havecloseddate=False
        haveassdate=False
        startdate=0
        for change in reversed(changes):
            #print(change)
            if change[4]=='closed' and havecloseddate==False:
                #print("Closed date:")
                #print(change[0])
                closeddate=str(change[0])
                #print(closeddate)
                #print(startweek)
                if int(datetime.strftime(cleanDate(closeddate),"%Y%m%d")) < startweek:
                    print("Ticket closed > 90 days ago! Skipping.")
                    skip=True
                    continue
                else:
                    havecloseddate=True
            if change[4]=='assigned' and haveassdate==False:
                #print("Assigned date:")
                #print(change[0])
                startdate=str(change[0])
                haveassdate=True
        if skip==True:
            continue
        createddate = str(p.ticket.get(ticket)[1])
        #print("Created:")
        #print(createddate)
        #print("\n")
        storeData(createddate,closeddate,startdate,area,options)

#fields = p.ticket.getTicketFields()
#for field in fields:
#   print(field)
#    print("\n")

def plotTotalsThruput():

    fig = plt.figure()

    ax = plt.subplot(111) 


    plt.grid(axis='y')
    plt.xlabel('Week Number')
    for label in (ax.get_xticklabels()):
        label.set_fontsize(5)
    plt.xticks(rotation=90)
    plt.ylabel=('Thruput (number of stories)')
    od = OrderedDict(sorted(Totals["Totals"][0].items()))
    plt.plot(od.keys(), od.values(),label="Totals")

    #use 15th percentile - "85% of the time team will deliver x stories per week - this is bottom 15% of the weekly thrupits
    text="50th Percentile: %d\n85th percentile: %d" % (int(np.median(list(od.values()))+0.5),int(np.percentile(list(od.values()),15)+0.5))
    plt.text(0.5,0.5,text, transform = ax.transAxes)

    plt.title("Total Throughput across all teams")
    #plt.show()

    return fig


def plotTotalsCumThruput():

    fig = plt.figure()

    ax = plt.subplot(111)

    plt.grid(axis='y')
    plt.xlabel('Week number')
    plt.xticks(rotation=90)
    for label in (ax.get_xticklabels()):
        label.set_fontsize(5)
    plt.ylabel=('Cumulative thruput (number of stories)')
    od = OrderedDict(sorted(Totals["Totals"][0].items()))
    cumulative = np.cumsum(list(od.values()))

    plt.plot(od.keys(), cumulative,label="Cumulative Totals")

    plt.title("Cumulative Total Throughput across all teams")
    #plt.show()

    return fig

def plotThruputHist(thruput,team):

    pprint.pprint("Thruput hist for team %s" % team)
    
    fig=plt.figure()

    ax = plt.subplot(111)

    #python3 - values() is now a view, convert to list to make it work
    d=np.array(list(thruput.values()))    
    numbins=d.max()-d.min()
    if numbins==0:
        numbins=1
    n, bins, patches = plt.hist(x=d,bins=numbins)

    #plt.grid(axis='Count')
    plt.xlabel("Thruput (stories delivered per week)")

    title = team + ' weekly thruput histogram'
    plt.title(title)

    maxfreq=n.max()

    plt.ylim(ymax=np.ceil(maxfreq/10)*10 if maxfreq % 10 else maxfreq + 10)

    text="50th percentile: %d\n85th percentile: %d" % (int(np.median(d)+0.5),int(np.percentile(d,85)+0.5))

    plt.text(0.5,0.5,text, transform = ax.transAxes)

    return fig


def plotLeadTimeHist(leadtimes,team):

    pprint.pprint("Leadtime for team %s" % team)
       
    fig = plt.figure()

    ax = plt.subplot(111)

    d=np.array(leadtimes)
    numbins = d.max() - d.min()
    if numbins==0:
        numbins=1
    n, bins, patches = plt.hist(x=d,bins=numbins)#color='#0504aa'

    plt.grid(axis='y')
    plt.xlabel('Leadtime (days)')
    
    title = team + ' Leadtime Histogram'
    plt.title(title)

    maxfreq = n.max()
    plt.ylim(ymax=np.ceil(maxfreq/10)*10 if maxfreq % 10 else maxfreq + 10)

    text="50th percentile: %d\n85th percentile: %d" % (int(np.median(d)+0.5),int(np.percentile(d,85)+0.5))

    plt.text(0.5,0.5,text, transform = ax.transAxes)
    #plt.show()
    return fig

def plotCycleTimeHist(cycletimes,team):

    pprint.pprint("Cycletime for team %s" % team)
   
    fig = plt.figure()

    ax = plt.subplot(111)

    d=np.array(cycletimes)
    numbins = d.max() - d.min()
    if numbins==0:
        numbins=1
    n, bins, patches = plt.hist(x=d,bins=numbins)#color='#0504aa'

    plt.grid(axis='y')
    plt.xlabel('Cycletime (days)')
    
    title = team + ' Cycletime Histogram'
    plt.title(title)

    maxfreq = n.max()
    plt.ylim(ymax=np.ceil(maxfreq/10)*10 if maxfreq % 10 else maxfreq + 10)

    text="50th percentile: %d\n85th percentile: %d" % (int(np.median(d)+0.5),int(np.percentile(d,85)+0.5))

    plt.text(0.5,0.5,text, transform = ax.transAxes)
    #plt.show()
    return fig


def plotThruput(thruput,team):

    pprint.pprint("Throughput for team %s" % team)

    fname=team + "_thruputs.txt"

    f = open(fname,"w")
    
    fig = plt.figure()

    ax = plt.subplot(111) 

    plt.grid(axis='y')
    plt.xlabel('Week Number')
    for label in (ax.get_xticklabels()):
        label.set_fontsize(5)
    plt.xticks(rotation=90)
    plt.ylabel('Throughput (number of stories)')
    #print(thruput.items())
    od = OrderedDict(sorted(thruput.items()))

    title = team + ' Weekly Throughput (last 90 days)'
    plt.title(title)

    #use 15th percentile - "85% of the time team will deliver x stories per week - this is bottom 15% of the weekly thrupits
    text="50th percentile: %d\n85th percentile: %d" % (int(np.median(list(od.values()))+0.5),int(np.percentile(list(od.values()),15)+0.5))

    plt.text(0.5,0.5,text, transform = ax.transAxes)

    for k,v in od.items():
        out = str(k) + "," + str(v) + "\n"
        f.write(out)
    f.close()

    #print(od.keys())
    #print(od.values())
   
    plt.plot(od.keys(), od.values(),label=team)

    

    #plt.legend()
    #plt.show()

    return fig

for area in ConfigSectionMap('Areas').values():
    print(area + ":")
    options=[]
    try:
        settings = Config.options(area)
        for setting in settings:
            val = Config.get(area,setting)
            options.append(val)
        print(options)
    except:
        print("Unexpected error:")
        raise

    setup(area,options)

    query_res = p.ticket.query(options[1])
    getData(area,options,query_res)

pp1 = PdfPages('teamleadtimes.pdf')
pp2 = PdfPages('teamthruputs.pdf')
pp3 = PdfPages('teamthruputhist.pdf')
pp4 = PdfPages('teamcycletimes.pdf')

'''Graphical output got teams (leadtime hist and thruput plot)
'''
for team in Teams:
    if len(Teams[team][1]) > 0:#in the cas eof no thruout, then can't plot a histogram of leadtimes!
        plot1 = plotLeadTimeHist(Teams[team][1],team)
        pp1.savefig(plot1)
        plot2 = plotThruput(Teams[team][0],team)
        pp2.savefig(plot2)
        plot3 = plotThruputHist(Teams[team][0],team)
        pp3.savefig(plot3)
        if len(Teams[team][2]) > 0: #if no cycletimes, can't plot them...
            plot4 = plotCycleTimeHist(Teams[team][2],team)
            pp4.savefig(plot4)
#        saveTeamThruputs(Teams[team][0],team)
    else:
        pprint.pprint("Skipping throught put and leadtime hist for team %s as they have 0 thruput!" % team)

pp1.close()
pp2.close()
pp3.close()
pp4.close()

pp1 = PdfPages('rollupthruputs.pdf')
plot1= plotTotalsThruput()
pp1.savefig(plot1)
plot2 = plotTotalsCumThruput()
pp1.savefig(plot2)

pp1.close()


pp1 = PdfPages("TotalLeadtimes.pdf")
plot1 = plotLeadTimeHist(Totals["Totals"][1],"Total")
pp1.savefig(plot1)

pp1.close()

if len(Totals["Totals"][2]) > 0:
    pp1 = PdfPages("TotalCycletimes.pdf")
    plot1 = plotCycleTimeHist(Totals["Totals"][2],"Total")
    pp1.savefig(plot1)
    pp1.close()


