#!/usr/bin/python
#-*-coding:utf-8 -*-

import MySQLdb
import snowflake.client
import datetime
import json

# snowflake_start_server
snowflake.client.setup('localhost', 8910)
#print snowflake.client.get_guid()

now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#print now_time


# 打开数据库连接
db = MySQLdb.connect("10.206.20.189", "root", "123456", "pem", charset='utf8')
# 使用cursor()方法获取操作游标
cursor = db.cursor()

category_name_dict = {'signal': '告警类型', 'equipType': '设备类型', 'businessType': '业务类型', 'propType': '字段类型', 'equipMold': '设备分类', 'stationLevel': '局站类型', 'TSemaphore': '信号类型'}
#category_name_dict_json = json.dumps(category_name_dict, encoding='UTF-8', ensure_ascii=False)
#print category_name_dict_json
category_id_dict = {}

# SQL 查询语句  第一层type 第二层pid 第三层description 名称label 编码value 排序sort 备注remarks
# 只有一层的话 SELECT distinct type where type in ('TSemaphore','propType','stationLevel')
# SELECT distinct type,pid,description,label,value,sort,remarks FROM MGR_DICT where type in ('TSemaphore','propType','stationLevel')
sql_category = " SELECT distinct description FROM MGR_DICT where type = 'signal' and pid = '遥调' "
p_id = 4136046154863345665

prefix = " insert into sys_code_categroy (id, code_name, code_code, p_id, state, modify_user, modify_date, create_user, create_date) values ( "

try:
    # 执行SQL语句
    cursor.execute(sql_category)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        type = row[0]

        seq = snowflake.client.get_guid()
        category_id_dict[type] = seq
        #  cName = category_name_dict[type]
        vs = ",'%s', '%s', '%d', '%d', '%s','%s','%s','%s' );" % ( type, type, p_id, 0, '12', now_time, '12', now_time)

        # 打印结果
        print prefix,seq,vs
    #print category_id_dict
except:
    print "Error: unable to fecth data"


sql_code = " SELECT description, label, value, remarks, sort FROM MGR_DICT where type in ('signal') and pid = '遥调' order by type "
prefix = " insert into sys_code (id, code_category_id, full_name, short_name, code_value, p_id, remark, sort, modify_user, modify_date, create_user, create_date) values ( "

try:
    # 执行SQL语句
    cursor.execute(sql_code)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        type = row[0]
        label = row[1]
        value = row[2]
        remarks = row[3]
        sort = row[4]

        seq = snowflake.client.get_guid()
        ccId = category_id_dict[type]
        vs = ",'%s','%s','%s','%s', '%d', '%s','%s','%s','%s','%s','%s' );" % (ccId, label, label, value, p_id, remarks, sort, '12', now_time, '12', now_time)

        # 打印结果
        print prefix,seq,vs
except:
    print "Error: unable to fecth data"


# 关闭数据库连接
db.close()
