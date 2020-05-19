# python函数模板合集

model中主要是一些常用的用python操作Excel的函数，一般会包括输入和输出的数据的地址。

# 地址匹配

correctcity中是地址匹配的函数，读取的数据一般是不整齐的，该函数的作用是识别输入字段中的地址信息，如果是三级地址会返回相应的二级地址，比如：

肥西县--合肥
高碑店--保定
河北满城--保定

地址中可以含有‘县’或者‘市’等字段，也可以不含有，都可以识别；
如果是一段话中含有地址信息也可以识别出来。

该函数的匹配需要用到一个基表，基表中的地址包括 一级地址（省）---二级地址（地级市）---三级地址（县）
基表中的数据已经去重，不会出现重复的情况，比如：

吉林省朝阳市
北京市朝阳区

这时候字段中的朝阳 会返回 朝阳市（吉林）

下面是一个例子，输入输出可以看做列表形式

|    输入字段    | 输出自段 |
| :------------: | :------: |
|     凤台县     |   淮南   |
|     马鞍山     |  马鞍山  |
|     宁晋县     |   邢台   |
|     沙河市     |   邢台   |
|      邯郸      |   邯郸   |
|    蔡右后旗    | 乌兰察布 |
| 阿坝藏族自治州 |  阿坝州  |
| 阜阳市-界首市  |  阜阳市  |

