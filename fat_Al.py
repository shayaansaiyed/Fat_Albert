from lxml import etree
from io import StringIO, BytesIO
from sched_Class import Schedule

listOfSchedule = []

tree = etree.parse("thing.xml")
xml_list = tree.findall("class")


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
