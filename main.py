# event coordinator's info
import json 
# google sheets data 
from sheets import get_cullen_events
# autofilling the form 
from autofill import fill_form
# filtering dates 
from datetime import datetime

# loading in the Event Coordinator's info 
def load_config(): 
    with open("config.json") as f: 
        return json.load(f)

def pick_cutoff(): 
    date_input = input("Show events from what date to beyond? (MM/DD/YYYY) or press Enter for all upcoming: ").strip()
    if date_input: 
        try:
            return datetime.strptime(date_input, "%m/%d/%Y")
        except ValueError: 
            print("Invalid date format, showing all upcoming events instead.")
            return None 
    return None 

def show_menu(events): 
    print("\n===============================================")
    print("Upcoming events (Cullen College of Engineering):\n")
    for i, event in enumerate(events, 1): 
        print(f"    [{i}] {event['date']} - {event['title']}")
    print("\n===============================================")

def pick_event(events): 
    while True: 
        try: 
            choice = int(input("\nPick an event: "))
            if 1 <= choice <= len(events): 
                return events[choice-1]
            else: 
                print(f"Please enter a number between 1 and {len(events)}.")
        except ValueError: 
            print("Please enter a valid number.")



# calling sheets.py to get the Cullen Event Data from google sheets 

# testing to see if sheets.py function works -- it does! 
# print(event_data[0])

# testing fill form 

def main(): 
    print("================")
    print("SASE Room Booker")
    print("================")

    config = load_config()
    cutoff = pick_cutoff()
    events = get_cullen_events(cutoff)

    if not events: 
        print("\nNo upcoming events found for Cullen College of Engineering")
        return 
    
    while True: 
        show_menu(events)
        event = pick_event(events)

        print(f"\nOpening form for: {event['title']} on {event['date']}")
        fill_form(event, config)

        another = input("\nBook another event? (y/n): ").strip().lower()
        if another != "y": 
            print("\nDone! Goodbye!")
            break
    
if __name__ == "__main__": 
    main()