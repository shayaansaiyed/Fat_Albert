from lxml import etree
from io import StringIO, BytesIO
from sched_Class import Schedule
from random import randint

fileNames = ["Advanced College Essay", "Calculus 2", "Objected Oriented Programming"]

weekdays = {"MON": 0, "TUE":1, "WED":2, "THU":3, "FRI":4, "SAT":5, "SUN":6}

courses = {}

def permute(perms):
    """
    Returns list permutations given a list where each element is a list of
    possible values in that position.

    perms: list of lists, where each elemental list contains possible values
        for that position (list<list>)
    returns: list of permutations, where each permutation is a list
        (list<list>)
    """
    if len(perms) == 1: return [[classNum] for classNum in perms[0]]
    subperms = permute(perms[1:])
    newPerms = []
    for classNum in perms[0]:
        for subperm in subperms: newPerms.append([classNum] + subperm)
    return newPerms

def isTimeCompatible(A, B):
    return (A.endTime < B.startTime or B.endTime < A.startTime)

def isDateCompatible(A, B):
    for x in range(len(A.weekdayList)):
        if(A.weekdayList[x] in B.weekdayList): return False
    return True

def isValidSchedule(sched):
    for i in xrange(1, len(sched)):
        for j in xrange(i):
            if not isDateCompatible(sched[i], sched[j]) and \
            not isTimeCompatible(sched[i], sched[j]): return False
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

if __name__ == "__main__":
    schedules = permute([courses[courseName] for courseName in fileNames])
    validSchedules = []
    for sched in schedules:
        if isValidSchedule(sched): validSchedules.append(sched)
    '''
    for vSched in validSchedules:
        print("=" * 25 + "\n")
        for classSched in vSched: classSched.printOut()
        print("\n" * 2 + "=" * 25)
    '''
    print("=" * 25 + "\n")
    for classSched in validSchedules[randint(0, len(validSchedules))]: classSched.printOut()
    resp = raw_input("Is this schedule okay? (y/n): ").lower()
    valid = resp[0] == "y" or resp[0] == "n"
    while not valid or resp[0] == "n":
        if not valid:
            print("Invalid input!")
        else:
            print("\n" * 2 + "=" * 25)
            print("=" * 25 + "\n")
            for classSched in validSchedules[randint(0, len(validSchedules))]: classSched.printOut()
        resp = raw_input("Is this schedule okay? (y/n): ").lower()
        valid = resp[0] == "y" or resp[0] == "n"
