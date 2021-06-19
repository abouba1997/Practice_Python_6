import datetime as dt

#1
def nearest_weekend_day(day, month, year):
    date_get = dt.date(year, month, day)
    str_day = date_get.strftime("%a")
    if str_day == "Mon" or str_day == "Tue" or str_day == "Sun":
        return "Sunday"
    else:
        return "Saturday"

#2
def remain_day_to_string(day, month, year):
    date_get = dt.date(year, month, day)
    date_spring_current = dt.date(year, 3, 1) # First day of spring in year
    date_spring_next = dt.date(year + 1, 3, 1) # First day of spring in year
    if (date_spring_current - date_get).days < 0 :
        return str((date_spring_next - date_get).days) + ' days'
    else:
        return str((date_spring_current - date_get).days) + ' days'

#3
def events_shift(schedule, time):
    shifted_events = []
    t = time.split(':')
    time_added = dt.timedelta(hours=int(t[0]),  minutes=int(t[1]))
    for i in schedule:
        tt = i[0].split(':')
        subject = i[1]
        new_time = dt.timedelta(hours=int(tt[0]), minutes=int(tt[1])) + time_added
        shifted_events.append((str(new_time), subject))
    return shifted_events
        

print("\n\n******************** TEST CASES ********************\n")
print("The nearest day to the weekend is : ", nearest_weekend_day(20, 6, 2021))
print("\nThe number of day before spring is: ", remain_day_to_string(1,2,2021))
print("\nThe timetable before shifting\n")
Schedule = [("8:00" ,  "Algebra"), ("9:45", "Geometry"), ("12:10", "Programming"), ("13:45", "Physic")]
print(*Schedule, sep='\n')
print("\nThe shifted timetable\n")
print(*events_shift(Schedule, '2:00'), sep='\n')