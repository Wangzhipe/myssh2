#!/usr/bin/python
# -*- coding: utf-8 -*-
#����ģ��
import MySQLdb as mdb
import os
import datetime

#��ȡ�ļ���д��list���ӵ����п�ʼ
tlist =[]
file = '/home/soul/sql-tmp/test.txt'
with open(file,'r+') as tfile:
        tfile.readline()
        for line in tfile.readlines()[3:]:
                lines = line.split()
#               print lines
#ת��Ϊ�ֵ䡢Ԫ�� ��֮��sql��ȡ�Ľ��ͳһ
				tlist.append(tuple(lines))

#�������ݿ�
con = mdb.connect(host='���ݿ��ַ',port=�˿�,user='�û�',password='����',db='���ݿ�����')
#���������α�
cur = con.cursor()
#�õ��澯sql
alarm_sql = 'select * from alarm_table'
cur.execute(sql)
#�õ��ֵ�alarm_data
alarm_data = cur.fetchall()

#���������ݣ��澯û��  ��Ҫinsert
inst = [ t_alarm for t_alarm in tlist if t_alarm not in alarm_data ]
for i in inst:
	cur.execute(insert into alarm_table value(%s,%s,%s,%s,%s,%s),i)
	con.commit()
	print (i+' dn alarm')
#�澯�У���������û��  ��Ҫcancel
canc = [ alarm for alarm in alarm_data if alarm not in t_alarm ]
for c in canc:
	print (c+' dn cancel')
	cur.execute('delete from alarm_table where dn = c[0],and alarm_time = c[1] alarm_number = c[2])
	con.commit()
#�����У��澯Ҳ�У��Ա�ʱ��
comp = [t_alarm for t_alarm in tlist if t_alarm in alarm_data]
for p in comp:
	now = datetime.datetime.now()
	t2 = datetime.datetime.striptime(p[1],'%Y-%m-%d_%H:%M:%S')
	if (now - t2).total_seconds()/3600 >48:
		print (p+' dn alarm')
		cur.execute('delete from alarm_table where dn = p[0],and alarm_time = p[1] alarm_number = p[2])
		con.commit()
#�ύ����
#�ر����ݿ�
con.close()
