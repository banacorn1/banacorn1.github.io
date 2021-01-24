import os
import hashlib
import wget

#File_list:所有文件
#File_not_find:未找到的文件
#Incomplete_file:残缺,不完整的文件
#File_path:文件路径
#List_length:列表长度

#打开文件列表


file = open(r"file_list.emp","r")

File_list = file.readlines()                #转化为列表
File_not_find = []                          #未找到的文件列表
Incomplete_file = []                        #残缺,不完整的文件列表
List_length = len(File_list)                #列表长度

num = 0

while num < List_length:
    a = File_list[num]                      #读取列表
    a = a.split(" ")                        #分割
    File_path = a[0]                        #文件路径
    file_md5 = a[1]                         #文件MD5
    file_name = a[2]                        #文件名

    cmd_return = os.path.exists(File_path)
    if cmd_return == False:                                        #检测文件是否存在
        print(f"file not found({File_path})")
        File_not_find.append(a)
    else:
        file_open = open(File_path,"rb")
        file_open = file_open.read()
        file_md5_true = hashlib.md5(file_open).hexdigest()
        
        if file_md5 == file_md5_true:                           #检测文件是否完整
            pass
            print(f"Complete documentation({File_path})")
        else:
            print(f"Incomplete file({File_path})")
            Incomplete_file.append(a)
            pass
        pass
    num += 1
    pass
pass

#处理错误文件
#Document_modification:文件修改
if type(File_not_find) == list:
    Document_modification = ""
    for Document_modification in File_not_find:
        print(type(Document_modification))
        print(Document_modification)
        File_path = Document_modification[0]                        #文件路径
        file_name = Document_modification[3]                        #文件名
        print(file_name)
        wget.download("http://banacorn1.github.io/"+file_name,"./"+file_name)             #第一个为下载地址,第二个为保存地址
        print(f"File download complete90{File_path}")
        pass
    pass
else:
    pass

if type(Incomplete_file) == list:
    Document_modification = ""
    for Document_modification in Incomplete_file:
        print(type(Document_modification))
        print(Document_modification)
        File_path = Document_modification[0]                        #文件路径
        file_name = Document_modification[3]                        #文件名
        print(file_name)
        wget.download("http://banacorn1.github.io/"+file_name,"./"+file_name)             #第一个为下载地址,第二个为保存地址
        print(f"File download complete({File_path})")
        pass
    pass
else:
    pass

print("All documents are complete!"+"http://banacorn1.github.io/"+file_name)


#print(File_list,"\n",File_not_find,"\n",Incomplete_file,"\n",)
