#!/usr/bin/python
#-*-coding:utf-8 -*-

import MySQLdb
import snowflake.client
import datetime
import json

# snowflake_start_server
#snowflake.client.setup('localhost', 8910)
#print snowflake.client.get_guid()

now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#print now_time


# 打开数据库连接
db = MySQLdb.connect("10.206.20.189", "root", "123456", "pem", charset='utf8')
# 使用cursor()方法获取操作游标
cursor = db.cursor()

sql_area = " select id,parent_id,parentIds,code,name from MGR_AREA where remarks = '行政区划代码' and parent_id is not null "
prefix = " insert into con_node_manage (id, parent_node_id, parent_node_code, parent_name_ide, child_node_code, child_node_name, create_user_id, create_time, update_user_id, update_time, is_del) values ( "

try:
    # 执行SQL语句
    cursor.execute(sql_area)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        id = row[0]
        parentId = row[1]
        parentIds = row[2]
        code = row[3]
        name = row[4]

        vs = "'%s','%s','%s','%d','%s','%s','%s','%s','%s','%s','%d' );" % ( id, parentId, parentIds, 0, code, name, '12', now_time, '12', now_time, 0)

        # 打印结果
        print prefix,vs
        #print category_id_dict
except:
    print "Error: unable to fecth data"

# 关闭数据库连接
db.close()