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

def isCompatible(class_1, class_2):
	"""
	Determines whether class times conflict between class_1 and class_2.
	Assumes class times are on the same day of the week.

	class_1: academic class object (Schedule)
	class_2: academic class object (Schedule)
	returns: compatibility; True when classes don't conflict, False otherwise
		(bool)
	"""
	return class_1.endTime < class_2.startTime or class_2.endTime < class_1.startTime

def shareDay(class_1, class_2):
	"""
	Determines if class_1 and class_2 share a day of the week.

	class_1: academic class object (Schedule)
	class_2: academic class object (Schedule)
	returns: whether a day is shared (bool)
	"""
	for day_1 in class_1.weekdayList:
		for day_2 in class_2.weekdayList:
			if day_1 == day_2: return True
	return False