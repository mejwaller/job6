#project,date,totalticktets,closedtickets,opentickets

#for each project
#append to file (first write adds column titles)
#plot (x=date) totaltickets(bar), closedtickets (line
#cumulative flow?)

#totals
#per above
from xmlrpc.client import ServerProxy
from datetime import datetime, timedelta
import getpass

uname = raw_input("Trac username:")
pwd = getpass.getpass("Trac (windows) password:")

date = datetime.today().strftime("%Y-%m-%d")
print(date)

p = ServerProxy("https://"+uname + ":" + pwd +"@trac.psenterprise.com/login/rpc")

print("Milestone 2021.1.0...")
#milestone 7.1.0
new = str(len(p.ticket.query("milestone=2021.1.0&status=new&max=0")))
assigned = str(len(p.ticket.query("milestone=2021.1.0&status=assigned&max=0")))
reopened = str(len(p.ticket.query("milestone=2021.1.0&status=reopened&max=0")))
closed = str(len(p.ticket.query("milestone=2021.1.0&status=closed&max=0")))
total = str(len(p.ticket.query("milestone=2021.1.0&max=0")))

f = open('710.csv','a')

f.write(date + "," + new + "," + assigned + "," + reopened + "," + closed + "," + total + "\n")

f.close()

print("Milestone 2021.2.0 (8.0)...")
#milestone 2021.2.0
new = str(len(p.ticket.query("milestone=2021.2.0&status=new&max=0")))
assigned = str(len(p.ticket.query("milestone=2021.2.0&status=assigned&max=0")))
reopened = str(len(p.ticket.query("milestone=2021.2.0&status=reopened&max=0")))
closed = str(len(p.ticket.query("milestone=2021.2.0&status=closed&max=0")))
total = str(len(p.ticket.query("milestone=2021.2.0&max=0")))

f = open('80.csv','a')

f.write(date + "," + new + "," + assigned + "," + reopened + "," + closed + "," + total + "\n")

f.close()

print("Milestone 2021.2.0 (IME)...")
#milestone 2021.2.0 IME
new = str(len(p.ticket.query("component=Dev_IME|Dev_EDM&milestone=2021.2.0&status=new&max=0")))
assigned = str(len(p.ticket.query("component=Dev_IME|Dev_EDM&milestone=2021.2.0&status=assigned&max=0")))
reopened = str(len(p.ticket.query("component=Dev_IME|Dev_EDM&milestone=2021.2.0&status=reopened&max=0")))
closed = str(len(p.ticket.query("component=Dev_IME|Dev_EDM&milestone=2021.2.0&status=closed&max=0")))
total = str(len(p.ticket.query("component=Dev_IME|Dev_EDM&milestone=2021.2.0&max=0")))

f = open('IME21_2.csv','a')

f.write(date + "," + new + "," + assigned + "," + reopened + "," + closed + "," + total + "\n")

f.close()



print("gProperties...")
#gProperties
new = str(len(p.ticket.query("milestone=~gProp&status=new&max=0&component=gProperties")))
assigned = str(len(p.ticket.query("milestone=~gProp0&status=assigned&max=0&component=gProperties")))
reopened = str(len(p.ticket.query("milestone=~gProp&status=reopened&max=0&component=gProperties")))
closed = str(len(p.ticket.query("milestone=~gProp&status=closed&max=0&component=gProperties")))
total = str(len(p.ticket.query("milestone=~gProp&max=0&component=gProperties")))

f=open("gprop.csv",'a')

f.write(date + "," + new + "," + assigned + "," + reopened + "," + closed + "," + total + "\n")

f.close()

print("EDM...")
#EDM
new = str(len(p.ticket.query("status=new&max=0&component=Dev_EDM")))
assigned = str(len(p.ticket.query("status=assigned&max=0&component=Dev_EDM")))
reopened = str(len(p.ticket.query("status=reopened&max=0&component=Dev_EDM")))
closed = str(len(p.ticket.query("status=closed&max=0&component=Dev_EDM")))
total = str(len(p.ticket.query("component=Dev_EDM&max=0")))

f = open('edm.csv','a')

f.write(date + "," + new + "," + assigned + "," + reopened + "," + closed + "," + total + "\n")

f.close()

print("BPE...")
#BPE
new = str(len(p.ticket.query("keywords=~bayesian&milestone=2021.2.0&status=new&max=0")))
assigned = str(len(p.ticket.query("keywords=~bayesian&milestone=2021.2.0&status=assigned&max=0")))
reopened = str(len(p.ticket.query("keywords=~bayesian&milestone=2021.2.0&status=reopened&max=0")))
closed = str(len(p.ticket.query("keywords=~bayesian&milestone=2021.2.0&status=closed&max=0")))
total = str(len(p.ticket.query("keywords=~bayesian&milestone=2021.2.0&max=0")))

f = open('bpe.csv','a')

f.write(date + "," + new + "," + assigned + "," + reopened + "," + closed + "," + total + "\n")

f.close()

print("State estimation...")
#state estimation
new = str(len(p.ticket.query("keywords=~state_estimation&milestone=2021.2.0&status=new&max=0")))
assigned = str(len(p.ticket.query("keywords=~state_estimation&milestone=2021.2.0&status=assigned&max=0")))
reopened = str(len(p.ticket.query("keywords=~state_estimation&milestone=2021.2.0&status=reopened&max=0")))
closed = str(len(p.ticket.query("keywords=~state_estimation&milestone=2021.2.0&status=closed&max=0")))
total = str(len(p.ticket.query("keywords=~state_estimation&milestone=2021.2.0&max=0")))

f = open('stateest.csv','a')

f.write(date + "," + new + "," + assigned + "," + reopened + "," + closed + "," + total + "\n")

f.close()

print("gFP utilities UI...")
#gfP Utilities UI
new = str(len(p.ticket.query("keywords=~gformulate_utilities_ui&milestone=gFP_2.0&status=new&max=0")))
assigned = str(len(p.ticket.query("keywords=~gformulate_utilities_ui&milestone=gFP_2.0&status=assigned&max=0")))
reopened = str(len(p.ticket.query("keywords=~gformulate_utilities_ui&milestone=gFP_2.00&status=reopened&max=0")))
closed = str(len(p.ticket.query("keywords=~gformulate_utilities_ui&milestone=gFP_2.0&status=closed&max=0")))
total = str(len(p.ticket.query("keywords=~gformulate_utilities_ui&milestone=gFP_2.0&max=0")))

f = open('gfputils.csv','a')

f.write(date + "," + new + "," + assigned + "," + reopened + "," + closed + "," + total + "\n")

f.close()

print("Live DoF...")
#Live DoF
new = str(len(p.ticket.query("summary~=[Live|[LPR&status=new&max=0")))
assigned = str(len(p.ticket.query("summary~=[Live|[LPR&status=assigned&max=0")))
reopened = str(len(p.ticket.query("summary~=[Live|[LPR&status=reopened&max=0")))
closed = str(len(p.ticket.query("summary~=[Live|[LPR&status=closed&max=0")))
total = str(len(p.ticket.query("summary~=[Live|[LPR&max=0")))

f = open('livedof.csv','a')

f.write(date + "," + new + "," + assigned + "," + reopened + "," + closed + "," + total + "\n")

f.close()

print("New results manager...")
new = str(len(p.ticket.query("keywords=~nrm&status=new&max=0")))
assigned = str(len(p.ticket.query("keywords=~nrm&status=assigned&max=0")))
reopened = str(len(p.ticket.query("keywords=~nrm&status=reopened&max=0")))
closed = str(len(p.ticket.query("keywords=~nrm&status=closed&max=0")))
total = str(len(p.ticket.query("keywords=~nrm0&max=0")))

f = open('nrm.csv','a')

f.write(date + "," + new + "," + assigned + "," + reopened + "," + closed + "," + total + "\n")

f.close()


print("SbPA...")
#sbpa
new = str(len(p.ticket.query("keywords=~sbpa&milestone=2021.1.0&status=new&max=0")))
assigned = str(len(p.ticket.query("keywords=~sbpa&milestone=2021.1.0&status=assigned&max=0")))
reopened = str(len(p.ticket.query("keywords=~sbpa&milestone=2021.1.0&status=reopened&max=0")))
closed = str(len(p.ticket.query("keywords=~sbpa&milestone=2021.1.0&status=closed&max=0")))
total = str(len(p.ticket.query("keywords=~sbpa&milestone=2021.1.0&max=0")))

f = open('sbpa.csv','a')

f.write(date + "," + new + "," + assigned + "," + reopened + "," + closed + "," + total + "\n")

f.close()

print("Team 1 gProperties")
#team 1
new = str(len(p.ticket.query("owner=agams|charlesp|samuelv&component=~gProperties&status=new&max=0")))
assigned = str(len(p.ticket.query("owner=agams|charlesp|samuelv&component=~gProperties&status=assigned&max=0")))
reopened = str(len(p.ticket.query("owner=agams|charlesp|samuelv&component=~gProperties&status=reopened&max=0")))
closed = str(len(p.ticket.query("owner=agams|charlesp|samuelv&component=~gProperties&status=closed&max=0")))
total = str(len(p.ticket.query("owner=agams|charlesp|samuelv&component=~gProperties&max=0")))

f = open('team1.csv','a')

f.write(date + "," + new + "," + assigned + "," + reopened + "," + closed + "," + total + "\n")

f.close()

print("Team 3...")
#team3
new = str(len(p.ticket.query("milestone=2021.2.0&keywords=~state_estimation|solver:|surrogate_modelling|ddap_ds&component=Dev_IME&status=new&max=0")))
assigned = str(len(p.ticket.query("milestone=2021.2.0&keywords=~state_estimation|solver:|surrogate_modelling|ddap_ds&component=Dev_IME&status=assigned&max=0")))
reopened = str(len(p.ticket.query("milestone=2021.2.0&keywords=~state_estimation|solver:|surrogate_modelling|ddap_ds&component=Dev_IME&status=reopened&max=0")))
closed = str(len(p.ticket.query("milestone=2021.2.0&keywords=~state_estimation|solver:|surrogate_modelling|ddap_ds&component=Dev_IME&status=closed&max=0")))
total = str(len(p.ticket.query("milestone=2021.2.0&keywords=~state_estimation|solver:|surrogate_modelling|ddap_ds&component=Dev_IME&max=0")))

f = open('team3.csv','a')

f.write(date + "," + new + "," + assigned + "," + reopened + "," + closed + "," + total + "\n")

f.close()

print("Team 5...")
#Team 5
new = str(len(p.ticket.query("milestone=~2021.2.&owner=duaneg|mariof|tristanz|luked&status=new&max=0")))
assigned = str(len(p.ticket.query("milestone=~2021.2.&owner=duaneg|mariof|tristanz|luked&status=assigned&max=0")))
reopened = str(len(p.ticket.query("milestone=~12021.2.&owner=duaneg|mariof|tristanz|luked&status=reopened&max=0")))
closed = str(len(p.ticket.query("milestone=~2021.2.&owner=duaneg|mariof|tristanz|luked&status=closed&max=0")))
total = str(len(p.ticket.query("milestone=~2021.2.&owner=duaneg|mariof|tristanz|luked&max=0")))

f = open('team5.csv','a')

f.write(date + "," + new + "," + assigned + "," + reopened + "," + closed + "," + total + "\n")

f.close()

print("Arch...")
#arch
new = str(len(p.ticket.query("milestone=~2021.2.&keywords~=architecture&status=new&max=0")))
assigned = str(len(p.ticket.query("milestone=~2021.2.&keywords~=architecture&status=assigned&max=0")))
reopened = str(len(p.ticket.query("milestone=~12021.2.&keywords~=architecture&status=reopened&max=0")))
closed = str(len(p.ticket.query("milestone=~2021.2.&keywords~=architecture&status=closed&max=0")))
total = str(len(p.ticket.query("milestone=~2021.2.&keywords~=architecture&max=0")))

f = open('arch.csv','a')

f.write(date + "," + new + "," + assigned + "," + reopened + "," + closed + "," + total + "\n")

f.close()


