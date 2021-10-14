import math

class Category:

  def __init__(self, category_name):
    self.category_name = category_name
    self.ledger = []

  def check_funds(self, amount):
    current_funds = 0
    for transactions in self.ledger:
      current_funds += transactions["amount"]

    if amount > current_funds:
      return False
    else:
      return True

  def deposit(self, amount, desc=""):
    self.ledger.append({"amount": amount, "description": desc })

  def withdraw(self, amount, desc=""):
    check = self.check_funds(amount)
    amount = -abs(amount) 
    if check:
      self.ledger.append({"amount": amount, "description": desc })
    return check

  def get_balance(self):
    current_funds = 0
    for transactions in self.ledger:
      current_funds += transactions["amount"]
    return current_funds

  def transfer(self, amount, transfer_category):
    tx_amount = -abs(amount) 

    check = self.check_funds(amount)
    if check:
      self.ledger.append({"amount": tx_amount, "description": "Transfer to {}".format(transfer_category.category_name)})
      transfer_category.ledger.append({"amount": amount, "description": "Transfer from {}".format(self.category_name)})
    return check

  def __str__(self):
    stars_len = (30 - len(self.category_name)) // 2
    output_line = "".rjust(stars_len, "*") + self.category_name + "".ljust(stars_len, "*") + "\n"

    total = 0
    for transactions in self.ledger:
      output_line += transactions["description"][:23].ljust(23, " ") + ('{0:.2f}'.format(transactions["amount"])).rjust(7, " ") + "\n"
      total += transactions["amount"]

    output_line += "Total: {}".format(total)
    return output_line


def create_spend_chart(categories):

  total_value = 0
  category_list = []
  category_value = []
  percentage = []

  for category in categories:
    category_list.append(category.category_name)
    value = 0
    for transactions in category.ledger:
      if transactions["amount"] < 0: # withdrawal
        value += transactions["amount"]
    category_value.append(value)
    total_value += value
  
  for value in category_value:
    percentage.append(math.floor(abs(value)/abs(total_value)*10)*10)

  output_line = "Percentage spent by category\n"
  for index in range(100,-1,-10):
    line = str(index).rjust(3," ") + "|"
    for idx,pct in enumerate(percentage):
      if pct >= index and idx == 0:
        line += " o"
      elif pct >= index:
        line += "  o"
      elif idx == 0:
        line += "  "
      else:
        line += "   "
    line = line.ljust(14, " ")
    output_line += line + "\n"

  output_line += "    ----------\n"

  longest_str = len(max(category_list, key=len))
  for i in range(0, longest_str):
    line = "   "
    for name in category_list:      
      if i < len(name) and idx == 0:
        line += " " + name[i]
      elif i < len(name):
        line += "  " + name[i]
      elif idx == 0:
        line += "  "
      else:
        line += "   "

    line = line.ljust(14, " ")
    output_line += line + "\n"

  output_line = output_line[:-1]
  return output_line