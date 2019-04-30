#!/usr/local/easyops/python/bin/python
# -*- coding: utf-8 -*-

import os
import re
import sys
import time
import json
import logging
import traceback
import requests

logger = logging.getLogger('mylog')
logger.setLevel(logging.WARNING)
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(logging.Formatter('[%(asctime)s %(filename)s L%(lineno)d %(levelname)s] %(message)s'))
logger.addHandler(handler)
reload(sys)
sys.setdefaultencoding('utf-8')


#CMDB服务器地址
EASYOPS_CMDB_HOST = '192.168.100.162'
#CMDB org编号，可以在服务器的 /root/.easyops 查看
EASYOPS_ORG = '8888'
#CMDB请求的用户名称，easyops为管理员用户
EASYOPS_USER = 'easyops'



# send http query
def do_http(method, url, data={}, files={}, headers={}):
    try:
        method = method.lower()
        if method in ["get", "delete"]:
            resp = requests.request(method, url, params=data, headers=headers, timeout=(1, 60))
        else:
            if files:
                resp = requests.request(methoe, url, data=data, files=files, headers=headers, timeout=(2, 60))
            else:
                headers["content-type"] = 'application/json'
                resp = requests.request(method, url, data=json.dumps(data), headers=headers, timeout=(2, 60))
        return True, resp
    except Exception, e:
        print traceback.format_exc()
        return False, None


# common EasyOps http request method
def http_request(url, method='GET', headers=None, **kwargs):
    # examine the url
    if not (url.startswith('http://') or url.startswith('https://')):
        logger.error(u'url: {url}'.format(url=url))
        raise Exception(u'the url should be start with \'http(s)://\'')

    logger.debug(u'request the url: {url}'.format(url=url))

    # examine the http method
    method = str.upper(method)
    http_methods = ['GET', 'OPTIONS', 'HEAD', 'POST', 'PUT', 'PATCH', 'DELETE']
    if method not in http_methods:
        raise Exception(u'unsupported http method: {method}'.format(method=method))

    # examine the headers
    if not headers:
        headers = dict()
    if 'org' not in headers:
        headers['org'] = EASYOPS_ORG
    if 'user' not in headers:
        headers['user'] = EASYOPS_USER

    # execute the request
    '''
    print url
    print method
    print headers
    print params
    '''
    http_ret = requests.request(url=url, method=method, headers=headers, **kwargs)
    if http_ret.status_code == 200:
        try:
            ret_obj = http_ret.json()
            if ret_obj['code'] == 0:
                return ret_obj['data']
            else:
                logger.error(http_ret.text)
                raise Exception(u'Return Code: {code}'.format(code=ret_obj['code']))
        except ValueError:
            return http_ret.content
    else:
        logger.error(http_ret.text)
        raise Exception(u"the http response status code: "
                        u"{status_code}".format(status_code=http_ret.status_code))


# the http request for EasyOps CMDB
def send_cmdb_query(uri, method='GET', headers=None, params=None, paging=False, **kwargs):
    # construct the url
    url = u"http://{ip}{uri}".format(ip=EASYOPS_CMDB_HOST, uri=uri)

    # construct the headers
    if not headers:
        headers = dict()
    headers['Host'] = 'cmdb.easyops-only.com'

    # construct the params
    if params is None:
        params = {'page': 1, 'pageSize': 3000}
    else:
        if not isinstance(params, dict):
            message = u'the type of params should be dictionary, ' \
                      u'but receive: {params}'.format(params=params)
            raise Exception(message)

        if 'page' not in params:
            params['page'] = 1

        if 'pageSize' not in params:
            params['pageSize'] = 3000

    # execute the request
    ret_data = {}
    if paging:
        # with paging, all the result can be receive
        ret_list = []
        while True:
            ret_data = http_request(url=url, method=method, headers=headers, params=params, **kwargs)
            ret_total = ret_data['total']
            ret_list += ret_data['list']

            # when the size of current page is less than pageSize, that will be the last page, break
            if len(ret_data['list']) < params['pageSize']:
                logger.debug(u"all the data has been received, the request is finished")
                break

            # when the size of current data is larger than (or equal) res_total, break
            if len(ret_list) < ret_total:
                params['page'] += 1
            else:
                logger.debug(u"all the data has been received, the request is finished")
                break

        # when the all the requests are finished, bring the result to ret_data
        ret_data['list'] = ret_list
    else:
        ret_data = http_request(url=url, method=method, headers=headers, params=params, **kwargs)

    return ret_data


# cmdb search api
# ###搜索实例接口(新)
# POST /object/@object_id/instance/_search
# 参数说明：
# object_id -> CMDB资源模型ID              string    必填
# query     -> 查询条件(写法为mongo查询写法) array
# page -> 获取的页码数，默认1               int
# page_size -> 获取每页的数量，默认30        int
# fields -> 过滤字段, 留空代表返回所有字段    array
# sort -> 按字段排序, 留空代表不排序
def cmdb_search(objectId, params, paging=False):
    uri = u'/object/{objectId}/instance/_search'.format(objectId=objectId)
    return send_cmdb_query(uri, paging=paging, method='POST', json=params)


# cmdb add api
# ###创建实例接口
# POST /object/@object_id/instance
# 参数说明：
# object_id -> CMDB资源模型ID    string    必填
# name -> 新增的实例名称          string    必填
def cmdb_add(objectId, params):
    uri = u'/object/{objectId}/instance'.format(objectId=objectId)
    return send_cmdb_query(uri, method='POST', json=params)


# cmdb modity api
# ###修改实例接口
# PUT /object/@object_id/instance/@instanceId
# 参数说明：
# object_id -> CMDB资源模型ID    string    必填
# instanceId -> 实例ID          string    必填
# name -> 新增的实例名称          string    必填
def cmdb_modity(objectId, instanceId, params):
    uri = u'/object/{objectId}/instance/{instanceId}'.format(objectId=objectId, instanceId=instanceId)
    return send_cmdb_query(uri=uri, method='PUT', json=params)


# cmdb delete api
# ###删除实例接口
# DELETE /object/@object_id/instance/@instanceId
# 参数说明：
# object_id -> CMDB资源模型ID    string    必填
# instanceId -> 实例ID          string    必填
def cmdb_del(objectId, instanceId):
    uri = u'/object/{objectId}/instance/{instanceId}'.format(objectId=objectId, instanceId=instanceId)
    return send_cmdb_query(uri=uri, method='DELETE')



if __name__=='__main__':
    #cmdb查询接口使用, 查询应用(APP)列表:
    params = {
        'fields': {'name': True, '_id': False, 'instanceId': False},      # 返回结果仅仅显示name字段(返回结果中，会默认返回instanceId和_id字段，如果不需要，请将它设置为False)
        # 'query': {'name': {'$eq': u"gsnews应用"}},             # 查询名称为 gsnews应用 的APP
        'page': 1,
        'page_size': 1000,
        'sort': {'name': True},  # 按照名称排序
    }
    print cmdb_search(objectId='APP', params=params, paging=True)


    #cmdb创建接口使用, 创建一个应用(APP):
    params = {
        'name': u'测试新增应用test'    #新建该名称的应用
    }
    instanceId = cmdb_add(objectId='APP', params=params)['instanceId']  #587a8a8a0bc7d  #新增应用，获取该应用的实例ID，用于后面的接口测试。
    #print instanceId

    #cmdb修改接口使用,修改一个应用(APP):
    params = {
        'name': u"应用名称修改测试"   #将名称修改为“应用名称修改测试”
    }
    print cmdb_modity(objectId="APP", instanceId = instanceId, params=params)

    #cmdb删除接口使用,删除一个应用(APP):
    print cmdb_del(objectId="APP", instanceId=instanceId)


