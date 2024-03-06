def namecheck (s):

	# checks that a name only includes alphabetic characters, -, or single quote
	# names must be between 2 and 40 characters long
	# quoted strings and -- are disallowed

	namex = r"^[a-zA-Z][a-zA-Z-']{1,39}$"
	if re.match (namex, s):
		if re.search ("'.*'", s) or re.search ("--", s):
			return False
		else:
			return True
	else:
			return False

