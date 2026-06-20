# accessing the google sheets API
import gspread

# EVENT COORDINATOR INFO - Edit this to your own information 
ec_first    =  John
ec_last     =  Doe 
ec_email    = jdoe@email.com 
ec_psid     = 1234567 
org         = SASE  # NEVER CHANGE THIS!!!

# opening up the google sheets 
gc = gspread.service_account()
SPREADSHEET_NAME = "test_cullen"
sh = gc.open(SPREADSHEET_NAME)  # this is the ENTIRE wksh 
worksheet = sh.sheet1           # this is the specific tab we work with 

# testing -- it works! 
print(sh.sheet1.get('C2'))

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

all_rows = worksheet.get_all_values() 
TARGET_BUILDING = "Cullen College of Engineering Building"
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

print(event_data[0])
