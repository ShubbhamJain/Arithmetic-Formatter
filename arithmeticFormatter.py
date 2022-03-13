def arithmetic_arranger(problems, show = False):
  arranged_problems = ''
  firstLine = ''
  secondLine = ''
  thirdLine = ''
  resultLine = ''

  problemLen = len(problems)
  if (problemLen > 5):
    return 'Error: Too many problems.'

  for index, problem in enumerate(problems):
    prob = problem.split()
    operator = prob[1]

    try:
      oprand1 = int(prob[0])
      oprand2 = int(prob[2])
    except Exception:
       return 'Error: Numbers must only contain digits.'

    if ((len(prob[0]) > 4) | len(prob[2]) > 4):
      return 'Error: Numbers cannot be more than four digits.'

    result = 0

    if (operator == '+'):
      result = oprand1 + oprand2
    elif (operator == '-'):
      result = oprand1 - oprand2
    else:
      return 'Error: Operator must be \'+\' or \'-\'.'
    
    result = str(result)

    upperRow = ''
    lowerRow = ''
    alignedUpperRow = ''
    alignedLowerRow = ''
    alignedResultRow = result
    lineRow = ''
    lineRowLen = 2

    if (len(prob[0]) > len(prob[2])):
      upperRow = f'{oprand1}'
      lowerRow = f'{oprand2}'

      alignedUpperRow = upperRow.rjust(len(upperRow) + 2)
      alignedLowerRow = lowerRow.rjust(len(prob[0])-len(prob[2]) + len(lowerRow) + 1)
      alignedResultRow = alignedResultRow.rjust(len(upperRow) + 2)
      lineRowLen += len(prob[0])
    elif (len(prob[0]) < len(prob[2])):
      upperRow = f'{oprand1}'
      lowerRow = f'{oprand2}'

      alignedUpperRow = upperRow.rjust(len(prob[2])-len(prob[0]) + len(upperRow) + 2)
      alignedLowerRow = lowerRow.rjust(len(lowerRow) + 1)
      alignedResultRow = alignedResultRow.rjust(len(lowerRow) + 2)
      lineRowLen += len(prob[2])
    else:
      upperRow = f'{oprand1}'
      lowerRow = f'{oprand2}'
      alignedUpperRow = upperRow.rjust(len(upperRow) + 2)
      alignedLowerRow = lowerRow.rjust(len(lowerRow) + 1)
      alignedResultRow = alignedResultRow.rjust(len(lowerRow) + 2)
      lineRowLen += len(prob[0])
    
    alignedLowerRow = operator + alignedLowerRow

    for line in range(lineRowLen):
      lineRow += '-'
    
    if index != problems[-1]:
      firstLine += alignedUpperRow + '    '
      secondLine += alignedLowerRow + '    '
      thirdLine += lineRow + '    '
      resultLine += alignedResultRow + '    '
    else:
      firstLine += alignedUpperRow
      secondLine += alignedLowerRow
      thirdLine += lineRow
      resultLine += alignedResultRow

  if (show):
    arranged_problems = firstLine.rstrip() + '\n' + secondLine.rstrip() + '\n' + thirdLine.rstrip() + '\n' + resultLine.rstrip()
  else:
    arranged_problems = firstLine.rstrip() + '\n' + secondLine.rstrip() + '\n' + thirdLine.rstrip()
  
  return arranged_problems

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))