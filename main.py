import gspread

gc = gspread.service_account()

sh = gc.open("test_cullen")

print(sh.sheet1.get('C2'))