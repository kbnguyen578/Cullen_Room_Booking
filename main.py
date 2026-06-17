# accessing the google sheets API
import gspread

# opening up the google sheets 
gc = gspread.service_account()
SPREADSHEET_NAME = "test_cullen"
sh = gc.open(SPREADSHEET_NAME)

# testing -- it works! 
print(sh.sheet1.get('C2'))

# columns + their field 
title_col = 'C'
date_col = 'D'
desc_col = 'E'
start_time_col = 'F'
end_time_col = 'G'
loc_1_col = 'P'
loc_2_col = 'Q'
loc_3_col = 'R'
building_col = 'H'

