files=input()
arr=[]
for i in range(len(files)):
  arr.append((files[i],i))

t=[]
result=[]

for word,rank in arr:
  sign=[' ','.','-']
  a=[i for i in range(65,91)]
  b=[i for i in range(97,123)]
  S=sign+a+b

for i in range(len(word)):
    if (ord(word[i]) not in S) and (word[i] not in S):
      start_num_index=i
      for j in range(start_num_index,len(word)):
        if word[j] in S:
          end_num_index=j
          break
    break

head=word[:start_num_index].lower()
num=int(word[start_num_index:end_num_index])
tail=word[end_num_index:].lower()
t.append((head,num,tail,rank))
t=sorted(t,key=lambda x:(x[0],x[1],x[3]))

for h,n,t,r in t:
    result.append(h+str(n)+t)

print(result)




  


