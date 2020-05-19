# -*- coding: utf-8 -*-
"""
   Author : gaolei82
   Date：2020/4/10
"""
import pandas as pd
import re
import nltk

df = pd.read_excel(r'D:\gaolei82\Desktop\新建文件夹\项目存档\蒙牛项目\地址匹配\地址匹配.xlsx',sheetname='Sheet2')
sdf = pd.read_excel(r'D:\gaolei82\Desktop\新建文件夹\项目存档\蒙牛项目\地址匹配\基表.xlsx',sheetname='Sheet1')
city = df['city'].tolist()
city1 = []
for i in city:
    city1.append(str(i))


def geo_checker(word):
    if len(word)>2:
        if '-' in word:
            word = word[0:word.find('-')]
        elif (u'省' in word or u'自治区' in word):
            word=word.replace(u'省','').replace(u'自治区','')
        elif (u'地区' in word or u'自治州' in word or u'盟' in word):
            word=word.replace(u'地区','').replace(u'自治州','').replace(u'盟','')
        elif (u'自治县' in word or u'矿区' in word or u'自治旗' in word):
            word=word.replace(u'自治县','').replace(u'矿区','').replace(u'自治旗','')
        elif u'县' in word :
            word=word.replace(u'县','')
        elif u'市' in word:
              if (u'天津' in word or u'北京' in word or u'重庆' in word or u'上海' in word):
                  word=word.replace(u'市','')
              if u'区' in word:
                  word=word.replace(u'区','')
              word=word.replace(u'市','')
        elif u'区' in word:
            word=word.replace(u'区','')
        else:
            pass
    else:
            pass
    return word


def city_checker(city):
    if len(city)>2:
        if '-' in city:
            city = city[0:city.find('-')]
    else:
        pass
    return city


if __name__ == '__main__':
    ncity = []
    for i in city1:
        ncity.append(city_checker(i))
    #print(city)
    scity = []
    county = sdf['county'].tolist()
    city = sdf['city'].tolist()
    print(ncity)
    #print(county)
    #print(city)
    for i in range(len(ncity)):
        for j in range(len(county)):
            if re.search(county[j],ncity[i]):
                ncity[i] = city[j]
            else:
                pass
    print(ncity)
    pdscity = pd.DataFrame(ncity)
    pdscity.to_excel(r'D:\gaolei82\Desktop\新建文件夹\项目存档\蒙牛项目\地址匹配\scity.xlsx',header=0)






