import json 
from sheets import get_cullen_events

# loading in the Event Coordinator's info 
with open("config.json") as f: 
    config = json.load(f)

event_data = get_cullen_events()

print(event_data[0])
