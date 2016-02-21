from lxml import etree
from io import StringIO, BytesIO
from sched_Class import Schedule

fileNames = ["Advanced College Essay", "Calculus 2", "Objected Oriented Programming"]

weekdays = {"MON": 0, "TUE":1, "WED":2, "THU":3, "FRI":4, "SAT":5, "SUN":6}


for x in range(len(xml_list)):
    start = xml_list[x].find("startTime").text
    end = xml_list[x].find("endTime").text

courses = {}


def isTimeCompatible( A, B):
    return (A.endTime < B.startTime or B.endTime < A.startTime)

def isDateCompatible(A,B):
    for x in range(len(A.weekdayList)):
        if(A.weekdayList[x] in B.weekdayList):
           return False
    return True
    
for classNameIndex in range(len(fileNames)):
    listOfSchedule = []
    
    tree = etree.parse(fileNames[classNameIndex] + ".xml")
    xml_list = tree.findall("class")
    

    for x in range(len(xml_list)):
        start = xml_list[x].find("startTime").text
        end = xml_list[x].find("endTime").text

        startTime = 60*int(start[:2]) + int(start[3:5])
        endTime = 60*int(end[:2]) + int(end[3:5])

        wkDays = xml_list[x].find("weekDays").text

        firstWeekDay = wkDays[:3].upper()
        weekdayList=[]
        
        weekdayList.append(weekdays[firstWeekDay])


        if len(wkDays) != 3:
            secondWeekDay = wkDays[4:].upper()

        weekdayList.append(weekdays[secondWeekDay])   
            
        classNum = xml_list[x].find("classNum").text
        prof = xml_list[x].find("professor").text
        
        schedule = Schedule(startTime, endTime, prof, classNum,weekdayList)
        listOfSchedule.append(schedule)

    #for x in range(len(listOfSchedule)):
        #listOfSchedule[x].printOut()

    courses[fileNames[classNameIndex]] = listOfSchedule


A=courses[fileNames[0]][0]
B=courses[fileNames[0]][10]

A.printOut()
B.printOut()

C = isTimeCompatible(A,B)
D = isDateCompatible(A,B)
print C
print D
