from fastapi.testclient import TestClient
from main import app
import datetime

# globals for correct column names and schemas
DB_COL_NAMES = ['State', 'Deadline_in_person', 'Deadline_by_mail', 'Deadline_online', 'Election_day_registration', 'Online_registration_link', 'Description']
TEST_JSON = {
    "State" : "Puerto Rico",
    "Deadline_in_person": "2018-10-08",
    "Deadline_by_mail": "2018-10-10", 
    "Deadline_online": "2018-10-12",  
    "Election_day_registration": "", 
    "Online_registration_link": "https://en.wikipedia.org/wiki/Puerto_Rico", 
    "Description": "Postmarked or submitted 30 days before the election."
}

client = TestClient(app)

#supporting function, not a test
def is_valid_date_format(date_string, date_format):
    """
    Determines if string is in valid date format.

    Args:
        date_string (str): date string to test
        date_format (str): date format to test string against

    Returns
        boolean: whether or not string is in date format
    """
    try:
        datetime.datetime.strptime(date_string, date_format)
        return True
    except ValueError:
        return False

#make sure we get a 200 status code for response
def test_response_status_code():
    response = client.get("/voter_reg_deadlines/")
    assert response.status_code == 200

#make sure response time stays below 1s
def test_response_time_below_one_sec():
    response = client.get("/voter_reg_deadlines/")
    assert response.elapsed.total_seconds() < 1

#make sure user is unable to add data to database through api call
def test_user_unable_to_push_data_to_db():
    response = client.put("/voter_reg_deadlines/", json = TEST_JSON)
    assert response.status_code == 405

#make sure the data looks as expected (51 rows, 7 cols)
def test_response_has_correct_shape():
    response = client.get("/voter_reg_deadlines/")
    #track rows that have more or less than 7 columns
    problem_rows = []
    for row in response.json():
        if len(row) != 7: 
            problem_rows.append(row)
    assert len(response.json()) == 51
    assert len(problem_rows) == 0

# test that column names are as correct and in order
def test_data_has_correct_column_names():
    response = client.get("/voter_reg_deadlines/")
    #track rows that have different columns from expected
    problem_rows = []
    for row in response.json():
        if list(row.keys()) != DB_COL_NAMES:
            problem_rows.append(row)
    assert len(problem_rows) == 0

# test that state values are unique and strings
def test_state_col_is_unique_string_values():
    response = client.get("/voter_reg_deadlines/")
    states = set()
    problem_states = []
    for row in response.json():
        states.add(row['State'])
        if not isinstance(row['State'], str):
            problem_states.append(row['State'])
    assert len(states) == 51
    assert len(problem_states) == 0

# test that the date columns (Deadline_in_person, Deadline_by_mail, Deadline_online) are strings in date format
def test_date_cols_are_strings_in_date_format():
    response = client.get("/voter_reg_deadlines/")
    deadline_in_person = {}
    deadline_by_mail = {}
    deadline_online = {}
    for row in response.json():
        if not is_valid_date_format(row['Deadline_in_person'], "%Y-%m-%d"):
            deadline_in_person[row['State']] = row['Deadline_in_person']
        if not is_valid_date_format(row['Deadline_by_mail'], "%Y-%m-%d"):
            deadline_by_mail[row['State']] = row['Deadline_by_mail']
        if not is_valid_date_format(row['Deadline_online'], "%Y-%m-%d"):
            deadline_online[row['State']] = row['Deadline_online']
    assert len(deadline_in_person) == 0
    assert len(deadline_by_mail) == 0
    assert len(deadline_online) == 0