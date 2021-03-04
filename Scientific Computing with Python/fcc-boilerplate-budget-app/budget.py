class Category:
  def __init__(item, catname):
    item.catname = catname
    item.ledger = []

  def deposit(item, amount, description=""):
    item.ledger.append({"amount": amount, "description": description})

  def get_balance(item):
    sum = 0
    for i in item.ledger:
      sum += i["amount"]
    return sum

  def check_funds(item, amount):
    if (item.get_balance() >= amount):
      return True
    else:
      return False

  def withdraw(item, amount, description=""):
    if item.check_funds(amount) is True:
      item.ledger.append({"amount": -1 * amount, "description": description})
      return True
    else:
      return False

  def transfer(item1, amount, item2):
    if item1.check_funds(amount) is True:
      item1.ledger.append({"amount": -1 * amount, "description": "Transfer to " + item2.catname})
      item2.ledger.append({"amount": amount, "description": "Transfer from " + item1.catname})
      return True
    else:
      return False

  def __str__(item):
    star = (30 - len(item.catname)) // 2
    line = "*" * star + item.catname + "*" * (30 - star - len(item.catname)) + "\n"
    for i in range(len(item.ledger)):
      a = (item.ledger[i])["description"]
      b = float((item.ledger[i])["amount"])
      bb = "{:.2f}".format(b)
      line += a[:23] + " " * (23 - len(a)) + " " * (7 - len(bb)) + bb + "\n"
    line += "Total: " + str(item.get_balance())
    return line

def create_spend_chart(chart):
  sumwd = []
  lentab = []
  for k in chart:
    lentab.append(len(k.catname))
    for i in range(len(k.ledger)):
      if (k.ledger[i])["amount"] < 0:
        sumwd.append(-1 * (k.ledger[i])["amount"])

  totalsum = sum(sumwd)
  percent = []
  for j in range(len(sumwd)):
    sum100 = int(100 * sumwd[j] / totalsum)
    leftover = sum100 % 10
    sum100 -= leftover
    percent.append(sum100)

  line = "Percentage spent by category\n"
  for l in range(12 + max(lentab)):
    if l < 11:
      number = str(100 - 10 * l)
      line += " " * (3 - len(number)) + number + "| "
      for m in range(len(chart)):
        if percent[m] < int(number):
          line += "   "
        else:
          line += "o  "
      line += "\n"
    elif l == 11:
      line += " " * 4 + "-" * (1 + len(chart) * 3) + "\n"
    else:
      n = l - 12
      line += " " * 5
      for p in chart:
        if n < len(p.catname):
          line += p.catname[n] + "  "
        else:
          line += "   "
      if l < (11 + max(lentab)):
        line += "\n"

  return line