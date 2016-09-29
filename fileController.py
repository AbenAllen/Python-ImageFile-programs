import os,glob
# -*- coding: UTF-8 -*-
file_list = []
text_list = []
create_list = []
file_address  = raw_input("Enter File Path:").strip(' ')
def traverseDirByOSWalk(path):
    path = os.path.expanduser(path)
    for (dirname, subdir, subfile) in os.walk(path):
        for f in subfile:
            if os.path.splitext(f)[1]=='.jpg' or os.path.splitext(f)[1]=='.png':
                # print os.path.splitext(f)[0]
                file_list.append(os.path.splitext(f)[0])


traverseDirByOSWalk(file_address)
print file_list

file_abs = file_address +'/item_ref.txt'
file_write = file_address + '/write.txt'
f = open(file_abs,'r')
# print f.read()
for line in f.readlines():
    line = line.strip('\n')
    line = line.strip('\r')
    text_list.append(line)
f.close()

# with open(file_abs,'r') as f:
#     b_list = f.readline()
#
print text_list

for str in text_list:
    if str not in file_list:
        create_list.append(str)

        with open(file_write,'a') as f:
            f.write(str+'\n')





print create_list