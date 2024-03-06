import doNormalProcessing

import os
import datetime

def log_error(message, data, error_type):
    # Log the error with a timestamp. For the purpose of this example,
    # we will just print it to the console. In a real application, you would
    # write this to a file or an error logging service.
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{timestamp} - ERROR - {error_type}: {message} - Data: {data}")

def do_exception_processing(cr_data, name, postcode, dob, error_type):
    # Define what constitutes request failure or assertion error
    REQUEST_FAILURE = "Request Failure"
    ASSERTION_ERROR = "Assertion Error"

    # Log the error first
    if error_type == REQUEST_FAILURE:
        log_error("Credit check request failed", cr_data, REQUEST_FAILURE)
    elif error_type == ASSERTION_ERROR:
        log_error("Data assertion error", cr_data, ASSERTION_ERROR)
    
    # Handle the error, e.g., by cleaning up, sending notifications, etc.
    # The specific actions depend on business requirements.
    # For instance, you might want to:
    # - Notify the user that an error occurred
    # - Retry the operation if applicable
    # - Revert any partial changes made during the process

    # For this example, let's just print out what might be done.
    if cr_data[4] == 1:
        print("Notifying user of credit check failure due to external service issue.")
    elif cr_data[4] == 2:
        print("Notifying user of credit check failure due to internal data handling issue.")
    else:
        print("Unknown error code. Investigating the issue.")

    # Clean up any resources if necessary
    # For example, you might want to delete any temporary files created
    # during the process or release any held resources.
    
    # Since there's no mention of specific resources to clean up in the provided code,
    # this is a placeholder for such actions.
    print("Clean up any allocated resources.")

# This function should be called with the necessary parameters when an exception occurs.
# For example:
# do_exception_processing(['John Doe', '12345', '1980-01-01', 500, 1], 'John Doe', '12345', '1980-01-01', REQUEST_FAILURE)


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

