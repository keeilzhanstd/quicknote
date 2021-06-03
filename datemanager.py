import datetime as dt

class DateManager:
	@staticmethod	
	def getToday():
		return dt.date.today()

	@staticmethod
	def getTomorrow():
		return dt.date.today() + dt.timedelta(days=1)
