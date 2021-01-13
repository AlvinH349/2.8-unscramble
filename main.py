def unscramble(str):
  matchlist = []
  sortstr = ''.join(sorted(str))

  listfile = open('test.txt', 'r') 

  for word in listfile:
    sortword = ''.join(sorted(word)).strip()

    if sortstr == sortword:
      matchlist.append(word.replace('\n',''))
  
  return matchlist

inputw = input("Input a string: ")
ml = unscramble(inputw)
print(ml)