def add_time(begin, duration, opday=None):
  infday = None
  forday = None

  if opday is not None:
    forday = (opday.lower()).capitalize()

  refday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

  dtime = begin.split()
  intime = dtime[0].split(":")
  durtime = duration.split(":")
  intime = [int(i) for i in intime]
  durtime = [int(i) for i in durtime]
  if "PM" in dtime[1]:
    intime[0] += 12

  fintime = [intime[i] + durtime[i] for i in range(2)]

  if fintime[1] >= 60:
    #Added hour
    fintime[0] += (fintime[1] // 60)
    #Remaining minute
    fintime[1] %= 60

  nday = (fintime[0] - (fintime[0] % 24)) // 24

  if fintime[0] > 24:
    #Remaining hour
    if fintime[0] % 24 == 0:
        fintime[0] = fintime[0] % 24 + 24
    else:
        fintime[0] %= 24
  
  if nday == 1:
    infday = "(next day)"
  elif nday > 1:
    infday = "({} days later)"
    
  if fintime[0] > 12:
    fintime[0] -= 12
    if fintime[0] == 12:
        fin12 = "AM"
    else:
        fin12 = "PM"
  else:
    if fintime[0] == 12:
        fin12 = "PM"
    else:
        fin12 = "AM"

  if forday is not None and nday > 0:
    forday = refday[(refday.index(forday) + nday) % 7]

  finish = str(fintime[0]) + ":" + str("{:02d}".format(fintime[1])) + " " + fin12
  if forday is not None:
    finish += ", " + forday
  if infday is not None:
    finish += " " + infday.format(nday)

  return finish