

class Schedule(object):
    def __init__(self, start, end, prof, dayOfWeek, classNumber):
        self.startTime = start
        self.endTime = end
        self.professor = prof
        self.daysOfWeek = dayOfWeek
        self.classNumber = classNumber
    def printOut(self):
        print self.classNumber
        print self.startTime + " - " + self.endTime
        print self.daysOfWeek
        print self.professor
