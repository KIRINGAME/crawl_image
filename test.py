

def invest(amount, time, rate=0.05):
    if amount <= 0:
        return 0
    if time <= 0:
        return 0

    for i in range(1,time+1):
        amount = amount*(1+rate)
        print(str(amount))
    return amount


#_base_amount = 100000
#_amount = invest(_base_amount,3)
#print("amount:" + str(_amount) + " ,rate: " + str(_amount-_base_amount))


def test_cn_moblie(phone_num):
    phone_num=str(phone_num)
    if len(phone_num) != 11:
        print("LEN ERROR")
        return

    CN_mobile=[134,135,158,186]
    phone_num_pre = phone_num[:3]
    if int(phone_num_pre) in CN_mobile:
        print(phone_num_pre)
    else:
        print("NOT IN CNMOBILE")


#test_cn_moblie(15810190369)

def open_file():
    path="/Users/xuequn/Desktop/pytest"
    for i in range(1,10):
        file = open(path+'/'+str(i),'w')
        file.write(str(i))

#open_file()


#fruit=["pineapple",'pear']
#fruit.insert(1,'grape')
#print(fruit)
#fruit[0:0]=['Orange']
#print(fruit)
#fruit.remove("grape")
#print(fruit)
#fruit[0]='Grapefruit'
#print(fruit)
#del fruit[0:2]
#print(fruit)

c={i:j for i,j in zip(range(1,10),'abcdef')}
# print(c)



# import string
# path = '/Users/xuequn/Desktop/pytest/1'
# with open(path, 'r') as text:
#     if text.readable():
#         words = [raw_word.strip(string.punctuation).lower() for raw_word in text.read().split()]
#         word_index = set(words)
#         counts_dict = {index:words.count(index) for index in word_index}
#         for word in sorted(counts_dict, key=lambda x: counts_dict[x], reverse=True):
#             print('{} -- {} times'.format(word,counts_dict[word]))
class TestA:
    attr = 1
    def __init__(self):
        self.attr = 2
obj_a = TestA()
# TestA.attr = 2
# obj_a.attr = 2
# obj_b = TestA()
# print(TestA.attr)
# print(obj_a.attr)
# print(obj_b.attr)

import sys
# print(sys.path[3])

print('*'*100)
import os
import xlwings as xw

def get_file_data(file_path):
    # with open(file_path,'r') as file:
        try:
            # if file.readable():
            print('#'*10)
            print(file_path)
            # print('{}**\n{}'.format(file_path,file.read()))
            # 连接到excel
            workbook = xw.Book(file_path)  # 连接excel文件
            # 连接到指定单元格
            data_range = workbook.sheets('build_list').range('A1')
            # 写入数据
            data_range.value = [1, 2, 3]
            # 保存
            workbook.save()
        except KeyError:
            print('ERROR')
            return




def get_all_text(path):
    if os.path.isdir(path):
        for _file in os.listdir(path):
            (filename, extension) = os.path.splitext(_file)
            print(filename,extension)
            if extension == '.txt':
                _file_path = os.path.join(path,_file)
                get_file_data(_file_path)


# get_all_file('/Users/xuequn/Desktop/New/Bin/asset/mb/server/area_refresh')
get_all_text('/Users/xuequn/Desktop/New/Bin/asset/mb/building')
