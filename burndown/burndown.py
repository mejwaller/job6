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

#startdate = date.fromisoformat('2021-01-18')
t2startdate = date.fromisoformat('2021-03-08')
#endate = date.fromisoformat('2021-03-31')
startdate = date.fromisoformat('2021-06-03')
endate = date.fromisoformat('2021-08-31')

p = ServerProxy("https://"+uname + ":" + pwd +"@trac.psenterprise.com/login/rpc")
#print(p.system.getAPIVersion())

imequerystr="component=Dev_IME&milestone=2021.2.0&status!=closed&max=0"
v212querystr="milestone=2021.2.0&status!=closed&max=0"
t3querystr="keywords=~state_estimation|solver:|surrogate_modelling|ddap_ds&component=Dev_IME&status!=closed&milestone=2021.2.0&max=0"
ldofquerystr="summary~=[Live|[LPR&status!=closed&max=0"
edmquerystr="component=Dev_EDM&status!=closed&max=0"
nrmquerystr="keywords=~nrm&status!=closed&max=0"

p = ServerProxy("https://"+uname + ":" + pwd +"@trac.psenterprise.com/login/rpc")

imetickets=p.ticket.query(imequerystr)
v212tickets=p.ticket.query(v212querystr)
t3tickets=p.ticket.query(t3querystr)
ldoftickets=p.ticket.query(ldofquerystr)
edmtickets=p.ticket.query(edmquerystr)
nrmtickets=p.ticket.query(nrmquerystr)

totrem=0
ldoftotrem=0
startpoints=70
pointsrem=0
starthrs=1007
ldofstarthrs=47
t3starthrs=13
capacity=5
numdevs=5
imestart=77
v212start=160
edmstart=22
nrmstart=2

print(v212tickets)
print(len(v212tickets))

print("2021.2...")
v212rem=len(v212tickets)

print(imetickets)
print(len(imetickets))

print("IME 2021.2...")
imerem=len(imetickets)


print(t3tickets)
print(len(t3tickets))

print("Team 3...")
t3rem=len(t3tickets)

print(ldoftickets)
print(len(ldoftickets))

print("Live DoF...")
ldoftotrem = len(ldoftickets)

print(edmtickets)
print(len(edmtickets))

print("EDM...")
edmrem=len(edmtickets)

print(nrmtickets)
print(len(nrmtickets))

print("New results manager...")
nrmrem=len(nrmtickets)

daysrem = len(list(get_working_days(now,endate)))
print("Days remaining:")
print(daysrem)
t3idealrem = t3starthrs-(t3starthrs/daysrem)
ldofidealrem = ldofstarthrs-(ldofstarthrs/daysrem)
v212idealrem = v212start-(v212start/daysrem)
imeidealrem = imestart - (imestart/daysrem)
edmidealrem = edmstart - (edmstart/daysrem)
nrmidealrem = nrmstart - (nrmstart/daysrem)

f = open("v212burndown.csv","a")

f.write(str(startdate) + "," + str(curdate) + "," + str(endate) + "," + str(v212rem) + "," + str(v212idealrem) + "\n")

f.close()

f = open("imeburndown.csv","a")

f.write(str(startdate) + "," + str(curdate) + "," + str(endate) + "," + str(imerem) + "," + str(imeidealrem) + "\n")

f = open("team3burndown.csv","a")

f.write(str(startdate) + "," + str(curdate) + "," + str(endate) + "," + str(t3rem) + "," + str(t3idealrem) + "\n")

f.close()

f = open("livedofburndown.csv","a")

f.write(str(startdate) + "," + str(curdate) + "," + str(endate) + "," + str(ldoftotrem) + "," + str(ldofidealrem) + "\n")

f.close()

f = open("edmburndown.csv","a")

f.write(str(startdate) + "," + str(curdate) + "," + str(endate) + "," + str(edmrem) + "," + str(edmidealrem) + "\n")

f.close()

f = open("nrmburndown.csv","a")

f.write(str(startdate) + "," + str(curdate) + "," + str(endate) + "," + str(nrmrem) + "," + str(nrmidealrem) + "\n")


