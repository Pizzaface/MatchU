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

def find_meeting_times(schedule1, schedule2, schedule3, schedule4=None):
	max_min_times = {}
	for i in range(1, 8):
		sch1_day = schedule1[i]
		sch2_day = schedule2[i]
		sch3_day = schedule3[i]

		day_starts = [sch1_day[0], sch2_day[0], sch3_day[0]]
		day_ends = [sch1_day[1], sch2_day[1], sch3_day[1]]
		sch4_day = None
		if not schedule4 == None:
			sch4_day = schedule4[i]
			day_starts.append(sch4_day[0])
			day_ends.append(sch4_day[1])

		max_min_times[i] = [max(day_starts), min(day_ends)]


	return max_min_times

print(find_meeting_times(schedule1, schedule2, schedule3, schedule4))
