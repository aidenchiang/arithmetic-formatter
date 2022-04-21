def arithmetic_arranger(problems, showANS=False):
  arranged_problems = " "
  if (len(problems) > 5):
    return 'Error: Too many problems.'
  for e in problems:
    if (e.find('*') > 0):
      return "Error: Operator must be '+' or '-'."
    if (e.find('/') > 0):
      return "Error: Operator must be '+' or '-'."
    if (e.upper().isupper() == True):
      return "Error: Numbers must only contain digits."
    if (e.find('+') != -1):
      temp = e.split('+')
      if (len(str(temp[0]).strip()) > 4):
        return "Error: Numbers cannot be more than four digits."
      if (len(str(temp[1]).strip()) > 4):
        return "Error: Numbers cannot be more than four digits."
    if (e.find('-') != -1):
      temp = e.split('-')
      if (len(str(temp[0]).strip()) > 4):
        return "Error: Numbers cannot be more than four digits."
      if (len(str(temp[1]).strip()) > 4):
        return "Error: Numbers cannot be more than four digits."
  for e in problems:        # top row 
    if (e.find('+') != -1):
      op = '+'
    if (e.find('-') != -1):
      op = '-'
    temp = e.split(op)
    maxL = max(len(temp[0].strip()), len(temp[1].strip())) + 2
    arranged_problems = arranged_problems + temp[0].rjust(maxL)
    i = 0
    while (i < 4):
      arranged_problems = arranged_problems + " "
      i = i + 1
  arranged_problems = arranged_problems.rstrip()
  arranged_problems = arranged_problems + "\n"
  for e in problems:            # second row
    if (e.find('+') != -1):
      op = '+'
    if (e.find('-') != -1):
      op = '-'
    temp = e.split(op)
    maxL = max(len(temp[0].strip()), len(temp[1].strip())) + 1
    arranged_problems = arranged_problems + op
    arranged_problems = arranged_problems + temp[1].rjust(maxL)
    i = 0
    while (i < 4):
      arranged_problems = arranged_problems + " "
      i = i + 1
  arranged_problems = arranged_problems.rstrip()
  arranged_problems = arranged_problems + "\n"
  for e in problems:
    if (e.find('+') != -1):
      op = '+'
    if (e.find('-') != -1):
      op = '-'
    temp = e.split(op)
    maxL = max(len(temp[0].strip()), len(temp[1].strip())) + 2
    i = 0
    while (i < maxL):
      arranged_problems = arranged_problems + "-"
      i = i + 1
    i = 0
    while (i < 4):
      arranged_problems = arranged_problems + " "
      i = i + 1
  arranged_problems = arranged_problems.rstrip()
  if (showANS == True):
    arranged_problems = arranged_problems + "\n"
    for e in problems:
      soln = None
      if (e.find('+') != -1):
        op = '+'
      if (e.find('-') != -1):
        op = '-'
      temp = e.split(op)
      maxL = max(len(temp[0].strip()), len(temp[1].strip())) + 2
      if (e.find('+') != -1):
        soln = int(temp[0]) + int(temp[1])
      if (e.find('-') != -1):
        soln = int(temp[0])- int(temp[1])
      arranged_problems = arranged_problems + str(soln).rjust(maxL)
      i = 0
      while (i < 4):
        arranged_problems = arranged_problems + " "
        i = i + 1
  arranged_problems = arranged_problems.rstrip()
  return arranged_problems