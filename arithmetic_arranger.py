def arithmetic_arranger(problems):
  import re

  arranged_problems = ""
  first_line = ""
  second_line = ""
  third_line = ""

  if (len(problems) > 5):
    return "Error: Too many problems."

  for problem in problems:

    if not ("+" in problem or "-" in problem):
        return "Error: Operator must be '+' or '-'."
    
    if "+" in problem:
      first_op = problem.split("+")[0].strip()
      second_op = problem.split("+")[1].strip()
      operand = "+"
    else:
      first_op = problem.split("-")[0].strip()
      second_op = problem.split("-")[1].strip()
      operand = "-"

    if (re.search("^[0-9]+$",first_op) == None or re.search("^[0-9]+$",second_op) == None):
        return "Error: Numbers must only contain digits."

    if (len(first_op) > 4 or len(second_op) > 4):
        return "Error: Numbers cannot be more than four digits."

    longestLen = len(first_op) if len(first_op) > len(second_op) else len(second_op)

    if len(first_op) == longestLen:
      first_line += "  " + first_op + "    "
      second_line += operand + " " + second_op.rjust(longestLen," ") + "    "
      
    else:
      first_line += first_op.rjust(longestLen+2," ")  + "    "
      second_line += operand + " " + second_op + "    "
    third_line += "".rjust(longestLen + 2, "-") + "    "

    arranged_problems = first_line[:-4] + "\n" + second_line[:-4] + "\n" + third_line[:-4] + "\n"

  return arranged_problems

print(arithmetic_arranger(["32 + 658", "3801 - 2", "45 + 43", "123 + 49"]))