import json 
from sheets import get_cullen_events
from autofill import fill_form

# loading in the Event Coordinator's info 
with open("config.json") as f: 
    config = json.load(f)

# calling sheets.py to get the Cullen Event Data from google sheets 
event_data = get_cullen_events()

# testing to see if sheets.py function works -- it does! 
# print(event_data[0])

# testing fill form 
fill_form(event_data[0], config)