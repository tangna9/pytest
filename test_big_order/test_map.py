__author__ = 'tangna'

#array = [1, 2, 3]
#square_array = map(lambda i:i**2, array)
#print square_array

#print [i**2 for i in array]

import os
import os.path
rootdir = "D:\\tangna\\spilt_order\\"

#遍历目录,找到所有文件名
filenames_list = [filenames for parent, dirnames, filenames in os.walk(rootdir)]

#循环所有文件内容，把文件中大写转为小写后重新写入文件
for filename in filenames:
    print "filename:", filename, type(filename)
    file = rootdir+filename
    with open(file, 'r') as f:
        old_file_content = f.read()
        new_file_content = old_file_content.lower()
    with open(file, 'w') as f:
        f.write(new_file_content)


# str_list = ["IS_ORDER_FORCIBLY_SPLITTED", "MOBILE_MAC", "COUPON_APPLY_ID", "MOBILE_IMSI", "MOBILE_IMEI", "IDENTITY_NUM", "From_platform" ]
# str2_list = [i.lower() for i in str_list]
# print str2_list