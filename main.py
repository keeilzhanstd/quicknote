import os
import sys

from filemanager import JSONPopulator
from inputcontroller import StandardInputController
from datemanager import DateManager

class Plan:
	def __init__(self, body, date_added):
		self.body = body
		self.date_added = date_added

	def __str__(self):
		return "{" + f'"added":"{self.date_added}","body":"{self.body}"' + "},"

class Datestamp:
	def __init__(self, date):
		self.plans = []
		self.date = date

	def __str__(self):
		planslist = []
		for el in self.plans:
			planslist.append(el.__str__())
		return "{" + f'"datestamp":"{self.date}","plans": {planslist}' + "},"

	def addPlan(self, plan):
		self.plans.append(plan)

class Data:
	def __init__(self):
		self.datestamps = []
		pass

	def __str__(self):
		datestampslist = []
		for el in self.datestamps:
			datestampslist.append(el.__str__())

		return f"{datestampslist}".replace('\'', '').replace('\\', '').replace(',', '').replace('} {', '},{').replace('\"\"', '\",\"')

	def addDatestamp(self, datestamp):
		self.datestamps.append(datestamp)

	def createOrModify(self, date, message):

		if date == "tomorrow":
			date = DateManager.getTomorrow().strftime("%Y-%m-%d")
		elif date == "today":
			date = DateManager.getToday().strftime("%Y-%m-%d")

		createNew = True
		for d in self.datestamps:
			if d.date == date:
				p = Plan(message, DateManager.getToday())
				d.addPlan(p)
				createNew = False
				return
		if createNew:
			p = Plan(message, DateManager.getToday())
			ds = Datestamp(date)
			ds.addPlan(p)
			d = Data()
			self.addDatestamp(ds)
			return

class Application:
	def __init__(self):
		self.createModel()

	def createModel(self):
		self.populatedJson = JSONPopulator.read()
		self.data = Data()
		for datestamp in self.populatedJson:
			dateContent = Datestamp(datestamp["datestamp"])
			for plan in datestamp["plans"]:
				plan = Plan(plan["body"], plan["added"])
				dateContent.addPlan(plan)
			self.data.addDatestamp(dateContent)

	def start(self, flags=[], params=[]):

		if len(flags) == 0:
			result = self.fetchByDate(params)
			if result != None:
				print(f"Planned for {params[0]}:")
				for element in result:
					print(f'\t{element}')
			else:
				print(f"Nothing found for {params[0]}")
		else:
			if "-a" in flags:
				if len(params) < 2:
					print("Usage: qnote -a [date (yyyy-mm-dd), today, tomorrow] \"Message\" ")
					exit()
				self.writeToDate(params)

	def fetchByDate(self, params):
		searchDate = params[0]
		for datestamp in self.data.datestamps:
			plans = []
			flag = False
			if datestamp.date == DateManager.getToday().strftime("%Y-%m-%d") and searchDate == "today":
				plans = self.retrievePlans(datestamp.plans)
				flag = not flag
			elif datestamp.date == DateManager.getTomorrow().strftime("%Y-%m-%d") and searchDate == "tomorrow":
				plans = self.retrievePlans(datestamp.plans)
				flag = not flag
			elif datestamp.date == searchDate:
				plans = self.retrievePlans(datestamp.plans)
				flag = not flag

			if flag:
				return plans
		
		return None

	def writeToDate(self, params):
		date = params[0]
		message = params[1]
		process = self.data.createOrModify(date, message)
		print(f"{message} added to {date}")
	
	def deleteByDate(self, params):
		pass

	def end(self):
		JSONPopulator.write(self.data.__str__())

def main():
	
	#Getting command line input.
	terminal = StandardInputController(sys.argv)
	terminal.validateCommand()

	app = Application()
	app.start(terminal.flags, terminal.command)
	app.end()

if __name__ == '__main__':
	main()