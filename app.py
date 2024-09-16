itemsU = ['California', 'Alaska', 'Hawaii', 'Oregon', 'Washington']
itemsL = ['california', 'alaska', 'hawaii', 'oregon', 'washington']
input = input('Enter a state: ')
print()
input = input.casefold()
if input in itemsL:
  n = 0
  while itemsL[n] != input:
    n += 1
  if n == 0:
    suffix = 'st'
  elif n == 1:
    suffix = 'nd'
  elif n == 2:
    suffix = 'rd'
  else:
    suffix = 'th'
  print(itemsU[n], 'is the', str(n + 1) + '%s term in the list.' % suffix)
else:
  print('The item is not in the list.')
