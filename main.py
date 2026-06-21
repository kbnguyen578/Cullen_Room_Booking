import json 
from sheets import get_cullen_events

# loading in the Event Coordinator's info 
with open("config.json") as f: 
    config = json.load(f)

event_data = get_cullen_events()

# testing to see if sheets.py function works -- it does! 
# print(event_data[0])
