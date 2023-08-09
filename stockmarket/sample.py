import csv
i=0

x=[]
y=[]
i=0
with open(r'E:\django\stockmarket\static\ibm.csv','r',encoding='utf-8')as file:
    filecontent=csv.reader(file)
    for row in filecontent:
        try:
            i=i+1
            if i!=1:
                datarow=[]
                datarow.append(row[0])
                x.append(datarow)
                y.append(float(row[4]))
        except:
            pass
print(x,y)
