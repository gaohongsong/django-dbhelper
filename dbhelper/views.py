# -*- coding: utf-8 -*-
"""
隐藏后台功能单元，执行文件上传、db导出、db删除
"""
import datetime
import subprocess

from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse
from django.db import connection
from django.conf import settings


@permission_required('is_superuser')
def drop_table(request):
    """
    清空表，危险操作
    """

    try:
        cursor = connection.cursor()

        # 取消外键关联
        cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
        cursor.execute("show tables;")

        result_tuple = cursor.fetchall()
        for result in result_tuple:
            table_name = result[0]
            drop_table_sql = "drop table " + table_name  # +" if exists "+table_name
            cursor.execute(drop_table_sql)

        return HttpResponse(u'命令执行成功')
    except Exception, e:
        return HttpResponse(u'命令执行异常:%s' % e)


@permission_required('is_superuser')
def dump_db(request):
    """
    dbdump操作
    """

    db = settings.DATABASES['default']
    dbfile = 'static/{}.sql'.format(db.get('NAME'))
    dumpcmd = 'mysqldump'
    dumpdb = '{dumpcmd} --user={user} ' \
             '--password={password} ' \
             '--host={host} ' \
             '--port={port} ' \
             '--single-transaction ' \
             '{dbname} > {dbfile}'.format(dumpcmd=dumpcmd,
                                          user=db.get('USER'),
                                          password=db.get('PASSWORD'),
                                          host=db.get('HOST'),
                                          port=db.get('HOST'),
                                          dbname=db.get('NAME'),
                                          dbfile=dbfile)

    p = subprocess.Popen(dumpdb, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    out, err = p.communicate()

    try:
        with open(dbfile, 'rb') as fd:
            file_content = fd.read()
            response = HttpResponse(file_content)
            response['Content-Type'] = 'application/octet-stream'
            response['Content-Disposition'] = 'attachment;filename="%s_%s.sql"' % (db.get('NAME'),
                                                                                   datetime.datetime.now())
    except IOError:
        return HttpResponse(u'<h3>磁盘中不存在该文件!</h3>')
    except Exception, e:
        return HttpResponse(u'<h3>系统异常!</h3><br><p>%s</p>' % e)
    return response


def init_data(request):
    return HttpResponse("todo")
