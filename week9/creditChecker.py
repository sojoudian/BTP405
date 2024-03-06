import doNormalProcessing

def credit_checker (name, postcode, dob):

	# Assume that the function check_credit_rating calls an external service 
	# to get a person's credit rating. It takes a name, postcode (zip code) 
	# and date of birth as parameters and returns a sequence with the database 
	# information (name, postcode, date of birth) plus a credit score between 0 and 
	# 600. The final element in the sequence is an error_code which may 
	# be 0 (successful completion), 1 or 2.
	NAME = 0
	POSTCODE = 1
	DOB = 2
	RATING = 3
	RETURNCODE = 4
	REQUEST_FAILURE = True
	ASSERTION_ERROR = False

	cr = ['', '', '', -1, 2]

	# Check credit rating simulates call to external service
	cr = check_credit_rating (name, postcode, dob)
	try:
		assert cr [NAME] == name and cr [POSTCODE] == postcode and cr [DOB] == dob \
			and (cr [RATING] >= 0 and cr [RATING] <= 600) and \
			(cr[RETURNCODE] >= 0 and cr[RETURNCODE] <= 2)
		if cr[RETURNCODE] == 0:
			doNormalProcessing (cr)
		else:
			do_exception_processing (cr, name, postcode, dob, REQUEST_FAILURE)
	except AssertionError:
			do_exception_processing (cr, name, postcode, dob, ASSERTION_ERROR)

