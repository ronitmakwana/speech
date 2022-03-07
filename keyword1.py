# import pandas as pd
# import geopandas as gpd


# file = pd.read_excel('/home/ronit/Downloads/keyword/Station.xls', sheet_name="14.02.22")
# # print(file)
# # file.loc[0:]
# f = file[['Abnormalities/ Deficiencies found ( In Brief)','Department/Area inspected Such as Loco/Coach/Track/Station etc.']]

# data = f['Abnormalities/ Deficiencies found ( In Brief)']


# list1 = data.astype(str).str.split(' ')
# # list1
# lo = []
# match = ['broken']
# for matches in match:
# #     print(matches)
#     print('----------')
#     for i,index in enumerate(list1):
        
#         # print(i)
#         if  matches in index:
            
#             x = ' '.join(index)
#             # print(i,'======>',x)
# #             print('----------')
#             # print('matched')
#             # print('-----------')
# #             f = file[['Abnormalities/ Deficiencies found ( In Brief)','Department/Area inspected Such as Loco/Coach/Track/Station etc.']]
         
#             l = file.loc[i]

#             fd = l[6]
#             lo.append(fd)

#             # df = pd.DataFrame(data=l)
#             # df1_transposed = df.T
# print(lo)

# listofdata= []
# for lll in lo:
#     sc = lll.split(" ")
#     # print(sc)
# #     print(conset)
#     gf = gpd.read_file('/home/ronit/Downloads/keyword/IR STATION MASTER MEITY.shp')
#     d =gf.columns[4]
#     data1 = gf[d]


#     list2 = data1.astype(str).str.split(' ')
#     # print(list1)
#     for con in sc:
#         for dx,cons in enumerate (list2):
#     #         print(dx,cons)
#             if con in cons:
# #           
#                 y = ' '.join(cons)
# #                 print(y)
#                 lc = gf.loc[dx]
# #                 cols = lc[8]
# #                 print(lc,'==========================================')
#                 listofdata.append(lc)
# # print(listofdata)
# dataframes = pd.DataFrame(data=listofdata)
# print(dataframes)
# print('-----------')

# print("Searching finished")


import pandas as pd

import geopandas as gpd


file = pd.read_excel('/home/ronit/Downloads/keyword/Station.xls', sheet_name="14.02.22")
# print(file)
# file.loc[0:]
# fa = file[['Abnormalities/ Deficiencies found ( In Brief)','Department/Area inspected Such as Loco/Coach/Track/Station etc.','Remarks']]
f = file.columns[7]
# print(f)
dc =file.columns[11]
fo = file[f]
# print(fo)
data5 = file[dc]
fe = file.columns[6]
foe=file[fe]





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
# data = f['Abnormalities/ Deficiencies found ( In Brief)']
list1 = fo.astype(str).str.split(' ')
# print(list1)
# list1
lo = []
da =[]
no =[]
match = ['broken','cabin']
for matches in match:
#     print(matches)
    print('----------')
    for i,index in enumerate(list1):
        
        # print(i,index)
        if  matches in index:
            
            x = ' '.join(index)
            # print('======>',x)
#             print('----------')
            # print('matched')
            # print('-----------')
            # a = file[['Abnormalities/ Deficiencies found ( In Brief)','Department/Area inspected Such as Loco/Coach/Track/Station etc.']]
         
            l = data5.loc[i]
            # print(l)
            
            da.append(l)
            
            loa = fo.loc[i]
            # print(loa)
            lo.append(loa)
            lap = foe.loc[i]
            no.append(lap)
            df3 = pd.DataFrame(data=lo)
            df1_transposed = df3.T
            # print(df1_transposed)

            # df = pd.DataFrame(data=l)
          
            # df1_transposed = df.T
            # print(df1_transposed)
# print(no,'-----------------------------------------------------')
lw = []
ga = pd.DataFrame(data=da)
# print(ga)
# cg = ga.columns
# cx = cg[11]
# dh = ga[cx]
# print(dh)
# for qk in dh:
#     # print(qk)
#     lw.append(qk)
# init = iter(ga)  
dic1 = ga.to_dict('dict')
# res_dct = dict(zip(init, init))    
print(dic1)  
# print(lw)

# qp = "Remarks"+str(lw)
# print(qp)
# dic1 = qp.to_dict('dict')
# print(dic1)

# print(dh)
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
print('====================================================\n')
listofdata= []
for lll in no:
    # print(lll)
    sc = lll.split(" ")
    # print(sc)

#     print(conset)
    gf = gpd.read_file('/home/ronit/Downloads/keyword/IR STATION MASTER MEITY.shp')
    d =gf.columns[4]
    b = gf.columns[[4,5,7,8]]
    dataa=gf[b]
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
               
                lc = dataa.loc[dx]
                # print(lc)
#                 cols = lc[8]
#                 print(lc,'==========================================')
                listofdata.append(lc)
                

# print(listofdata)
daf = pd.DataFrame(data=listofdata)
# print(daf)

dic = daf.to_dict('dict')
print(dic)
# init = iter(new)  
# res_dct = dict(zip(init, init))  
# print(res_dct)
                
                
# print(listofdata)
# pq =[]
# dataframes = pd.DataFrame(data=listofdata)
# # print(dataframes)
# va = dataframes.columns
# q = va[[4,5,7,8]]
# dat = dataframes[q]
# w = dat.values
# print(dat)
# for dw in dat:
#     # print()
#     pq.append(w)


# p = pq[0]
# ak= []
# for qp in p:
#     aa= "Station : "+str(qp)
    # ak.append(aa)
#     for aq in qp:
#         print(aq)
#         ak.append(aq)
# qt = ak.split(' ')
# print(qt)


# daf = pd.DataFrame(data=ak)
# print(daf)
# dfq = daf.to_dict('dict')
# print(dfq)
# df_reset=dat.set_index('STATION CO')
# dic = dat.to_dict('dict')
# print(dic)
print('-----------')

print("Searching finished")

