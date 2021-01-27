import getpass
from xmlrpc.client import ServerProxy
from datetime import date,datetime, timedelta
from dateutil import rrule


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

def cleanDate(datestr):

    #string=datestr.split('T')[0]
    date=datetime.strptime(datestr,'%Y-%m-%d')

    #print(date)

    return date



uname = raw_input("Trac username:")
pwd = getpass.getpass("Trac (windows) password:")

curdate = datetime.today().strftime("%Y-%m-%d")

now = cleanDate(curdate)

startdate = date.fromisoformat('2021-01-18')
endate = date.fromisoformat('2021-03-31')

p = ServerProxy("https://"+uname + ":" + pwd +"@trac.psenterprise.com/login/rpc")
#print(p.system.getAPIVersion())

t4querystr="owner=josephw|laszlok|lukeu|nashwann|yuzhao|zhelyazo&status!=closed&milestone^=7.&max=0"
t3querystr="owner=grzegorzr|ianw|jamesr|jingleiz|johnf&status!=closed&milestone^=7.&max=0"
ldofquerystr="summary~=[Live&milestone=7.1.0&status!=closed&max=0"

p = ServerProxy("https://"+uname + ":" + pwd +"@trac.psenterprise.com/login/rpc")

t4tickets=p.ticket.query(t4querystr)
t3tickets=p.ticket.query(t3querystr)
ldoftickets=p.ticket.query(ldofquerystr)

totrem=0
ldoftotrem=0
startpoints=70
pointsrem=0
starthrs=610
ldofstarthrs=290
capacity=5
numdevs=5

print(t4tickets)
print(len(t4tickets))


print("Team 4...")
for ticket in t4tickets:
    print(ticket)
    strhrs = p.ticket.get(ticket)[3].get("estimatedhours")
    hrsleft = int (strhrs) if strhrs.isdigit() else 0
    print(hrsleft)
    totrem+=int(hrsleft)

print(totrem)

print(t3tickets)
print(len(t3tickets))

print("Team 3...")
for ticket in t3tickets:
    print(ticket)
    strpts = p.ticket.get(ticket)[3].get("storypoints")
    ptsleft = int (strpts) if strpts.isdigit() else 0
    print(ptsleft)
    pointsrem+=int(ptsleft)

print(ldoftickets)
print(len(ldoftickets))

print("Live DoF...")
for ticket in ldoftickets:
    print(ticket)
    strhrs = p.ticket.get(ticket)[3].get("estimatedhours")
    hrsleft = int (strhrs) if strhrs.isdigit() else 0
    print(hrsleft)
    ldoftotrem+=int(hrsleft)

idealrem = starthrs-(len(list(get_working_days(startdate,now)))*capacity*numdevs)
ldofidealrem = ldofstarthrs-(len(list(get_working_days(startdate,now)))*capacity*numdevs)


f = open('team4burndown.csv','a')

f.write(str(startdate) + "," + str(curdate) + "," + str(endate) + "," + str(totrem) + "," + str(idealrem) + "\n")

f.close()

f = open("team3burndown.csv","a")

f.write(str(startdate) + "," + str(curdate) + "," + str(endate) + "," + str(startpoints) + "," + str(pointsrem) + "\n")

f.close()

f = open("livedofburndown.csv","a")

f.write(str(startdate) + "," + str(curdate) + "," + str(endate) + "," + str(ldoftotrem) + "," + str(ldofidealrem) + "\n")

f.close()
