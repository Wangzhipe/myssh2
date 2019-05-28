#!/usr/bin/python
# -*- coding: utf-8 -*-
#导入模块
import MySQLdb as mdb
import os
import datetime

#读取文件，写入list，从第三行开始
tlist =[]
file = '/home/soul/sql-tmp/test.txt'
with open(file,'r+') as tfile:
        tfile.readline()
        for line in tfile.readlines()[3:]:
                lines = line.split()
#               print lines
#转换为字典、元组 和之后sql提取的结果统一
				tlist.append(tuple(lines))

#连接数据库
con = mdb.connect(host='数据库地址',port=端口,user='用户',password='密码',db='数据库名字')
#创建操作游标
cur = con.cursor()
#得到告警sql
alarm_sql = 'select * from alarm_table'
cur.execute(sql)
#得到字典alarm_data
alarm_data = cur.fetchall()

#来的有数据，告警没有  需要insert
inst = [ t_alarm for t_alarm in tlist if t_alarm not in alarm_data ]
for i in inst:
	cur.execute(insert into alarm_table value(%s,%s,%s,%s,%s,%s),i)
	con.commit()
	print (i+' dn alarm')
#告警有，来的数据没有  需要cancel
canc = [ alarm for alarm in alarm_data if alarm not in t_alarm ]
for c in canc:
	print (c+' dn cancel')
	cur.execute('delete from alarm_table where dn = c[0],and alarm_time = c[1] alarm_number = c[2])
	con.commit()
#来的有，告警也有，对比时间
comp = [t_alarm for t_alarm in tlist if t_alarm in alarm_data]
for p in comp:
	now = datetime.datetime.now()
	t2 = datetime.datetime.striptime(p[1],'%Y-%m-%d_%H:%M:%S')
	if (now - t2).total_seconds()/3600 >48:
		print (p+' dn alarm')
		cur.execute('delete from alarm_table where dn = p[0],and alarm_time = p[1] alarm_number = p[2])
		con.commit()
#提交操作
#关闭数据库
con.close()
