# accessing the google sheets API
import gspread

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


def get_cullen_events(): 
    # opening up the google sheets 
    gc = gspread.service_account(filename=GSPREAD_CREDENTIALS_FILENAME)
    sh = gc.open(SPREADSHEET_NAME)  # this is the ENTIRE wksh 
    worksheet = sh.sheet1           # this is the specific tab we work with  

    # gets data for ALL events 
    all_rows = worksheet.get_all_values() 

    event_data = []

    #  retrieve data for only Cullen College forms, ignore the header row 
    for row in all_rows[1:]: 
        if row[7] == TARGET_BUILDING: 
            event_data.append({
                "title":        row[2], 
                "date":         row[3], 
                "desc":         row[4],
                "start_time":   row[5], 
                "end_time":     row[6], 
                "loc_1":        row[15], 
                "loc_2":        row[16], 
                "loc_3":        row[17]
            })
    
    return event_data

# test to see for loop works -- it does! 
# print(event_data[0])
