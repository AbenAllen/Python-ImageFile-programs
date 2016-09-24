import os,glob
import shutil
# -*- coding: UTF-8 -*-
file_list = []
text_list = []
create_list = []
imgfilename_list = []
file_address  = raw_input("Enter File Path:").strip(' ').decode('gbk')
def traverseDirByOSWalk(path):
    path = os.path.expanduser(path)
    for (dirname, subdir, subfile) in os.walk(path):
        for f in subfile:
            if os.path.splitext(f)[0] in text_list:
                imgFileName = os.path.join(dirname,f)
                imgfilename_list.append(imgFileName)



file_itemref = os.path.join(file_address,'item_ref.txt')
file_write = os.path.join(file_address,'write.txt')
img_folder = os.path.join(file_address,'new_img_folder')

f = open(file_itemref,'r')# f file_itemrefName
# print f.read()
for line in f.readlines():
    line = line.strip('\n')
    line = line.strip('\r')
    text_list.append(line)
f.close()

traverseDirByOSWalk(file_address)

def addImgToPath(targetDir):
    if os.path.isdir(targetDir):
        print  'yyyyyyyy'
        shutil.rmtree(targetDir)

        # addImgToPath(targetDir)
    else:
        print 'xxxxxxxxx'
        os.makedirs(targetDir)
        for str in  imgfilename_list:
            shutil.copy(str,targetDir)


addImgToPath(img_folder)

# if not os.path.isdir(img_folder):
#     addImgToPath(img_folder)

print imgfilename_list



#/Users/xuxuben/Desktop/img+txt
