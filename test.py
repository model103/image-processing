def is_bab(s):
  flag = True
  for i in range(len(s)):
    if s[len(s)-i-1] != s[i]:
      flag = False
  return flag

def find_longtes(s):
  bob =[]
  length =[]
  for i in range(len(s)):
    for j in range(i,len(s)):
      if is_bab(s[i:j]):
        bob.append(s[i:j])
        length.append(j-i)
  max_length = max(length)
  index = length.index(max_length)
  return bob[index], max_length

s = 'aaabbbaaaccc'
print(find_longtes(s))