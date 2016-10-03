from datetime import date, timedelta

start_date = date(1901,1,1)
end_date = date(2000,12,31)

current_date = start_date
count = 0
while current_date.weekday()!=6: current_date+=timedelta(days=1)
while current_date <= end_date:
    if current_date.day == 1:
        count+=1
        print(current_date.strftime('%A, %d/%b/%Y'))
    current_date+=timedelta(days=7)

print(count)