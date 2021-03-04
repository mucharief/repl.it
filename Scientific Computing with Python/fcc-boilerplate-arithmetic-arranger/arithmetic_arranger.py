def arithmetic_arranger(data, call = False):
  if len(data) > 5:
    return("Error: Too many problems.")

  numup, oper, numdn, maxsp, answer = ([] for i in range(5))
  for i in data:
    dummy1 = i.split()
    numup.append(dummy1[0])
    oper.append(dummy1[1])
    numdn.append(dummy1[2])
    maxsp.append(max(len(dummy1[0]), len(dummy1[2])))

    if len(dummy1[0]) > 4 or len(dummy1[2]) > 4:
        return "Error: Numbers cannot be more than four digits."

    if dummy1[0].isdigit() is False or dummy1[2].isdigit() is False:
        return "Error: Numbers must only contain digits."

    if "+" in dummy1[1]:
        answer.append(str(int(dummy1[0])+int(dummy1[2])))
    elif "-" in dummy1[1]:
        answer.append(str(int(dummy1[0])-int(dummy1[2])))
    else:
        return "Error: Operator must be '+' or '-'."

  line1, line2, line3, line4 = ("" for j in range(4))
  j = 0
  while j < len(numup):
    line1 += " " * (2 + maxsp[j] - len(numup[j])) + numup[j]
    line2 += oper[j] + " " * (1 + maxsp[j] - len(numdn[j])) + numdn[j]
    line3 += "-" *(2 + maxsp[j])
    line4 += " " * (2 + maxsp[j] - len(answer[j])) + answer[j]
    if j != len(numup) - 1:
        line1 += " " * 4
        line2 += " " * 4
        line3 += " " * 4
        line4 += " " * 4
    j += 1
  linepar = line1 + "\n" + line2 + "\n" + line3
  lineall = line1 + "\n" + line2 + "\n" + line3 + "\n" + line4

  if call is False: 
    return linepar
  else:
    return lineall