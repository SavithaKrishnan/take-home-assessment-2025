# https://www.youtube.com/watch?v=jM-zWp8dNQA-- FastAPI testing
# https://www.youtube.com/watch?v=wMxqlHhCUHg-- data validation

from fastapi.testclient import TestClient
from main import app

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


#validate data types

#make sure the data looks as expected (51 rows, 7 cols)
def test_data_has_correct_shape():
    response = client.get("/voter_reg_deadlines/")
    #track rows that have more or less than 7 columns
    problem_rows = []
    for row in response.json():
        if len(row) != 7: 
            problem_rows.append(row)
    print(problem_rows)
    assert len(response.json()) == 51
    assert len(problem_rows) == 0

# test that column names are as expected
def test_data_has_correct_column_names():
    response = client.get("/voter_reg_deadlines/")
    #track rows that have different columns from expected
    problem_rows = []
    for row in response.json():
        if list(row.keys()) != DB_COL_NAMES:
            problem_rows.append(row)
    print(problem_rows)
    assert len(problem_rows) == 0

# test that state values are unique
def test_state_col_is_unique():
    response = client.get("/voter_reg_deadlines/")
    states = set()
    for row in response.json():
        states.add(row['State'])
    assert len(states) == 51



'''# test that data has correct json schema (correct columns names/order and data types)
def test_data_has_correct_schema():
    response = client.get("/voter_reg_deadlines/")
    problem_rows = []
    for row_object in response.json():
        print(row_object)
        if not validate_json_data(str(row_object).replace("\'", "\""), JSON_SCHEMA):
            problem_rows.append(row_object)
    print(row_object)
    assert len(problem_rows) == 0'''

'''#supporting function (not a test)
def validate_json_data(data, schema):
    try:
        json_data = json.loads(data)
        json_validator = json.JSONValidator(schema)
        json_validator.validate(json_data)
        return True
    except json.JSONDecodeError as e:
        print("Invalid JSON format:", e)
        return False
    except ValidationError as e:
        print("JSON validation error:", e)
        return False'''

'''JSON_SCHEMA = {
    "type": "object",
    "properties": {
        "State": {"type": "string"},
        "Deadline_in_person": {"type": "string", "format": "date"},
        "Deadline_by_mail": {"type": "string", "format": "date"},
        "Deadline_online": {"type": "string", "format": "date"},
        "Election_day_registration": {"type": ["string", "null"]},
        "Online_registration_link": {"type": ["string", "null"]},
        "Description": {"type": ["string", "null"]}
    },
    "required": ["State", "Deadline_in_person", "Deadline_by_mail", "Deadline_online", "Election_day_registration", "Online_registration_link", "Description"]
}'''