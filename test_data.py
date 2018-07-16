# -*- coding: utf8 -*-
'HeHe,it looks like the mood is not happy now...'
__author__ = 'HardyHu'

import sys
sys.path.append('../db_fixture')
from mysql_db import DB


#创建测试数据
datas = {
	#发布会表数据
	'sign_event':[
	{'id':1,'name':'红米Pro发布会','`limit`':2000,'status':1,'address':'北京会展中心','start_time':'2018-08-20 14:00:00'},
	{'id':2,'name':'可参加人数为0','`limit`':0,'status':1,'address':'北京会展中心','start_time':'2018-10-20 14:00:00'},
	{'id':3,'name':'当前状态为0关闭','`limit`':2000,'status':0,'address':'北京会展中心','start_time':'2017-12-20 14:00:00'},
	{'id':4,'name':'发布会已结束','`limit`':2000,'status':1,'address':'北京会展中心','start_time':'2001-08-20 14:00:00'},
	{'id':5,'name':'小米5发布会','`limit`':2000,'status':1,'address':'北京国家会议中心','start_time':'2018-05-20 13:14:20'},
	],

	#嘉宾数据
	'sign_guest':[
	{'id':1,'realname':'alen','phone':'13511001100','email':'alen@gmai.com','sign':0,'event_id':1},
	{'id':2,'realname':'who','phone':'13511001101','email':'who@gmai.com','sign':1,'event_id':1},
	{'id':3,'realname':'tom','phone':'13511001102','email':'tom@gmai.com','sign':0,'event_id':5},
	],
}

#将测试数据插入表
def init_data():
	db = DB()
	for table,data in datas.items():
		db.clear(table)
		for d in data:
			db.insert(table,d)
	db.close()
    # DB().init_data(datas)



if __name__ == '__main__':
	init_data()
