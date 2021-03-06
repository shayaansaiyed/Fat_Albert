numToDay = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

class Schedule(object):
    def __init__(self, start, end, prof, classNumber,weekdayList):
        self.startTime = start
        self.endTime = end
        self.professor = prof
        self.classNumber = classNumber
        self.weekdayList = weekdayList
    def printOut(self):
        print("Class number: {0}".format(self.classNumber))
        print("Professor: {0}".format(self.professor))
        print("Time: {0} {1}:{2}-{3}:{4}".format(", ".join([numToDay[d] for d in self.weekdayList]) + "; ",
            str(self.startTime/60).zfill(2), str(self.startTime%60).zfill(2),
            str(self.endTime/60).zfill(2), str(self.endTime%60)).zfill(2))
        print "\n"
