from lxml import etree
from io import StringIO, BytesIO

listOfSchedule = []

tree = etree.parse("file:///Users/shayaansaiyed/Documents/Projects/Hack%20Project/thing.xml")
xml_list = tree.findall("class")

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
        print 

for x in range(len(xml_list)):
    start = xml_list[x].find("startTime").text
    end = xml_list[x].find("endtTime").text
    prof = xml_list[x].find("professor").text
    wkDays = xml_list[x].find("weekDays").text
    classNum = xml_list[x].find("classNum").text
    schedule = Schedule(start, end, prof, wkDays, classNum)
    listOfSchedule.append(schedule)



for x in range(len(listOfSchedule)):
    listOfSchedule[x].printOut()
