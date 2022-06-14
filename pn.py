import pandas as pd

data = pd.read_csv('/home/ronit/Documents/test.csv')
s = data.head(7)
h = s.columns[0]
s['result'] = "0"
s['matched']="NOT_MATCHED"
# dic = {'result':[]}
col = s[h]

# print(h)
# print(col)

l = col.astype(str).str.split(' ')
# print(l)
list1 = ['45','555','232','1213','2225','6646']
k =[]
for j in list1:
    for index,i in enumerate(l):
        if j in i:
           s['result'].loc[index] = "1"
           s['matched'].loc[index] =j
        #    print(y)
        

# print(len(k))
# print(dic)
print(s)
newcol = s['result']
# print(newcol)
one = []
zero =[]
for i,rows in newcol.iteritems():
    if rows == '1':
        # print(i,rows)
        one.append(rows)
    if rows == '0':
    
        # print(i,rows)
        zero.append(rows)
# data.to_csv('new.csv',sep=',',encoding='utf_8')

print('------')
print(len(one),'=','1')
print(len(zero),'=','0')

