#2.Find anagrams in a huge text. 
#Input:“the cat act in tic tac toe.”
#Output: cat, tac, act

#Josephine.nakka
#importing default dic
from collections import defaultdict

#formating list of words
def anagram(candidates):
  table = defaultdict(list)
 #sorting each word  
  for e in candidates:
    table[''.join(sorted(e.lower()))].append(e)

  return [v for k,v in table.items() if len(v) > 1] 
#arry of words need to find anagarms
if __name__ == '__main__':
    print(anagram(["the", "cat", "act", "in", "tic", "tac", "toe"]))
    

