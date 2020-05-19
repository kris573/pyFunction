# -*- coding: utf-8 -*-
"""
   Author : gaolei82
   Date：2020/4/8
"""
import pandas as pd

def clusterfun(inputpath,outputpath):
    '''
    假设数据有三列，分别为a,b,c,该函数能够实现对a,b 列使用groupby,对c列求和
    :param inputpath: 需要处理的数据，通常是一个excel
    :param outputpath: 输出的excel
    :return:

    '''
    data = pd.read_excel(inputpath,sheetname='Sheet1', header=0)
    a = data['a']
    b = data['b']
    c = data['c']
    qw = {'a': a, 'b': b, 'c': c}
    qwe = pd.DataFrame(qw)
    qwer = qwe.groupby(['a', 'b'], as_index=False)['c'].sum()
    qwer.to_excel(outputpath, header=0)

def mergefun(leftdata,rightdata,outputpath):
    '''
    该函数实现的是数据合并的功能，类似于excel的vlookup函数，借助于pandas,实现的速度比excel
    要快很多,尤其是在面对大数据量的时候,匹配的左边的列是a，右边的是b，左连接
    :param leftdata: 左边的数据
    :param rightdata: 右边的数据
    :param outputpath: 输出的结果写入excel
    :return:
    '''
    data_result = pd.merge(leftdata,rightdata,left_on='a',right_on='b',how='left')
    df_result = pd.DataFrame(data_result)
    df_result.to_excel(outputpath)

def cityformat(inputpath,outputpath):
    '''
    在项目中经常要用到地址匹配的情况，该函数实现的是对应需要清洗的某一列数据a，根据省市进行切分，输出不含市的地址
    接下来如有需要再进行其他操作，假设输入和输出均为excel的格式(如果不含'省'和'市'则不能通过
    :param inputpath: 输入的地址
    :param outputpath: 输出的地址
    :return:
    '''
    df = pd.read_excel('inputpath', 'Sheet1')
    city = list(df['a'])
    # print(city)
    cit = []

    for i in city:
        if '省' in i:
            cit.append(i.split('省')[1])
        else:
            cit.append(i)
    print(cit)
    city1 = []
    for i in cit:
        if '市' in i:
            city1.append(i.split('市')[0])
        else:
            city1.append(i)
    city2 = pd.DataFrame(city1)
    city2.to_excel('outputpath',header=0)

def cargofacts(inputpath):
    '''
    统计汽运车型的装载率
    :param inputpath: 需要读取的文件地址
    :return:
    '''
    df_data = None
    j = 0
    xlsx_names = [x for x in os.listdir(inputpath) if x.endswith(".xlsx") and not x.startswith('~$')]
    for xlsx_name in xlsx_names:
        # try:
        j=j+1
        print('开始运行:{name}'.format(name=xlsx_name))
        print('第{n}个'.format(n=j))
        time_start1 = time.time()
        path = os.path.join(inputpath, xlsx_name)
        df = pd.read_excel(path, sheetname='装运单明细')
        df_se=pd.read_excel(path,sheetname='交货单明细')
