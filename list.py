import os
path="path"   

#获取该目录下所有文件，存入列表中
fileList=os.listdir(path)
f1 = open("./targe_name.txt", 'w')
n=0
for i in (fileList):
    
    #设置旧文件名（就是路径+文件名）
    oldname=path+ os.sep + fileList[n]   # os.sep添加系统分隔符

    #print(fileList[n][-3:-1])
    
    if (fileList[n][-3:-1]=="JP"):
        f1.write("path for your data structure"+fileList[n]+"\n")

    #设置新文件名
        #newname=path +fileList[n][0:-4]+".jpg"
        #print(newname) 
        #os.rename(oldname,newname)   #用os模块中的rename方法对文件改名
        #print(oldname,'======>',newname)
    
    n+=1
f1.close()
