 
word=list("woeiwoq111.py")
 
for i in range(len(word)):
  if (ord(word[i]) not in S) and (word[i] not in S):
    start_num_index=i
    for j in range(start_num_index,len(word)):
        if word[j] in S:
            end_num_index=j
            break
        break

print(start_num_index,end_num_index)