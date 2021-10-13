def add_time(start, duration, day=None):

  # initialization of vars
  start_time = start.split()[0]
  am_pm = start.split()[1]
  start_hour = int(start_time.split(":")[0])
  start_mins = int(start_time.split(":")[1])

  duration_hour = int(duration.split(":")[0])
  duration_mins = int(duration.split(":")[1])

  day_output = ""
  day_index = -1

  days_list = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
  if day is not None:    
    day_index = days_list.index(day.capitalize())

  # compute total minutes
  total_mins = start_mins + duration_mins
  add_hour = False
  if total_mins > 59:
    total_mins -= 60
    add_hour = True

  # if overflow from minutes, add to hours
  if add_hour:
    total_hours = start_hour + duration_hour + 1
  else:
    total_hours = start_hour + duration_hour

  # if PM, add 12 hours
  if am_pm == "PM":
    total_hours += 12

  no_of_days = total_hours // 24
  total_hours = total_hours % 24
  
  if total_hours < 12:
    am_pm = "AM"
    if total_hours == 0:
      total_hours = 12
  else:
    am_pm = "PM"
    if total_hours != 12:   
      total_hours = total_hours % 12 

  if no_of_days == 1:
    day_output = " (next day)"
  elif no_of_days > 1:
    day_output = " ({} days later)".format(no_of_days)

  day_index = (day_index + no_of_days) % 7 

  if day is not None:
    new_time = str(total_hours) + ":" + str(total_mins).zfill(2)  + " " + am_pm + ", " + days_list[day_index] + day_output
  else:
    new_time = str(total_hours) + ":" + str(total_mins).zfill(2)  + " " + am_pm + day_output

  return new_time