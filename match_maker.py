import math

schedule1 = {
	1: [9, 20],
	2: [13, 20],
	3: [13, 20],
	4: [13, 20],
	5: [13, 20],
	6: [13, 20],
	7: [13, 20]
}
schedule2 = {
	1: [9, 20],
	2: [18, 20],
	3: [16, 20],
	4: [12, 20],
	5: [10, 20],
	6: [12, 23],
	7: [11, 20]
}

schedule3 = {
	1: [10, 20],
	2: [18, 20],
	3: [13, 20],
	4: [10, 20],
	5: [9, 20],
	6: [8, 23],
	7: [9, 20]
}
schedule4 = {
	1: [10, 20],
	2: [12, 20],
	3: [11, 20],
	4: [10, 20],
	5: [12, 20],
	6: [12, 23],
	7: [12, 20]
}

schedule5 = {
	1: [1, 2],
	2: [3, 4],
	3: [5, 7],
	4: [1, 5],
	5: [3, 4],
	6: [5, 6],
	7: [7, 8]
}
schedule6 = {
	1: [20, 22],
	2: [22, 23],
	3: [23, 24],
	4: [6, 7],
	5: [9, 10],
	6: [1, 2],
	7: [3, 4]
}

schedule7 = {
	1: [4, 5],
	2: [6, 7],
	3: [1, 2],
	4: [23, 24],
	5: [17, 18],
	6: [11, 12],
	7: [6, 7]
}
schedule8 = {
	1: [5, 6],
	2: [7, 8],
	3: [10, 11],
	4: [11, 12],
	5: [12, 13],
	6: [18, 19],
	7: [10, 15]
}


def find_meeting_times(schedule1, schedule2, schedule3, schedule4=None):
    max_min_times = {}
    for i in range(1, 8):
        sch1_day = schedule1[i]
        sch2_day = schedule2[i]
        sch3_day = schedule3[i]

        day_starts = [sch1_day[0], sch2_day[0], sch3_day[0]]
        day_ends = [sch1_day[1], sch2_day[1], sch3_day[1]]
        sch4_day = None
        if schedule4 is not None:
            sch4_day = schedule4[i]
            day_starts.append(sch4_day[0])
            day_ends.append(sch4_day[1])

        max_min_times[i] = [max(day_starts), min(day_ends)]

        time_difference = {}
        time_difference[i] = (min(day_ends) - max(day_starts))

    for key in time_difference:
        total_hours = 0
        total_hours += time_difference[key]

    if total_hours < 6:
        print("Schedule does not work.")
    else:
        print("Schedule works!")

    return max_min_times, time_difference


print(find_meeting_times(schedule1, schedule2, schedule3, schedule4))


class Student:

    def __init__(self, name, uid, email):
        self.name = name
        self.uid = uid
        self.email = email
        self.schedule = []
        self.project = ""
        self.role = ""

    def pick_project(self, project):
        self.project = project

    def pick_role(self, role):
        self.role = role

    def pick_schedule(self, schedule):
        self.schedule = schedule


Jim = Student('Jim', '1', 'jim@usf.edu')
Jumbo = Student('Jumbo', '2', 'jumbo@usf.edu')
Jenny = Student('Jenny', '3', 'jenny@usf.edu')
Jaime = Student('Jaime', '4', 'jaime@usf.edu')
Alpha = Student('Alpha', '5', 'alpha@usf.edu')
Beta = Student('Beta', '6', 'beta@usf.edu')
Charlie = Student('Charlie', '7', 'charlie@usf.edu')
Delta = Student('Delta', '8', 'delta@usf.edu')
Echo = Student('Echo', '9', 'echo@usf.edu')
Foxtrot = Student('Foxtrot', '10', 'foxtrot@usf.edu')
Golf = Student('Golf', '11', 'golf@usf.edu')
Hotel = Student('Hotel', '12', 'hotel@usf.edu')

Jim.pick_project('Student Matching System') #1
Jumbo.pick_project('Student Matching System') #1
Jenny.pick_project('Mesh Sensor Network Array') #1.1
Jaime.pick_project('Student Matching System') #1
Alpha.pick_project('Student Matching System') #1
Beta.pick_project('Student Matching System') #2
Charlie.pick_project('Mesh Sensor Network Array') #1.1
Delta.pick_project('Student Matching System') #2
Echo.pick_project('Student Matching System') #2
Foxtrot.pick_project('Student Matching System') #2
Golf.pick_project('Mesh Sensor Network Array') #1.1
Hotel.pick_project('Mesh Sensor Network Array') #1.1

Jim.pick_schedule(schedule1)
Jumbo.pick_schedule(schedule2)
Jenny.pick_schedule(schedule3)
Jaime.pick_schedule(schedule4)
Alpha.pick_schedule(schedule1)
Beta.pick_schedule(schedule2)
Charlie.pick_schedule(schedule3)
Delta.pick_schedule(schedule4)
Echo.pick_schedule(schedule1)
Foxtrot.pick_schedule(schedule2)
Golf.pick_schedule(schedule3)
Hotel.pick_schedule(schedule4)

students = []
students.append(Jim)
students.append(Jumbo)
students.append(Jenny)
students.append(Jaime)
students.append(Alpha)
students.append(Beta)
students.append(Charlie)
students.append(Delta)
students.append(Echo)
students.append(Foxtrot)
students.append(Golf)
students.append(Hotel)


def make_group(students):
    group = []
    group.append(students[0])
    for i in range(1, 4):
        if students[i].project == students[0].project:
            group.append(students[i])

    return group


def add_to_group(student, groups):
    group = []
    if groups.__len__() == 0:
        group.append(student)
        groups.append(group)
        return groups
    for i in range(groups.__len__()):
        if groups[i].__len__() < 4:
            if groups[i].__len__() == 0:
                group.append(student)
                groups.append(group)
                return groups
            if groups[i][0].project == student.project:
                groups[i].append(student)
                return groups
            else:
                group = []
                group.append(student)
                groups.append(group)
                return groups
        elif groups[i].__len__() >= 4:
            continue
        else:
            group = []
            group.append(student)
            groups.append(group)
            return groups


groups = []
groupCount = math.ceil(students.__len__() / 4)

for i in range(students.__len__()):
    groups = add_to_group(students[i], groups)
    #print(students[i].name)

for group in groups:
    print("-----")
    for student in group:
        print(student.name)