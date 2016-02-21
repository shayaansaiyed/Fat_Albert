class Schedule(object):
    def __init__(self, start, end, prof, classNumber,weekdayList):
        self.startTime = start
        self.endTime = end
        self.professor = prof
        self.classNumber = classNumber
        self.weekdayList = weekdayList
    def printOut(self):
        print self.classNumber
        print self.startTime
        print self.endTime
        print self.professor
        print self.weekdayList
        print "\n"
