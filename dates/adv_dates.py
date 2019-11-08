from datetime import datetime, timedelta

today = datetime.today()
seven_days_ago = today-timedelta(days=7)
list_days = []
while seven_days_ago < today:
    # process daily transactions for tjis date
    seven_days_ago = seven_days_ago + timedelta(days=1)
    list_days.append(seven_days_ago)
    
print(len(list_days))