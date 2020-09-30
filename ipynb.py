#!/usr/bin/env python
# coding: utf-8

# In[17]:


import csv
f=open('gender.csv')
data=csv.reader(f)

m= []
f=[]
count=0
line=[]

name= input('찾고싶은 지역의 이름을 알려주세요: ')
for row in data :
    
    if name in row[0]:
        #이름이 있으면 새로운 리스트에 row[0]을 넣어라 
        count=count+1
        print(row[0])

        
if(count>=2):
    same=input('정확한 지역명 입력:')
    for same in row[0]:
        for i in row[3:104]:
            m.append(-int(i))
        for i in row[106:]:
            f.append(int(i))
        break
else:
    for name in row[0]:
            for i in row[3:104]:
                m.append(-int(i))
            for i in row[106:]:
                f.append(int(i))
            break
    
    
        
    
import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.figure(figsize=(10,5),dpi=300)
plt.rc('font',family='Malgun Gothic')
plt.rcParams['axes.unicode_minus']= False
plt.title(name+'지역의 남녀 성별 인구 분포')
plt.barh(range(101),m,label='남성')
plt.barh(range(101),f,label='여성')
plt.legend()
plt.show()    
    
        
            
              

    
    


# In[ ]:




