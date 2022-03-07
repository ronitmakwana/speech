import pandas as pd

import geopandas as gpd


file = pd.read_excel('/home/ronit/Downloads/keyword/Station.xls', sheet_name="14.02.22")
# print(file)
# file.loc[0:]
f = file[['Abnormalities/ Deficiencies found ( In Brief)','Department/Area inspected Such as Loco/Coach/Track/Station etc.']]
f
# list =[]
# for i in f:
#     list.append(f)
# #     print(list[:-1])
    
# k = list[:-1]
# k
# for i in f:
#     print(i)
# cols  = file.columns.to_list()
# col = cols[7]
# print(col)
# print('---------------------------------------------')
# list =[]
data = f['Abnormalities/ Deficiencies found ( In Brief)']
# # print(data)
# list.append(data)
# list
# for i in list:
#     k = i[81]
#     s = k.split(' ')
#     print(s)
#     if 'Broken' in s:
#         print('matched')
#         print(k)
#     else:
# #         print('matched not')

list1 = data.astype(str).str.split(' ')
# list1
lo = []
match = ['broken']
for matches in match:
#     print(matches)
    print('----------')
    for i,index in enumerate(list1):
        
#         print(i)
        if  matches in index:
            
            x = ' '.join(index)
            print(i,'======>',x)
#             print('----------')
            print('matched')
            print('-----------')
#             f = file[['Abnormalities/ Deficiencies found ( In Brief)','Department/Area inspected Such as Loco/Coach/Track/Station etc.']]
         
            l = file.loc[i]
            fd = l[6]
            lo.append(fd)

            df = pd.DataFrame(data=l)
            df1_transposed = df.T
print(lo)
# file = 'keywprds.txt'
# with open(file,'a') as f:
#     f.write(str(lo))
#     print('=======saved=======')
# for il in lo:
#     print(il)
#             print(df1_transposed)
#             li = []
#             lo.append(df1_transposed)
#             print(li)
#             for ll in li:
#                 print(ll[0:2])
# for kk in lo:

#     df1 = pd.DataFrame(data=kk)
# # df1 = df1.T
#     print (df1)

# for i,index in enumerate(list1):
#     d = i,index
# #     print(d)
#     k = index[81:93]
#     for ik in k:
# #         print(ik)
    
# #         s = ik.split(' ')
#     #     print(s)
#         if 'Broken' in s:
#             print('matched')
#             print(k)
#         else:
#             print('matched not')


# import pandas as pd
  
    
# fo = pd.read_csv('keywprds.txt')
# # fo
# # print(fo)
# list = [""]
# for ff in fo:
# #     print(len(ff))
#     spl = ff.split(" ")
#     spl.pop(0)
#     #print(spl)
#     for sp in spl:
        
#         st= str(sp)
#         re = st.replace("]",' ')
#         rep = re.replace("'"," ")
     
#         list.append(rep)
# print(type(list))
# conset = set(list)
# print(conset)
# for ll in list:
#     print(ll)
# conset = set(lo)
# sc = lo.split(" ")
listofdata= []
for lll in lo:
    sc = lll.split(" ")
    print(sc)
#     print(conset)
    gf = gpd.read_file('/home/ronit/Downloads/keyword/IR STATION MASTER MEITY.shp')
    d =gf.columns[4]
    data = gf[d]

    # dl = []
    # dl.append(data)
    # print(dl)

    list1 = data.astype(str).str.split(' ')
    # print(list1)
    for con in sc:
#         print(con)

    # # data
        for dx,cons in enumerate (list1):
    #         print(dx,cons)
    #     for dm,i in e/numerate(data,0):
    #         print(i)
            if con in cons:
#                 print('matched-----------------------------------------------------yyyyyyyyyyyyyyyyy')
                y = ' '.join(cons)
#                 print(y)
               
                lc = gf.loc[dx]
#                 cols = lc[8]
#                 print(lc,'==========================================')
                listofdata.append(lc)
# print(listofdata)
dataframes = pd.DataFrame(data=listofdata)
print(dataframes)
print('-----------')

print("Searching finished")

