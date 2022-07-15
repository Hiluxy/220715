def solution(files):
  arr=[]
  t=[]
  answer=[]
  S=[' ','.','-']+[i for i in range(97,123)]

  for i in range(len(files)):
    arr.append((files[i].lower(),i))


  for word,rank in arr:

    #word에서 숫자 시작/끝 인덱스 구함
    for i in range(len(word)):
        if (ord(word[i]) not in S) and (word[i] not in S):
          start_num_index=i
          for j in range(start_num_index,len(word)):
            if word[j] in S:
              end_num_index=j
              break
        break
    
    #head/num/tail로 나눔
    head=word[:start_num_index].lower()
    num=int(word[start_num_index:end_num_index])
    tail=word[end_num_index:].lower()

    #t=[(),(),()] 만들기
    t.append((head,num,tail,rank))
  
  t=sorted(t,key=lambda x:(x[0],x[1],x[3]))

  for h,n,t,r in t:
    if r==rank:
      answer.append(word)
    
  return answer


re=solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"])
print(re)