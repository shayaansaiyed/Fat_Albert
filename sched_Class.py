

class Schedule(object):
    def __init__(self, start, end, prof, dayOfWeek, classNumber,weekdayList):
        self.startTime = start
        self.endTime = end
        self.professor = prof
        self.daysOfWeek = dayOfWeek
        self.classNumber = classNumber
        self.weekdayList = weekdayList
    def printOut(self):
        print self.classNumber
        print self.startTime
        print self.endTime
        print self.daysOfWeek
        print self.professor
        print self.weekdayList
        print "\n"
