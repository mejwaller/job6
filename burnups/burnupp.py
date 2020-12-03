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
pwd = getpass.getpass("Trac (windows) password:)

date = datetime.today().strftime("%Y-%m-%d")
print(date)

p = ServerProxy("https://"+uname + ":" + pwd +"@trac.psenterprise.com/login/rpc")

print("Milestone 7.1.0...")
#milestone 7.1.0
new = str(len(p.ticket.query("milestone=7.1.0&status=new&max=0")))
assigned = str(len(p.ticket.query("milestone=7.1.0&status=assigned&max=0")))
reopened = str(len(p.ticket.query("milestone=7.1.0&status=reopened&max=0")))
closed = str(len(p.ticket.query("milestone=7.1.0&status=closed&max=0")))
total = str(len(p.ticket.query("milestone=7.1.0&max=0")))

f = open('710.csv','a')

f.write(date + "," + new + "," + assigned + "," + reopened + "," + closed + "," + total + "\n")

f.close()

print("gProperties...")
#gProperties
new = str(len(p.ticket.query("milestone=7.1.0&status=new&max=0&component=gProperties")))
assigned = str(len(p.ticket.query("milestone=7.1.0&status=assigned&max=0&component=gProperties")))
reopened = str(len(p.ticket.query("milestone=7.1.0&status=reopened&max=0&component=gProperties")))
closed = str(len(p.ticket.query("milestone=7.1.0&status=closed&max=0&component=gProperties")))
total = str(len(p.ticket.query("milestone=7.1.0&max=0&component=gProperties")))

f=open("gprop.csv",'a')

f.write(date + "," + new + "," + assigned + "," + reopened + "," + closed + "," + total + "\n")

f.close()

print("gsa...")
#gsa
new = str(len(p.ticket.query("keywords=~gsa&milestone=7.1.0&status=new&max=0")))
assigned = str(len(p.ticket.query("keywords=~gsa&milestone=7.1.0&status=assigned&max=0")))
reopened = str(len(p.ticket.query("keywords=~gsa&milestone=7.1.0&status=reopened&max=0")))
closed = str(len(p.ticket.query("keywords=~gsa&milestone=7.1.0&status=closed&max=0")))
total = str(len(p.ticket.query("keywords=~gsa&milestone=7.1.0&max=0")))

f = open('gsa.csv','a')

f.write(date + "," + new + "," + assigned + "," + reopened + "," + closed + "," + total + "\n")

f.close()

print("Surrogate modelling...")
#surrogate modelling
new = str(len(p.ticket.query("keywords=~surrogate_modelling&milestone=7.1.0&status=new&max=0")))
assigned = str(len(p.ticket.query("keywords=~surrogate_modelling&milestone=7.1.0&status=assigned&max=0")))
reopened = str(len(p.ticket.query("keywords=~surrogate_modelling&milestone=7.1.0&status=reopened&max=0")))
closed = str(len(p.ticket.query("keywords=~surrogate_modelling&milestone=7.1.0&status=closed&max=0")))
total = str(len(p.ticket.query("keywords=~surrogate_modelling&milestone=7.1.0&max=0")))

f = open('surrogatemodelling.csv','a')

f.write(date + "," + new + "," + assigned + "," + reopened + "," + closed + "," + total + "\n")

f.close()

print("EDM...")
#EDM
new = str(len(p.ticket.query("milestone=7.1.0&status=new&max=0&component=Dev_EDM")))
assigned = str(len(p.ticket.query("milestone=7.1.0&status=assigned&max=0&component=Dev_EDM")))
reopened = str(len(p.ticket.query("milestone=7.1.0&status=reopened&max=0&component=Dev_EDM")))
closed = str(len(p.ticket.query("milestone=7.1.0&status=closed&max=0&component=Dev_EDM")))
total = str(len(p.ticket.query("milestone=7.1.0&component=Dev_EDM&max=0")))

f = open('edm.csv','a')

f.write(date + "," + new + "," + assigned + "," + reopened + "," + closed + "," + total + "\n")

f.close()

print("BPE...")
#BPE
new = str(len(p.ticket.query("keywords=~bayesian&milestone=7.1.0&status=new&max=0")))
assigned = str(len(p.ticket.query("keywords=~bayesian&milestone=7.1.0&status=assigned&max=0")))
reopened = str(len(p.ticket.query("keywords=~bayesian&milestone=7.1.0&status=reopened&max=0")))
closed = str(len(p.ticket.query("keywords=~bayesian&milestone=7.1.0&status=closed&max=0")))
total = str(len(p.ticket.query("keywords=~bayesian&milestone=7.1.0&max=0")))

f = open('bpe.csv','a')

f.write(date + "," + new + "," + assigned + "," + reopened + "," + closed + "," + total + "\n")

f.close()

print("UoM...")
#UoM
new = str(len(p.ticket.query("milestone=7.1.0&status=new&max=0&summary=~[UoM")))
assigned = str(len(p.ticket.query("milestone=7.1.0&status=assigned&max=0&summary=~[UoM")))
reopened = str(len(p.ticket.query("milestone=7.1.0&status=reopened&max=0&summary=~[UoM")))
closed = str(len(p.ticket.query("milestone=7.1.0&status=closed&max=0&summary=~[UoM")))
total = str(len(p.ticket.query("milestone=7.1.0&max=0&summary=~[UoM")))

f = open('uom.csv','a')

f.write(date + "," + new + "," + assigned + "," + reopened + "," + closed + "," + total + "\n")

f.close()


print("Process scheduling...")
#process scheduling
new = str(len(p.ticket.query("milestone=7.1.0&status=new&max=0&keywords=~sbpa_process_scheduling")))
assigned = str(len(p.ticket.query("milestone=7.1.0&status=assigned&max=0&keywords=~sbpa_process_scheduling")))
reopened = str(len(p.ticket.query("milestone=7.1.0&status=reopened&max=0&keywords=~sbpa_process_scheduling")))
closed = str(len(p.ticket.query("milestone=7.1.0&status=closed&max=0&keywords=~sbpa_process_scheduling")))
total = str(len(p.ticket.query("milestone=7.1.0&max=0&keywords=~sbpa_process_scheduling")))

f = open('procsched.csv','a')

f.write(date + "," + new + "," + assigned + "," + reopened + "," + closed + "," + total + "\n")

f.close()


print("Trajectories...")
#trajectories
new = str(len(p.ticket.query("keywords=~sbpa_trajectories&milestone=7.1.0&status=new&max=0")))
assigned = str(len(p.ticket.query("keywords=~sbpa_trajectories&milestone=7.1.0&status=assigned&max=0")))
reopened = str(len(p.ticket.query("keywords=~sbpa_trajectories&milestone=7.1.0&status=reopened&max=0")))
closed = str(len(p.ticket.query("keywords=~sbpa_trajectories&milestone=7.1.0&status=closed&max=0")))
total = str(len(p.ticket.query("keywords=~sbpa_trajectories&milestone=7.1.0&max=0")))

f = open('trajectories.csv','a')

f.write(date + "," + new + "," + assigned + "," + reopened + "," + closed + "," + total + "\n")

f.close()

print("State estimation...")
#state estimation
new = str(len(p.ticket.query("keywords=~state_estimation&milestone=7.1.0&status=new&max=0")))
assigned = str(len(p.ticket.query("keywords=~state_estimation&milestone=7.1.0&status=assigned&max=0")))
reopened = str(len(p.ticket.query("keywords=~state_estimation&milestone=7.1.0&status=reopened&max=0")))
closed = str(len(p.ticket.query("keywords=~state_estimation&milestone=7.1.0&status=closed&max=0")))
total = str(len(p.ticket.query("keywords=~state_estimation&milestone=7.1.0&max=0")))

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
new = str(len(p.ticket.query("summary~=[Live&milestone=7.1.0&status=new&max=0")))
assigned = str(len(p.ticket.query("summary~=[Live&milestone=7.1.0&status=assigned&max=0")))
reopened = str(len(p.ticket.query("summary~=[Live&milestone=7.1.0&status=reopened&max=0")))
closed = str(len(p.ticket.query("summary~=[Live&milestone=7.1.0&status=closed&max=0")))
total = str(len(p.ticket.query("summary~=[Live&milestone=7.1.0&max=0")))

f = open('livedof.csv','a')

f.write(date + "," + new + "," + assigned + "," + reopened + "," + closed + "," + total + "\n")

f.close()

print("Model versioning...")
#model versioning
new = str(len(p.ticket.query("keywords=~model_versioning&milestone=7.1.0&status=new&max=0")))
assigned = str(len(p.ticket.query("keywords=~model_versioning&milestone=7.1.0&status=assigned&max=0")))
reopened = str(len(p.ticket.query("keywords=~model_versioning&milestone=7.1.0&status=reopened&max=0")))
closed = str(len(p.ticket.query("keywords=~model_versioning&milestone=7.1.0&status=closed&max=0")))
total = str(len(p.ticket.query("keywords=~model_versioning&milestone=7.1.0&max=0")))

f = open('modelv.csv','a')

f.write(date + "," + new + "," + assigned + "," + reopened + "," + closed + "," + total + "\n")

f.close()

print("Model spec dialogs...")
#model spec dialogs
new = str(len(p.ticket.query("keywords=~sbpa_usability&milestone=7.1.0&status=new&max=0")))
assigned = str(len(p.ticket.query("keywords=~sbpa_usability&milestone=7.1.0&status=assigned&max=0")))
reopened = str(len(p.ticket.query("keywords=~sbpa_usability&milestone=7.1.0&status=reopened&max=0")))
closed = str(len(p.ticket.query("keywords=~sbpa_usability&milestone=7.1.0&status=closed&max=0")))
total = str(len(p.ticket.query("keywords=~sbpa_usability&milestone=7.1.0&max=0")))

f = open('modspec.csv','a')

f.write(date + "," + new + "," + assigned + "," + reopened + "," + closed + "," + total + "\n")

f.close()
























