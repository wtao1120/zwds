#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
術數基礎 陰陽、五行、方向、天干、生肖、性別
"""
class p_592a_6975_v(object):
    """
    道生萬物
    """
    def __str__(self):
        return self.p_540d_7a31_v


class p_5169_5100_v(p_592a_6975_v):
    """
    陰、陽
    """
    def __init__(self, p_540d_7a31_v, p_6578_5b57_v):
        self.p_540d_7a31_v = p_540d_7a31_v
        self.p_6578_5b57_v = p_6578_5b57_v

p_9670_v = p_5169_5100_v(p_540d_7a31_v = "陰", p_6578_5b57_v = 0)
p_967d_v = p_5169_5100_v(p_540d_7a31_v = "陽", p_6578_5b57_v = 1)


class p_65b9_5411_v(object):
    """
    東、西、南、北
    """
    def __init__(self, p_540d_7a31_v):
        self.p_540d_7a31_v = p_540d_7a31_v

    def __str__(self):
        return self.p_540d_7a31_v

p_6771_v = p_65b9_5411_v("東")
p_897f_v = p_65b9_5411_v("西")
p_5357_v = p_65b9_5411_v("南")
p_5317_v = p_65b9_5411_v("北")
p_4e2d_v = p_65b9_5411_v("中")


class p_5929_5e72_v(object):
    """
    天干參數
    """
    def __init__(self, p_540d_7a31_v, p_9670_967d_v):
        self.p_540d_7a31_v = p_540d_7a31_v
        self.p_9670_967d_v = p_9670_967d_v

    def __str__(self):
        return self.p_540d_7a31_v

p_7532_v = p_5929_5e72_v(p_540d_7a31_v = '甲', p_9670_967d_v = p_967d_v)
p_4e59_v = p_5929_5e72_v(p_540d_7a31_v = '乙', p_9670_967d_v = p_9670_v)
p_4e19_v = p_5929_5e72_v(p_540d_7a31_v = '丙', p_9670_967d_v = p_967d_v)
p_4e01_v = p_5929_5e72_v(p_540d_7a31_v = '丁', p_9670_967d_v = p_9670_v)
p_620a_v = p_5929_5e72_v(p_540d_7a31_v = '戊', p_9670_967d_v = p_967d_v)
p_5df1_v = p_5929_5e72_v(p_540d_7a31_v = '己', p_9670_967d_v = p_9670_v)
p_5e9a_v = p_5929_5e72_v(p_540d_7a31_v = '庚', p_9670_967d_v = p_967d_v)
p_8f9b_v = p_5929_5e72_v(p_540d_7a31_v = '辛', p_9670_967d_v = p_9670_v)
p_58ec_v = p_5929_5e72_v(p_540d_7a31_v = '壬', p_9670_967d_v = p_967d_v)
p_7678_v = p_5929_5e72_v(p_540d_7a31_v = '癸', p_9670_967d_v = p_9670_v)

p_5929_5e72_8868_v = [p_7532_v, p_4e59_v, p_4e19_v, p_4e01_v, p_620a_v, p_5df1_v, p_5e9a_v, p_8f9b_v, p_58ec_v, p_7678_v]


class p_5730_652f_v(object):
    """
    地支參數
    """
    def __init__(self, p_540d_7a31_v, p_9670_967d_v, p_65b9_5411_v, p_6642_9593_v):
        self.p_540d_7a31_v = p_540d_7a31_v
        self.p_9670_967d_v = p_9670_967d_v
        self.p_65b9_5411_v = p_65b9_5411_v
        self.p_6642_9593_v = p_6642_9593_v

    def __str__(self):
        return self.p_540d_7a31_v

p_5b50_v = p_5730_652f_v(p_540d_7a31_v = '子', p_9670_967d_v = p_967d_v, p_65b9_5411_v= p_5317_v, p_6642_9593_v=(23, 1))
p_4e11_v = p_5730_652f_v(p_540d_7a31_v = '丑', p_9670_967d_v = p_9670_v, p_65b9_5411_v= p_5317_v, p_6642_9593_v=(1, 3))
p_5bc5_v = p_5730_652f_v(p_540d_7a31_v = '寅', p_9670_967d_v = p_967d_v, p_65b9_5411_v= p_5317_v, p_6642_9593_v=(3, 5))
p_536f_v = p_5730_652f_v(p_540d_7a31_v = '卯', p_9670_967d_v = p_9670_v, p_65b9_5411_v= p_897f_v, p_6642_9593_v=(5, 7))
p_8fb0_v = p_5730_652f_v(p_540d_7a31_v = '辰', p_9670_967d_v = p_967d_v, p_65b9_5411_v= p_897f_v, p_6642_9593_v=(7, 9))
p_5df3_v = p_5730_652f_v(p_540d_7a31_v = '巳', p_9670_967d_v = p_9670_v, p_65b9_5411_v= p_897f_v, p_6642_9593_v=(9, 11))
p_5348_v = p_5730_652f_v(p_540d_7a31_v = '午', p_9670_967d_v = p_967d_v, p_65b9_5411_v= p_5357_v, p_6642_9593_v=(11, 13))
p_672a_v = p_5730_652f_v(p_540d_7a31_v = '未', p_9670_967d_v = p_9670_v, p_65b9_5411_v= p_5357_v, p_6642_9593_v=(13, 15))
p_7533_v = p_5730_652f_v(p_540d_7a31_v = '申', p_9670_967d_v = p_967d_v, p_65b9_5411_v= p_5357_v, p_6642_9593_v=(15, 17))
p_9149_v = p_5730_652f_v(p_540d_7a31_v = '酉', p_9670_967d_v = p_9670_v, p_65b9_5411_v= p_6771_v, p_6642_9593_v=(17, 19))
p_620c_v = p_5730_652f_v(p_540d_7a31_v = '戌', p_9670_967d_v = p_967d_v, p_65b9_5411_v= p_6771_v, p_6642_9593_v=(19, 21))
p_4ea5_v = p_5730_652f_v(p_540d_7a31_v = '亥', p_9670_967d_v = p_9670_v, p_65b9_5411_v= p_6771_v, p_6642_9593_v=(21, 23))

p_5730_652f_8868_v = [p_5b50_v, p_4e11_v, p_5bc5_v, p_536f_v, p_8fb0_v, p_5df3_v, p_5348_v, p_672a_v, p_7533_v, p_9149_v, p_620c_v, p_4ea5_v]


class p_751f_8096_v(object):
    """
    十二生肖
    """
    def __init__(self, p_540d_7a31_v, p_5730_652f_v):
        self.p_540d_7a31_v = p_540d_7a31_v
        self.p_5730_652f_v = p_5730_652f_v

    def __str__(self):
        return self.p_540d_7a31_v

p_9f20_v = p_751f_8096_v("鼠", p_5b50_v)
p_725b_v = p_751f_8096_v("牛", p_4e11_v)
p_864e_v = p_751f_8096_v("虎", p_5bc5_v)
p_5154_v = p_751f_8096_v("兔", p_536f_v)
p_9f8d_v = p_751f_8096_v("龍", p_8fb0_v)
p_86c7_v = p_751f_8096_v("蛇", p_5df3_v)
p_99ac_v = p_751f_8096_v("馬", p_5348_v)
p_7f8a_v = p_751f_8096_v("羊", p_672a_v)
p_7334_v = p_751f_8096_v("猴", p_7533_v)
p_96de_v = p_751f_8096_v("雞", p_9149_v)
p_72d7_v = p_751f_8096_v("狗", p_620c_v)
p_8c6c_v = p_751f_8096_v("豬", p_4ea5_v)

# 地支對應陰陽
# 鼠.地支.陰陽

# 地支對應生肖
p_5b50_v.p_751f_8096_v = p_9f20_v
p_4e11_v.p_751f_8096_v = p_725b_v
p_5bc5_v.p_751f_8096_v = p_864e_v
p_536f_v.p_751f_8096_v = p_5154_v
p_8fb0_v.p_751f_8096_v = p_9f8d_v
p_5df3_v.p_751f_8096_v = p_86c7_v
p_5348_v.p_751f_8096_v = p_99ac_v
p_672a_v.p_751f_8096_v = p_7f8a_v
p_7533_v.p_751f_8096_v = p_7334_v
p_9149_v.p_751f_8096_v = p_96de_v
p_620c_v.p_751f_8096_v = p_72d7_v
p_4ea5_v.p_751f_8096_v = p_8c6c_v


class p_4e94_884c_v(object):
    """
    《韻會》五行，運于天地閒，未嘗停息，故名。

       火
     / |
    木 土->金
     \    /
       水
    
    依序相生、隔行相剋、逆序相洩、剋過相乘、剋逆相悔
    
    假設五行系統中有100％的能量，而五行各佔20％...
    靜止狀態下，五行間毫無交集，沒有生機。
    套用相生，相剋，相洩，五行系統的能量便會在五行之間轉移。
    
    五行之於斗數
    http://hk.myblog.yahoo.com/lawrencioy/article?mid=188
    """
    def __init__(self, p_540d_7a31_v):
        self.p_540d_7a31_v = p_540d_7a31_v
        self.p_76f8_751f_v = None
        self.p_76f8_524b_v = None
        self.p_5929_5e72_v = None
        self.p_5730_652f_v = None
        self.p_5c40_6578_v = None

    def __str__(self):
        return self.p_540d_7a31_v 

p_91d1_v = p_4e94_884c_v(p_540d_7a31_v = '金')
p_6728_v = p_4e94_884c_v(p_540d_7a31_v = '木')
p_6c34_v = p_4e94_884c_v(p_540d_7a31_v = '水')
p_706b_v = p_4e94_884c_v(p_540d_7a31_v = '火')
p_571f_v = p_4e94_884c_v(p_540d_7a31_v = '土')

# 五行相生關係
p_6728_v.p_76f8_751f_v = p_706b_v
p_706b_v.p_76f8_751f_v = p_571f_v
p_571f_v.p_76f8_751f_v = p_91d1_v
p_91d1_v.p_76f8_751f_v = p_6c34_v
p_6c34_v.p_76f8_751f_v = p_6728_v

# 五行相洩關係 (相生的相反)
p_6728_v.p_76f8_6d29_v = p_6c34_v
p_706b_v.p_76f8_6d29_v = p_6728_v
p_571f_v.p_76f8_6d29_v = p_706b_v
p_91d1_v.p_76f8_6d29_v = p_571f_v
p_6c34_v.p_76f8_6d29_v = p_91d1_v

# 五行相剋關係
p_6728_v.p_76f8_524b_v = p_571f_v
p_571f_v.p_76f8_524b_v = p_6c34_v
p_6c34_v.p_76f8_524b_v = p_706b_v
p_706b_v.p_76f8_524b_v = p_91d1_v
p_91d1_v.p_76f8_524b_v = p_6728_v

# 相乘關係同相剋關係 <- 相剋過度
p_6728_v.p_76f8_4e58_v = p_571f_v
p_571f_v.p_76f8_4e58_v = p_6c34_v
p_6c34_v.p_76f8_4e58_v = p_706b_v
p_706b_v.p_76f8_4e58_v = p_91d1_v
p_91d1_v.p_76f8_4e58_v = p_6728_v

# 五行相悔關係 (相剋的相反 <- 被反剋)
p_6728_v.p_76f8_6094_v = p_91d1_v
p_571f_v.p_76f8_6094_v = p_6728_v
p_6c34_v.p_76f8_6094_v = p_571f_v
p_706b_v.p_76f8_6094_v = p_6c34_v
p_91d1_v.p_76f8_6094_v = p_706b_v

# 方向對應五行
p_6771_v.p_4e94_884c_v = p_6728_v
p_897f_v.p_4e94_884c_v = p_91d1_v
p_5357_v.p_4e94_884c_v = p_706b_v
p_5317_v.p_4e94_884c_v = p_6c34_v
p_4e2d_v.p_4e94_884c_v = p_571f_v

# 五行對應方向
p_6728_v.p_65b9_5411_v = p_6771_v
p_706b_v.p_65b9_5411_v = p_5357_v
p_571f_v.p_65b9_5411_v = p_4e2d_v
p_91d1_v.p_65b9_5411_v = p_897f_v
p_6c34_v.p_65b9_5411_v = p_5317_v

# 五行對應天干
p_6728_v.p_5929_5e72_v = p_7532_v, p_4e59_v
p_706b_v.p_5929_5e72_v = p_4e19_v, p_4e01_v
p_571f_v.p_5929_5e72_v = p_620a_v, p_5df1_v
p_91d1_v.p_5929_5e72_v = p_5e9a_v, p_8f9b_v
p_6c34_v.p_5929_5e72_v = p_58ec_v, p_7678_v

# 天干對應五行
p_7532_v.p_4e94_884c_v = p_6728_v
p_4e59_v.p_4e94_884c_v = p_6728_v
p_4e19_v.p_4e94_884c_v = p_706b_v
p_4e01_v.p_4e94_884c_v = p_706b_v
p_620a_v.p_4e94_884c_v = p_571f_v
p_5df1_v.p_4e94_884c_v = p_571f_v
p_5e9a_v.p_4e94_884c_v = p_91d1_v
p_8f9b_v.p_4e94_884c_v = p_91d1_v
p_58ec_v.p_4e94_884c_v = p_6c34_v
p_7678_v.p_4e94_884c_v = p_6c34_v

# 五行對應地支
p_6728_v.p_5730_652f_v = p_5bc5_v, p_536f_v
p_706b_v.p_5730_652f_v = p_5df3_v, p_5348_v 
p_571f_v.p_5730_652f_v = p_8fb0_v, p_620c_v, p_4e11_v, p_672a_v
p_91d1_v.p_5730_652f_v = p_7533_v, p_9149_v
p_6c34_v.p_5730_652f_v = p_5b50_v, p_4ea5_v

# 地支對應五行
p_5bc5_v.p_4e94_884c_v = p_6728_v
p_536f_v.p_4e94_884c_v = p_6728_v
p_5df3_v.p_4e94_884c_v = p_706b_v
p_5348_v.p_4e94_884c_v = p_706b_v
p_8fb0_v.p_4e94_884c_v = p_571f_v
p_620c_v.p_4e94_884c_v = p_571f_v
p_4e11_v.p_4e94_884c_v = p_571f_v
p_672a_v.p_4e94_884c_v = p_571f_v
p_7533_v.p_4e94_884c_v = p_91d1_v
p_9149_v.p_4e94_884c_v = p_91d1_v
p_5b50_v.p_4e94_884c_v = p_6c34_v
p_4ea5_v.p_4e94_884c_v = p_6c34_v

# 季節與五行強弱的統計表，旺、相、休、囚、死


class p_6027_5225_v(object):
    def __init__(self, p_540d_7a31_v, p_9670_967d_v):
        self.p_540d_7a31_v = p_540d_7a31_v
        self.p_9670_967d_v = p_9670_967d_v

    def __str__(self):
        return self.p_540d_7a31_v 

p_7537_v = p_6027_5225_v("男", p_967d_v)
p_5973_v = p_6027_5225_v("女", p_9670_v)