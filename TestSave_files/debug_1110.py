# 主程序，對三酷貓釣魚記賬內容進行統計
# from learn.debug_1110 import *        #引入自定義模塊
# d_date1={'鯽魚':[17,10.5],'鯉魚':[8,6.2],'鰱魚':[7,4.7]}            #1月1日釣魚記錄
# d_date2={'草魚':[2,7.2],'鯽魚':[3,12],'黑魚':[6,15]}                #1月2日釣魚記錄
# d_date3={'烏龜':[1,78.10],'鯽魚':[1,10.78],'草魚':[5,7.92]}         #1月3日釣魚記錄
# fish_records={'1月1日':d_date1,'1月2日':d_date2,'1月3日':d_date3}         #所有記錄
# #------------------------天統計
# print('===魚每日統計==================')
# for day,day_record in fish_records.items():
#     day_stat(day,day_record)
# #======================================
# print('\n=========魚所有數量統計')
# name1=''
# maxstat=['',0,'',0,0,0]           #前四個元素記錄最大值，后兩個記錄總數量、總金額
# all_stat=allday_stat(fish_records,maxstat)
# for name1,subs in all_stat.items():
#     print('%s數量%d金額%.2f'%(name1,subs[0],subs[1]))
# #===========================================
# print('\n============最大值，總數量，總金額打印===========')
# PrintMaxValues(maxstat)
# #============================================================================================================================
# #統計魚自定義模塊
# def day_stat(day,fishs):            #第一個自定義函數，統計每天的魚，并保存到統計字典里
#     '''統計每天的魚，并保存到統計字典里
#     day為字符串參數
#     fishs為兩層嵌套字典參數'''
#     nums=0          #數量
#     amount=0            #金額
#     for name0,sub_records in fishs.items():
#         print('%s數量%d單價%.2f元'%(name0,sub_records[0],sub_records[1]))
#         nums+=sub_records[0]
#         amount+=sub_records[0]*sub_records[1]
#     print('%s數量小計%d金額小計%.2f'%(day,nums,amount))
# def allday_stat(fishs,maxstat):         #第二個自定義函數，統計所有的魚，并保存到統計字典里
#     '''統計所有的魚，并保存到統計字典里
#     fishs為兩層嵌套字典參數'''
#     name1=""
#     sub_recods={}
#     stat_record={}
#     for day,day_record in fishs.items():            #循環獲取每天記錄（元組形式）
#         for name1,sub_recods in day_record.items():         #循環獲取當天魚相關記錄
#             if name1 in stat_record:                             #判斷魚是否在統計字典里，存在，則做累計處理
#                 stat_record[name1][0]+=sub_recods[0]             #每種魚數量累計
#                 stat_record[name1][1]+=sub_recods[0]*sub_recods[1]       #魚金額累計
#             else:
#                 stat_record[name1]=[sub_recods[0],sub_recods[0]*sub_recods[1]]          #第一次累計，直接在字典里賦值
# #=========================================================================
#     for name1,nums in stat_record.items():
#         if  maxstat[1]<nums[0]:         #求最大數量
#             maxstat[0]=name1
#             maxstat[1]=nums[0]
#         if maxstat[3]<nums[1]:          #求最大金額
#             maxstat[2]=name1
#             maxstat[3]=nums[1]
#         maxstat[4]=maxstat[4]+nums[0]               #求所有數量
#         maxstat[5]=maxstat[5]+nums[1]               #求累計總金額
#     return stat_record
# def PrintMaxValues(maxstat1):
#     '''打印最大值
#     maxstat1[:4]為列表參數，記錄最大值
#     maxstat1[4]記錄總數量
#     maxstat1[5]記錄總金額'''
#     print('最大數量的魚是%s,%d條'%(maxstat1[0],maxstat1[1]))
#     print('最大金額的魚是%s,%.2f元'%(maxstat1[2],maxstat1[3]))
#     print('釣魚總數量為%d,總金額為%.2f元'%(maxstat1[4],maxstat1[5]))
# #============================================================================================================================
# import os
# print(os.environ)
# nums=['noe','two','three','four','five','six','seven']
# t=open(r'd:\jie\t2.txt','a')                            #追加寫入模式打開文件
# for get_one in nums:                                    #循環，迭代獲取列表元素
#     t.write(get_one+'\n')                               #把每個元素循環寫入文件中，末行加\n
# t.close()                                               #關閉文件
# print('連續寫入完成！')                                  #提示寫入結束
# t1=open(r'd:\jie\t2.txt','r')
# dd=1
# while dd:
#     dd=t1.readline()
#     print(dd)
# t1=open(r'd:\jie\t2.txt','r')
# L_s=t1.readlines()
# print(L_s)
# import os
# tt=os.path.abspath(os.path.curdir)
# print(tt)
# ========================================================================================================
# import os       #導入os模塊
# import sys          #導入sys模塊
# get_cur_path=os.path.abspath(os.path.curdir)        #在當前路徑建立子路徑files
# f_n=get_cur_path+'\\TestSave_files'
# try:
#     if not os.path.isdir(f_n):          #確認路徑是否已存在
#         os.makedirs(f_n)                #不存在建立子路徑
# except:
#     print("子文件%s建立出錯！"%(f_n))           #提示建立出錯
#     sys.exit()                                  #退出程序
# #-----------------上面為動態建立文件夾
# f_n=f_n+'\\result.txt'      #準備在新建立的子路徑下存放文件t3.txt
# flag=False
# try:
#     f=open(f_n,'w')             #第一次執行，在新路徑下建立新文件t3.txt，并打開
#     print(f.write("OK"))            #寫入OK，并返回2字節的數字
#     flag=True
#     print('文件%s寫入正常！'%(f_n))
# except:
#     print('打開%s文件出錯，請檢查'%(f_n))
# finally:
#     if flag:
#         f.close()
#         print('文件做關閉處理')
#     else:
#         print('程序關閉')
# ========================================================================================================
# import sys
# class BuildNewXML():
#     def __init__(self,filename=None):
#         self.filename=filename
#         self.__get__f=None
#     def openfile(self):
#         if self.filename==None:
#             print("沒有提供文件名！在建立實例時，請提供建立文件的名稱！")
#             return False
#         try:
#             self.__get__f=open(self.filename,'a',encoding='utf-8')
#         except:
#             print('打開%s文件有問題！'%(self.filename))
#             return False
#     def writeXML(self,n,element):
#         try:
#             if n==0:
#                 self.__get__f.write(element+'\n')
#             else:
#                 self.__get__f.write(''*n+element+'\n')
#         except:
#             print('往%s文件寫%s出錯！'%(self.filename,element))
#     def closeXML(self):
#         if self.__get__f:
#             self.__get__f.close()
# #---------------------------------------
# filename="storehouse.xml"
# flag=False
# content={1:[0,'<storehouse>'],
#          2: [4, '<goods category="fish">'],
#          3: [8, '<title>淡水魚</title>'],
#          4: [8, '<name>鯽魚</name>'],
#          5: [8, '<amount>18</amount>'],
#          6: [8, '<price>8</price>'],
#          7:[4,'</goods>'],
#          8:[4,'<goods category="fruit">'],
#          9: [8, '<title>溫帶水果</title>'],
#          10: [8, '<name>猊候桃</name>'],
#          11: [8, '<amount>10</amount>'],
#          12: [8, '<price>10</price>'],
#          13:[4,'</goods>'],
#          14:[0,'</storehouse>']}
# build_xml=BuildNewXML(filename)
# try:
#     build_xml.openfile()
#     for get_item in content.items():
#         build_xml.writeXML(get_item[1][0],get_item[1][1])
#     flag=True
# except:
#     print('往文件寫內容出錯，退出程序！')
#     sys.exit()
# finally:
#     if flag:
#         build_xml.closeXML()
#         print('往%s寫內容完成！'%(filename))
# ========================================================================================================
# import xml.sax
# import sys
# get_record=[]               #全局列表變量，準備接受獲取的XML內容
# class GetStorehouse(xml.sax.ContentHandler):    #自定義獲取倉庫商品類（事件處理器）
#     def __init__(self):         #類初始化保留函數
#         self.CurrentData=""         #自定義當前元素標籤名屬性
#         self.title=""           #自定義商品二級分類屬性
#         self.name=""            #自定義商品名稱內容屬性
#         self.amount=""          #自定義商品數量內容屬性
#         self.price=""           #自定義商品價格內容屬性
#     def startElement(self,label,attributes):            #遇到元素開始標籤時，觸發該函數
#         self.CurrentData=label                          #label為實例對象在解釋時傳遞的標籤名
#         if label=="goods":                                   #二級子元素的開始標籤名比較
#             category=attributes["category"]                 #獲取元素中屬性對應的值
#             return category
#     def endElement(self,label):         #遇到元素結束標籤時，觸發該函數
#         global get_record               #聲明全局變量將要被函數體里使用
#         if self.CurrentData=="title":
#             get_record.append(self.title)
#         elif self.CurrentData=="name":
#             get_record.append(self.name)
#         elif self.CurrentData=="amount":
#             get_record.append(self.amount)
#         elif self.CurrentData=="price":
#             get_record.append=="price"
#     def characters(self,content):                   #遇到元素里的內容，把值賦給實例屬性
#         if self.CurrentData=="title":
#             self.title=content
#         elif self.CurrentData=="name":
#             self.name=content
#         elif self.CurrentData=="amount":
#             self.amount=content
#         elif self.CurrentData=="price":
#             self.price=content
# parser=xml.sax.make_parser()            #創建一個解釋器的XMLReader對象
# parser.setFeature(xml.sax.handler.feature_namespaces,0)     #關閉解釋命令空間
# Handler=GetStorehouse()                                 #建立事件處理器實例
# parser.setContentHandler(Handler)                       #為解釋器設置事件處理實例
# parser.parse("storehouse.xml")                          #正式解釋指定XML文件內容
# print(get_record)                                       #打印全局列表變量的獲取結果
# ========================================================================================================
# import tkinter
# MainForm=tkinter.Tk()
# MainForm.geometry("250x150")
# def reset():   #自定義囘調函數
#    print('1')
# MainForm.title("三酷貓！")
#
# def time_3 ():
#     i = 0
#     for i in range(60):
#         print(i)
#         return str(i)
# # MainForm.iconbitmap('D:\\study')
# MainForm['background']='LightSlateGray'
# btn1=tkinter.Button(MainForm,text="退出",fg="black",command=reset)
# btn2=tkinter.Button(MainForm,text=time_3(),fg="black",command=reset)
# btn2.pack()
# btn1.pack()
# MainForm.mainloop()
# ========================================================================================================
# import tkinter
# MainForm=tkinter.Tk()
# MainForm.geometry("250x100")
# btn1=tkinter.Button(MainForm,text="1",fg="black")
# btn2=tkinter.Button(MainForm,text="2",fg="black")
# btn3=tkinter.Button(MainForm,text="3",fg="black")
# btn1.pack(side="left",padx="1m")
# btn2.pack(side="left",padx="1m")
# btn3.pack(side="left",padx="1m")
# MainForm.mainloop()
# ========================================================================================================+++++++++++++++++++++++++++++++++
# from tkinter import *
# root=Tk()       #創建窗體
# m1=Menu(root)       #創建菜單實例
# root.config(menu=m1)        #為窗體設置菜單屬性
# def callback():         #定義菜單鼠標單機事件囘調函數
#     root.title("OK")        #調用成功，在窗體標題上顯示OK
# filemenu=Menu(m1)           #在m1菜單實例上建立新的子菜單實例
# m1.add_cascade(label="File",menu=filemenu)              #在m1上設置子菜單名并聯名子菜單1
# filemenu.add_command(label="New",command=callback)      #在子菜單增加選擇項名稱和事件
# filemenu.add_command(label="Open...",command=callback)      #增加Open...選項
# filemenu.add_separator()                                    #增加分割線
# filemenu.add_command(label="Exit",command=callback)          #增加Exit選項
# helpmenu=Menu(m1)                                                       #在m1新創建幫組子菜單實例2
# m1.add_cascade(label="Help",menu=helpmenu)                          #在m1上設置子菜單并關連子菜單2
# helpmenu.add_command(label="About...",command=callback)                #Help子菜單增加About...選項
# mainloop()
# ===========================================================================================================================================
# import webbrowser
# import request
# webbrowser.open('https://gcrc.efoxconn.com/#/CRC')
# ==========================================================================================================
# from tkinter import*
# import tkinter.messagebox
# root=Tk()
# class Example(Frame):
#     def __init__(self):
#         super().__init__()          #繼承父類init
#         self.initUI()               #初始化調用initUI（）函數
#     def initUI(self):
#         self.master.title("演示鼠標右鍵跳出菜單")     #在窗體上設置標題（master代表窗體）
#         self.menu=Menu(self.master,tearoff=0)        #在窗體Frame上創建菜單對象
#         self.menu.add_command(label="提示",command=self.showClick)    #跳出菜單第一項
#         self.menu.add_command(label="退出",command=self.onExit)       #跳出菜單第二項
#         self.master.bind("<Button-3>",self.showMenu)                    #窗體鼠標右鍵事件，調用showMenu函數
#         self.pack()     #在窗體定位
#     def showMenu(self,e):           #定義鼠標右鍵囘調函數showMenu
#         self.menu.post(e.x_root,e.y_root)       #彈出對話框
#     def showClick(self):                            #“提示”菜單事件囘調函數
#         tkinter.messagebox.showinfo('提示','鼠標點擊上了！')              #顯示提示對話框
#     def onExit(self):               #“退出”菜單事件毀掉函數
#         self.quit()                 #退出軟件
# root.geometry("250x150")            #設置窗體外觀大小
# app = Example()                     #實例化調用
# root.mainloop()                     #啟動窗體消息循環功能
# ==========================================================================================================
# import tkinter.tix
# from tkinter.constants import * #導入常量模塊
# root=tkinter.tix.Tk()           #創建窗體實例
# top=tkinter.tix.Frame(root,relief=RAISED,bd=1)  #創建框架實例
# top.pack(side="left")                           #框架組件在窗體上的定位
# top.dir=tkinter.tix.DirList(top)                #在框架實例上創建DirList實例
# top.dir.hlist['width']=40                       #設置DirList的寬度
# top.dir.pack(side="left")                       #DirList在框架上的定位
# top.btn=tkinter.tix.Button(top,text=">>",pady=0)    #在框架上創建Button組件實例
# top.btn.pack(side="left")                           #btn對象在框架上的定位
# top.ent=tkinter.tix.LabelEntry(top,label="安裝路徑：",labelside='top')           #在框架上創建定位
# top.ent.pack(side='left')                           #ent對象在框架上的定位
# root.mainloop()
# ==========================================================================================================
# import tkinter.tix
# from tkinter.constants import * #導入常量模塊
# root=tkinter.tix.Tk()           #創建窗體實例
# top=tkinter.tix.Frame(root,relief=RAISED,bd=1)  #創建框架實例
# top.pack(side="left")                           #框架組件在窗體上的定位
# top.dir=tkinter.tix.DirTree(top)                #在框架實例上創建DirList實例
# top.dir.hlist['width']=40                       #設置DirList的寬度
# top.dir.pack(side="left")                       #DirList在框架上的定位
# top.btn=tkinter.tix.Button(top,text=">>",pady=0)    #在框架上創建Button組件實例
# top.btn.pack(side="left")                           #btn對象在框架上的定位
# top.ent=tkinter.tix.LabelEntry(top,label="安裝路徑：",labelside='top')           #在框架上創建定位
# top.ent.pack(side='left')                           #ent對象在框架上的定位
# root.mainloop()
# ==========================================================================================================
# from tkinter import tix
# import tkinter
# def btnDialog(w):        #自定義按鈕對話框函數
#     bbox=tix.ButtonBox(w,orientation=tix.HORIZONTAL)    #創建水平的ButtonBox實例
#     bbox.add('ok',text='確認',underline=0,width=5,command=lambda w=w:w.destroy()) #增加‘確認’按鈕，帶窗體關閉功能
#     bbox.add('close', text='取消', underline=0, width=5, command=lambda w=w: w.destroy())  # 增加‘取消’按鈕，帶窗體關閉功能
#     bbox.pack(side=tix.BOTTOM,fill=tix.X)                               #bbbox對象在窗體上的定位
# if __name__ =='__main__':           #如果直接調用并執行該文件
#     root=tix.Tk()                       #創建窗體實例
#     btnDialog(root)                     #調用btnDialog自定義函數
#     root.mainloop()                     #啟動窗體的消息循環功能
# ============================================================================================================
# import tkinter as tk
# from tkinter import scrolledtext    #導入scrolledtext模塊
# root=tk.Tk()                        #創建窗體實例
# root.title("滾動文本框")             #設置窗體標題
# root.geometry("200x200")            #設置窗體外觀大小
# sWidth=10   #設置文本框的長度
# sHeight=10       #設置文本框的高度
# s_show=scrolledtext.ScrolledText(root,width=sWidth,height=sHeight,wrap=tk.WORD)     #在窗體上創建scrolledtext實例
# s_show.insert('insert',"一行10個字符一行10個字符一行10個字符一行10個字符一行10個字符"
#                        "一行10個字符一行10個字符一行10個字符一行10個字符一行10個字符一行10個字符一行10個字符一行10"
#                        "個字符一行10個字符一行10個字符一行10個字符一行10個字符一行10個字符一行10個字符一行10個字符一"
#                        "行10個字符一行10個字符一行10個字符一行10個字符一行10個字符一行10個字符一行10個字符一行10個字符")       #插入12個字符內容（一個漢字為2個字符）
# s_show.grid(column=0,columnspan=2)          #在窗體設置s_show對象的位置
# root.mainloop()
# ============================================================================================================
# import sqlite3
# # conn1 = sqlite3.connect(":memory:")#基于内存的数据库
# # conn1.close()
# conn = sqlite3.connect("First.db")#基于硬盘的数据库实例
# cur=conn.cursor()   #通過建立數據庫遊標對象，準備讀寫操作
# # cur.execute('''Create table T_fish(date text,name text,nums int,price real,Explain text)''') #創建對應的表結構對象
# # cur.execute("insert into T_fish Values('2018-3-28','黑魚','10','28.3','Tom')")            #插入一行記錄結果信息
# conn.commit()   #保存提交，確保數據保存成功
# cur.execute('select * from T_fish')     #對T_fish執行數據查找命令
# for row in cur.fetchall():          #以一條記錄為元組單位返回結果給row
#     print(row)                      #打印元組記錄
# cur.execute("insert into T_fish Values('2018-3-29','鯉魚','17','10.3','John')")  # 插入一行記錄結果信息
# cur.execute("insert into T_fish Values('2018-3-30','鰱魚','9','9.2','Tim')")  # 插入一行記錄結果信息
# cur.execute('delete from T_fish where nums=10')         #刪除數量為10的記錄
# conn.commit()
# print("====================================================")
# cur.execute('select * from T_fish')     #對T_fish執行數據查找命令
# for row in cur.fetchall():          #以一條記錄為元組單位返回結果給row
#     print(row)                      #打印元組記錄
# conn.close()                        #關閉數據庫鏈接
# ============================================================================================================
# import threading
# print(threading.active_count())
# print(threading.current_thread())
# print(threading.enumerate())
# print(threading.TIMEOUT_MAX)
# ============================================================================================================
# from time import *      #導入time模塊（主要調用sleep（）方法）
# from datetime import datetime       #導入datetime模塊的datetime
# tickets = [
#     ['2018-4-7 8:00','北京','沈楊',10,120],
#     ['2018-4-7 9:00', '上海', '寧波', 5, 100],
#     ['2018-4-7 12:00', '天津', '北京', 20, 55],
#     ['2018-4-7 14:00', '廣州', '武漢', 0, 200],
#     ['2018-4-7 16:00', '重慶', '西安', 3, 180],
#     ['2018-4-7 18:00', '深圳', '上海', 49, 780],
#     ['2018-4-7 18:10', '武漢', '長沙', 10, 210],        #模擬火車票在線銷售信息表
#     ]
# def buy_ticket(name,nums,data1,start_station):  #自定義買火車函數
#     i = 0
#     sleep(1)        #讓函數暫停一秒
#     for get_record in tickets:      #循環獲取列表記錄
#         if get_record[0]==data1 and get_record[1]==start_station:   #比較時間、始發站
#             if get_record[3]>=nums: #比較票數的數量
#                 tickets[i][3]=get_record[3]-nums        #票數量夠，減去已購買數量
#                 return nums     #返回購買數量，終止函數調用
#             else:
#                 print('%s現存票數數量不夠，無法購買！'%(name))    #票數據不夠，給出提示
#                 return -1           #返回操作終止標誌-1
#         i+=1
#     print("%s今日無票，無法購買！"%(name))    #循環結束，還沒有找到購票記錄
#     return -1
# if __name__=='__main__':
#     print('開始時間：',datetime.now())       #程序執行開始時間
#     result = buy_ticket('張山',3,'2018-4-7 9:00','上海')
#     if result > 0 :
#         print('張山購買%d張票成功!'%(3))
#     result = buy_ticket('李四',1,'2018-4-7 14:00','廣州')
#     if result > 0:
#         print('李四購買%d張票成功！'%(1))
#     result = buy_ticket('王五',2,'2018-4-7 9:00','上海')
#     if result > 0:
#         print('王五購買%d張票成功'%(2))
#     print('結束時間：',datetime.now())
#     print('剩餘票數為：\n')
#     for gets in tickets:
#         print(gets)
# ============================================================================================================
# import threading    #threading函數方式實現
# from time import *      #導入time模塊（主要調用sleep（）方法）
# from datetime import datetime       #導入datetime模塊的datetime
# tickets = [
#     ['2018-4-7 8:00','北京','沈楊',10,120],
#     ['2018-4-7 9:00', '上海', '寧波', 5, 100],
#     ['2018-4-7 12:00', '天津', '北京', 20, 55],
#     ['2018-4-7 14:00', '廣州', '武漢', 0, 200],
#     ['2018-4-7 16:00', '重慶', '西安', 3, 180],
#     ['2018-4-7 18:00', '深圳', '上海', 49, 780],
#     ['2018-4-7 18:10', '武漢', '長沙', 10, 210],        #模擬火車票在線銷售信息表
#     ]
# def buy_ticket(name,nums,data1,start_station):  #自定義買火車函數
#     i = 0
#     sleep(1)        #讓函數暫停一秒
#     for get_record in tickets:      #循環獲取列表記錄
#         if get_record[0]==data1 and get_record[1]==start_station:   #比較時間、始發站
#             if get_record[3]>=nums: #比較票數的數量
#                 tickets[i][3]=get_record[3]-nums        #票數量夠，減去已購買數量
#                 return nums     #返回購買數量，終止函數調用
#             else:
#                 print('%s現存票數數量不夠，無法購買！'%(name))    #票數據不夠，給出提示
#                 return -1           #返回操作終止標誌-1
#         i+=1
#     print("%s今日無票，無法購買！"%(name))    #循環結束，還沒有找到購票記錄
#     return -1
# if __name__ =='__main__':
#     print('開始時間：',datetime.now())
#     t1 = threading.Thread(target=buy_ticket,args=('張山',3,'2018-4-7 9:00','上海'))
#     t2 = threading.Thread(target=buy_ticket,args=('李四',1,'2018-4-7 14:00','廣州'))
#     t3 = threading.Thread(target=buy_ticket,args=('王五',2,'2018-4-7 9:00','上海'))
#     t1.start()      #啟動線程t1運行
#     t2.start()      #啟動線程t2運行
#     t3.start()      #啟動線程t3運行
#     t1.join()       #阻塞線程直至線程t1終止，釋放該進程
#     t2.join()       #阻塞線程直至線程t2終止，釋放該進程
#     t3.join()       #阻塞線程直至線程t3終止，釋放該進程
#     print('結束時間',datetime.now())
#     print('剩餘票數為：\n')
#     for gets in tickets:
#         print(gets)
# ================================================================================================================
# import threading    #threading類方式實現
# from time import *
# from datetime import datetime
# tickets = [
#     ['2018-4-7 8:00','北京','沈楊',10,120],
#     ['2018-4-7 9:00', '上海', '寧波', 5, 100],
#     ['2018-4-7 12:00', '天津', '北京', 20, 55],
#     ['2018-4-7 14:00', '廣州', '武漢', 0, 200],
#     ['2018-4-7 16:00', '重慶', '西安', 3, 180],
#     ['2018-4-7 18:00', '深圳', '上海', 49, 780],
#     ['2018-4-7 18:10', '武漢', '長沙', 10, 210],        #模擬火車票在線銷售信息表
#     ]
# def buy_ticket(name,nums,data1,start_station):  #自定義買火車函數
#     i = 0
#     sleep(1)        #讓函數暫停一秒
#     for get_record in tickets:      #循環獲取列表記錄
#         if get_record[0]==data1 and get_record[1]==start_station:   #比較時間、始發站
#             if get_record[3]>=nums: #比較票數的數量
#                 tickets[i][3]=get_record[3]-nums        #票數量夠，減去已購買數量
#                 print('%s購買%d張票成功！'%(name,nums))
#                 return
#             else:
#                 print('%s現存票數數量不夠，無法購買！'%(name))    #票數據不夠，給出提示
#                 return -1           #返回操作終止標誌-1
#         i+=1
#     print("%s今日無票，無法購買！"%(name))    #循環結束，還沒有找到購票記錄
#     return -1
# class MThread(threading.Thread):                #新增繼承Thread類的子類MThread
#     def __init__(self,target,args):                 #定義類的構造函數__init__
#         threading.Thread.__init__(self)             #繼承父類__init__
#         self.target = target                        #把自定義函數傳遞給變量
#         self.args = args                            #Z自定義函數的參數，傳遞給類變量
#     def run(self) -> None:                                  #重寫run方法
#         self.target(*self.args)                             #線程在此執行自定義函數
# if __name__ == '__main__':      #若為主程序，執行自定義函數
#     visitor=[('張山',3,'2018-4-7 9:00','上海'),
#              ('李四',1,'2018-4-7 14:00','廣州'),
#              ('王五',2,'2018-4-7 9:00','上海')]         #以列表形式定義搶票訪問內容
#     class_do_list=[]        #定義裝線程對象的空列表
#     print('開始時間：',datetime.now())
#     for get_r in visitor:
#         get_one = MThread(target=buy_ticket,args=get_r)
#         class_do_list.append(get_one)
#     for i in range (len(class_do_list)):
#         class_do_list[i].start()
#     for i in range(len(class_do_list)):
#         class_do_list[i].join()
#     print('結束時間：',datetime.now())
#     print('剩餘票數為：\n')
#     for gets in tickets:
#         print(gets)
# ============================================================================================================
# import threading    #threading類方式實現
# from time import *
# from datetime import datetime
# tickets = [
#     ['2018-4-7 8:00', '北京' , '沈楊' ,10,120],
#     ['2018-4-7 9:00', '上海', '寧波', 5, 100],
#     ['2018-4-7 12:00', '天津', '北京', 20, 55],
#     ['2018-4-7 14:00', '廣州', '武漢', 0, 200],
#     ['2018-4-7 16:00', '重慶', '西安', 3, 180],
#     ['2018-4-7 18:00', '深圳', '上海', 49, 780],
#     ['2018-4-7 18:10', '武漢', '長沙', 10, 210],        #模擬火車票在線銷售信息表
#
#     ['2018-4-8 8:00', '北京', '沈楊', 10, 120],
#     ['2018-4-8 9:00', '上海', '寧波', 5, 100],
#     ['2018-4-8 12:00', '天津', '北京', 20, 55],
#     ['2018-4-8 14:00', '廣州', '武漢', 0, 200],
#     ['2018-4-8 16:00', '重慶', '西安', 3, 180],
#     ['2018-4-8 18:00', '深圳', '上海', 49, 780],
#     ['2018-4-8 18:10', '武漢', '長沙', 10, 210],  # 模擬火車票在線銷售信息表
#
#     ['2018-4-9 8:00', '北京', '沈楊', 10, 120],
#     ['2018-4-9 9:00', '上海', '寧波', 990, 100],
#     ['2018-4-9 12:00', '天津', '北京', 20, 55],
#     ['2018-4-9 14:00', '廣州', '武漢', 0, 200],
#     ['2018-4-9 16:00', '重慶', '西安', 3, 180],
#     ['2018-4-9 18:00', '深圳', '上海', 49, 780],
#     ['2018-4-9 18:10', '武漢', '長沙', 10, 210],  # 模擬火車票在線銷售信息表
#     ]
#
# def update_prcie(start_station,nums):
#     j=0
#     while j<len(tickets):
#         tickets[j][3] = tickets[j][3]+nums
#         j+=1
#
# def buy_ticket(name,nums,data1,start_station):  #自定義買火車函數
#     i = 0
#     # sleep(1)        #讓函數暫停一秒
#     for get_record in tickets:      #循環獲取列表記錄
#         if get_record[0]==data1 and get_record[1]==start_station:   #比較時間、始發站
#             if get_record[3]>=nums: #比較票數的數量
#                 tickets[i][3]=get_record[3]-nums        #票數量夠，減去已購買數量
#                 print('%s購買%d張票成功！'%(name,nums))
#                 return
#             else:
#                 print('%s現存票數數量不夠，無法購買！'%(name))    #票數據不夠，給出提示
#                 return -1           #返回操作終止標誌-1
#         i+=1
#     print("%s今日無票，無法購買！"%(name))    #循環結束，還沒有找到購票記錄
#     return -1
# class MThread(threading.Thread):                #新增繼承Thread類的子類MThread
#     def __init__(self,target,args):                 #定義類的構造函數__init__
#         threading.Thread.__init__(self)             #繼承父類__init__
#         self.target = target                        #把自定義函數傳遞給變量
#         self.args = args                            #Z自定義函數的參數，傳遞給類變量
#     def run(self) -> None:                                  #重寫run方法
#         self.target(*self.args)                             #線程在此執行自定義函數
# if __name__ == '__main__':      #若為主程序，執行自定義函數
#     class_do_list=[]
#     print('開始時間：',datetime.now())
#     get_one = MThread(target=update_prcie,args=('上海',5))            #一個更新火車票數量線程
#     class_do_list.append(get_one)
#     for get_i in range(500):            #循環產生500個幷發線程
#         get_one=MThread(target=buy_ticket,args=(get_i,2,'2018-4-9 9:00','上海'))
#         class_do_list.append(get_one)
#     get_one=MThread(target=update_prcie,args=('上海',5))      #一個更新火車票數量線程
#     class_do_list.append(get_one)
#     for i in range(len(class_do_list)):
#         class_do_list[i].start()
#     for i in range (len(class_do_list)):
#         class_do_list[i].join()
#     print('結束時間：',datetime.now())
#     print('剩餘票數為：\n')
#     for gets in tickets:
#         print(gets)
# ==============================================================================================================
# import queue
# import threading
# import time
# import random
# q_data = queue.Queue(10)    #創建10個元素的隊列實例
# do_thread_num=5             #指定5個線程的變量
# def getOne(one,j):          #自定義獲取隊列元素輸出打印函數
#     time.sleep(random.random()*3)       #讓線程休眠隨機秒
#     print('線程序號%d,獲取元素%d\n'%(j,one))
# class MyThread(threading.Thread):               #自定義獲取隊列元素線程類
#     def __init__(self,func,data,j):             #類構造函數，傳遞參數
#         threading.Thread.__init__(self)         #繼承線程類構造函數
#         self.data=data                          #把隊列對象傳遞給data變量
#         self.j=j                                #把隊列調用序號傳遞給J變量
#         self.func=func                          #把自定義函數傳遞給func變量
#     def run(self) -> None:                      #重寫run方法
#         while self.data.qsize()>0:      #根據實際大小，循環
#             self.func(self.data.get(),self.j)       #獲取隊列元素，調用自定義輸出函數
# if __name__=='__main__':
#     for data in range(do_thread_num*2):     #循環10次，從0到9
#         q_data.put(data)            #給隊列增加0到9的元素值
#     for j in range(do_thread_num):    #這裡只讓一個線程讀10個元素
#         t1 = MyThread(getOne,q_data,j).start()      #啟動線程讀隊列元素
# ==============================================================================================================
# Process(group =None,target = None,name=None,args=(),Kwargs={},*,daemon=None)
# '''
# group可選保留參數
# target傳遞進程需要處理的自定義函數
# name參數指定進程名
# args以元組形式傳遞自定義函數的參數
# kwargs以字典形式傳遞自定義函數的參數
# daemon可選參數，指定值為True時，表示該進程為守護進程。默認狀態為非守護進程
# '''
# from multiprocessing import Process
# from datetime import datetime
# def do1(j):
#     print("第%d進程！"%(j))
# class MyProcess(Process):
#     def __init__(self,target,args):
#         Process.__init__(self)
#         self.target = target
#         self.args = args
#     def run(self) -> None:
#         self.target(self.args)
# if __name__=='__main__':
#     print('開始時間：',datetime.now())
#     for i in range(10):
#         p1=MyProcess(target=do1,args=(i,))
#         p1.start()
#         p1.join()
#     print('結束時間：',datetime.now())
# ==============================================================================================================
# import multiprocessing
# from datetime import datetime
# def do1(j):
#     print('進程%d'%(j))
# if __name__ == '__main__':
#     print('開始時間：',datetime.now())
#     pool = multiprocessing.Pool()      # cpu幾核
#     for i in range(10):
#         pool.apply_async(do1,(i,))
#     pool.close()
#     pool.join()
#     print('結束時間：',datetime.now())
# ==============================================================================================================
# 基於pipe的多進程，用在兩個端對端的進程通信
# from multiprocessing import Process,Pipe
# def do_send(conn_s,j):
#     conn_s.send({'發送序號':j,'鯽魚':[18,10,5],'鯉魚':[8,6.2]})     #send發送一條字典
#     conn_s.close()
# if __name__ == '__main__':
#     receive_conn,send_conn=Pipe()       #管道對象返回兩個鏈接對象
#     i = 0
#     while i < 2:
#         i+=1
#         pp = Process(target=do_send,args=(send_conn,i))     #調用進程對象創建發送
#         pp.start()                                          #啟動進程發送
#         print('接受數據成功%s成功！'%(receive_conn.recv()))  #接收管道發送數據
#         pp.join()                                           #阻塞，等待進程執行完畢
# ==============================================================================================================
# 基於queue的多進程，多端點通信
# from multiprocessing import Process,Queue
# q_object = Queue(5)         #創建5個元素的隊列實例
# def SendData(qObject,data):     #發送函數，通過隊列對象qObject發送data信息
#     qObject.put(data)           #用put方法發送data信息
# def receiveData(qObject):       #接收函數，通過對象qObject接收信息
#     if qObject.empty()>0:           #隊列消息為空時，不接收信息
#         print('隊列信息為空！')
#     else:
#         show_data = qObject.get()           #隊列對象qObject通過get（）方法接收信息
#         print('輸出%s'%(show_data))           #輸出信息
# if __name__=='__main__':
#     send_data = [0,'Tom',10,'China']                #發送數據
#     for i in range(5):      #循環發送、接收5條信息
#         send_data[0]=i      #對列表第一個元素進行修改
#         p1 = Process(target=SendData,args=(q_object,send_data))     #進程實例調用發送函數
#         p1.start()      #啟動線程p1
#         p2 = Process(target=receiveData,args=(q_object,))   #進程調用接收函數并創建實例
#         p2.start()      #啟動進程P2
# ==============================================================================================================
# import math
# def sums(*num):
#     '''
#     >>>sums(1,2,3,4,5)
#     15
#     >>>sums('s',2,3,4,5)
#     '''
#     total = math.trunc(sum(num))
#     return total
#     # print("累加為：%f"%total)
# if __name__ == '__main__':
#         import doctest
#         doctest.testmod(verbose=False)
# ==============================================================================================================
# import math
# def suns(*num):
#     total=math.trunc((sum(num)))
#     return total
# if __name__=='__main__':
#     import doctest
#     doctest.testfile('./TestSave_files/test_content.txt',verbose=False)
# ==============================================================================================================
# import unittest
# def showMsg(msg):
#     return "%s"%(msg)
# def do_divide(a,b):
#     return (a/b)
# def ShowTrue(flag):
#     return (flag)
# class TestSomeFunc(unittest.TestCase):
#     def testrun(self):
#         self.assertEqual('OK',showMsg('OK'))
#         self.assertNotEqual('OK',showMsg('NO'))
#         self.assertTrue(do_divide(1,2))
#         self.assertIs(ShowTrue(False),False)
#         self.assertIs(int(do_divide(1,2)),1)
#         self.assertIs(int(do_divide(1,2)),1)
# if __name__=='__main__':
#     unittest.main()
# ==============================================================================================================
# 进度条功能
# import time
#
# for i in range(10):
#     print("\r" + "■"*i, sep="", end="")
#     time.sleep(0.2)
# print("\n下载完成")
# ==============================================================================================================
# import requests
# import re
# import ssl
# from requests.packages.urllib3.exceptions import InsecureRequestWarning
#
# ssl._create_default_https_context = ssl._create_unverified_context
# #关闭安全请求警告
# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
#
# #设置代理ip
# proxies = {
# 	"http":"http://X2003899:foxconn12@10.36.6.68:3128",
#     # "https":"http://X2003899:foxconn12@10.36.6.68:3128"
# }

# r = requests.get('http://wwww.baidu.com',proxies=proxies)
# print(r.text)
# response = requests.request("get","http://www.baidu.com",proxies = proxies)
# print(response.text)
# pa = re.compile(r'<a.+>(.+?)</a>')
# option = pa.findall(r.text)
# for get_text in option:
#     print(get_text)

# ==============================================================================================================
# 列表去重
# lise_my = ['1','1','1','aa','aa','aa','2']
# print(lise_my)
# lise2 = list(set(lise_my))               #列表失去原有顺序，但是速度快
# lise2 = list(dict.fromkeys(lise_my))     #Python3.6及以上才支持,保留顺序速度中
# from collections import OrderedDict   #Python3.6以下，它由collections提供，保留顺序速度稍慢
# lise2 = list(OrderedDict.fromkeys(lise_my))
# print(lise2)
##==============================================================================================================
# week_day = 20
# weekend = 40
# print(int(142*50+(142*50/21.75/8)*1.5*week_day+(142*50/21.75/8)*2*weekend-300-568-305-200))
##==============================================================================================================
# 复利
# year = -24 + 60
# mon = 12 * 3000
# li = 1.05
#
#
# def count(year):
#     if year == 1:
#         total_mon = mon * pow(li, 1)
#     else:
#         total_mon = mon * pow(li, year) + count(year - 1)
#     return total_mon
#
#
# total_mon = int(count(year))
# print(f"all {total_mon}, every year {int(total_mon*(li-1))},every month {int(total_mon*(li-1)/12)}")
# print(f"{total_mon/(mon*year)-1}")
##==============================================================================================================

##==============================================================================================================
# ca_mon = 183363 #185815,62047,123768,3438   183363,94947,88416,2456
# first_pay = ca_mon*0.5 #0.3339181443909265,0.5178089363721143,9089,3608.相差6302，3265.5
# print(62047+123768)
# every_month_pay = 123768*pow(1.0475,3)/36
# print(every_month_pay)
##==============================================================================================================
# squares = [values**2 for values in range (1,21)]
# print(squares)
##==============================================================================================================
# with open('./result.txt') as file_object:
#     contents = file_object.read()
# print(23+20)
##==============================================================================================================
# #生成数据
# import matplotlib.pyplot as plt
#
# x_values = range(1,1001)
# y_values = [x**2 for x in x_values]
#
# plt.style.use('seaborn')
# fig,ax = plt.subplots()
# # ax.plot(imput_value,squares,linewidth=3) #linewidth線的寬度
# ax.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,s=10) # s點的尺寸,顏色c='red'/(0,0.8,0)，顏色映射c=y_values,cmap=plt.cm.Blues,
#
# #設置圖表標題給座標軸加上標籤
# ax.set_title("平方数",fontsize=24)
# ax.set_xlabel("值",fontsize=14)
# ax.set_ylabel("值的平方",fontsize=14)
# #設置刻度標記大小
# ax.tick_params(axis='both',labelsize=14)
# #設置每個座標軸的取值範圍,x和y座標的最小值和最大值
# ax.axis([0,1100,0,1100000])
#
# plt.rcParams['font.sans-serif']=['SimHei'] #显示中文标签
# plt.rcParams['axes.unicode_minus']=False   #解决负号“-”显示为方块的问题
# plt.show()
#自動保存圖表
# plt.savefig('squares_plot.png',bbox_inches='tight')#保存目錄，裁剪空白區域
# ##==============================================================================================================
# # 随机漫步
# from random import choice
# import matplotlib.pyplot as plt
#
# class RandomWalk:
#     '''一个生成随机漫步数据的类'''
#     def __init__(self,num_points=5000):
#         '''初始化随机漫步的属性'''
#         self.num_points = num_points
#
#         #所有随机漫步都始于（0，0）
#         self.x_values = [0]
#         self.y_values = [0]
#
#     def fill_walk(self):
#         '''计算随机漫步包含所有的点'''
#
#         #不断漫步，直到列表达到指定长度
#         while len(self.x_values) < self.num_points:
#
#             #决定前进方向及沿这个方向前进的距离
#             x_direction  = choice([1,-1])
#
#             x_distance = choice([0,1,2,3,4])
#             x_step = x_direction*x_distance
#
#             y_direction = choice([1, -1])
#
#             y_distance = choice([0, 1, 2, 3, 4])
#             y_step = y_direction * y_distance
#
#             #拒绝原地踏步
#             if x_step == 0 and y_step == 0:
#                 continue
#
#             #计算下一个点的x值和y值
#             x = self.x_values[-1] + x_step
#             y = self.y_values[-1] + y_step
#
#             self.x_values.append(x)
#             self.y_values.append(y)
#
# #创建一个randomwalk实例
# rw = RandomWalk(50000)
# rw.fill_walk()
# #将所有的点都绘制出来
# plt.style.use('classic')
# fig,ax = plt.subplots(figsize=(12,8))
# point_numbers = range(rw.num_points)
# ax.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,edgecolors='none',s=1)
#
# #突出起点和终点
# ax.scatter(0,0,c='green',edgecolors='none',s=100)
# ax.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=100)
#
# #隐藏坐标轴
# ax.get_xaxis().set_visible(False)
# ax.get_yaxis().set_visible(False)
#
# plt.show()
##==============================================================================================================
# 直方图
# from random import randint
# from plotly.graph_objs import Bar,Layout
# from plotly import offline
#
#
# class Die:
#     '''表示一个骰子'''
#     def __init__(self,num_sides=6):
#         '''骰子默认为6面'''
#         self.num_sides = num_sides
#
#     def roll(self):
#         '''返回一个位于1和骰子面数之间的随机值'''
#         return randint(1,self.num_sides)
#
# #创建两个D6
# die_1 = Die()
# die_2 = Die(10)
#
# #掷几次骰子并将结果储存在一个队列中
# results = []
# for roll_num in range(50_000):
#     result = die_1.roll()+die_2.roll()
#     results.append(result)
#
# #分析结果
# frequencies = []
# max_result = die_1.num_sides + die_2.num_sides
# for value in range(2,max_result+1):
#     frequency = results.count(value)
#     frequencies.append(frequency)
#
# #对结果可视化
# x_values = list(range(2,max_result+1))
# data = [Bar(x=x_values,y=frequencies)]#Bar()表示用于绘制条形图的数据集
#
# x_axis_config = {'title':'结果','dtick':1}
# y_axis_config = {'title':'结果的频率'}
# my_layout = Layout(title='掷一个D6和一个d10 50000次的结果',xaxis=x_axis_config,yaxis=y_axis_config)
# offline.plot({'data':data,'layout':my_layout},filename='d6_d10.html')
##==============================================================================================================
# 下载数据 CSV文件格式处理
# import csv
# from datetime import datetime
# import matplotlib.pyplot as plt
#
# filename = r'C:\Users\X2003899\Downloads\source_code\chapter_16\the_csv_file_format\data\death_valley_2018_simple.csv'
# with open(filename) as f:
#     reader = csv.reader(f)
#     header_row = next(reader)
#     # for index,column_header in enumerate(header_row):
#     #     print(index,column_header)
#     #从文件中获取日期和最高温度
#     dates,highs,lows = [],[],[]
#     for row in reader:
#         current_date = datetime.strptime(row[2],'%Y-%m-%d')
#         try:
#             high = int(row[4])
#             low = int(row[5])
#         except:
#             print(f"Missing data for {current_date}")
#         else:
#             dates.append(current_date)
#             highs.append(high)
#             lows.append(low)
#     # print(highs)
#
# #=根据最高温和最低温绘制图形
# plt.style.use('seaborn')
# fig,ax = plt.subplots()
# ax.plot(dates,highs,c='red',alpha=0.5)
# ax.plot(dates,lows,c='blue',alpha=0.5)
# ax.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)
#
# #设置图形格式
# ax.set_title("2018年每日最高温度",fontsize=24)
# ax.set_xlabel('',fontsize=16)
# fig.autofmt_xdate()
# ax.set_ylabel('温度（F）',fontsize=16)
# ax.tick_params(axis='both',which='major',labelsize=16)
#
# plt.rcParams['font.sans-serif']=['SimHei'] #显示中文标签
# plt.rcParams['axes.unicode_minus']=False   #解决负号“-”显示为方块的问题
# plt.show()
##==============================================================================================================
# 下载数据 JSON格式处理
# import json
# import plotly.express as px
# import pandas as pd
# #探索数据结构
# filename = r'C:\Users\X2003899\Downloads\source_code\chapter_16\mapping_global_data_sets\data\eq_data_30_day_m1.json'
# with open(filename) as f:
#     all_eq_data = json.load(f)
#
# # readable_file = 'readable_eq_data.json'
# # with open(readable_file,'w') as f:
# #     json.dump(all_eq_data,f,indent=4)
#
# all_eq_dicts = all_eq_data['features']
#
# mags,titles,lons,lats = [],[],[],[]
# for eq_dict in all_eq_dicts:
#     mag = eq_dict['properties']['mag']
#     title = eq_dict['properties']['title']
#     lon = eq_dict['geometry']['coordinates'][0]
#     lat = eq_dict['geometry']['coordinates'][1]
#     mags.append(mag)
#     titles.append(title)
#     lons.append(lon)
#     lats.append(lat)
#
# # '''
# # # print(mags[:10])
# # # print(titles[:2])
# # # print(lons[:5])
# # # print(lats[:5])
# # #
# # # fig = px.scatter(
# # #     x=lons,
# # #     y=lats,
# # #     labels={'x':'经度','y':'纬度'},
# # #     range_x=[-200,200],
# # #     range_y=[-90,90],
# # #     width=800,
# # #     height=800,
# # #     title='全球地震散点图',
# # # )
# # '''
#
#
# data = pd.DataFrame(
#     data=zip(lons,lats,titles,mags),
#     columns=['经度','纬度','位置','震级']
# )
# fig = px.scatter(
#     data,
#     x='经度',
#     y='纬度',
#     range_x=[-200,200],
#     range_y=[-90,90],
#     width=800,
#     height=800,
#     title='全球地震散点图',
#     size='震级',
#     size_max=10,
#     color='震级',
#     hover_name='位置',
# )
# fig.write_html('global_earthquakes.html')
# fig.show()
##==============================================================================================================
# https://api.github.com/rate_limit
# https://api.github.com/search/repositories?q=language:python&sort=stars
# import requests
# from plotly.graph_objs import Bar
# from plotly import offline
#
# import ssl
# from requests.packages.urllib3.exceptions import InsecureRequestWarning
# #关闭安全请求警告
# ssl._create_default_https_context = ssl._create_unverified_context
# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
# #设置代理ip
# proxies = {
# 	# "http":"http://X2003899:foxconn12@10.36.6.68:3128",
#     "https":"http://X2003899:foxconn12@10.36.6.68:3128"
# }
#
# #执行API调用并储存响应
# url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
# headers = {'Accept':'application/vnd.github.v3+json'}
# r = requests.get(url,headers=headers,proxies=proxies)
# print(f"Status code:{r.status_code}")
#
# #处理结果
# #将api响应赋给一个变量
# response_dict = r.json()
# repo_dicts = response_dict['items']
# repo_links,stars,labels = [],[],[]
# for repo_dict in repo_dicts:
#     repo_name = repo_dict['name']
#     repo_url = repo_dict['html_url']
#     repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
#     repo_links.append(repo_link)
#     stars.append(repo_dict['stargazers_count'])
#
#     owner = repo_dict['owner']['login']
#     description = repo_dict['description']
#     label = f"{owner}<br />{description}"
#     labels.append(label)
#
# data = [{
#     'type':'bar',
#     'x':repo_links,
#     'y':stars,
#     'hovertext':labels,
#     'marker':{
#         'color':'rgb(60,100,150)',
#         'line':{'width':1.5,'color':'rgb(25,25,25)'}
#     },
#     'opacity':0.6,
# }]
# my_layout = {
#     'title':'GitHub上最受欢迎的python项目',
#     'titlefont':{'size':28},
#     'xaxis':{
#         'title':'Repository',
#         'titlefont':{'size':24},
#         'tickfont':{'size':14},
#     },
#     'yaxis':{
#         'title':'Stars',
#         'titlefont':{'size':24},
#         'tickfont':{'size':14},
#     },
# }
#
# fig = {'data':data,'layout':my_layout}
# offline.plot(fig,filename='python_repos.html')
##==============================================================================================================
# 银行
# guxi0 = 0.2933
# guxi1 = 0.266
# guxi2 = 0.2628
# guxi3 = 0.2506
# guxi4 = 0.2408
# guxi5 = 0.2343
# guxi6 = 0.2333
# guxi7 = 0.2554
# guxi8 = 0.2617
# guxi9 = 0.239
# guxi10 = 0.203
# guxi11 = 0.184
# guxi12 = 0.17
# guxi13 = 0.165
# guxi14 = 0.133
# guxi15 = 0.016
# print(f"{guxi0/0.03:.3f}\t{guxi0/0.035:.3f}\t{guxi0/0.04:.3f}\t{guxi0/0.045:.3f}\t{guxi0/0.05:.3f}\t{guxi0/0.055:.3f}\t{guxi0/0.06:.3f}\t{guxi0/0.065:.3f}\t{guxi0/0.07:.3f}")
# print(f"{guxi1/0.03:.3f}\t{guxi1/0.035:.3f}\t{guxi1/0.04:.3f}\t{guxi1/0.045:.3f}\t{guxi1/0.05:.3f}\t{guxi1/0.055:.3f}\t{guxi1/0.06:.3f}\t{guxi1/0.065:.3f}\t{guxi1/0.07:.3f}")
# print(f"{guxi2/0.03:.3f}\t{guxi2/0.035:.3f}\t{guxi2/0.04:.3f}\t{guxi2/0.045:.3f}\t{guxi2/0.05:.3f}\t{guxi2/0.055:.3f}\t{guxi2/0.06:.3f}\t{guxi2/0.065:.3f}\t{guxi2/0.07:.3f}")
# print(f"{guxi3/0.03:.3f}\t{guxi3/0.035:.3f}\t{guxi3/0.04:.3f}\t{guxi3/0.045:.3f}\t{guxi3/0.05:.3f}\t{guxi3/0.055:.3f}\t{guxi3/0.06:.3f}\t{guxi3/0.065:.3f}\t{guxi3/0.07:.3f}")
# print(f"{guxi4/0.03:.3f}\t{guxi4/0.035:.3f}\t{guxi4/0.04:.3f}\t{guxi4/0.045:.3f}\t{guxi4/0.05:.3f}\t{guxi4/0.055:.3f}\t{guxi4/0.06:.3f}\t{guxi4/0.065:.3f}\t{guxi4/0.07:.3f}")
# print(f"{guxi5/0.03:.3f}\t{guxi5/0.035:.3f}\t{guxi5/0.04:.3f}\t{guxi5/0.045:.3f}\t{guxi5/0.05:.3f}\t{guxi5/0.055:.3f}\t{guxi5/0.06:.3f}\t{guxi5/0.065:.3f}\t{guxi5/0.07:.3f}")
# print(f"{guxi6/0.03:.3f}\t{guxi6/0.035:.3f}\t{guxi6/0.04:.3f}\t{guxi6/0.045:.3f}\t{guxi6/0.05:.3f}\t{guxi6/0.055:.3f}\t{guxi6/0.06:.3f}\t{guxi6/0.065:.3f}\t{guxi6/0.07:.3f}")
# print(f"{guxi7/0.03:.3f}\t{guxi7/0.035:.3f}\t{guxi7/0.04:.3f}\t{guxi7/0.045:.3f}\t{guxi7/0.05:.3f}\t{guxi7/0.055:.3f}\t{guxi7/0.06:.3f}\t{guxi7/0.065:.3f}\t{guxi7/0.07:.3f}")
# print(f"{guxi8/0.03:.3f}\t{guxi8/0.035:.3f}\t{guxi8/0.04:.3f}\t{guxi8/0.045:.3f}\t{guxi8/0.05:.3f}\t{guxi8/0.055:.3f}\t{guxi8/0.06:.3f}\t{guxi8/0.065:.3f}\t{guxi8/0.07:.3f}")
# print(f"{guxi9/0.03:.3f}\t{guxi9/0.035:.3f}\t{guxi9/0.04:.3f}\t{guxi9/0.045:.3f}\t{guxi9/0.05:.3f}\t{guxi9/0.055:.3f}\t{guxi9/0.06:.3f}\t{guxi9/0.065:.3f}\t{guxi9/0.07:.3f}")
# print(f"{guxi10/0.03:.3f}\t{guxi10/0.035:.3f}\t{guxi10/0.04:.3f}\t{guxi10/0.045:.3f}\t{guxi10/0.05:.3f}\t{guxi10/0.055:.3f}\t{guxi10/0.06:.3f}\t{guxi10/0.065:.3f}\t{guxi10/0.07:.3f}")
# print(f"{guxi11/0.03:.3f}\t{guxi11/0.035:.3f}\t{guxi11/0.04:.3f}\t{guxi11/0.045:.3f}\t{guxi11/0.05:.3f}\t{guxi11/0.055:.3f}\t{guxi11/0.06:.3f}\t{guxi11/0.065:.3f}\t{guxi11/0.07:.3f}")
# print(f"{guxi12/0.03:.3f}\t{guxi12/0.035:.3f}\t{guxi12/0.04:.3f}\t{guxi12/0.045:.3f}\t{guxi12/0.05:.3f}\t{guxi12/0.055:.3f}\t{guxi12/0.06:.3f}\t{guxi12/0.065:.3f}\t{guxi12/0.07:.3f}")
# print(f"{guxi13/0.03:.3f}\t{guxi13/0.035:.3f}\t{guxi13/0.04:.3f}\t{guxi13/0.045:.3f}\t{guxi13/0.05:.3f}\t{guxi13/0.055:.3f}\t{guxi13/0.06:.3f}\t{guxi13/0.065:.3f}\t{guxi13/0.07:.3f}")
# print(f"{guxi14/0.03:.3f}\t{guxi14/0.035:.3f}\t{guxi14/0.04:.3f}\t{guxi14/0.045:.3f}\t{guxi14/0.05:.3f}\t{guxi14/0.055:.3f}\t{guxi14/0.06:.3f}\t{guxi14/0.065:.3f}\t{guxi14/0.07:.3f}")
# print(f"{guxi15/0.03:.3f}\t{guxi15/0.035:.3f}\t{guxi15/0.04:.3f}\t{guxi15/0.045:.3f}\t{guxi15/0.05:.3f}\t{guxi15/0.055:.3f}\t{guxi15/0.06:.3f}\t{guxi15/0.065:.3f}\t{guxi15/0.07:.3f}")
##====================================================================================================================================================================================================
# from apscheduler.schedulers.blocking import BlockingScheduler
# def myjob():
#     print('sss')
# sched = BlockingScheduler()
# sched.add_job(myjob,'interval',seconds=2,id='myjob_id')
# sched.start()
##=====================================================================================================================================
# import time
#
# print(time.strftime("%Y%m%d_%H%M%S", time.localtime()))
##=====================================================================================================================================
# import re
#
# result_dict = {}
# processed = None
# processeds = None
# sub_result_dict = {}
# result_list = []
# sernum ='FOC09018908'
# # item_list = [178, 179, 180, 181]
# item_list = [178]
# object_words = ['Power', 'Freq Err', 'EVM']
# log_file_name = 'result.txt'
# f = open(log_file_name)
# data = f.read()
# f.close()
# result1 = data.find('* P A S S E D *')
# result2 = data.find('*  P A S S  *')
# result3 = data.find('* F A I L E D *')
# result4 = data.find('*  F A I L  *')
# if result1 != -1 or result3 != -1:
#     processeds = data.split('Total Test Time:')
#     processed = processeds[0].split('Test Result:')
# if result2 != -1:
#     processeds = data.split('*  P A S S  *')
#     processed = processeds[0].split('ERROR_MESSAGE')
# if result4 != -1:
#     processeds = data.split('*  F A I L  *')
#     processed = processeds[0].split('ERROR_MESSAGE')
# result_dict['sernum'] = {}
#
#
# def extract_power_value(result_list=None, key_words=None):
#     power_value_dict = {}
#     # print(f"aaaaaaaaaaaaa{result_list}")
#     if not key_words:
#         raise Exception("No key words")
#     for key in result_list:
#         # print(f"aaaaaaaaaaaaa{key}")
#         key_str = key.split(':')[0].strip()
#         for word in key_words:
#             if word == key_str:
#                 power = re.search(r'([+-]?\d*\.\d\d|[+-]?\d+)', key)
#                 # print(power)
#                 power_value_dict[word] = float(power.group())
#     return power_value_dict
#
#
# for elements in processed:
#     elements_items = elements.split('\n') # 变成每一行
#     for i in elements_items:
#         if re.match(r'\d+\.[ ]?\w+', i):
#             item_number_str = re.search(r'(\d+)\.', i)
#             if item_number_str:
#                 item_number = item_number_str.group(1)
#                 if int(item_number) in item_list or str(item_number) in item_list:
#                     power_value = extract_power_value(result_list=elements_items, key_words=object_words)
#                     # print(f"{item_number}   {power_value}")
#                     sub_result_dict[i] = power_value
#                     result_list.append(sub_result_dict)
#                     # print(result_list)
#                     sub_result_dict = {}
# result_dict[sernum] = result_list
# print('Result Dict is:{}'.format(result_dict))
# 最后的最后log.find_value('Litepoint analyse Result Dict is:{}'.format(self.litpoint_record_dict))
# {'str1name': 'Power_178_179_180_181', 'str1': '20.25_20.34_20.33_20.36', 'str2name': 'Freq Err_178_179_180_181',
#  'str2': '-1.71_-1.71_-1.71_-1.71', 'str3name': 'EVM_178_179_180_181', 'str3': '-40.14_-39.79_-41.21_-40.36'}
##=====================================================================================================================================
# import os
# import re

# path_list = os.listdir()
# for i_name in range(0,len(path_list),1):
#     try:
#         path_list[i_name].index('.txt')
#         file_name = path_list[i_name]
#         f1 = open(file_name, 'r+', encoding='utf-8')  # 打开本地的test.txt文本文件
#         content = f1.read()
#         f1.close()  # 关闭操作
#         for cc in range(1, 9, 1):
#             aa = re.findall(f"ANT{cc}\\u0020+---[\s\S]*?PASS[\s\S]*?Secs.", content)
#             for key in range(0, len(aa), 1):
#                 content = content.replace(aa[key], f"ANT{cc}     ---------------------- J{cc}")
#         with open(file_name, "w", encoding='utf-8') as f2:  # 再次打开test.txt文本文件
#             f2.write(content)  # 将替换后的内容写入到test.txt文本文件中
#             f2.close()
#     except:
#         pass
##=====================================================================================================================================
# from collections import Counter
# s = 'aaabbbccffgg'
# def minDeletions(s):
#     lst=sorted(list(Counter(s).values()),reverse=True)
#     ans=0
#     print(lst)
#     for i in range(1,len(lst)):
#         print(f"lst[i]={lst[i]}***i={i}")
#         if lst[i]>=lst[i-1]:
#             print(f"lst[i]={lst[i]}      lst[i-1]={lst[i-1]}")
#             if lst[i-1]>0:
#                 print(f"lst[i-1]={lst[i-1]}>0")
#                 ans+=lst[i]-lst[i-1]+1
#                 print(f"ans={ans}=lst[i]{lst[i]}-lst[i-1]{lst[i-1]} +1")
#                 lst[i]=lst[i-1]-1
#                 print(f"lst[i]={lst[i]} = lst[i-1]-1={lst[i-1]}-1")
#             else:
#                 ans+=lst[i]
#                 print(f"ans={ans}    lst[i]={lst[i]}###")
#                 lst[i]=0
#     print(lst)
#     return ans
#
# def minDeletions2(s):# 把后面的都减1
#     c = sorted(Counter(s).values(), reverse=True)
#     res = 0
#     print(c)
#     for i in range(len(c) - 1):
#         if c[i] == c[i + 1]:
#             for j in range(i + 1, len(c)):
#                 if c[j] == c[i] > 0:
#                     print(f"c[j]={c[j]}, c[i]={c[i]} j={j}, i={i}")
#                     res += 1
#                     c[j] -= 1
#                     print(f"然后c[j]={c[j]} {c}")
#     return res
#
# print(minDeletions(s))
# print(minDeletions2(s))
##=====================================================================================================================================
# 你有一些球的库存 inventory ，里面包含着不同颜色的球。一个顾客想要 任意颜色 总数为 orders 的球。
# 这位顾客有一种特殊的方式衡量球的价值：每个球的价值是目前剩下的 同色球 的数目。
# 比方说还剩下 6 个黄球，那么顾客买第一个黄球的时候该黄球的价值为 6 。这笔交易以后，只剩下 5 个黄球了，所以下一个黄球的价值为 5 （也就是球的价值随着顾客购买同色球是递减的）。
# 给你整数数组 inventory ，其中 inventory[i] 表示第 i 种颜色球一开始的数目。同时给你整数 orders ，表示顾客总共想买的球数目。你可以按照 任意顺序 卖球。
# 请你返回卖了 orders 个球以后 最大 总价值之和。由于答案可能会很大，请你返回答案对 10 ** 9 + 7 取余数 的结果。
# 输入：inventory = [2,5], orders = 4
# 输出：14
# 解释：卖 1 个第一种颜色的球（价值为 2 )，卖 3 个第二种颜色的球（价值为 5 + 4 + 3）。
# 最大总和为 2 + 5 + 4 + 3 = 14 。
# 提示
# 1 <= inventory.length <= 10 ** 5
# 1 <= inventory[i] <= 10 ** 9
# 1 <= orders <= min(sum(inventory[i]), 10 ** 9)
# 我们可以二分查找 最后一次卖出时，球的价格 x。
# 最后的答案由两部分组成：
# 对于所有数量 > x 的颜色，其肯定会减小到 x，因此用等差数列求和公式求和即可。
# 如果执行完第 1 步，仍有剩余的 orders，则这些 orders 一定会以价格 x 卖出。
#
# inventory = [497978859,167261111,483575207,591815159]
# orders = 836556809
# class Solution:
#     def maxProfit(self,inventory, orders):
#         mod = 10 ** 9 + 7
#         # 二分查找 T 值
#         l, r, T = 0, max(inventory), -1
#         while l <= r:
#             mid = (l + r) // 2
#             total = sum(ai - mid for ai in inventory if ai >= mid)
#             if total <= orders:
#                 T = mid
#                 r = mid - 1
#             else:
#                 l = mid + 1
#         range_sum = lambda x, y: (x + y) * (y - x + 1) // 2
#         rest = orders - sum(ai - T for ai in inventory if ai >= T)
#         ans = 0
#         for ai in inventory:
#             if ai >= T:
#                 if rest > 0:
#                     ans += range_sum(T, ai)
#                     rest -= 1
#                 else:
#                     ans += range_sum(T + 1, ai)
#
#         return ans % mod
#
#
# aa = Solution()
# bb = aa.maxProfit(inventory, orders)
# print(bb)
# from typing import List
#
#
# class Solution:
#     def maxProfit(self, inventory: List[int], orders: int) -> int:
#         max_num = 10 ** 9 + 7
#         res = 0
#         low, high = 0, 10 ** 9
#         threshold = None
#         while low <= high:
#             mid = low + ((high - low) >> 1)
#             temp = 0
#             for i in range(len(inventory)):
#                 if inventory[i] >= mid:
#                     temp += (inventory[i] - mid)
#             if temp <= orders:
#                 threshold = mid
#                 high = mid - 1
#             else:
#                 low = mid + 1
#         temp = 0
#         for i in range(len(inventory)):
#             if inventory[i] > threshold:
#                 temp += (inventory[i] - threshold)
#         temp = orders - temp
#         for i in range(len(inventory)):
#             if inventory[i] >= threshold:
#                 if temp > 0:
#                     # 等差数列求和公式
#                     res += ((inventory[i] + threshold) * (inventory[i] - (threshold) + 1) // 2)
#                     temp -= 1
#                 else:
#                     # 等差数列求和公式
#                     res += ((inventory[i] + threshold + 1) * (inventory[i] - (threshold + 1) + 1) // 2)
#         return res % max_num
##=====================================================================================================================================
# from sortedcontainers import SortedList
#
#
# class Solution(object):
#     def createSortedArray(self, instructions):
#         """
#         :type instructions: List[int]
#         :rtype: int
#         解释：一开始 nums = [] 。
#         插入 1 ，代价为 min(0, 0) = 0 ，现在 nums = [1] 。
#         插入 3 ，代价为 min(1, 0) = 0 ，现在 nums = [1,3] 。
#         插入 3 ，代价为 min(1, 0) = 0 ，现在 nums = [1,3,3] 。
#         插入 3 ，代价为 min(1, 0) = 0 ，现在 nums = [1,3,3,3] 。
#         插入 2 ，代价为 min(1, 3) = 1 ，现在 nums = [1,2,3,3,3] 。
#         插入 4 ，代价为 min(5, 0) = 0 ，现在 nums = [1,2,3,3,3,4] 。
#         插入 2 ，代价为 min(1, 4) = 1 ，现在 nums = [1,2,2,3,3,3,4] 。
#         插入 1 ，代价为 min(0, 6) = 0 ，现在 nums = [1,1,2,2,3,3,3,4] 。
#         插入 2 ，代价为 min(2, 4) = 2 ，现在 nums = [1,1,2,2,2,3,3,3,4] 。
#         总代价为 0 + 0 + 0 + 0 + 1 + 0 + 1 + 0 + 2 = 4 。
#         """
#         mod = 10 ** 9 + 7
#         total_coast = 0
#         nums = []
#         res = 0
#         sl = SortedList()
#
#         for num in instructions:
#             cost1 = sl.bisect_left(num)
#             cost2 = len(sl) - sl.bisect_right(num)
#             cost = cost1 if cost1 < cost2 else cost2
#             res = (res + cost) % mod
#             sl.add(num)
        # for i_value in instructions:
        #     l,r = 0,len(nums)-1
        #     mid = (l + r) // 2
        #     if r==-1:
        #         total_coast +=0
        #         nums.append(i_value)
        #         continue
        #     if l==r==0:
        #         if nums[0]>=i_value:
        #             nums.insert(0,i_value)
        #             total_coast += 0
        #             continue
        #         else:
        #             nums.insert(1, i_value)
        #             total_coast += 0
        #             continue
        #     while l <= r:
        #         mid = (l+r)//2
        #         if i_value < nums[mid]:
        #             r = mid - 1
        #         elif i_value > nums[mid]:
        #             l = mid + 1
        #         elif i_value == nums[mid]:
        #             l_list = nums[:mid]
        #             r_list = nums[mid:]
        #             r_list.reverse()
        #             l_total = r_total = 0
        #             try:
        #                 l_total = l_list.index(nums[mid])
        #             except:
        #                 l_total = len(l_list)
        #             try:
        #                 r_total = r_list.index(nums[mid])
        #             except:
        #                 pass
        #             if l_total >= r_total:
        #                 total_coast += r_total
        #             else:
        #                 total_coast += l_total
        #             nums.insert(mid, i_value)
        #             break
        #     else:
        #         nums.append(i_value)
        #         # nums = sorted(nums,reverse=False)
        #         l_none_total = nums.index(i_value)
        #         tpmp_list2 = nums[l_none_total:]
        #         # tpmp_list2.reverse()
        #         r_none_total = tpmp_list2.index(i_value)
        #         if l_none_total>=r_none_total:
        #             total_coast += r_none_total
        #         else:
        #             total_coast += l_none_total
        #         total_coast += 0
        # return res

# instructions2 = [2,1, 3, 3, 3, 2, 4, 2, 1, 2]
# aa = Solution()
# bb = aa.createSortedArray(instructions)
# print(bb)
# print(0//2)#0
# print(1//2)#0
# print(2//2)#1
##=====================================================================================================================================
# 一些恶魔抓住了公主（P）并将她关在了地下城的右下角。地下城是由 M x N 个房间组成的二维网格。我们英勇的骑士（K）最初被安置在左上角的房间里，他必须穿过地下城并通过对抗恶魔来拯救公主。
# 骑士的初始健康点数为一个正整数。如果他的健康点数在某一时刻降至 0 或以下，他会立即死亡。
# 有些房间由恶魔守卫，因此骑士在进入这些房间时会失去健康点数（若房间里的值为负整数，则表示骑士将损失健康点数）；其他房间要么是空的（房间里的值为 0），
# 要么包含增加骑士健康点数的魔法球（若房间里的值为正整数，则表示骑士将增加健康点数）。
# 为了尽快到达公主，骑士决定每次只向右或向下移动一步。
# 骑士的健康点数没有上限。
# 任何房间都可能对骑士的健康点数造成威胁，也可能增加骑士的健康点数，包括骑士进入的左上角房间以及公主被监禁的右下角房间。
# 编写一个函数来计算确保骑士能够拯救到公主所需的最低初始健康点数。
# 例如，考虑到如下布局的地下城，如果骑士遵循最佳路径 右 -> 右 -> 下 -> 下，则骑士的初始健康点数至少为 7。

# -2 (K)	 -3	     3
# -5	     -10	 1
# 10	     30	    -5 (P)

# class Solution:
#     def calculateMinimumHP(self, dungeon):
#         n, m = len(dungeon), len(dungeon[0])
#         BIG = 10**9
#         dp = [[BIG] * (m + 1) for _ in range(n + 1)]
#         dp[n][m - 1] = dp[n - 1][m] = 1
#         for i in range(n - 1, -1, -1):
#             for j in range(m - 1, -1, -1):
#                 minn = min(dp[i + 1][j], dp[i][j + 1])
#                 dp[i][j] = max(minn - dungeon[i][j], 1)
#
#         return dp[0][0]
# 真的是牛
##=====================================================================================================================================
# sn,  freq,   ANT,   Target Power,  Measured Power,  Measured EVM
##=====================================================================================================================================
import os
import re

# path_list = os.listdir()
# for i_name in range(0,len(path_list),1):
#     try:
#         path_list[i_name].index('.txt')
#         file_name = path_list[i_name]
#         f1 = open(file_name, 'r+', encoding='utf-8')  # 打开本地的test.txt文本文件
#         content = f1.read()
#         f1.close()  # 关闭操作
#         for cc in range(1, 9, 1):
#             aa = re.findall(f"ANT{cc}\\u0020+---[\s\S]*?PASS[\s\S]*?Secs.", content)
#             for key in range(0, len(aa), 1):
#                 content = content.replace(aa[key], f"ANT{cc}     ---------------------- J{cc}")
#         with open(file_name, "w", encoding='utf-8') as f2:  # 再次打开test.txt文本文件
#             f2.write(content)  # 将替换后的内容写入到test.txt文本文件中
#             f2.close()
#     except:
#         pass
##=====================================================================================================================================








































