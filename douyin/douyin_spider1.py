# -*- encoding=utf8 -*-

#用airtest连接手机之后，随便找到一个用户列表，比如人民网的粉丝列表里，运行该脚本就能跑了。
__author__ = "zhouzhuofei"

from airtest.core.api import *

auto_setup(__file__)
from airtest.core.api import *
from poco.drivers.unity3d import UnityPoco
poco = UnityPoco()

import time
import numpy as np
import pandas as pd
import time
import csv

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
fp = open('自己所设的csv文件位置','wt',newline='',encoding='utf_8_sig')
writer = csv.writer(fp)
for i in range(0,100):
    for j in range(0,6):
        poco(name = "com.ss.android.ugc.aweme:id/dls")[j].click()
        
        usr = poco(name="com.ss.android.ugc.aweme:id/bqe").get_text()
        douyin_num = poco(name="com.ss.android.ugc.aweme:id/dnn").get_text()
        nd = poco(name="android.widget.TextView")
        nd_text = [a.get_text() for a in nd]
        huozan = poco(name="com.ss.android.ugc.aweme:id/a4f").get_text()
        guanzhu = poco(name="com.ss.android.ugc.aweme:id/ah0").get_text()
        fans = poco(name="com.ss.android.ugc.aweme:id/agw").get_text()
        zdx = poco(name="com.ss.android.ugc.aweme:id/title")
        zdx_text = [b.get_text() for b in zdx]
        writer.writerow((usr,douyin_num,nd_text,huozan,guanzhu,fans,zdx_text))
        
        
        poco(name="com.ss.android.ugc.aweme:id/j4").click()
        
    print(i)
    poco.swipe([0.5,0.8],[0.5,0.2])
    
fp.close()
        



