# SL/VF Technical Take Home

> Build a state voter registration search tool

- [Evaluation](#evaluation)
- [What we are looking for](#what-we-are-looking-for)
- [Submitting your code](#submitting-your-code)
- [Questions or Concerns](#questions-or-concerns)
- [Running the code](#running-the-code)

## Evaluation

1. Using the provided voter_registration_deadlines.csv, use the language and ORM framework of your choice to parse and store the info from voter_registration_deadlines.csv for each state into a sql database (This is already done in the sample provided). This is a sample of old data taken from various voter registration sites in 2018, and does not represent the current reality of these states. It should only be used for the purposes of this exercise.
2. Create a UI that displays the list of all the states and their voter information. The user should be able to filter and sort this table.
3. Create an api endpoint that will retrieve the data for this table from the backend DB.
4. Write tests to validate the api call(s).
5. Include a Readme (Or add to this one if you choose to clone this repo) that describes the steps necessary for building and running the application as well as running the tests locally.

You may use any pattern or library that you find suitable to accomplish this assessment. Internally, we use Python and SQL Alchemy (SwingLeft) or NodeJS and Knex (VoteForward) backend and for the frontend we use React with Panda-UI and Chakra-UI for styling on the Next.Js framework.

Additionally, we have provided a sample hello-world framework which you may modify and use for this exercise. This sample already imports the voter data into a postgres DB, and sets up an API endpoint and frontend page for you to work from or use as an example.

Alternatively, you may submit an equivalent open-source code sample you have written. If you choose to go with this route, please include as much detail as possible about which factors of your sample we should evaluate, and be prepared to discuss your code sample in the follow-up interview.

## What we are looking for

- Does it work?
- Is the code clean and accessible to others?
- Does the code handle edge case conditions?

For the UX, we do not expect a fancy graphic design or style, but please make sure that the UI is clean and usable on both desktop and mobile web browsers.

## Time Limit

The purpose of the test is not to measure the speed of code creation. Please try to finish by the end of Wednsday, June 25, but extra allowances are fine and will not be strictly penalized.

## Submitting Your Code

The preferred way to submit your code is to create a fork of this repo, push your changes to the forked repo, and then open a pull request for the new commit.
Alternatively, you may submit the code in the form of a zip file and send it to dcarden@swingleft.org. If you do this, please be sure to include a README in your submission with full details on how to set up and run your code.

## Questions or Concerns

If you have any questions at all, feel free to reach out to [dcarden@swingleft.org](mailto:dcarden@swingleft.org)

## Running The Code

[If you choose to clone this repo and work from the hello-world sample, please use the directions below. If you implement another solution using a different language or framework, please update these directions to reflect your code.]

### Installation

1. Pull down the repo.
2. Open a terminal.
3. `npm install --no-save`
4. `npm run db:create-db`
5. `npm run dev`
6. Open a new terminal.
7. `pip install -r requirements.txt`
8. Navigate to the `new_api` folder (`cd src/app/api/new_api`).
9. `uvicorn main:app --reload`
10. To run API call validation tests, tests can be found in `test_main.py` (`take-home-assessment-2025/src/app/api/new_api/test_main.py`). Open a new terminal and run `pytest`.



