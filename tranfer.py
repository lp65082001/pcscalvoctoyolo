import os
import re
import numpy as np
import time


dist = np.array(["class1","class2"])
path="./"    


fileList=os.listdir(path)
temp = re.compile("([a-zA-Z]+)([0-9+]+)")
n=0
for i in (fileList):
    oldname=path+ os.sep + fileList[n] 
    
    if (fileList[n][-3:-1]=="xm"): 
        f1 = open(oldname[0:-3]+"txt", 'w')
        print(fileList[n])
        num2 = 0
        with open(oldname) as f:
            for line in f.readlines():
                a = re.split("\t|<|>",line)   
    
                if (len(a)>6):
                    #num2 = 0       
                    if (a[3]=="name"):
                        #print(a[4])
                        name = np.where(dist == temp.match(a[4]).groups()[0])[0][0]
                        #detect the multi-classes
                        #if (name == 1):
                            #print(oldname)
                    if (a[3]=="width"):
                        xx = int(a[4])
                    if (a[3]=="height"):
                        yy = int(a[4])
                    if (a[4]=="xmin"):
                        xm = a[5]       
                    if (a[4]=="ymin"):
                        ym = a[5]
                    if (a[4]=="xmax"):
                        xma = a[5]
                    if (a[4]=="ymax"):
                        yma = a[5]
                        num2 = 1
                    if(num2 == 1 ):                      
                        coodx = ((int(xm) + int(xma))/2)/xx
                        coody = ((int(ym) + int(yma))/2)/yy
                        width = (int(xma) - int(xm))/xx
                        height = (int(yma) - int(ym))/yy

                        #check the x,y,w,h fall in 0<x<1
                        if (coodx>=1 or coody >=1 or width >=1 or height >=1):
                            print(oldname)
                    
                        f1.write(str(name)+" "+str(coodx)+" "+str(coody)+" "+str(width)+" "+str(height)+"\n")    
                        num2 = 0
        f1.close()
    #time.sleep(1)
    n+=1

print("done")
