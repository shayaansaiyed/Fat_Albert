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