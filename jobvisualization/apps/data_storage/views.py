from datetime import datetime
from apps.data_storage import job_query as City
from apps.data_storage.models import WriteOnly, DiceJobs
from apps.data_storage import python_crawler

python_crawler.customCrawler()

WriteOnly.objects.all().delete()

def updateBase():
	print "updateBase"
	results = City.job_query("Front End")
	for result in results:
		WriteOnly.objects.create(
			num_jobs = result['numJobs'],
			city_name = result['name'],
			stateName = result['stateName'],
			stateAbbreviation = result['stateAbbreviation'],
			latitude = result['latitude'],
			longitude = result['longitude'],
			job_title = "Front End",
			created_at = datetime.now()
		)

	print "Added Front end results"

	results = City.job_query("Back End")
	for result in results:
		WriteOnly.objects.create(
			num_jobs = result['numJobs'],
			city_name = result['name'],
			stateName = result['stateName'],
			stateAbbreviation = result['stateAbbreviation'],
			latitude = result['latitude'],
			longitude = result['longitude'],
			job_title = "Back End",
			created_at = datetime.now()
		)
	print "Added Backend results"

	results = City.job_query("Full Stack")
	for result in results:
		WriteOnly.objects.create(
			num_jobs = result['numJobs'],
			city_name = result['name'],
			stateName = result['stateName'],
			stateAbbreviation = result['stateAbbreviation'],
			latitude = result['latitude'],
			longitude = result['longitude'],
			job_title = "Full Stack",
			created_at = datetime.now()
		)
	print "Added Fullstack results"


	results = python_crawler.customCrawler()
	for result in results:
		newSalary = aveAmount(result['salary'])
		d = DiceJobs.objects.create(
			title = result['title'],
			skills = result['skills'],
			salary = newSalary,
			location = result['location'],
			posted = result['posted'],
			created_at = datetime.now(),
		)
		print d

	return True

def aveAmount(salary):
  if not any(char.isdigit()for char in salary):
    return None
  salary = salary.replace(" ", "")
  salary = salary.replace('K', "000")
  salary = salary.replace('k', "000")
  salary = salary.replace('$', "")
  salary = salary.replace(',',"")
  salary = salary.replace('to', "-")

  for i in salary:
    if not ('0' <= i <= '9') and not (i == '-' or i =='.'):
      salary = salary.replace(i, "")

  if salary.find("-") > 0:
    for i in range(len(salary)):
      if salary[i] == '-':
        minNum = salary[:i]
        break
    maxNum = salary[i+1:]
    minNum = int(float(minNum))
    maxNum = int(float(maxNum))
    ave = (minNum + maxNum)/2
  else:
    ave = int(float(salary))
  print 'ave', ave
  return ave

updateBase()


