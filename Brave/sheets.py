# accessing the google sheets API
import gspread
# for filtering events already passed/done 
from datetime import datetime 

# testing -- it works! 
# print(sh.sheet1.get('C2'))

# columns + their field 
# title_col = 'C'       | [2] 
# date_col = 'D'        | [3]
# desc_col = 'E'        | [4] 
# start_time_col = 'F'  | [5]
# end_time_col = 'G'    | [6] 
# loc_1_col = 'P'       | [15]
# loc_2_col = 'Q'       | [16]
# loc_3_col = 'R'       | [17]
# building_col = 'H'    | [7] (0-based)

TARGET_BUILDING = "Cullen College of Engineering Building"
SPREADSHEET_NAME = "test_cullen"
GSPREAD_CREDENTIALS_FILENAME = "service_account.json"


def get_cullen_events(cutoff=None): 
    # opening up the google sheets 
    print("In sheets.py")
    gc = gspread.service_account(filename=GSPREAD_CREDENTIALS_FILENAME)
    sh = gc.open(SPREADSHEET_NAME)  # this is the ENTIRE wksh 
    worksheet = sh.sheet1           # this is the specific tab we work with  
    print("Opened Google Sheets successfully.")

    # gets data for ALL events 
    all_rows = worksheet.get_all_values() 
    today = datetime.today()

    events = []

    #  retrieve data for only Cullen College forms, ignore the header row 
    for row in all_rows[1:]: 
        # get only cullen building events 
        if row[7] != TARGET_BUILDING:
            continue 
        
        try: 
            event_date = datetime.strptime(row[3], "%m/%d/%Y")
            # print (event_date)
        except ValueError: 
            continue 
        
        # event passed already--skip! 
        # if event_date < today: 
        #     continue 
        
        if cutoff and event_date < cutoff: 
            continue 

        
        events.append({
            "title":        row[2], 
            "date":         row[3], 
            "desc":         row[4],
            "start_time":   row[5], 
            "end_time":     row[6], 
            "loc_1":        row[15], 
            "loc_2":        row[16], 
            "loc_3":        row[17]
        })
    
    return events

# test to see for loop works -- it does! 
# print(event_data[0])
