## 目录

1. [APP - 查询应用的集群和设备的数量](#-cluster_and_device_num_in_app-POST)
2. [OBJECT_PATH - 获取查询策略](#-get_relation_query_strategy-GET)
3. [OBJECT_PATH - 更新查询策略](#-update_relation_query_strategy-PUT)
4. [OBJECT_PATH - 删除关系查询策略](#-delete_relation_query_strategy-DELETE)
5. [OBJECT_PATH - 更新查询策略v2](#-update_relation_query_strategy_v2-PUT)
6. [OBJECT_PATH - 获取资源模型路径列表](#-get_object_relation_path-GET)
7. [OBJECT_PATH - 创建关系查询策略v2](#-create_relation_query_strategy_v2-POST)
8. [OBJECT_PATH - 创建关系查询策略](#-create_relation_query_strategy-POST)
9. [OBJECT_PATH - 删除关系查询策略v2](#-delete_relation_query_strategy_v2-DELETE)
10. [OBJECT_PATH - 获取查询策略列表v2](#-list_relation_query_strategy_v2-get)
11. [OBJECT_PATH - 获取查询策略v2](#-get_relation_query_strategy_v2-GET)
12. [BUSINESS_INSTANCE - 查询应用系统子系统拓扑](#-get_business_graph-GET)
13. [BUSINESS_INSTANCE - 搜索系统的子系统以及，以及递归的获取子系统的子系统](#-searchSubSystem-POST)
14. [BUSINESS_INSTANCE - 查询应用系统的所有子系统以及所有子系统的子系统所包含的应用](#-searchAppInSystem-POST)
15. [BUSINESS_INSTANCE - 批量获取业务业务树全路径](#-get_business_tree_list-GET)
16. [INSTANCE_PATH_SEARCH - 关系查询v1](#-pathSearchV1-POST)
17. [INSTANCE_PATH_SEARCH - 关系查询v3](#-pathSearchV3-POST)
18. [INSTANCE_PATH_SEARCH - 关系查询v2](#-pathSearchV2-POST)
19. [INSTANCE_PATH_SEARCH - 关系查询v4](#-pathSearchV4-POST)
20. [INSTANCE_EXTEND - 批量修改实例权限](#-update_permission_batch-PUT)
21. [INSTANCE_EXTEND - 全文搜索](#-fulltext_search-GET)
22. [INSTANCE_EXTEND - 自动发现的接口](#-auto_discovery-POST)
23. [INSTANCE_EXTEND - 批量编辑实例(导入实例)](#-import_instance-POST)
24. [OBJECT - 模型导出](#-export-GET)
25. [OBJECT - 更新模型关系分组](#-update_relation_group-PUT)
26. [OBJECT - 删除模型属性](#-delete_property-DELETE)
27. [OBJECT - 删除模型](#-delete-DELETE)
28. [OBJECT - 获取单个模型](#-get-GET)
29. [OBJECT - import objects check](#-import_check-POST)
30. [OBJECT - 获取单个模型关系](#-get_relation-GET)
31. [OBJECT - 创建模型属性](#-create_property-POST)
32. [OBJECT - 创建模型关系分组](#-create_relation_group-POST)
33. [OBJECT - 更新模型关系](#-update_relation-PUT)
34. [OBJECT - 删除模型关系分组](#-delete_relation_group-DELETE)
35. [OBJECT - 批量导入模型](#-import-POST)
36. [OBJECT - 获取模型属性](#-get_property-GET)
37. [OBJECT - 创建模型关系](#-create_relation-POST)
38. [OBJECT - 分页获取模型列表](#-list-list)
39. [OBJECT - 创建模型](#-create-POST)
40. [OBJECT - 更新模型属性](#-update_property-PUT)
41. [OBJECT - 更新模型](#-update-PUT)
42. [OBJECT - 删除模型关系](#-delete_relation-DELETE)
43. [INSTANCE_RELATION - 批量设置关系](#-set-POST)
44. [INSTANCE_RELATION - 实例关系发现](#-discovery-POST)
45. [INSTANCE_RELATION - 批量移除关系](#-remove-POST)
46. [INSTANCE_RELATION - 批量添加关系](#-append-POST)
47. [INSTANCE_RELATION - 统计关系实例数量](#-count_relation_instance-GET)
48. [INSTANCE_QUERY_STRATEGY - 删除关系查询策略](#-delete-DELETE)
49. [INSTANCE_QUERY_STRATEGY - 获取查询策略](#-get-GET)
50. [INSTANCE_QUERY_STRATEGY - 按模型获取查询策略列表](#-list-GET)
51. [INSTANCE_QUERY_STRATEGY - 创建查询策略](#-create-POST)
52. [INSTANCE_QUERY_STRATEGY - 修改查询策略](#-update-PUT)
53. [INSTANCE - 搜索实例列表指定关系是否大于等于max约束](#-relation_max_check-POST)
54. [INSTANCE - 实例搜索接口](#-search-POST)
55. [INSTANCE - 单个实例关系统计](#-instance_relation_count-GET)
56. [INSTANCE - 更新实例v2](#-update_v2-PUT)
57. [INSTANCE - 删除实例](#-delete-DELETE)
58. [INSTANCE - 获取单个实例](#-get-GET)
59. [INSTANCE - 实例搜索统计实例数量](#-search_total-POST)
60. [INSTANCE - 实例分页列表查询](#-list-GET)
61. [INSTANCE - 实例计数统计接口](#-aggregate_count_attr-GET)
62. [INSTANCE - 获取实例默认值模板](#-get_default_value_template-GET)
63. [INSTANCE - 创建实例v2](#-create_v2-POST)
64. [EXPORT - 导出资源模型路径查询的实例v2](#-export_relation_instances_v2-POST)
65. [EXPORT - 导出资源模型路径查询的实例v4](#-export_relation_instances_v4-POST)
66. [EXPORT - 实例导出](#-export_instance-POST)

## <a id='-cluster_and_device_num_in_app-POST'></a> cluster_and_device_num_in_app POST
>查询应用的集群和设备的数量<br>

### - 测试关键字
```
cluster and device num request 
```
### - 接口访问URL
```
POST /cluster_and_device_num_in_app
```
### - 参数


#### body 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| appIds | string[] | 是 | 应用实例ID列表 |  | {'gte': 1}



### - 返回码
|返回码|备注|
|---|---|
| 0 | success

### - 请求示例
```json
{
    "appIds": [
        "fake_appIds"
    ]
}
```

### - 返回示例
```json
{
    "56e0dbec4da6f": {
        "device": 0,
        "cluster": 0
    },
    "56dff11497f66": {
        "device": 38,
        "cluster": 0
    }
}
```
## <a id='-get_relation_query_strategy-GET'></a> get_relation_query_strategy GET
>获取查询策略<br>

### - 测试关键字
```
get relation query strategy request 
```
### - 接口访问URL
```
GET /object/:object_id/relation_query_strategy/:id
```
### - 参数
#### URI 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| object_id | string | 是 |  |  | []
| id | string | 是 |  |  | []



### - 返回值说明
|名称|类型|备注|
|---|---|---|
| id | string | 策略ID(可以自定义, 不给定后台会默认生成)
| byPath | string | v4(全量查询字段）
| name | string | 策略名称
| type | string | 策略类型(org 或者 user)
| query | map[] | 策略内容(包含查询条件和返回的字段, 不指定返回的字段则默认返回name字段, alias ${objectId}.name)
| fields_sort | string[] | 查询出来的字段的排序
| object_id | string | 策略所属模型id
| ctime | string | 创建时间
| creator | string | 创建用户
| available | bool | 路径是否可用


### - 返回码
|返回码|备注|
|---|---|
| 0 | success


### - 返回示例
```json
{
    "code": 0,
    "data": {
        "byPath": "fake_byPath",
        "available": true,
        "name": "fake_name",
        "creator": "fake_creator",
        "fields_sort": [
            "fake_fields_sort"
        ],
        "object_id": "fake_object_id",
        "query": [
            {}
        ],
        "type": "fake_type",
        "id": "fake_id",
        "ctime": "fake_ctime"
    },
    "error": "",
    "codeExplain": ""
}
```
## <a id='-update_relation_query_strategy-PUT'></a> update_relation_query_strategy PUT
>更新查询策略<br>

### - 测试关键字
```
update relation query strategy request 
```
### - 接口访问URL
```
PUT /object/:object_id/relation_query_strategy/:id
```
### - 参数
#### URI 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| object_id | string | 是 |  |  | []
| id | string | 是 |  |  | []


#### body 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| id | string | 否 | 策略ID(可以自定义, 不给定后台会默认生成) |  | 
| byPath | string | 否 | v4(全量查询字段） |  | 
| name | string | 否 | 策略名称 |  | 
| type | string | 否 | 策略类型(org 或者 user) |  | 
| query | map[] | 否 | 策略内容(包含查询条件和返回的字段, 不指定返回的字段则默认返回name字段, alias ${objectId}.name) |  | 
| fields_sort | string[] | 否 | 查询出来的字段的排序 |  | 


### - 返回值说明
|名称|类型|备注|
|---|---|---|
| id | string | 策略ID(可以自定义, 不给定后台会默认生成)
| byPath | string | v4(全量查询字段）
| name | string | 策略名称
| type | string | 策略类型(org 或者 user)
| query | map[] | 策略内容(包含查询条件和返回的字段, 不指定返回的字段则默认返回name字段, alias ${objectId}.name)
| fields_sort | string[] | 查询出来的字段的排序
| object_id | string | 策略所属模型id
| ctime | string | 创建时间
| creator | string | 创建用户
| available | bool | 路径是否可用


### - 返回码
|返回码|备注|
|---|---|
| 0 | success

### - 请求示例
```json
{
    "byPath": "fake_byPath",
    "name": "fake_name",
    "fields_sort": [
        "fake_fields_sort"
    ],
    "query": [
        {}
    ],
    "type": "fake_type",
    "id": "fake_id"
}
```

### - 返回示例
```json
{
    "code": 0,
    "data": {
        "byPath": "fake_byPath",
        "available": true,
        "name": "fake_name",
        "creator": "fake_creator",
        "fields_sort": [
            "fake_fields_sort"
        ],
        "object_id": "fake_object_id",
        "query": [
            {}
        ],
        "type": "fake_type",
        "id": "fake_id",
        "ctime": "fake_ctime"
    },
    "error": "",
    "codeExplain": ""
}
```
## <a id='-delete_relation_query_strategy-DELETE'></a> delete_relation_query_strategy DELETE
>删除关系查询策略<br>

### - 测试关键字
```
delete relation query strategy request 
```
### - 接口访问URL
```
DELETE /object/:object_id/relation_query_strategy/:id
```
### - 参数
#### URI 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| object_id | string | 是 |  |  | []
| id | string | 是 |  |  | []




### - 返回码
|返回码|备注|
|---|---|
| 0 | success


## <a id='-update_relation_query_strategy_v2-PUT'></a> update_relation_query_strategy_v2 PUT
>更新查询策略v2<br>

### - 测试关键字
```
update relation query strategy v2 request 
```
### - 接口访问URL
```
PUT /v2/object/:object_id/relation_query_strategy/:id
```
### - 参数
#### URI 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| object_id | string | 是 |  |  | []
| id | string | 是 |  |  | []


#### body 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| id | string | 否 | 策略ID(可以自定义, 不给定后台会默认生成) |  | 
| byPath | string | 否 | 查询策略版本: v3: 精确查询, v4: 全量查询 |  | 
| name | string | 否 | 策略名称 |  | 
| type | string | 否 | 策略类型(org 或者 user) |  | 
| path_list | map[] | 否 | 策略内容(包含查询条件和返回的字段, 不指定返回的字段则默认返回name字段, alias ${objectId}.name) |  | 


### - 返回值说明
|名称|类型|备注|
|---|---|---|
| id | string | 策略ID(可以自定义, 不给定后台会默认生成)
| byPath | string | v4(全量查询字段）
| name | string | 策略名称
| type | string | 策略类型(org 或者 user)
| path_list | map[] | 策略内容(包含查询条件和返回的字段, 不指定返回的字段则默认返回name字段, alias ${objectId}.name)
| object_id | string | 策略所属模型id
| ctime | string | 创建时间
| creator | string | 创建用户


### - 返回码
|返回码|备注|
|---|---|
| 0 | success

### - 请求示例
```json
{
    "type": "fake_type",
    "path_list": [
        {}
    ],
    "byPath": "fake_byPath",
    "id": "fake_id",
    "name": "fake_name"
}
```

### - 返回示例
```json
{
    "code": 0,
    "data": {
        "name": "fake_name",
        "creator": "fake_creator",
        "byPath": "fake_byPath",
        "object_id": "fake_object_id",
        "path_list": [
            {}
        ],
        "type": "fake_type",
        "id": "fake_id",
        "ctime": "fake_ctime"
    },
    "error": "",
    "codeExplain": ""
}
```
## <a id='-get_object_relation_path-GET'></a> get_object_relation_path GET
>获取资源模型路径列表<br>

### - 测试关键字
```
get object relation path request 
```
### - 接口访问URL
```
GET /object_relation_path
```
### - 参数

#### query 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| src_object_id | string | 是 | 路径起始资源模型ID |  | []
| dst_object_id | string | 是 | 路径结束资源模型ID |  | []
| max_depth | int | 否 | 搜索最大深度，默认为5 | 5 | []
| with_cycle | bool | 否 | 是否带环搜索，默认false true | False | []
| black_list | string | 否 | 屏蔽节点列表，;分割，默认USER | USER | []
| max_sub_node | int | 否 | 搜索最大模型数，默认为100 | 100 | []



### - 返回码
|返回码|备注|
|---|---|
| 0 | success


### - 返回示例
```json
{
    "code": 0,
    "data": [
        {
            "path": [
                {}
            ],
            "id": "fake_id"
        }
    ],
    "error": "",
    "codeExplain": ""
}
```
## <a id='-create_relation_query_strategy_v2-POST'></a> create_relation_query_strategy_v2 POST
>创建关系查询策略v2<br>

### - 测试关键字
```
create relation query strategy v2 request 
```
### - 接口访问URL
```
POST /v2/object/:object_id/relation_query_strategy
```
### - 参数
#### URI 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| object_id | string | 是 |  |  | []


#### body 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| id | string | 否 | 策略ID(可以自定义, 不给定后台会默认生成) |  | 
| byPath | string | 否 | 查询策略版本: v3: 精确查询, v4: 全量查询 | v3 | {'pattern': '^(v3|v4)$'}
| name | string | 是 | 策略名称 |  | []
| type | string | 否 | 策略类型(org 或者 user) | org | {'pattern': '^(org|user)$'}
| path_list | map[] | 是 | 策略内容(包含查询条件和返回的字段, 不指定返回的字段则默认返回name字段, alias ${objectId}.name) |  | []


### - 返回值说明
|名称|类型|备注|
|---|---|---|
| id | string | 策略ID(可以自定义, 不给定后台会默认生成)
| byPath | string | v4(全量查询字段）
| name | string | 策略名称
| type | string | 策略类型(org 或者 user)
| path_list | map[] | 策略内容(包含查询条件和返回的字段, 不指定返回的字段则默认返回name字段, alias ${objectId}.name)
| object_id | string | 策略所属模型id
| ctime | string | 创建时间
| creator | string | 创建用户


### - 返回码
|返回码|备注|
|---|---|
| 0 | success

### - 请求示例
```json
{
    "type": "fake_type",
    "path_list": [
        {}
    ],
    "byPath": "fake_byPath",
    "id": "fake_id",
    "name": "fake_name"
}
```

### - 返回示例
```json
{
    "code": 0,
    "data": {
        "name": "fake_name",
        "creator": "fake_creator",
        "byPath": "fake_byPath",
        "object_id": "fake_object_id",
        "path_list": [
            {}
        ],
        "type": "fake_type",
        "id": "fake_id",
        "ctime": "fake_ctime"
    },
    "error": "",
    "codeExplain": ""
}
```
## <a id='-create_relation_query_strategy-POST'></a> create_relation_query_strategy POST
>创建关系查询策略<br>

### - 测试关键字
```
create relation query strategy request 
```
### - 接口访问URL
```
POST /object/:object_id/relation_query_strategy
```
### - 参数
#### URI 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| object_id | string | 是 |  |  | []


#### body 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| id | string | 否 | 策略ID(可以自定义, 不给定后台会默认生成) |  | 
| byPath | string | 否 | v4(全量查询字段） | v3 | {'pattern': '^(v3|v4)$'}
| name | string | 是 | 策略名称 |  | []
| type | string | 否 | 策略类型(org 或者 user) | org | {'pattern': '^(org|user)$'}
| query | map[] | 是 | 策略内容(包含查询条件和返回的字段, 不指定返回的字段则默认返回name字段, alias ${objectId}.name) |  | []
| fields_sort | string[] | 否 | 查询出来的字段的排序 |  | 


### - 返回值说明
|名称|类型|备注|
|---|---|---|
| id | string | 策略ID(可以自定义, 不给定后台会默认生成)
| byPath | string | v4(全量查询字段）
| name | string | 策略名称
| type | string | 策略类型(org 或者 user)
| query | map[] | 策略内容(包含查询条件和返回的字段, 不指定返回的字段则默认返回name字段, alias ${objectId}.name)
| fields_sort | string[] | 查询出来的字段的排序
| object_id | string | 策略所属模型id
| ctime | string | 创建时间
| creator | string | 创建用户
| available | bool | 路径是否可用


### - 返回码
|返回码|备注|
|---|---|
| 0 | success

### - 请求示例
```json
{
    "byPath": "fake_byPath",
    "name": "fake_name",
    "fields_sort": [
        "fake_fields_sort"
    ],
    "query": [
        {}
    ],
    "type": "fake_type",
    "id": "fake_id"
}
```

### - 返回示例
```json
{
    "code": 0,
    "data": {
        "byPath": "fake_byPath",
        "available": true,
        "name": "fake_name",
        "creator": "fake_creator",
        "fields_sort": [
            "fake_fields_sort"
        ],
        "object_id": "fake_object_id",
        "query": [
            {}
        ],
        "type": "fake_type",
        "id": "fake_id",
        "ctime": "fake_ctime"
    },
    "error": "",
    "codeExplain": ""
}
```
## <a id='-delete_relation_query_strategy_v2-DELETE'></a> delete_relation_query_strategy_v2 DELETE
>删除关系查询策略v2<br>

### - 测试关键字
```
delete relation query strategy v2 request 
```
### - 接口访问URL
```
DELETE /v2/object/:object_id/relation_query_strategy/:id
```
### - 参数
#### URI 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| object_id | string | 是 |  |  | []
| id | string | 是 |  |  | []




### - 返回码
|返回码|备注|
|---|---|
| 0 | success


## <a id='-list_relation_query_strategy_v2-get'></a> list_relation_query_strategy_v2 Get
>获取查询策略列表v2<br>

### - 测试关键字
```
list relation query strategy v2 request 
```
### - 接口访问URL
```
get /v2/object/:object_id/relation_query_strategy
```
### - 参数
#### URI 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| object_id | string | 是 | 资源模型ID |  | []

#### query 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| type | string | 否 | 策略类型(org, user, 指定org只会获取系统级别的查询策略, 指定user只会获取自己的用户级查询策略) |  | []



### - 返回码
|返回码|备注|
|---|---|
| 0 | success


### - 返回示例
```json
{
    "code": 0,
    "data": [
        {
            "name": "fake_name",
            "creator": "fake_creator",
            "byPath": "fake_byPath",
            "object_id": "fake_object_id",
            "path_list": [
                {}
            ],
            "type": "fake_type",
            "id": "fake_id",
            "ctime": "fake_ctime"
        }
    ],
    "error": "",
    "codeExplain": ""
}
```
## <a id='-get_relation_query_strategy_v2-GET'></a> get_relation_query_strategy_v2 GET
>获取查询策略v2<br>

### - 测试关键字
```
get relation query strategy v2 request 
```
### - 接口访问URL
```
GET /v2/object/:object_id/relation_query_strategy/:id
```
### - 参数
#### URI 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| object_id | string | 是 |  |  | []
| id | string | 是 |  |  | []



### - 返回值说明
|名称|类型|备注|
|---|---|---|
| id | string | 策略ID(可以自定义, 不给定后台会默认生成)
| byPath | string | v4(全量查询字段）
| name | string | 策略名称
| type | string | 策略类型(org 或者 user)
| path_list | map[] | 策略内容(包含查询条件和返回的字段, 不指定返回的字段则默认返回name字段, alias ${objectId}.name)
| object_id | string | 策略所属模型id
| ctime | string | 创建时间
| creator | string | 创建用户


### - 返回码
|返回码|备注|
|---|---|
| 0 | success


### - 返回示例
```json
{
    "code": 0,
    "data": {
        "name": "fake_name",
        "creator": "fake_creator",
        "byPath": "fake_byPath",
        "object_id": "fake_object_id",
        "path_list": [
            {}
        ],
        "type": "fake_type",
        "id": "fake_id",
        "ctime": "fake_ctime"
    },
    "error": "",
    "codeExplain": ""
}
```
## <a id='-get_business_graph-GET'></a> get_business_graph GET
>查询应用系统子系统拓扑<br>

### - 接口访问URL
```
GET /systems/_graph_mode
```
### - 详细说明
>查询应用系统展示出树状或者拓扑状的数据结构<br>

### - 参数



### - 返回值说明
|名称|类型|备注|
|---|---|---|
| topic_vertices | map[] | 根节点
| vertices | map[] | 节点
| edges | map[] | 边


### - 返回码
|返回码|备注|
|---|---|
| 0 | success


### - 返回示例
```json
{
    "message": "",
    "code": 0,
    "data": {
        "topic_vertices": [
            {
                "instanceId": "59b94392c3652",
                "@rid": "59b94392c3652",
                "name": "ens_client"
            }
        ],
        "vertices": [
            {
                "instanceId": "59cf06df730ef",
                "@rid": "59cf06df730ef",
                "name": "cmdb"
            }
        ],
        "edges": [
            {
                "_relation_id": "system_sub_system",
                "in": "59b94392c3652",
                "@rid": "59cf06df730ef59b94392c3652",
                "out": "59cf06df730ef"
            }
        ]
    },
    "error": ""
}
```
## <a id='-searchSubSystem-POST'></a> searchSubSystem POST
>搜索系统的子系统以及，以及递归的获取子系统的子系统<br>

### - 测试关键字
```
search sub system request 
```
### - 接口访问URL
```
POST /system/:system_instance_id/_search_subsystem
```
### - 详细说明
>关于搜索条件的文档说明请参考[实例搜索接口]的说明<br>

### - 参数
#### URI 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| system_instance_id | string | 是 | 父系统的实例ID |  | {'gte': 1}


#### body 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| page | int | 否 | 页码 | 1 | {'gte': 1}
| page_size | int | 否 | 页大小 | 30 | {'gte': 1, 'lte': 3000}
| query | map | 否 | 查询条件,与[实例搜索接口]的query字段说明一致 |  | 
| fields | map | 否 | 过滤的字段列表, 留空代表返回所有字段(true: 表示指定获取字段, false: 表示指定不获取的字段)(支持关系数据的二级jsonPath格式的指定字段如clusters.name) |  | 
| sort | map | 否 | 按字段排序, 留空默认按照实例ID降序排序(1表示升序, -1表示降序) |  | 
| permission | string[] | 否 | 按照权限过滤(通用实例都有`read`, `update`, `delete`权限控制, 主机实例在通用实例权限基础上有额外的`operate`权限, 应用实例在通用实例权限基础上有额外的`developClusterOperate`, `testClusterOperate`, `prereleaseClusterOperate`, `productionClusterOperate`权限) |  | 
| only_relation_view | bool | 否 | 对于关联的实例数据是否只获取relation_view中指定的属性, 这个字段为true时, 会覆盖fields字段中指定的二级字段设置 | False | []
| only_my_instance | bool | 否 | 是否只获取与自己有关的那部分数据, 默认为false | False | []


### - 返回值说明
|名称|类型|备注|
|---|---|---|
| total | int | total
| page | int | page
| page_size | int | page_size
| list | map[] | 实例列表


### - 返回码
|返回码|备注|
|---|---|
| 0 | success

### - 请求示例
```json
{
    "sort": {},
    "permission": [
        "fake_permission"
    ],
    "fields": {},
    "page_size": 8,
    "only_relation_view": true,
    "only_my_instance": true,
    "query": {},
    "page": 8
}
```

### - 返回示例
```json
{
    "code": 0,
    "data": {
        "total": 8,
        "list": [
            {}
        ],
        "page": 8,
        "page_size": 8
    },
    "error": "",
    "codeExplain": ""
}
```
## <a id='-searchAppInSystem-POST'></a> searchAppInSystem POST
>查询应用系统的所有子系统以及所有子系统的子系统所包含的应用<br>

### - 测试关键字
```
search app in system request 
```
### - 接口访问URL
```
POST /system/:system_instance_id/_search_apps
```
### - 详细说明
>关于搜索条件的文档说明请参考[实例搜索接口]的说明<br>

### - 参数
#### URI 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| system_instance_id | string | 是 | 系统的实例ID |  | {'gte': 1}


#### body 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| page | int | 否 | 页码 | 1 | {'gte': 1}
| page_size | int | 否 | 页大小 | 30 | {'gte': 1, 'lte': 3000}
| query | map | 否 | 查询条件,与[实例搜索接口]的query字段说明一致 |  | 
| fields | map | 否 | 过滤的字段列表, 留空代表返回所有字段(true: 表示指定获取字段, false: 表示指定不获取的字段)(支持关系数据的二级jsonPath格式的指定字段如clusters.name) |  | 
| sort | map | 否 | 按字段排序, 留空默认按照实例ID降序排序(1表示升序, -1表示降序) |  | 
| permission | string[] | 否 | 按照权限过滤(通用实例都有`read`, `update`, `delete`权限控制, 主机实例在通用实例权限基础上有额外的`operate`权限, 应用实例在通用实例权限基础上有额外的`developClusterOperate`, `testClusterOperate`, `prereleaseClusterOperate`, `productionClusterOperate`权限) |  | 
| only_relation_view | bool | 否 | 对于关联的实例数据是否只获取relation_view中指定的属性, 这个字段为true时, 会覆盖fields字段中指定的二级字段设置 | False | []
| only_my_instance | bool | 否 | 是否只获取与自己有关的那部分数据, 默认为false | False | []
| include_sub_systems | bool | 否 | 是否包含子系统以及子系统的子系统的应用 | True | []


### - 返回值说明
|名称|类型|备注|
|---|---|---|
| total | int | total
| page | int | page
| page_size | int | page_size
| list | map[] | 实例列表


### - 返回码
|返回码|备注|
|---|---|
| 0 | success

### - 请求示例
```json
{
    "sort": {},
    "include_sub_systems": true,
    "permission": [
        "fake_permission"
    ],
    "fields": {},
    "page_size": 8,
    "only_relation_view": true,
    "only_my_instance": true,
    "query": {},
    "page": 8
}
```

### - 返回示例
```json
{
    "code": 0,
    "data": {
        "total": 8,
        "list": [
            {}
        ],
        "page": 8,
        "page_size": 8
    },
    "error": "",
    "codeExplain": ""
}
```
## <a id='-get_business_tree_list-GET'></a> get_business_tree_list GET
>批量获取业务业务树全路径<br>

### - 测试关键字
```
business tree list request 
```
### - 接口访问URL
```
GET /system/business_tree/list
```
### - 参数

#### query 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| ids | string | 是 | 应用系统的实例ID列表,使用逗号分隔 |  | {'gte': 1}



### - 返回码
|返回码|备注|
|---|---|
| 0 | success


### - 返回示例
```json
{
    "code": 0,
    "data": [
        {
            "instanceId": "fake_instanceId",
            "parents": [
                {
                    "instanceId": "fake_instanceId",
                    "name": "fake_name"
                }
            ],
            "name": "fake_name"
        }
    ],
    "error": "",
    "codeExplain": ""
}
```
## <a id='-pathSearchV1-POST'></a> pathSearchV1 POST
>关系查询v1<br>

### - 测试关键字
```
path search v1 request 
```
### - 接口访问URL
```
POST /path/_search
```
### - 参数


#### body 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| page | int | 否 | 页数 | 1 | []
| page_size | int | 否 | 每页数量 | 200 | []
| only_relation_view | bool | 否 | 对于关联的实例数据是否只获取relation_view中指定的属性(默认为 instanceId, _object_id, name[主机实例数据为hostname]) | True | []
| path | map[] | 是 | 关系路径 |  | []


### - 返回值说明
|名称|类型|备注|
|---|---|---|
| page | int | 页数
| page_size | int | 每页数量
| total | int | 结果总数
| list | map[] | 结果列表


### - 返回码
|返回码|备注|
|---|---|
| 0 | success

### - 请求示例
```json
{
    "only_relation_view": true,
    "page": 8,
    "page_size": 8,
    "path": [
        {}
    ]
}
```

### - 返回示例
```json
{
    "code": 0,
    "data": {
        "total": 8,
        "list": [
            {}
        ],
        "page": 8,
        "page_size": 8
    },
    "error": "",
    "codeExplain": ""
}
```
## <a id='-pathSearchV3-POST'></a> pathSearchV3 POST
>关系查询v3<br>

### - 测试关键字
```
path search request 
```
### - 接口访问URL
```
POST /v3/path/_search
```
### - 参数


#### body 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| page | int | 否 | 页数 | 1 | []
| page_size | int | 否 | 每页数量 | 200 | []
| alias_id_sort | map | 否 | 以alias_id表示的字段排序 |  | 
| path | map[] | 是 | 关系路径 |  | []


### - 返回值说明
|名称|类型|备注|
|---|---|---|
| page | int | 页数
| page_size | int | 每页数量
| total | int | 结果总数
| list | value | 结果列表


### - 返回码
|返回码|备注|
|---|---|
| 0 | success

### - 请求示例
```json
{
    "path": [
        {}
    ],
    "alias_id_sort": {},
    "page": 8,
    "page_size": 8
}
```

### - 返回示例
```json
{
    "code": 0,
    "data": {
        "total": 8,
        "page": 8,
        "page_size": 8
    },
    "error": "",
    "codeExplain": ""
}
```
## <a id='-pathSearchV2-POST'></a> pathSearchV2 POST
>关系查询v2<br>

### - 测试关键字
```
path search v2 request 
```
### - 接口访问URL
```
POST /v2/path/_search
```
### - 参数


#### body 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| page | int | 否 | 页数 | 1 | []
| page_size | int | 否 | 每页数量 | 200 | []
| path | map[] | 是 | 关系路径 |  | []


### - 返回值说明
|名称|类型|备注|
|---|---|---|
| page | int | 页数
| page_size | int | 每页数量
| total | int | 结果总数
| list | map[] | 结果列表


### - 返回码
|返回码|备注|
|---|---|
| 0 | success

### - 请求示例
```json
{
    "path": [
        {}
    ],
    "page": 8,
    "page_size": 8
}
```

### - 返回示例
```json
{
    "code": 0,
    "data": {
        "total": 8,
        "list": [
            {}
        ],
        "page": 8,
        "page_size": 8
    },
    "error": "",
    "codeExplain": ""
}
```
## <a id='-pathSearchV4-POST'></a> pathSearchV4 POST
>关系查询v4<br>

### - 测试关键字
```
path search request 
```
### - 接口访问URL
```
POST /v4/path/_search
```
### - 参数


#### body 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| page | int | 否 | 页数 | 1 | {'gte': 1}
| page_size | int | 否 | 每页数量 | 100 | {'gte': 1}
| alias_id_sort | map | 否 | 以alias_id表示的字段排序 |  | 
| path | map[] | 是 | 关系路径 |  | []


### - 返回值说明
|名称|类型|备注|
|---|---|---|
| root | int | 起始点个数
| allPath | int | 全量路径个数
| list | value | 结果列表


### - 返回码
|返回码|备注|
|---|---|
| 0 | success

### - 请求示例
```json
{
    "path": [
        {}
    ],
    "alias_id_sort": {},
    "page": 8,
    "page_size": 8
}
```

### - 返回示例
```json
{
    "code": 0,
    "data": {
        "allPath": 8,
        "root": 8
    },
    "error": "",
    "codeExplain": ""
}
```
## <a id='-update_permission_batch-PUT'></a> update_permission_batch PUT
>批量修改实例权限<br>

### - 测试关键字
```
update permission batch request 
```
### - 接口访问URL
```
PUT /permission/:object_id/instances/_batch
```
### - 参数
#### URI 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| object_id | string | 是 | 资源模型ID |  | {'gte': 1}


#### body 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| ids | string[] | 是 | 实例ID列表 |  | {'gte': 1}
| field | string | 否 | 权限字段 |  | 
| fields | string[] | 否 | updateAthorizers, deleteAuthorizers, readAuthorizers, operateAuthorizers中的一个或多个 |  | 
| method | enum | 是 | 修改操作的类型(overwrite, append, pull)(在枚举之外的操作类型会报错) |  | []
| list | string[] | 是 | 用户,用户组列表 |  | []


### - 返回值说明
|名称|类型|备注|
|---|---|---|
| noAuthorizedList | map[] | 没有权限更新的实例列表


### - 返回码
|返回码|备注|
|---|---|
| 0 | success

### - 请求示例
```json
{
    "field": "fake_field",
    "method": "overwrite",
    "list": [
        "fake_list"
    ],
    "ids": [
        "fake_ids"
    ],
    "fields": [
        "fake_fields"
    ]
}
```

### - 返回示例
```json
{
    "code": 0,
    "data": {
        "noAuthorizedList": [
            {}
        ]
    },
    "error": "",
    "codeExplain": ""
}
```
## <a id='-fulltext_search-GET'></a> fulltext_search GET
>全文搜索<br>

### - 测试关键字
```
fulltext search request 
```
### - 接口访问URL
```
GET /fulltext/_search
```
### - 参数

#### query 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| page | int | 否 | 页码 | 1 | {'gte': 1}
| page_size | int | 否 | 页大小 | 30 | {'gte': 1}
| keyword | string | 否 | 搜索关键字 |  | 
| object_id | string | 否 | 资源模型Id |  | 


### - 返回值说明
|名称|类型|备注|
|---|---|---|
| page | int | 页码
| page_size | int | 页大小
| total | int | 总数
| list | map[] | 实例数据
| count | map | 模型实例统计数据,如:{"HOST": 10, "APP": 5}


### - 返回码
|返回码|备注|
|---|---|
| 0 | success


### - 返回示例
```json
{
    "code": 0,
    "data": {
        "count": {},
        "total": 8,
        "list": [
            {}
        ],
        "page": 8,
        "page_size": 8
    },
    "error": "",
    "codeExplain": ""
}
```
## <a id='-auto_discovery-POST'></a> auto_discovery POST
>自动发现的接口<br>

### - 测试关键字
```
auto discovery request 
```
### - 接口访问URL
```
POST /object/:object_id/instance/_import-json
```
### - 参数
#### URI 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| object_id | string | 是 | 资源模型ID |  | []


#### body 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| filter | map | 是 | 筛选器 |  | []
| update | map | 是 | 更新数据 |  | []
| upsert | bool | 是 | 存在即更新 |  | []



### - 返回码
|返回码|备注|
|---|---|
| 0 | success

### - 请求示例
```json
[
    {
        "filter": {},
        "update": {},
        "upsert": true
    }
]
```

### - 返回示例
```json
{
    "code": 0,
    "data": [
        {
            "instanceId": "fake_instanceId",
            "effected": true,
            "code": 8,
            "matched": true
        }
    ],
    "error": "",
    "codeExplain": ""
}
```
## <a id='-import_instance-POST'></a> import_instance POST
>批量编辑实例(导入实例)<br>

### - 测试关键字
```
import instance request 
```
### - 接口访问URL
```
POST /object/:object_id/instance/_import
```
### - 参数
#### URI 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| object_id | string | 是 | 资源模型ID |  | []


#### body 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| keys | string[] | 是 | 导入实例的字段 |  | []
| datas | map[] | 是 | 导入实例数据列表 |  | []


### - 返回值说明
|名称|类型|备注|
|---|---|---|
| insert_count | int | 成功插入数量
| update_count | int | 成功更新数量
| failed_count | int | 失败数量
| data | fail_data.FailData[] | 失败数据


FailData-

|名称|类型|备注|
|---|---|---|
| code | int | 错误码
| error | string | 错误信息
| data | map[] | 错误数据

### - 返回码
|返回码|备注|
|---|---|
| 0 | success

### - 请求示例
```json
{
    "keys": [
        "fake_keys"
    ],
    "datas": [
        {}
    ]
}
```

### - 返回示例
```json
{
    "code": 0,
    "data": {
        "insert_count": 8,
        "data": [
            {
                "code": 8,
                "data": [
                    {}
                ],
                "error": "fake_error"
            }
        ],
        "failed_count": 8,
        "update_count": 8
    },
    "error": "",
    "codeExplain": ""
}
```
## <a id='-export-GET'></a> export GET
>模型导出<br>

### - 测试关键字
```
export request 
```
### - 接口访问URL
```
GET /object_export
```
### - 参数

#### query 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| object_ids | string | 否 | 资源模型ID,用分号隔开;为空时查询所有的资源模型 |  | []



### - 返回码
|返回码|备注|
|---|---|
| 0 | success


### - 返回示例
```json
{
    "message": "Success",
    "code": 0,
    "data": [
        "#\u8d44\u6e90\u6a21\u578b\u5217\u8868, \u53ea\u5305\u542bicon,objectId,name,attrList,category,memo,relation_groups,relation_list\u7b49\u5b57\u6bb5\u7684\u5185\u5bb9#"
    ],
    "error": "\u6210\u529f"
}
```
## <a id='-update_relation_group-PUT'></a> update_relation_group PUT
>更新模型关系分组<br>

### - 测试关键字
```
update relation group request 
```
### - 接口访问URL
```
PUT /object/:object_id/relation_group/:id
```
### - 参数
#### URI 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| object_id | string | 是 | 资源模型ID |  | []
| id | string | 是 | 分组ID |  | []


#### body 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| name | string | 否 | 分组名称 |  | []
| relations | relation_group_relation.RelationGroupRelation[] | 否 | 分组中的关系 |  | []

RelationGroupRelation-

|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| relation_side_id | string | 否 | 表示关系的left_id或者right_id的值, 用于表示分组的关系是关系的哪一端  |  | 

### - 返回值说明
|名称|类型|备注|
|---|---|---|
| id | string | ID
| name | string | 名称
| protected | bool | 是否是内置关系分组，内置的关系分组不允许删除


### - 返回码
|返回码|备注|
|---|---|
| 0 | success

### - 请求示例
```json
{
    "name": "fake_name",
    "relations": [
        {
            "relation_side_id": "fake_relation_side_id"
        }
    ]
}
```

### - 返回示例
```json
{
    "code": 0,
    "data": {
        "protected": true,
        "id": "fake_id",
        "name": "fake_name"
    },
    "error": "",
    "codeExplain": ""
}
```
## <a id='-delete_property-DELETE'></a> delete_property DELETE
>删除模型属性<br>

### - 测试关键字
```
delete property request 
```
### - 接口访问URL
```
DELETE /object/:object_id/attr/:attr_id
```
### - 参数
#### URI 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| object_id | string | 是 |  |  | {'gte': 1}
| attr_id | string | 是 |  |  | {'gte': 1}



### - 返回值说明
|名称|类型|备注|
|---|---|---|
| objectId | string | ID
| name | string | 名称
| icon | string | 图标
| category | string | 分类, 点分表示二级分类
| memo | string | 说明
| protected | bool | true代表是核心模型，是受保护的模型，不允许被删除
| view | map | 模型的视图设置
| attrList | property.Property[] | 属性列表
| relation_groups | relation_group.RelationGroup[] | 关系分组定义
| relation_list | relation.Relation[] | 关系列表
| updateAuthorizers | string[] | 编辑权限白名单
| deleteAuthorizers | string[] | 删除权限白名单


Property-

|名称|类型|备注|
|---|---|---|
| id | string | 属性ID: 对已有模型添加新的属性ID需要加下划线开头避免冲突
| name | string | 属性名称
| protected | bool | 是否是内置属性: 核心定义的内置属性默认都是核心属性, 核心属性不允许被删除、不允许修改约束
| custom | string | 是否是自定义字段: 历史遗留原因不是布尔值定义, 待废弃, 与protected字段含义重复, 优先使用protected字段
| unique | string | 是否唯一: 历史遗留原因不是布尔值定义
| readonly | string | 是否只读: 历史遗留原因不是布尔值定义
| required | string | 是否必填: 历史遗留原因不是布尔值定义
| tag | string[] | 属性分类
| description | string | 似乎没有什么作用的描述
| tips | string | 似乎没有什么作用的提示
| value | property_value.PropertyValue | 属性值类型定义

PropertyValue-

|名称|类型|备注|
|---|---|---|
| type | enum | 数据类型
| regex | value | type是enum时是枚举值数组, struct和structs没有regex, 其他的type时是正则表达式
| default_type | string | 默认值类型( value: 具体的值, function:可执行函数, auto-increment-id:自增ID, series-number:定长序列号)
| default | value | 默认值
| struct_define | struct_define.StructDefine[] | 结构体字段定义: 当type 为 struct 和 structs 时候为必填
| mode | string | 字符串模式定义: 多行文本和普通字符串
| prefix | string | 自增ID和流水号的前缀: 当default_type 是series-number和 auto-increment-id时候为必填
| start_value | int | 自增ID和流水号的起始值
| series_number_length | int | 流水号的固定长度

StructDefine-

|名称|类型|备注|
|---|---|---|
| id | string | 结构体字段ID
| name | string | 结构体字段名称
| type | enum | 数据类型
| regex | string[] | 仅仅在type是enum时有值，并且是字符串数组
| protected | bool | 是否是内置属性: 核心定义的内置属性默认都是核心属性, 核心属性不允许被删除、不允许修改约束

RelationGroup-

|名称|类型|备注|
|---|---|---|
| id | string | ID
| name | string | 名称
| protected | bool | 是否是内置关系分组，内置的关系分组不允许删除

Relation-

|名称|类型|备注|
|---|---|---|
| relation_id | string | 必须全局唯一: 新添加的关系ID字段建议增加下划线前缀
| name | string | 不是必填, 而且在引入了left_description和 right_description 之后这个字段几乎处于废弃状态
| protected | bool | 
| left_object_id | string | 关系左端的模型ID
| left_id | string | 关系左端模型中表达右端模型实例的别名字段: 比如应用的负责人需要在应用的实例中表达出一个字段; 对已有模型添加关系时这个ID需要加下划线前缀避免冲突
| left_description | string | 是与left_id 相反的含义, 但仅用于前端展示
| left_name | string | 是与left_id 对应的含义, 但仅用于前端展示
| left_min | int | 关系左端的资源模型实例至少包含多少数量的关系: 目前来说这个字段是过度设计的字段, 一般填0就好了
| left_max | int | 关系左端的资源模型实例最多包含多少数量的关系: 有数据库级别的索引支持, 一般情况填1 或者 -1, -1表示无限多
| left_groups | string[] | 关系在左端模型的哪些分组里
| left_tags | string[] | 
| right_object_id | string | 关系右端的模型ID
| right_id | string | 关系右端模型中表达左端模型实例的别名字段: 比如应用的负责人需要在应用的实例中表达出一个字段; 对已有模型添加关系时这个ID需要加下划线前缀避免冲突
| right_description | string | 是与right_id 相反的含义, 但仅用于前端展示
| right_name | string | 是与right_id 对应的含义, 但仅用于前端展示
| right_min | int | 关系右端的资源模型实例至少包含多少数量的关系: 目前来说这个字段是过度设计的字段, 一般填0就好了
| right_max | int | 关系右端的资源模型实例最多包含多少数量的关系: 有数据库级别的索引支持, 一般情况填1 或者 -1, -1表示无限多
| right_groups | string[] | 关系在右端模型的哪些分组里
| right_tags | string[] | 

### - 返回码
|返回码|备注|
|---|---|
| 0 | success


### - 返回示例
```json
{
    "code": 0,
    "data": {
        "category": "fake_category",
        "attrList": [
            {
                "name": "fake_name",
                "required": "fake_required",
                "tag": [
                    "fake_tag"
                ],
                "value": {
                    "struct_define": [
                        {
                            "regex": [
                                "fake_regex"
                            ],
                            "protected": true,
                            "type": "int",
                            "id": "fake_id",
                            "name": "fake_name"
                        }
                    ],
                    "series_number_length": 8,
                    "default_type": "fake_default_type",
                    "prefix": "fake_prefix",
                    "mode": "fake_mode",
                    "start_value": 8,
                    "type": "int"
                },
                "custom": "fake_custom",
                "readonly": "fake_readonly",
                "protected": true,
                "tips": "fake_tips",
                "unique": "fake_unique",
                "id": "fake_id",
                "description": "fake_description"
            }
        ],
        "name": "fake_name",
        "objectId": "fake_objectId",
        "memo": "fake_memo",
        "deleteAuthorizers": [
            "fake_deleteAuthorizers"
        ],
        "updateAuthorizers": [
            "fake_updateAuthorizers"
        ],
        "relation_list": [
            {
                "right_groups": [
                    "fake_right_groups"
                ],
                "right_min": 8,
                "left_object_id": "fake_left_object_id",
                "name": "fake_name",
                "right_id": "fake_right_id",
                "right_max": 8,
                "left_id": "fake_left_id",
                "left_max": 8,
                "left_min": 8,
                "right_description": "fake_right_description",
                "left_name": "fake_left_name",
                "protected": true,
                "left_description": "fake_left_description",
                "right_name": "fake_right_name",
                "relation_id": "fake_relation_id",
                "left_tags": [
                    "fake_left_tags"
                ],
                "right_tags": [
                    "fake_right_tags"
                ],
                "right_object_id": "fake_right_object_id",
                "left_groups": [
                    "fake_left_groups"
                ]
            }
        ],
        "protected": true,
        "relation_groups": [
            {
                "protected": true,
                "id": "fake_id",
                "name": "fake_name"
            }
        ],
        "view": {},
        "icon": "fake_icon"
    },
    "error": "",
    "codeExplain": ""
}
```
## <a id='-delete-DELETE'></a> delete DELETE
>删除模型<br>

### - 测试关键字
```
delete request 
```
### - 接口访问URL
```
DELETE /object/:object_id
```
### - 参数
#### URI 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| object_id | string | 是 |  |  | {'gte': 1}



### - 返回值说明
|名称|类型|备注|
|---|---|---|
| objectId | string | ID
| name | string | 名称
| icon | string | 图标
| category | string | 分类, 点分表示二级分类
| memo | string | 说明
| protected | bool | true代表是核心模型，是受保护的模型，不允许被删除
| view | map | 模型的视图设置
| attrList | property.Property[] | 属性列表
| relation_groups | relation_group.RelationGroup[] | 关系分组定义
| relation_list | relation.Relation[] | 关系列表
| updateAuthorizers | string[] | 编辑权限白名单
| deleteAuthorizers | string[] | 删除权限白名单


Property-

|名称|类型|备注|
|---|---|---|
| id | string | 属性ID: 对已有模型添加新的属性ID需要加下划线开头避免冲突
| name | string | 属性名称
| protected | bool | 是否是内置属性: 核心定义的内置属性默认都是核心属性, 核心属性不允许被删除、不允许修改约束
| custom | string | 是否是自定义字段: 历史遗留原因不是布尔值定义, 待废弃, 与protected字段含义重复, 优先使用protected字段
| unique | string | 是否唯一: 历史遗留原因不是布尔值定义
| readonly | string | 是否只读: 历史遗留原因不是布尔值定义
| required | string | 是否必填: 历史遗留原因不是布尔值定义
| tag | string[] | 属性分类
| description | string | 似乎没有什么作用的描述
| tips | string | 似乎没有什么作用的提示
| value | property_value.PropertyValue | 属性值类型定义

PropertyValue-

|名称|类型|备注|
|---|---|---|
| type | enum | 数据类型
| regex | value | type是enum时是枚举值数组, struct和structs没有regex, 其他的type时是正则表达式
| default_type | string | 默认值类型( value: 具体的值, function:可执行函数, auto-increment-id:自增ID, series-number:定长序列号)
| default | value | 默认值
| struct_define | struct_define.StructDefine[] | 结构体字段定义: 当type 为 struct 和 structs 时候为必填
| mode | string | 字符串模式定义: 多行文本和普通字符串
| prefix | string | 自增ID和流水号的前缀: 当default_type 是series-number和 auto-increment-id时候为必填
| start_value | int | 自增ID和流水号的起始值
| series_number_length | int | 流水号的固定长度

StructDefine-

|名称|类型|备注|
|---|---|---|
| id | string | 结构体字段ID
| name | string | 结构体字段名称
| type | enum | 数据类型
| regex | string[] | 仅仅在type是enum时有值，并且是字符串数组
| protected | bool | 是否是内置属性: 核心定义的内置属性默认都是核心属性, 核心属性不允许被删除、不允许修改约束

RelationGroup-

|名称|类型|备注|
|---|---|---|
| id | string | ID
| name | string | 名称
| protected | bool | 是否是内置关系分组，内置的关系分组不允许删除

Relation-

|名称|类型|备注|
|---|---|---|
| relation_id | string | 必须全局唯一: 新添加的关系ID字段建议增加下划线前缀
| name | string | 不是必填, 而且在引入了left_description和 right_description 之后这个字段几乎处于废弃状态
| protected | bool | 
| left_object_id | string | 关系左端的模型ID
| left_id | string | 关系左端模型中表达右端模型实例的别名字段: 比如应用的负责人需要在应用的实例中表达出一个字段; 对已有模型添加关系时这个ID需要加下划线前缀避免冲突
| left_description | string | 是与left_id 相反的含义, 但仅用于前端展示
| left_name | string | 是与left_id 对应的含义, 但仅用于前端展示
| left_min | int | 关系左端的资源模型实例至少包含多少数量的关系: 目前来说这个字段是过度设计的字段, 一般填0就好了
| left_max | int | 关系左端的资源模型实例最多包含多少数量的关系: 有数据库级别的索引支持, 一般情况填1 或者 -1, -1表示无限多
| left_groups | string[] | 关系在左端模型的哪些分组里
| left_tags | string[] | 
| right_object_id | string | 关系右端的模型ID
| right_id | string | 关系右端模型中表达左端模型实例的别名字段: 比如应用的负责人需要在应用的实例中表达出一个字段; 对已有模型添加关系时这个ID需要加下划线前缀避免冲突
| right_description | string | 是与right_id 相反的含义, 但仅用于前端展示
| right_name | string | 是与right_id 对应的含义, 但仅用于前端展示
| right_min | int | 关系右端的资源模型实例至少包含多少数量的关系: 目前来说这个字段是过度设计的字段, 一般填0就好了
| right_max | int | 关系右端的资源模型实例最多包含多少数量的关系: 有数据库级别的索引支持, 一般情况填1 或者 -1, -1表示无限多
| right_groups | string[] | 关系在右端模型的哪些分组里
| right_tags | string[] | 

### - 返回码
|返回码|备注|
|---|---|
| 0 | success


### - 返回示例
```json
{
    "code": 0,
    "data": {
        "category": "fake_category",
        "attrList": [
            {
                "name": "fake_name",
                "required": "fake_required",
                "tag": [
                    "fake_tag"
                ],
                "value": {
                    "struct_define": [
                        {
                            "regex": [
                                "fake_regex"
                            ],
                            "protected": true,
                            "type": "int",
                            "id": "fake_id",
                            "name": "fake_name"
                        }
                    ],
                    "series_number_length": 8,
                    "default_type": "fake_default_type",
                    "prefix": "fake_prefix",
                    "mode": "fake_mode",
                    "start_value": 8,
                    "type": "int"
                },
                "custom": "fake_custom",
                "readonly": "fake_readonly",
                "protected": true,
                "tips": "fake_tips",
                "unique": "fake_unique",
                "id": "fake_id",
                "description": "fake_description"
            }
        ],
        "name": "fake_name",
        "objectId": "fake_objectId",
        "memo": "fake_memo",
        "deleteAuthorizers": [
            "fake_deleteAuthorizers"
        ],
        "updateAuthorizers": [
            "fake_updateAuthorizers"
        ],
        "relation_list": [
            {
                "right_groups": [
                    "fake_right_groups"
                ],
                "right_min": 8,
                "left_object_id": "fake_left_object_id",
                "name": "fake_name",
                "right_id": "fake_right_id",
                "right_max": 8,
                "left_id": "fake_left_id",
                "left_max": 8,
                "left_min": 8,
                "right_description": "fake_right_description",
                "left_name": "fake_left_name",
                "protected": true,
                "left_description": "fake_left_description",
                "right_name": "fake_right_name",
                "relation_id": "fake_relation_id",
                "left_tags": [
                    "fake_left_tags"
                ],
                "right_tags": [
                    "fake_right_tags"
                ],
                "right_object_id": "fake_right_object_id",
                "left_groups": [
                    "fake_left_groups"
                ]
            }
        ],
        "protected": true,
        "relation_groups": [
            {
                "protected": true,
                "id": "fake_id",
                "name": "fake_name"
            }
        ],
        "view": {},
        "icon": "fake_icon"
    },
    "error": "",
    "codeExplain": ""
}
```
## <a id='-get-GET'></a> get GET
>获取单个模型<br>

### - 测试关键字
```
get request 
```
### - 接口访问URL
```
GET /object/:object_id
```
### - 参数
#### URI 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| object_id | string | 是 |  |  | {'gte': 1}



### - 返回值说明
|名称|类型|备注|
|---|---|---|
| objectId | string | ID
| name | string | 名称
| icon | string | 图标
| category | string | 分类, 点分表示二级分类
| memo | string | 说明
| protected | bool | true代表是核心模型，是受保护的模型，不允许被删除
| view | map | 模型的视图设置
| attrList | property.Property[] | 属性列表
| relation_groups | relation_group.RelationGroup[] | 关系分组定义
| relation_list | relation.Relation[] | 关系列表
| updateAuthorizers | string[] | 编辑权限白名单
| deleteAuthorizers | string[] | 删除权限白名单


Property-

|名称|类型|备注|
|---|---|---|
| id | string | 属性ID: 对已有模型添加新的属性ID需要加下划线开头避免冲突
| name | string | 属性名称
| protected | bool | 是否是内置属性: 核心定义的内置属性默认都是核心属性, 核心属性不允许被删除、不允许修改约束
| custom | string | 是否是自定义字段: 历史遗留原因不是布尔值定义, 待废弃, 与protected字段含义重复, 优先使用protected字段
| unique | string | 是否唯一: 历史遗留原因不是布尔值定义
| readonly | string | 是否只读: 历史遗留原因不是布尔值定义
| required | string | 是否必填: 历史遗留原因不是布尔值定义
| tag | string[] | 属性分类
| description | string | 似乎没有什么作用的描述
| tips | string | 似乎没有什么作用的提示
| value | property_value.PropertyValue | 属性值类型定义

PropertyValue-

|名称|类型|备注|
|---|---|---|
| type | enum | 数据类型
| regex | value | type是enum时是枚举值数组, struct和structs没有regex, 其他的type时是正则表达式
| default_type | string | 默认值类型( value: 具体的值, function:可执行函数, auto-increment-id:自增ID, series-number:定长序列号)
| default | value | 默认值
| struct_define | struct_define.StructDefine[] | 结构体字段定义: 当type 为 struct 和 structs 时候为必填
| mode | string | 字符串模式定义: 多行文本和普通字符串
| prefix | string | 自增ID和流水号的前缀: 当default_type 是series-number和 auto-increment-id时候为必填
| start_value | int | 自增ID和流水号的起始值
| series_number_length | int | 流水号的固定长度

StructDefine-

|名称|类型|备注|
|---|---|---|
| id | string | 结构体字段ID
| name | string | 结构体字段名称
| type | enum | 数据类型
| regex | string[] | 仅仅在type是enum时有值，并且是字符串数组
| protected | bool | 是否是内置属性: 核心定义的内置属性默认都是核心属性, 核心属性不允许被删除、不允许修改约束

RelationGroup-

|名称|类型|备注|
|---|---|---|
| id | string | ID
| name | string | 名称
| protected | bool | 是否是内置关系分组，内置的关系分组不允许删除

Relation-

|名称|类型|备注|
|---|---|---|
| relation_id | string | 必须全局唯一: 新添加的关系ID字段建议增加下划线前缀
| name | string | 不是必填, 而且在引入了left_description和 right_description 之后这个字段几乎处于废弃状态
| protected | bool | 
| left_object_id | string | 关系左端的模型ID
| left_id | string | 关系左端模型中表达右端模型实例的别名字段: 比如应用的负责人需要在应用的实例中表达出一个字段; 对已有模型添加关系时这个ID需要加下划线前缀避免冲突
| left_description | string | 是与left_id 相反的含义, 但仅用于前端展示
| left_name | string | 是与left_id 对应的含义, 但仅用于前端展示
| left_min | int | 关系左端的资源模型实例至少包含多少数量的关系: 目前来说这个字段是过度设计的字段, 一般填0就好了
| left_max | int | 关系左端的资源模型实例最多包含多少数量的关系: 有数据库级别的索引支持, 一般情况填1 或者 -1, -1表示无限多
| left_groups | string[] | 关系在左端模型的哪些分组里
| left_tags | string[] | 
| right_object_id | string | 关系右端的模型ID
| right_id | string | 关系右端模型中表达左端模型实例的别名字段: 比如应用的负责人需要在应用的实例中表达出一个字段; 对已有模型添加关系时这个ID需要加下划线前缀避免冲突
| right_description | string | 是与right_id 相反的含义, 但仅用于前端展示
| right_name | string | 是与right_id 对应的含义, 但仅用于前端展示
| right_min | int | 关系右端的资源模型实例至少包含多少数量的关系: 目前来说这个字段是过度设计的字段, 一般填0就好了
| right_max | int | 关系右端的资源模型实例最多包含多少数量的关系: 有数据库级别的索引支持, 一般情况填1 或者 -1, -1表示无限多
| right_groups | string[] | 关系在右端模型的哪些分组里
| right_tags | string[] | 

### - 返回码
|返回码|备注|
|---|---|
| 0 | success


### - 返回示例
```json
{
    "code": 0,
    "data": {
        "category": "fake_category",
        "attrList": [
            {
                "name": "fake_name",
                "required": "fake_required",
                "tag": [
                    "fake_tag"
                ],
                "value": {
                    "struct_define": [
                        {
                            "regex": [
                                "fake_regex"
                            ],
                            "protected": true,
                            "type": "int",
                            "id": "fake_id",
                            "name": "fake_name"
                        }
                    ],
                    "series_number_length": 8,
                    "default_type": "fake_default_type",
                    "prefix": "fake_prefix",
                    "mode": "fake_mode",
                    "start_value": 8,
                    "type": "int"
                },
                "custom": "fake_custom",
                "readonly": "fake_readonly",
                "protected": true,
                "tips": "fake_tips",
                "unique": "fake_unique",
                "id": "fake_id",
                "description": "fake_description"
            }
        ],
        "name": "fake_name",
        "objectId": "fake_objectId",
        "memo": "fake_memo",
        "deleteAuthorizers": [
            "fake_deleteAuthorizers"
        ],
        "updateAuthorizers": [
            "fake_updateAuthorizers"
        ],
        "relation_list": [
            {
                "right_groups": [
                    "fake_right_groups"
                ],
                "right_min": 8,
                "left_object_id": "fake_left_object_id",
                "name": "fake_name",
                "right_id": "fake_right_id",
                "right_max": 8,
                "left_id": "fake_left_id",
                "left_max": 8,
                "left_min": 8,
                "right_description": "fake_right_description",
                "left_name": "fake_left_name",
                "protected": true,
                "left_description": "fake_left_description",
                "right_name": "fake_right_name",
                "relation_id": "fake_relation_id",
                "left_tags": [
                    "fake_left_tags"
                ],
                "right_tags": [
                    "fake_right_tags"
                ],
                "right_object_id": "fake_right_object_id",
                "left_groups": [
                    "fake_left_groups"
                ]
            }
        ],
        "protected": true,
        "relation_groups": [
            {
                "protected": true,
                "id": "fake_id",
                "name": "fake_name"
            }
        ],
        "view": {},
        "icon": "fake_icon"
    },
    "error": "",
    "codeExplain": ""
}
```
## <a id='-import_check-POST'></a> import_check POST
>import objects check<br>

### - 测试关键字
```
import request 
```
### - 接口访问URL
```
POST /object_import_check
```
### - 详细说明
>批量导入模型前校验请求的数据是否合法<br>

### - 参数


#### body 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| objectId | string | 是 | ID |  | {'gte': 1}
| name | string | 是 | 名称 |  | {'gte': 1}
| icon | string | 否 | 图标 |  | 
| category | string | 否 | 分类, 点分表示二级分类 |  | 
| memo | string | 否 | 说明 |  | 
| attrList | create_property.CreateProperty[] | 否 | 属性列表 |  | 
| relation_groups | relation_group.RelationGroup[] | 否 | 关系分组列表 |  | 
| relation_list | create_relation.CreateRelation[] | 否 | 关系列表 |  | 

CreateProperty-创建属性的message

|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| id | string | 是 | 属性ID: 对已有模型添加新的属性ID需要加下划线开头避免冲突 |  | {'gte': 1}
| name | string | 是 | 属性名称 |  | {'gte': 1}
| unique | string | 否 | 是否唯一: 历史遗留原因不是布尔值定义 | false | []
| readonly | string | 否 | 是否只读: 历史遗留原因不是布尔值定义 | false | []
| required | string | 否 | 是否必填: 历史遗留原因不是布尔值定义 | false | []
| tag | string[] | 否 | 属性分类 |  | 
| description | string | 否 | 似乎没有什么作用的描述 |  | 
| tips | string | 否 | 似乎没有什么作用的提示 |  | 
| value | property_value.PropertyValue | 是 | 属性值类型定义 |  | {'gte': 1}
PropertyValue-

|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| type | enum | 否 | 数据类型 |  | 
| regex | value | 否 | type是enum时是枚举值数组, struct和structs没有regex, 其他的type时是正则表达式 |  | 
| default_type | string | 否 | 默认值类型( value: 具体的值, function:可执行函数, auto-increment-id:自增ID, series-number:定长序列号) |  | 
| default | value | 否 | 默认值 |  | 
| struct_define | struct_define.StructDefine[] | 否 | 结构体字段定义: 当type 为 struct 和 structs 时候为必填 |  | 
| mode | string | 否 | 字符串模式定义: 多行文本和普通字符串 |  | 
| prefix | string | 否 | 自增ID和流水号的前缀: 当default_type 是series-number和 auto-increment-id时候为必填 |  | 
| start_value | int | 否 | 自增ID和流水号的起始值 |  | 
| series_number_length | int | 否 | 流水号的固定长度 |  | 
StructDefine-

|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| id | string | 否 | 结构体字段ID |  | 
| name | string | 否 | 结构体字段名称 |  | 
| type | enum | 否 | 数据类型 |  | 
| regex | string[] | 否 | 仅仅在type是enum时有值，并且是字符串数组 |  | 
| protected | bool | 否 | 是否是内置属性: 核心定义的内置属性默认都是核心属性, 核心属性不允许被删除、不允许修改约束 |  | 
RelationGroup-

|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| id | string | 是 | ID |  | {'pattern': '^[0-9a-zA-Z_]{1,32}$'}
| name | string | 是 | 名称 |  | []
| protected | bool | 否 | 是否是内置关系分组，内置的关系分组不允许删除 |  | 
CreateRelation-

|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| name | string | 否 | 不是必填, 而且在引入了left_description和 right_description 之后这个字段几乎处于废弃状态 |  | 
| left_object_id | string | 是 | 关系左端的模型ID |  | []
| left_id | string | 是 | 关系左端模型中表达右端模型实例的别名字段: 比如应用的负责人需要在应用的实例中表达出一个字段; 对已有模型添加关系时这个ID需要加下划线前缀避免冲突 |  | {'pattern': '^[a-zA-Z][0-9a-zA-Z_]{0,31}$'}
| left_description | string | 是 | 是与left_id 相反的含义, 但仅用于前端展示 |  | []
| left_min | int | 否 | 关系左端的资源模型实例至少包含多少数量的关系: 目前来说这个字段是过度设计的字段, 一般填0就好了 | 0 | {'gte': 0}
| left_max | int | 否 | 关系左端的资源模型实例最多包含多少数量的关系: 有数据库级别的索引支持, 一般情况填1 或者 -1, -1表示无限多 | -1 | []
| left_groups | string[] | 否 | 关系在左端模型的哪些分组里 |  | 
| left_tags | string[] | 否 |  |  | 
| right_object_id | string | 是 | 关系右端的模型ID |  | []
| right_id | string | 是 | 关系右端模型中表达左端模型实例的别名字段: 比如应用的负责人需要在应用的实例中表达出一个字段; 对已有模型添加关系时这个ID需要加下划线前缀避免冲突 |  | {'pattern': '^[a-zA-Z][0-9a-zA-Z_]{0,31}$'}
| right_description | string | 是 | 是与right_id 相反的含义, 但仅用于前端展示 |  | []
| right_min | int | 否 | 关系右端的资源模型实例至少包含多少数量的关系: 目前来说这个字段是过度设计的字段, 一般填0就好了 | 0 | {'gte': 0}
| right_max | int | 否 | 关系右端的资源模型实例最多包含多少数量的关系: 有数据库级别的索引支持, 一般情况填1 或者 -1, -1表示无限多 | -1 | []
| right_groups | string[] | 否 | 关系在右端模型的哪些分组里 |  | 
| right_tags | string[] | 否 |  |  | 


### - 返回码
|返回码|备注|
|---|---|
| 0 | success

### - 请求示例
```json
[
    {
        "category": "fake_category",
        "attrList": [
            {
                "name": "fake_name",
                "required": "fake_required",
                "value": {
                    "struct_define": [
                        {
                            "regex": [
                                "fake_regex"
                            ],
                            "protected": true,
                            "type": "int",
                            "id": "fake_id",
                            "name": "fake_name"
                        }
                    ],
                    "series_number_length": 8,
                    "default_type": "fake_default_type",
                    "prefix": "fake_prefix",
                    "mode": "fake_mode",
                    "start_value": 8,
                    "type": "int"
                },
                "readonly": "fake_readonly",
                "tag": [
                    "fake_tag"
                ],
                "tips": "fake_tips",
                "unique": "fake_unique",
                "id": "fake_id",
                "description": "fake_description"
            }
        ],
        "name": "fake_name",
        "objectId": "fake_objectId",
        "memo": "fake_memo",
        "relation_list": [
            {
                "right_groups": [
                    "fake_right_groups"
                ],
                "right_min": 8,
                "left_object_id": "fake_left_object_id",
                "name": "fake_name",
                "right_id": "fake_right_id",
                "right_max": 8,
                "left_id": "fake_left_id",
                "left_max": 8,
                "right_description": "fake_right_description",
                "left_min": 8,
                "right_object_id": "fake_right_object_id",
                "left_description": "fake_left_description",
                "left_tags": [
                    "fake_left_tags"
                ],
                "right_tags": [
                    "fake_right_tags"
                ],
                "left_groups": [
                    "fake_left_groups"
                ]
            }
        ],
        "relation_groups": [
            {
                "protected": true,
                "id": "fake_id",
                "name": "fake_name"
            }
        ],
        "icon": "fake_icon"
    }
]
```

### - 返回示例
```json
{
    "message": "\u90e8\u5206\u8d44\u6e90\u6a21\u578b\u5bfc\u5165\u5931\u8d25",
    "code": 133124,
    "data": {
        "APP": {
            "cannot_created_references": [
                {
                    "id": "cpu",
                    "value": {
                        "type": "FK",
                        "external": [
                            {
                                "org_attr": "name",
                                "name": "\u540d\u79f0"
                            }
                        ],
                        "rule": {
                            "obj": "HOST_CPU",
                            "mode": "inner"
                        }
                    },
                    "name": "CPU\u4fe1\u606f"
                }
            ],
            "id_is_duplicated": true,
            "cannot_created_relations": [
                {
                    "left_id": "clusters",
                    "right_id": "app",
                    "relation_id": "APP_cluster_CLUSTER"
                }
            ],
            "duplicated_relations": [
                {
                    "left_id": "clusters",
                    "right_id": "app",
                    "relation_id": "APP_cluster_CLUSTER"
                }
            ],
            "name_is_duplicated": true
        }
    },
    "error": "\u90e8\u5206\u8d44\u6e90\u6a21\u578b\u5bfc\u5165\u5931\u8d25"
}
```
## <a id='-get_relation-GET'></a> get_relation GET
>获取单个模型关系<br>

### - 测试关键字
```
get relation request 
```
### - 接口访问URL
```
GET /object_relation/:relation_id
```
### - 参数
#### URI 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| relation_id | string | 是 | 关系ID |  | []



### - 返回值说明
|名称|类型|备注|
|---|---|---|
| relation_id | string | 必须全局唯一: 新添加的关系ID字段建议增加下划线前缀
| name | string | 不是必填, 而且在引入了left_description和 right_description 之后这个字段几乎处于废弃状态
| protected | bool | 
| left_object_id | string | 关系左端的模型ID
| left_id | string | 关系左端模型中表达右端模型实例的别名字段: 比如应用的负责人需要在应用的实例中表达出一个字段; 对已有模型添加关系时这个ID需要加下划线前缀避免冲突
| left_description | string | 是与left_id 相反的含义, 但仅用于前端展示
| left_name | string | 是与left_id 对应的含义, 但仅用于前端展示
| left_min | int | 关系左端的资源模型实例至少包含多少数量的关系: 目前来说这个字段是过度设计的字段, 一般填0就好了
| left_max | int | 关系左端的资源模型实例最多包含多少数量的关系: 有数据库级别的索引支持, 一般情况填1 或者 -1, -1表示无限多
| left_groups | string[] | 关系在左端模型的哪些分组里
| left_tags | string[] | 
| right_object_id | string | 关系右端的模型ID
| right_id | string | 关系右端模型中表达左端模型实例的别名字段: 比如应用的负责人需要在应用的实例中表达出一个字段; 对已有模型添加关系时这个ID需要加下划线前缀避免冲突
| right_description | string | 是与right_id 相反的含义, 但仅用于前端展示
| right_name | string | 是与right_id 对应的含义, 但仅用于前端展示
| right_min | int | 关系右端的资源模型实例至少包含多少数量的关系: 目前来说这个字段是过度设计的字段, 一般填0就好了
| right_max | int | 关系右端的资源模型实例最多包含多少数量的关系: 有数据库级别的索引支持, 一般情况填1 或者 -1, -1表示无限多
| right_groups | string[] | 关系在右端模型的哪些分组里
| right_tags | string[] | 


### - 返回码
|返回码|备注|
|---|---|
| 0 | success


### - 返回示例
```json
{
    "code": 0,
    "data": {
        "right_groups": [
            "fake_right_groups"
        ],
        "right_min": 8,
        "left_object_id": "fake_left_object_id",
        "name": "fake_name",
        "right_id": "fake_right_id",
        "right_max": 8,
        "left_id": "fake_left_id",
        "left_max": 8,
        "left_min": 8,
        "right_description": "fake_right_description",
        "left_name": "fake_left_name",
        "protected": true,
        "left_description": "fake_left_description",
        "right_name": "fake_right_name",
        "relation_id": "fake_relation_id",
        "left_tags": [
            "fake_left_tags"
        ],
        "right_tags": [
            "fake_right_tags"
        ],
        "right_object_id": "fake_right_object_id",
        "left_groups": [
            "fake_left_groups"
        ]
    },
    "error": "",
    "codeExplain": ""
}
```
## <a id='-create_property-POST'></a> create_property POST
>创建模型属性<br>

### - 测试关键字
```
create property request 
```
### - 接口访问URL
```
POST /object/:object_id/attr
```
### - 参数
#### URI 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| object_id | string | 是 |  |  | {'gte': 1}


#### body 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| id | string | 是 | 属性ID: 对已有模型添加新的属性ID需要加下划线开头避免冲突 |  | {'gte': 1}
| name | string | 是 | 属性名称 |  | {'gte': 1}
| unique | string | 否 | 是否唯一: 历史遗留原因不是布尔值定义 | false | []
| readonly | string | 否 | 是否只读: 历史遗留原因不是布尔值定义 | false | []
| required | string | 否 | 是否必填: 历史遗留原因不是布尔值定义 | false | []
| tag | string[] | 否 | 属性分类 |  | 
| description | string | 否 | 似乎没有什么作用的描述 |  | 
| tips | string | 否 | 似乎没有什么作用的提示 |  | 
| value | property_value.PropertyValue | 是 | 属性值类型定义 |  | {'gte': 1}

PropertyValue-

|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| type | enum | 否 | 数据类型 |  | 
| regex | value | 否 | type是enum时是枚举值数组, struct和structs没有regex, 其他的type时是正则表达式 |  | 
| default_type | string | 否 | 默认值类型( value: 具体的值, function:可执行函数, auto-increment-id:自增ID, series-number:定长序列号) |  | 
| default | value | 否 | 默认值 |  | 
| struct_define | struct_define.StructDefine[] | 否 | 结构体字段定义: 当type 为 struct 和 structs 时候为必填 |  | 
| mode | string | 否 | 字符串模式定义: 多行文本和普通字符串 |  | 
| prefix | string | 否 | 自增ID和流水号的前缀: 当default_type 是series-number和 auto-increment-id时候为必填 |  | 
| start_value | int | 否 | 自增ID和流水号的起始值 |  | 
| series_number_length | int | 否 | 流水号的固定长度 |  | 
StructDefine-

|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| id | string | 否 | 结构体字段ID |  | 
| name | string | 否 | 结构体字段名称 |  | 
| type | enum | 否 | 数据类型 |  | 
| regex | string[] | 否 | 仅仅在type是enum时有值，并且是字符串数组 |  | 
| protected | bool | 否 | 是否是内置属性: 核心定义的内置属性默认都是核心属性, 核心属性不允许被删除、不允许修改约束 |  | 

### - 返回值说明
|名称|类型|备注|
|---|---|---|
| objectId | string | ID
| name | string | 名称
| icon | string | 图标
| category | string | 分类, 点分表示二级分类
| memo | string | 说明
| protected | bool | true代表是核心模型，是受保护的模型，不允许被删除
| view | map | 模型的视图设置
| attrList | property.Property[] | 属性列表
| relation_groups | relation_group.RelationGroup[] | 关系分组定义
| relation_list | relation.Relation[] | 关系列表
| updateAuthorizers | string[] | 编辑权限白名单
| deleteAuthorizers | string[] | 删除权限白名单


Property-

|名称|类型|备注|
|---|---|---|
| id | string | 属性ID: 对已有模型添加新的属性ID需要加下划线开头避免冲突
| name | string | 属性名称
| protected | bool | 是否是内置属性: 核心定义的内置属性默认都是核心属性, 核心属性不允许被删除、不允许修改约束
| custom | string | 是否是自定义字段: 历史遗留原因不是布尔值定义, 待废弃, 与protected字段含义重复, 优先使用protected字段
| unique | string | 是否唯一: 历史遗留原因不是布尔值定义
| readonly | string | 是否只读: 历史遗留原因不是布尔值定义
| required | string | 是否必填: 历史遗留原因不是布尔值定义
| tag | string[] | 属性分类
| description | string | 似乎没有什么作用的描述
| tips | string | 似乎没有什么作用的提示
| value | property_value.PropertyValue | 属性值类型定义

PropertyValue-

|名称|类型|备注|
|---|---|---|
| type | enum | 数据类型
| regex | value | type是enum时是枚举值数组, struct和structs没有regex, 其他的type时是正则表达式
| default_type | string | 默认值类型( value: 具体的值, function:可执行函数, auto-increment-id:自增ID, series-number:定长序列号)
| default | value | 默认值
| struct_define | struct_define.StructDefine[] | 结构体字段定义: 当type 为 struct 和 structs 时候为必填
| mode | string | 字符串模式定义: 多行文本和普通字符串
| prefix | string | 自增ID和流水号的前缀: 当default_type 是series-number和 auto-increment-id时候为必填
| start_value | int | 自增ID和流水号的起始值
| series_number_length | int | 流水号的固定长度

StructDefine-

|名称|类型|备注|
|---|---|---|
| id | string | 结构体字段ID
| name | string | 结构体字段名称
| type | enum | 数据类型
| regex | string[] | 仅仅在type是enum时有值，并且是字符串数组
| protected | bool | 是否是内置属性: 核心定义的内置属性默认都是核心属性, 核心属性不允许被删除、不允许修改约束

RelationGroup-

|名称|类型|备注|
|---|---|---|
| id | string | ID
| name | string | 名称
| protected | bool | 是否是内置关系分组，内置的关系分组不允许删除

Relation-

|名称|类型|备注|
|---|---|---|
| relation_id | string | 必须全局唯一: 新添加的关系ID字段建议增加下划线前缀
| name | string | 不是必填, 而且在引入了left_description和 right_description 之后这个字段几乎处于废弃状态
| protected | bool | 
| left_object_id | string | 关系左端的模型ID
| left_id | string | 关系左端模型中表达右端模型实例的别名字段: 比如应用的负责人需要在应用的实例中表达出一个字段; 对已有模型添加关系时这个ID需要加下划线前缀避免冲突
| left_description | string | 是与left_id 相反的含义, 但仅用于前端展示
| left_name | string | 是与left_id 对应的含义, 但仅用于前端展示
| left_min | int | 关系左端的资源模型实例至少包含多少数量的关系: 目前来说这个字段是过度设计的字段, 一般填0就好了
| left_max | int | 关系左端的资源模型实例最多包含多少数量的关系: 有数据库级别的索引支持, 一般情况填1 或者 -1, -1表示无限多
| left_groups | string[] | 关系在左端模型的哪些分组里
| left_tags | string[] | 
| right_object_id | string | 关系右端的模型ID
| right_id | string | 关系右端模型中表达左端模型实例的别名字段: 比如应用的负责人需要在应用的实例中表达出一个字段; 对已有模型添加关系时这个ID需要加下划线前缀避免冲突
| right_description | string | 是与right_id 相反的含义, 但仅用于前端展示
| right_name | string | 是与right_id 对应的含义, 但仅用于前端展示
| right_min | int | 关系右端的资源模型实例至少包含多少数量的关系: 目前来说这个字段是过度设计的字段, 一般填0就好了
| right_max | int | 关系右端的资源模型实例最多包含多少数量的关系: 有数据库级别的索引支持, 一般情况填1 或者 -1, -1表示无限多
| right_groups | string[] | 关系在右端模型的哪些分组里
| right_tags | string[] | 

### - 返回码
|返回码|备注|
|---|---|
| 0 | success

### - 请求示例
```json
{
    "name": "fake_name",
    "required": "fake_required",
    "value": {
        "struct_define": [
            {
                "regex": [
                    "fake_regex"
                ],
                "protected": true,
                "type": "int",
                "id": "fake_id",
                "name": "fake_name"
            }
        ],
        "series_number_length": 8,
        "default_type": "fake_default_type",
        "prefix": "fake_prefix",
        "mode": "fake_mode",
        "start_value": 8,
        "type": "int"
    },
    "readonly": "fake_readonly",
    "tag": [
        "fake_tag"
    ],
    "tips": "fake_tips",
    "unique": "fake_unique",
    "id": "fake_id",
    "description": "fake_description"
}
```

### - 返回示例
```json
{
    "code": 0,
    "data": {
        "category": "fake_category",
        "attrList": [
            {
                "name": "fake_name",
                "required": "fake_required",
                "tag": [
                    "fake_tag"
                ],
                "value": {
                    "struct_define": [
                        {
                            "regex": [
                                "fake_regex"
                            ],
                            "protected": true,
                            "type": "int",
                            "id": "fake_id",
                            "name": "fake_name"
                        }
                    ],
                    "series_number_length": 8,
                    "default_type": "fake_default_type",
                    "prefix": "fake_prefix",
                    "mode": "fake_mode",
                    "start_value": 8,
                    "type": "int"
                },
                "custom": "fake_custom",
                "readonly": "fake_readonly",
                "protected": true,
                "tips": "fake_tips",
                "unique": "fake_unique",
                "id": "fake_id",
                "description": "fake_description"
            }
        ],
        "name": "fake_name",
        "objectId": "fake_objectId",
        "memo": "fake_memo",
        "deleteAuthorizers": [
            "fake_deleteAuthorizers"
        ],
        "updateAuthorizers": [
            "fake_updateAuthorizers"
        ],
        "relation_list": [
            {
                "right_groups": [
                    "fake_right_groups"
                ],
                "right_min": 8,
                "left_object_id": "fake_left_object_id",
                "name": "fake_name",
                "right_id": "fake_right_id",
                "right_max": 8,
                "left_id": "fake_left_id",
                "left_max": 8,
                "left_min": 8,
                "right_description": "fake_right_description",
                "left_name": "fake_left_name",
                "protected": true,
                "left_description": "fake_left_description",
                "right_name": "fake_right_name",
                "relation_id": "fake_relation_id",
                "left_tags": [
                    "fake_left_tags"
                ],
                "right_tags": [
                    "fake_right_tags"
                ],
                "right_object_id": "fake_right_object_id",
                "left_groups": [
                    "fake_left_groups"
                ]
            }
        ],
        "protected": true,
        "relation_groups": [
            {
                "protected": true,
                "id": "fake_id",
                "name": "fake_name"
            }
        ],
        "view": {},
        "icon": "fake_icon"
    },
    "error": "",
    "codeExplain": ""
}
```
## <a id='-create_relation_group-POST'></a> create_relation_group POST
>创建模型关系分组<br>

### - 测试关键字
```
create relation group request 
```
### - 接口访问URL
```
POST /object/:object_id/relation_group
```
### - 参数
#### URI 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| object_id | string | 是 | 资源模型ID |  | []


#### body 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| id | string | 是 | 分组ID |  | {'pattern': '^[0-9a-zA-Z_]{1,32}$'}
| name | string | 是 | 分组名称 |  | []
| relations | relation_group_relation.RelationGroupRelation[] | 否 | 分组中的关系 |  | []

RelationGroupRelation-

|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| relation_side_id | string | 否 | 表示关系的left_id或者right_id的值, 用于表示分组的关系是关系的哪一端  |  | 

### - 返回值说明
|名称|类型|备注|
|---|---|---|
| id | string | ID
| name | string | 名称
| protected | bool | 是否是内置关系分组，内置的关系分组不允许删除


### - 返回码
|返回码|备注|
|---|---|
| 0 | success

### - 请求示例
```json
{
    "id": "fake_id",
    "relations": [
        {
            "relation_side_id": "fake_relation_side_id"
        }
    ],
    "name": "fake_name"
}
```

### - 返回示例
```json
{
    "code": 0,
    "data": {
        "protected": true,
        "id": "fake_id",
        "name": "fake_name"
    },
    "error": "",
    "codeExplain": ""
}
```
## <a id='-update_relation-PUT'></a> update_relation PUT
>更新模型关系<br>

### - 测试关键字
```
update relation request 
```
### - 接口访问URL
```
PUT /object_relation/:relation_id
```
### - 参数
#### URI 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| relation_id | string | 是 | 关系ID |  | []


#### body 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| name | string | 否 | 不是必填, 而且在引入了left_description和 right_description 之后这个字段几乎处于废弃状态 |  | 
| left_description | string | 否 | 是与left_id 相反的含义, 但仅用于前端展示 |  | 
| left_groups | string[] | 否 | 关系在左端模型的哪些分组里 |  | 
| left_tags | string[] | 否 |  |  | 
| right_description | string | 否 | 是与right_id 相反的含义, 但仅用于前端展示 |  | 
| right_groups | string[] | 否 | 关系在右端模型的哪些分组里 |  | 
| right_tags | string[] | 否 |  |  | 


### - 返回值说明
|名称|类型|备注|
|---|---|---|
| relation_id | string | 必须全局唯一: 新添加的关系ID字段建议增加下划线前缀
| name | string | 不是必填, 而且在引入了left_description和 right_description 之后这个字段几乎处于废弃状态
| protected | bool | 
| left_object_id | string | 关系左端的模型ID
| left_id | string | 关系左端模型中表达右端模型实例的别名字段: 比如应用的负责人需要在应用的实例中表达出一个字段; 对已有模型添加关系时这个ID需要加下划线前缀避免冲突
| left_description | string | 是与left_id 相反的含义, 但仅用于前端展示
| left_name | string | 是与left_id 对应的含义, 但仅用于前端展示
| left_min | int | 关系左端的资源模型实例至少包含多少数量的关系: 目前来说这个字段是过度设计的字段, 一般填0就好了
| left_max | int | 关系左端的资源模型实例最多包含多少数量的关系: 有数据库级别的索引支持, 一般情况填1 或者 -1, -1表示无限多
| left_groups | string[] | 关系在左端模型的哪些分组里
| left_tags | string[] | 
| right_object_id | string | 关系右端的模型ID
| right_id | string | 关系右端模型中表达左端模型实例的别名字段: 比如应用的负责人需要在应用的实例中表达出一个字段; 对已有模型添加关系时这个ID需要加下划线前缀避免冲突
| right_description | string | 是与right_id 相反的含义, 但仅用于前端展示
| right_name | string | 是与right_id 对应的含义, 但仅用于前端展示
| right_min | int | 关系右端的资源模型实例至少包含多少数量的关系: 目前来说这个字段是过度设计的字段, 一般填0就好了
| right_max | int | 关系右端的资源模型实例最多包含多少数量的关系: 有数据库级别的索引支持, 一般情况填1 或者 -1, -1表示无限多
| right_groups | string[] | 关系在右端模型的哪些分组里
| right_tags | string[] | 


### - 返回码
|返回码|备注|
|---|---|
| 0 | success

### - 请求示例
```json
{
    "right_groups": [
        "fake_right_groups"
    ],
    "name": "fake_name",
    "right_description": "fake_right_description",
    "left_description": "fake_left_description",
    "left_tags": [
        "fake_left_tags"
    ],
    "right_tags": [
        "fake_right_tags"
    ],
    "left_groups": [
        "fake_left_groups"
    ]
}
```

### - 返回示例
```json
{
    "code": 0,
    "data": {
        "right_groups": [
            "fake_right_groups"
        ],
        "right_min": 8,
        "left_object_id": "fake_left_object_id",
        "name": "fake_name",
        "right_id": "fake_right_id",
        "right_max": 8,
        "left_id": "fake_left_id",
        "left_max": 8,
        "left_min": 8,
        "right_description": "fake_right_description",
        "left_name": "fake_left_name",
        "protected": true,
        "left_description": "fake_left_description",
        "right_name": "fake_right_name",
        "relation_id": "fake_relation_id",
        "left_tags": [
            "fake_left_tags"
        ],
        "right_tags": [
            "fake_right_tags"
        ],
        "right_object_id": "fake_right_object_id",
        "left_groups": [
            "fake_left_groups"
        ]
    },
    "error": "",
    "codeExplain": ""
}
```
## <a id='-delete_relation_group-DELETE'></a> delete_relation_group DELETE
>删除模型关系分组<br>

### - 测试关键字
```
delete relation group request 
```
### - 接口访问URL
```
DELETE /object/:object_id/relation_group/:id
```
### - 参数
#### URI 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| object_id | string | 是 | 资源模型ID |  | []
| id | string | 是 | 分组ID |  | []




### - 返回码
|返回码|备注|
|---|---|
| 0 | success


## <a id='-import-POST'></a> import POST
>批量导入模型<br>

### - 测试关键字
```
import request 
```
### - 接口访问URL
```
POST /object_import
```
### - 详细说明
>批量导入模型<br>

### - 参数


#### body 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| objectId | string | 是 | ID |  | {'gte': 1}
| name | string | 是 | 名称 |  | {'gte': 1}
| icon | string | 否 | 图标 |  | 
| category | string | 否 | 分类, 点分表示二级分类 |  | 
| memo | string | 否 | 说明 |  | 
| attrList | create_property.CreateProperty[] | 否 | 属性列表 |  | 
| relation_groups | relation_group.RelationGroup[] | 否 | 关系分组列表 |  | 
| relation_list | create_relation.CreateRelation[] | 否 | 关系列表 |  | 

CreateProperty-创建属性的message

|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| id | string | 是 | 属性ID: 对已有模型添加新的属性ID需要加下划线开头避免冲突 |  | {'gte': 1}
| name | string | 是 | 属性名称 |  | {'gte': 1}
| unique | string | 否 | 是否唯一: 历史遗留原因不是布尔值定义 | false | []
| readonly | string | 否 | 是否只读: 历史遗留原因不是布尔值定义 | false | []
| required | string | 否 | 是否必填: 历史遗留原因不是布尔值定义 | false | []
| tag | string[] | 否 | 属性分类 |  | 
| description | string | 否 | 似乎没有什么作用的描述 |  | 
| tips | string | 否 | 似乎没有什么作用的提示 |  | 
| value | property_value.PropertyValue | 是 | 属性值类型定义 |  | {'gte': 1}
PropertyValue-

|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| type | enum | 否 | 数据类型 |  | 
| regex | value | 否 | type是enum时是枚举值数组, struct和structs没有regex, 其他的type时是正则表达式 |  | 
| default_type | string | 否 | 默认值类型( value: 具体的值, function:可执行函数, auto-increment-id:自增ID, series-number:定长序列号) |  | 
| default | value | 否 | 默认值 |  | 
| struct_define | struct_define.StructDefine[] | 否 | 结构体字段定义: 当type 为 struct 和 structs 时候为必填 |  | 
| mode | string | 否 | 字符串模式定义: 多行文本和普通字符串 |  | 
| prefix | string | 否 | 自增ID和流水号的前缀: 当default_type 是series-number和 auto-increment-id时候为必填 |  | 
| start_value | int | 否 | 自增ID和流水号的起始值 |  | 
| series_number_length | int | 否 | 流水号的固定长度 |  | 
StructDefine-

|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| id | string | 否 | 结构体字段ID |  | 
| name | string | 否 | 结构体字段名称 |  | 
| type | enum | 否 | 数据类型 |  | 
| regex | string[] | 否 | 仅仅在type是enum时有值，并且是字符串数组 |  | 
| protected | bool | 否 | 是否是内置属性: 核心定义的内置属性默认都是核心属性, 核心属性不允许被删除、不允许修改约束 |  | 
RelationGroup-

|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| id | string | 是 | ID |  | {'pattern': '^[0-9a-zA-Z_]{1,32}$'}
| name | string | 是 | 名称 |  | []
| protected | bool | 否 | 是否是内置关系分组，内置的关系分组不允许删除 |  | 
CreateRelation-

|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| name | string | 否 | 不是必填, 而且在引入了left_description和 right_description 之后这个字段几乎处于废弃状态 |  | 
| left_object_id | string | 是 | 关系左端的模型ID |  | []
| left_id | string | 是 | 关系左端模型中表达右端模型实例的别名字段: 比如应用的负责人需要在应用的实例中表达出一个字段; 对已有模型添加关系时这个ID需要加下划线前缀避免冲突 |  | {'pattern': '^[a-zA-Z][0-9a-zA-Z_]{0,31}$'}
| left_description | string | 是 | 是与left_id 相反的含义, 但仅用于前端展示 |  | []
| left_min | int | 否 | 关系左端的资源模型实例至少包含多少数量的关系: 目前来说这个字段是过度设计的字段, 一般填0就好了 | 0 | {'gte': 0}
| left_max | int | 否 | 关系左端的资源模型实例最多包含多少数量的关系: 有数据库级别的索引支持, 一般情况填1 或者 -1, -1表示无限多 | -1 | []
| left_groups | string[] | 否 | 关系在左端模型的哪些分组里 |  | 
| left_tags | string[] | 否 |  |  | 
| right_object_id | string | 是 | 关系右端的模型ID |  | []
| right_id | string | 是 | 关系右端模型中表达左端模型实例的别名字段: 比如应用的负责人需要在应用的实例中表达出一个字段; 对已有模型添加关系时这个ID需要加下划线前缀避免冲突 |  | {'pattern': '^[a-zA-Z][0-9a-zA-Z_]{0,31}$'}
| right_description | string | 是 | 是与right_id 相反的含义, 但仅用于前端展示 |  | []
| right_min | int | 否 | 关系右端的资源模型实例至少包含多少数量的关系: 目前来说这个字段是过度设计的字段, 一般填0就好了 | 0 | {'gte': 0}
| right_max | int | 否 | 关系右端的资源模型实例最多包含多少数量的关系: 有数据库级别的索引支持, 一般情况填1 或者 -1, -1表示无限多 | -1 | []
| right_groups | string[] | 否 | 关系在右端模型的哪些分组里 |  | 
| right_tags | string[] | 否 |  |  | 


### - 返回码
|返回码|备注|
|---|---|
| 0 | success

### - 请求示例
```json
[
    {
        "category": "fake_category",
        "attrList": [
            {
                "name": "fake_name",
                "required": "fake_required",
                "value": {
                    "struct_define": [
                        {
                            "regex": [
                                "fake_regex"
                            ],
                            "protected": true,
                            "type": "int",
                            "id": "fake_id",
                            "name": "fake_name"
                        }
                    ],
                    "series_number_length": 8,
                    "default_type": "fake_default_type",
                    "prefix": "fake_prefix",
                    "mode": "fake_mode",
                    "start_value": 8,
                    "type": "int"
                },
                "readonly": "fake_readonly",
                "tag": [
                    "fake_tag"
                ],
                "tips": "fake_tips",
                "unique": "fake_unique",
                "id": "fake_id",
                "description": "fake_description"
            }
        ],
        "name": "fake_name",
        "objectId": "fake_objectId",
        "memo": "fake_memo",
        "relation_list": [
            {
                "right_groups": [
                    "fake_right_groups"
                ],
                "right_min": 8,
                "left_object_id": "fake_left_object_id",
                "name": "fake_name",
                "right_id": "fake_right_id",
                "right_max": 8,
                "left_id": "fake_left_id",
                "left_max": 8,
                "right_description": "fake_right_description",
                "left_min": 8,
                "right_object_id": "fake_right_object_id",
                "left_description": "fake_left_description",
                "left_tags": [
                    "fake_left_tags"
                ],
                "right_tags": [
                    "fake_right_tags"
                ],
                "left_groups": [
                    "fake_left_groups"
                ]
            }
        ],
        "relation_groups": [
            {
                "protected": true,
                "id": "fake_id",
                "name": "fake_name"
            }
        ],
        "icon": "fake_icon"
    }
]
```

### - 返回示例
```json
{
    "message": "\u90e8\u5206\u8d44\u6e90\u6a21\u578b\u5bfc\u5165\u5931\u8d25",
    "code": 133124,
    "data": [
        {
            "attrList": [
                {
                    "code": 0,
                    "id": "name",
                    "name": "\u540d\u79f0"
                }
            ],
            "relation_list": [
                {
                    "left_name": "left_name",
                    "code": 0,
                    "left_description": "left_description",
                    "right_name": "right_name",
                    "relation_id": "APP_business",
                    "right_description": "right_description"
                },
                {
                    "left_name": "left_name",
                    "code": 130500,
                    "left_description": "left_description",
                    "right_name": "right_name",
                    "error": "\u53c2\u6570\u683c\u5f0f\u9519\u8bef",
                    "right_description": "right_description",
                    "relation_id": "APP_user"
                }
            ],
            "code": 130500,
            "name": "\u5e94\u7528",
            "objectId": "APP",
            "error": "\u53c2\u6570\u683c\u5f0f\u9519\u8bef"
        }
    ],
    "error": "\u90e8\u5206\u8d44\u6e90\u6a21\u578b\u5bfc\u5165\u5931\u8d25"
}
```
## <a id='-get_property-GET'></a> get_property GET
>获取模型属性<br>

### - 测试关键字
```
get property request 
```
### - 接口访问URL
```
GET /object/:object_id/attr/:attr_id
```
### - 参数
#### URI 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| object_id | string | 是 |  |  | {'gte': 1}
| attr_id | string | 是 |  |  | {'gte': 1}



### - 返回值说明
|名称|类型|备注|
|---|---|---|
| id | string | 属性ID: 对已有模型添加新的属性ID需要加下划线开头避免冲突
| name | string | 属性名称
| protected | bool | 是否是内置属性: 核心定义的内置属性默认都是核心属性, 核心属性不允许被删除、不允许修改约束
| custom | string | 是否是自定义字段: 历史遗留原因不是布尔值定义, 待废弃, 与protected字段含义重复, 优先使用protected字段
| unique | string | 是否唯一: 历史遗留原因不是布尔值定义
| readonly | string | 是否只读: 历史遗留原因不是布尔值定义
| required | string | 是否必填: 历史遗留原因不是布尔值定义
| tag | string[] | 属性分类
| description | string | 似乎没有什么作用的描述
| tips | string | 似乎没有什么作用的提示
| value | property_value.PropertyValue | 属性值类型定义


PropertyValue-

|名称|类型|备注|
|---|---|---|
| type | enum | 数据类型
| regex | value | type是enum时是枚举值数组, struct和structs没有regex, 其他的type时是正则表达式
| default_type | string | 默认值类型( value: 具体的值, function:可执行函数, auto-increment-id:自增ID, series-number:定长序列号)
| default | value | 默认值
| struct_define | struct_define.StructDefine[] | 结构体字段定义: 当type 为 struct 和 structs 时候为必填
| mode | string | 字符串模式定义: 多行文本和普通字符串
| prefix | string | 自增ID和流水号的前缀: 当default_type 是series-number和 auto-increment-id时候为必填
| start_value | int | 自增ID和流水号的起始值
| series_number_length | int | 流水号的固定长度

StructDefine-

|名称|类型|备注|
|---|---|---|
| id | string | 结构体字段ID
| name | string | 结构体字段名称
| type | enum | 数据类型
| regex | string[] | 仅仅在type是enum时有值，并且是字符串数组
| protected | bool | 是否是内置属性: 核心定义的内置属性默认都是核心属性, 核心属性不允许被删除、不允许修改约束

### - 返回码
|返回码|备注|
|---|---|
| 0 | success


### - 返回示例
```json
{
    "code": 0,
    "data": {
        "name": "fake_name",
        "required": "fake_required",
        "tag": [
            "fake_tag"
        ],
        "value": {
            "struct_define": [
                {
                    "regex": [
                        "fake_regex"
                    ],
                    "protected": true,
                    "type": "int",
                    "id": "fake_id",
                    "name": "fake_name"
                }
            ],
            "series_number_length": 8,
            "default_type": "fake_default_type",
            "prefix": "fake_prefix",
            "mode": "fake_mode",
            "start_value": 8,
            "type": "int"
        },
        "custom": "fake_custom",
        "readonly": "fake_readonly",
        "protected": true,
        "tips": "fake_tips",
        "unique": "fake_unique",
        "id": "fake_id",
        "description": "fake_description"
    },
    "error": "",
    "codeExplain": ""
}
```
## <a id='-create_relation-POST'></a> create_relation POST
>创建模型关系<br>

### - 测试关键字
```
create relation request 
```
### - 接口访问URL
```
POST /object_relation
```
### - 参数


#### body 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| name | string | 否 | 不是必填, 而且在引入了left_description和 right_description 之后这个字段几乎处于废弃状态 |  | 
| left_object_id | string | 是 | 关系左端的模型ID |  | []
| left_id | string | 是 | 关系左端模型中表达右端模型实例的别名字段: 比如应用的负责人需要在应用的实例中表达出一个字段; 对已有模型添加关系时这个ID需要加下划线前缀避免冲突 |  | {'pattern': '^[a-zA-Z][0-9a-zA-Z_]{0,31}$'}
| left_description | string | 是 | 是与left_id 相反的含义, 但仅用于前端展示 |  | []
| left_min | int | 否 | 关系左端的资源模型实例至少包含多少数量的关系: 目前来说这个字段是过度设计的字段, 一般填0就好了 | 0 | {'gte': 0}
| left_max | int | 否 | 关系左端的资源模型实例最多包含多少数量的关系: 有数据库级别的索引支持, 一般情况填1 或者 -1, -1表示无限多 | -1 | []
| left_groups | string[] | 否 | 关系在左端模型的哪些分组里 |  | 
| left_tags | string[] | 否 |  |  | 
| right_object_id | string | 是 | 关系右端的模型ID |  | []
| right_id | string | 是 | 关系右端模型中表达左端模型实例的别名字段: 比如应用的负责人需要在应用的实例中表达出一个字段; 对已有模型添加关系时这个ID需要加下划线前缀避免冲突 |  | {'pattern': '^[a-zA-Z][0-9a-zA-Z_]{0,31}$'}
| right_description | string | 是 | 是与right_id 相反的含义, 但仅用于前端展示 |  | []
| right_min | int | 否 | 关系右端的资源模型实例至少包含多少数量的关系: 目前来说这个字段是过度设计的字段, 一般填0就好了 | 0 | {'gte': 0}
| right_max | int | 否 | 关系右端的资源模型实例最多包含多少数量的关系: 有数据库级别的索引支持, 一般情况填1 或者 -1, -1表示无限多 | -1 | []
| right_groups | string[] | 否 | 关系在右端模型的哪些分组里 |  | 
| right_tags | string[] | 否 |  |  | 


### - 返回值说明
|名称|类型|备注|
|---|---|---|
| relation_id | string | 必须全局唯一: 新添加的关系ID字段建议增加下划线前缀
| name | string | 不是必填, 而且在引入了left_description和 right_description 之后这个字段几乎处于废弃状态
| protected | bool | 
| left_object_id | string | 关系左端的模型ID
| left_id | string | 关系左端模型中表达右端模型实例的别名字段: 比如应用的负责人需要在应用的实例中表达出一个字段; 对已有模型添加关系时这个ID需要加下划线前缀避免冲突
| left_description | string | 是与left_id 相反的含义, 但仅用于前端展示
| left_name | string | 是与left_id 对应的含义, 但仅用于前端展示
| left_min | int | 关系左端的资源模型实例至少包含多少数量的关系: 目前来说这个字段是过度设计的字段, 一般填0就好了
| left_max | int | 关系左端的资源模型实例最多包含多少数量的关系: 有数据库级别的索引支持, 一般情况填1 或者 -1, -1表示无限多
| left_groups | string[] | 关系在左端模型的哪些分组里
| left_tags | string[] | 
| right_object_id | string | 关系右端的模型ID
| right_id | string | 关系右端模型中表达左端模型实例的别名字段: 比如应用的负责人需要在应用的实例中表达出一个字段; 对已有模型添加关系时这个ID需要加下划线前缀避免冲突
| right_description | string | 是与right_id 相反的含义, 但仅用于前端展示
| right_name | string | 是与right_id 对应的含义, 但仅用于前端展示
| right_min | int | 关系右端的资源模型实例至少包含多少数量的关系: 目前来说这个字段是过度设计的字段, 一般填0就好了
| right_max | int | 关系右端的资源模型实例最多包含多少数量的关系: 有数据库级别的索引支持, 一般情况填1 或者 -1, -1表示无限多
| right_groups | string[] | 关系在右端模型的哪些分组里
| right_tags | string[] | 


### - 返回码
|返回码|备注|
|---|---|
| 0 | success

### - 请求示例
```json
{
    "right_groups": [
        "fake_right_groups"
    ],
    "right_min": 8,
    "left_object_id": "fake_left_object_id",
    "name": "fake_name",
    "right_id": "fake_right_id",
    "right_max": 8,
    "left_id": "fake_left_id",
    "left_max": 8,
    "right_description": "fake_right_description",
    "left_min": 8,
    "right_object_id": "fake_right_object_id",
    "left_description": "fake_left_description",
    "left_tags": [
        "fake_left_tags"
    ],
    "right_tags": [
        "fake_right_tags"
    ],
    "left_groups": [
        "fake_left_groups"
    ]
}
```

### - 返回示例
```json
{
    "code": 0,
    "data": {
        "right_groups": [
            "fake_right_groups"
        ],
        "right_min": 8,
        "left_object_id": "fake_left_object_id",
        "name": "fake_name",
        "right_id": "fake_right_id",
        "right_max": 8,
        "left_id": "fake_left_id",
        "left_max": 8,
        "left_min": 8,
        "right_description": "fake_right_description",
        "left_name": "fake_left_name",
        "protected": true,
        "left_description": "fake_left_description",
        "right_name": "fake_right_name",
        "relation_id": "fake_relation_id",
        "left_tags": [
            "fake_left_tags"
        ],
        "right_tags": [
            "fake_right_tags"
        ],
        "right_object_id": "fake_right_object_id",
        "left_groups": [
            "fake_left_groups"
        ]
    },
    "error": "",
    "codeExplain": ""
}
```
## <a id='-list-list'></a> list List
>分页获取模型列表<br>

### - 测试关键字
```
list request 
```
### - 接口访问URL
```
list /object
```
### - 参数

#### query 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| page | int | 否 |  | 1 | {'gte': 1}
| page_size | int | 否 |  | 200 | {'gte': 1, 'lte': 3000}


### - 返回值说明
|名称|类型|备注|
|---|---|---|
| objectId | string | ID
| name | string | 名称
| icon | string | 图标
| category | string | 分类, 点分表示二级分类
| memo | string | 说明
| protected | bool | true代表是核心模型，是受保护的模型，不允许被删除
| view | map | 模型的视图设置
| attrList | property.Property[] | 属性列表
| relation_groups | relation_group.RelationGroup[] | 关系分组定义
| relation_list | relation.Relation[] | 关系列表
| updateAuthorizers | string[] | 编辑权限白名单
| deleteAuthorizers | string[] | 删除权限白名单


Property-

|名称|类型|备注|
|---|---|---|
| id | string | 属性ID: 对已有模型添加新的属性ID需要加下划线开头避免冲突
| name | string | 属性名称
| protected | bool | 是否是内置属性: 核心定义的内置属性默认都是核心属性, 核心属性不允许被删除、不允许修改约束
| custom | string | 是否是自定义字段: 历史遗留原因不是布尔值定义, 待废弃, 与protected字段含义重复, 优先使用protected字段
| unique | string | 是否唯一: 历史遗留原因不是布尔值定义
| readonly | string | 是否只读: 历史遗留原因不是布尔值定义
| required | string | 是否必填: 历史遗留原因不是布尔值定义
| tag | string[] | 属性分类
| description | string | 似乎没有什么作用的描述
| tips | string | 似乎没有什么作用的提示
| value | property_value.PropertyValue | 属性值类型定义

PropertyValue-

|名称|类型|备注|
|---|---|---|
| type | enum | 数据类型
| regex | value | type是enum时是枚举值数组, struct和structs没有regex, 其他的type时是正则表达式
| default_type | string | 默认值类型( value: 具体的值, function:可执行函数, auto-increment-id:自增ID, series-number:定长序列号)
| default | value | 默认值
| struct_define | struct_define.StructDefine[] | 结构体字段定义: 当type 为 struct 和 structs 时候为必填
| mode | string | 字符串模式定义: 多行文本和普通字符串
| prefix | string | 自增ID和流水号的前缀: 当default_type 是series-number和 auto-increment-id时候为必填
| start_value | int | 自增ID和流水号的起始值
| series_number_length | int | 流水号的固定长度

StructDefine-

|名称|类型|备注|
|---|---|---|
| id | string | 结构体字段ID
| name | string | 结构体字段名称
| type | enum | 数据类型
| regex | string[] | 仅仅在type是enum时有值，并且是字符串数组
| protected | bool | 是否是内置属性: 核心定义的内置属性默认都是核心属性, 核心属性不允许被删除、不允许修改约束

RelationGroup-

|名称|类型|备注|
|---|---|---|
| id | string | ID
| name | string | 名称
| protected | bool | 是否是内置关系分组，内置的关系分组不允许删除

Relation-

|名称|类型|备注|
|---|---|---|
| relation_id | string | 必须全局唯一: 新添加的关系ID字段建议增加下划线前缀
| name | string | 不是必填, 而且在引入了left_description和 right_description 之后这个字段几乎处于废弃状态
| protected | bool | 
| left_object_id | string | 关系左端的模型ID
| left_id | string | 关系左端模型中表达右端模型实例的别名字段: 比如应用的负责人需要在应用的实例中表达出一个字段; 对已有模型添加关系时这个ID需要加下划线前缀避免冲突
| left_description | string | 是与left_id 相反的含义, 但仅用于前端展示
| left_name | string | 是与left_id 对应的含义, 但仅用于前端展示
| left_min | int | 关系左端的资源模型实例至少包含多少数量的关系: 目前来说这个字段是过度设计的字段, 一般填0就好了
| left_max | int | 关系左端的资源模型实例最多包含多少数量的关系: 有数据库级别的索引支持, 一般情况填1 或者 -1, -1表示无限多
| left_groups | string[] | 关系在左端模型的哪些分组里
| left_tags | string[] | 
| right_object_id | string | 关系右端的模型ID
| right_id | string | 关系右端模型中表达左端模型实例的别名字段: 比如应用的负责人需要在应用的实例中表达出一个字段; 对已有模型添加关系时这个ID需要加下划线前缀避免冲突
| right_description | string | 是与right_id 相反的含义, 但仅用于前端展示
| right_name | string | 是与right_id 对应的含义, 但仅用于前端展示
| right_min | int | 关系右端的资源模型实例至少包含多少数量的关系: 目前来说这个字段是过度设计的字段, 一般填0就好了
| right_max | int | 关系右端的资源模型实例最多包含多少数量的关系: 有数据库级别的索引支持, 一般情况填1 或者 -1, -1表示无限多
| right_groups | string[] | 关系在右端模型的哪些分组里
| right_tags | string[] | 

### - 返回码
|返回码|备注|
|---|---|
| 0 | success


### - 返回示例
```json
{
    "code": 0,
    "data": {
        "total": 1,
        "list": [
            {
                "category": "fake_category",
                "attrList": [
                    {
                        "name": "fake_name",
                        "required": "fake_required",
                        "tag": [
                            "fake_tag"
                        ],
                        "value": {
                            "struct_define": [
                                {
                                    "regex": [
                                        "fake_regex"
                                    ],
                                    "protected": true,
                                    "type": "int",
                                    "id": "fake_id",
                                    "name": "fake_name"
                                }
                            ],
                            "series_number_length": 8,
                            "default_type": "fake_default_type",
                            "prefix": "fake_prefix",
                            "mode": "fake_mode",
                            "start_value": 8,
                            "type": "int"
                        },
                        "custom": "fake_custom",
                        "readonly": "fake_readonly",
                        "protected": true,
                        "tips": "fake_tips",
                        "unique": "fake_unique",
                        "id": "fake_id",
                        "description": "fake_description"
                    }
                ],
                "name": "fake_name",
                "objectId": "fake_objectId",
                "memo": "fake_memo",
                "deleteAuthorizers": [
                    "fake_deleteAuthorizers"
                ],
                "updateAuthorizers": [
                    "fake_updateAuthorizers"
                ],
                "relation_list": [
                    {
                        "right_groups": [
                            "fake_right_groups"
                        ],
                        "right_min": 8,
                        "left_object_id": "fake_left_object_id",
                        "name": "fake_name",
                        "right_id": "fake_right_id",
                        "right_max": 8,
                        "left_id": "fake_left_id",
                        "left_max": 8,
                        "left_min": 8,
                        "right_description": "fake_right_description",
                        "left_name": "fake_left_name",
                        "protected": true,
                        "left_description": "fake_left_description",
                        "right_name": "fake_right_name",
                        "relation_id": "fake_relation_id",
                        "left_tags": [
                            "fake_left_tags"
                        ],
                        "right_tags": [
                            "fake_right_tags"
                        ],
                        "right_object_id": "fake_right_object_id",
                        "left_groups": [
                            "fake_left_groups"
                        ]
                    }
                ],
                "protected": true,
                "relation_groups": [
                    {
                        "protected": true,
                        "id": "fake_id",
                        "name": "fake_name"
                    }
                ],
                "view": {},
                "icon": "fake_icon"
            }
        ],
        "page": 1,
        "page_size": 200
    },
    "error": "",
    "codeExplain": ""
}
```
## <a id='-create-POST'></a> create POST
>创建模型<br>

### - 测试关键字
```
create request 
```
### - 接口访问URL
```
POST /object
```
### - 参数


#### body 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| objectId | string | 是 | ID |  | {'gte': 1}
| name | string | 是 | 名称 |  | {'gte': 1}
| icon | string | 否 | 图标 |  | 
| category | string | 否 | 分类, 点分表示二级分类 |  | 
| memo | string | 否 | 说明 |  | 


### - 返回值说明
|名称|类型|备注|
|---|---|---|
| objectId | string | ID
| name | string | 名称
| icon | string | 图标
| category | string | 分类, 点分表示二级分类
| memo | string | 说明
| protected | bool | true代表是核心模型，是受保护的模型，不允许被删除
| view | map | 模型的视图设置
| attrList | property.Property[] | 属性列表
| relation_groups | relation_group.RelationGroup[] | 关系分组定义
| relation_list | relation.Relation[] | 关系列表
| updateAuthorizers | string[] | 编辑权限白名单
| deleteAuthorizers | string[] | 删除权限白名单


Property-

|名称|类型|备注|
|---|---|---|
| id | string | 属性ID: 对已有模型添加新的属性ID需要加下划线开头避免冲突
| name | string | 属性名称
| protected | bool | 是否是内置属性: 核心定义的内置属性默认都是核心属性, 核心属性不允许被删除、不允许修改约束
| custom | string | 是否是自定义字段: 历史遗留原因不是布尔值定义, 待废弃, 与protected字段含义重复, 优先使用protected字段
| unique | string | 是否唯一: 历史遗留原因不是布尔值定义
| readonly | string | 是否只读: 历史遗留原因不是布尔值定义
| required | string | 是否必填: 历史遗留原因不是布尔值定义
| tag | string[] | 属性分类
| description | string | 似乎没有什么作用的描述
| tips | string | 似乎没有什么作用的提示
| value | property_value.PropertyValue | 属性值类型定义

PropertyValue-

|名称|类型|备注|
|---|---|---|
| type | enum | 数据类型
| regex | value | type是enum时是枚举值数组, struct和structs没有regex, 其他的type时是正则表达式
| default_type | string | 默认值类型( value: 具体的值, function:可执行函数, auto-increment-id:自增ID, series-number:定长序列号)
| default | value | 默认值
| struct_define | struct_define.StructDefine[] | 结构体字段定义: 当type 为 struct 和 structs 时候为必填
| mode | string | 字符串模式定义: 多行文本和普通字符串
| prefix | string | 自增ID和流水号的前缀: 当default_type 是series-number和 auto-increment-id时候为必填
| start_value | int | 自增ID和流水号的起始值
| series_number_length | int | 流水号的固定长度

StructDefine-

|名称|类型|备注|
|---|---|---|
| id | string | 结构体字段ID
| name | string | 结构体字段名称
| type | enum | 数据类型
| regex | string[] | 仅仅在type是enum时有值，并且是字符串数组
| protected | bool | 是否是内置属性: 核心定义的内置属性默认都是核心属性, 核心属性不允许被删除、不允许修改约束

RelationGroup-

|名称|类型|备注|
|---|---|---|
| id | string | ID
| name | string | 名称
| protected | bool | 是否是内置关系分组，内置的关系分组不允许删除

Relation-

|名称|类型|备注|
|---|---|---|
| relation_id | string | 必须全局唯一: 新添加的关系ID字段建议增加下划线前缀
| name | string | 不是必填, 而且在引入了left_description和 right_description 之后这个字段几乎处于废弃状态
| protected | bool | 
| left_object_id | string | 关系左端的模型ID
| left_id | string | 关系左端模型中表达右端模型实例的别名字段: 比如应用的负责人需要在应用的实例中表达出一个字段; 对已有模型添加关系时这个ID需要加下划线前缀避免冲突
| left_description | string | 是与left_id 相反的含义, 但仅用于前端展示
| left_name | string | 是与left_id 对应的含义, 但仅用于前端展示
| left_min | int | 关系左端的资源模型实例至少包含多少数量的关系: 目前来说这个字段是过度设计的字段, 一般填0就好了
| left_max | int | 关系左端的资源模型实例最多包含多少数量的关系: 有数据库级别的索引支持, 一般情况填1 或者 -1, -1表示无限多
| left_groups | string[] | 关系在左端模型的哪些分组里
| left_tags | string[] | 
| right_object_id | string | 关系右端的模型ID
| right_id | string | 关系右端模型中表达左端模型实例的别名字段: 比如应用的负责人需要在应用的实例中表达出一个字段; 对已有模型添加关系时这个ID需要加下划线前缀避免冲突
| right_description | string | 是与right_id 相反的含义, 但仅用于前端展示
| right_name | string | 是与right_id 对应的含义, 但仅用于前端展示
| right_min | int | 关系右端的资源模型实例至少包含多少数量的关系: 目前来说这个字段是过度设计的字段, 一般填0就好了
| right_max | int | 关系右端的资源模型实例最多包含多少数量的关系: 有数据库级别的索引支持, 一般情况填1 或者 -1, -1表示无限多
| right_groups | string[] | 关系在右端模型的哪些分组里
| right_tags | string[] | 

### - 返回码
|返回码|备注|
|---|---|
| 0 | success

### - 请求示例
```json
{
    "category": "fake_category",
    "memo": "fake_memo",
    "name": "fake_name",
    "objectId": "fake_objectId",
    "icon": "fake_icon"
}
```

### - 返回示例
```json
{
    "code": 0,
    "data": {
        "category": "fake_category",
        "attrList": [
            {
                "name": "fake_name",
                "required": "fake_required",
                "tag": [
                    "fake_tag"
                ],
                "value": {
                    "struct_define": [
                        {
                            "regex": [
                                "fake_regex"
                            ],
                            "protected": true,
                            "type": "int",
                            "id": "fake_id",
                            "name": "fake_name"
                        }
                    ],
                    "series_number_length": 8,
                    "default_type": "fake_default_type",
                    "prefix": "fake_prefix",
                    "mode": "fake_mode",
                    "start_value": 8,
                    "type": "int"
                },
                "custom": "fake_custom",
                "readonly": "fake_readonly",
                "protected": true,
                "tips": "fake_tips",
                "unique": "fake_unique",
                "id": "fake_id",
                "description": "fake_description"
            }
        ],
        "name": "fake_name",
        "objectId": "fake_objectId",
        "memo": "fake_memo",
        "deleteAuthorizers": [
            "fake_deleteAuthorizers"
        ],
        "updateAuthorizers": [
            "fake_updateAuthorizers"
        ],
        "relation_list": [
            {
                "right_groups": [
                    "fake_right_groups"
                ],
                "right_min": 8,
                "left_object_id": "fake_left_object_id",
                "name": "fake_name",
                "right_id": "fake_right_id",
                "right_max": 8,
                "left_id": "fake_left_id",
                "left_max": 8,
                "left_min": 8,
                "right_description": "fake_right_description",
                "left_name": "fake_left_name",
                "protected": true,
                "left_description": "fake_left_description",
                "right_name": "fake_right_name",
                "relation_id": "fake_relation_id",
                "left_tags": [
                    "fake_left_tags"
                ],
                "right_tags": [
                    "fake_right_tags"
                ],
                "right_object_id": "fake_right_object_id",
                "left_groups": [
                    "fake_left_groups"
                ]
            }
        ],
        "protected": true,
        "relation_groups": [
            {
                "protected": true,
                "id": "fake_id",
                "name": "fake_name"
            }
        ],
        "view": {},
        "icon": "fake_icon"
    },
    "error": "",
    "codeExplain": ""
}
```
## <a id='-update_property-PUT'></a> update_property PUT
>更新模型属性<br>

### - 测试关键字
```
update property request 
```
### - 接口访问URL
```
PUT /object/:object_id/attr/:attr_id
```
### - 参数
#### URI 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| object_id | string | 是 |  |  | {'gte': 1}
| attr_id | string | 是 |  |  | {'gte': 1}


#### body 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| name | string | 否 | 属性名称 |  | 
| unique | string | 否 | 是否唯一: 历史遗留原因不是布尔值定义 |  | 
| readonly | string | 否 | 是否只读: 历史遗留原因不是布尔值定义 |  | 
| required | string | 否 | 是否必填: 历史遗留原因不是布尔值定义 |  | 
| tag | string[] | 否 | 属性分类 |  | 
| description | string | 否 | 似乎没有什么作用的描述 |  | 
| tips | string | 否 | 似乎没有什么作用的提示 |  | 
| value | property_value.PropertyValue | 否 | 属性值类型定义 |  | 

PropertyValue-

|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| type | enum | 否 | 数据类型 |  | 
| regex | value | 否 | type是enum时是枚举值数组, struct和structs没有regex, 其他的type时是正则表达式 |  | 
| default_type | string | 否 | 默认值类型( value: 具体的值, function:可执行函数, auto-increment-id:自增ID, series-number:定长序列号) |  | 
| default | value | 否 | 默认值 |  | 
| struct_define | struct_define.StructDefine[] | 否 | 结构体字段定义: 当type 为 struct 和 structs 时候为必填 |  | 
| mode | string | 否 | 字符串模式定义: 多行文本和普通字符串 |  | 
| prefix | string | 否 | 自增ID和流水号的前缀: 当default_type 是series-number和 auto-increment-id时候为必填 |  | 
| start_value | int | 否 | 自增ID和流水号的起始值 |  | 
| series_number_length | int | 否 | 流水号的固定长度 |  | 
StructDefine-

|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| id | string | 否 | 结构体字段ID |  | 
| name | string | 否 | 结构体字段名称 |  | 
| type | enum | 否 | 数据类型 |  | 
| regex | string[] | 否 | 仅仅在type是enum时有值，并且是字符串数组 |  | 
| protected | bool | 否 | 是否是内置属性: 核心定义的内置属性默认都是核心属性, 核心属性不允许被删除、不允许修改约束 |  | 

### - 返回值说明
|名称|类型|备注|
|---|---|---|
| objectId | string | ID
| name | string | 名称
| icon | string | 图标
| category | string | 分类, 点分表示二级分类
| memo | string | 说明
| protected | bool | true代表是核心模型，是受保护的模型，不允许被删除
| view | map | 模型的视图设置
| attrList | property.Property[] | 属性列表
| relation_groups | relation_group.RelationGroup[] | 关系分组定义
| relation_list | relation.Relation[] | 关系列表
| updateAuthorizers | string[] | 编辑权限白名单
| deleteAuthorizers | string[] | 删除权限白名单


Property-

|名称|类型|备注|
|---|---|---|
| id | string | 属性ID: 对已有模型添加新的属性ID需要加下划线开头避免冲突
| name | string | 属性名称
| protected | bool | 是否是内置属性: 核心定义的内置属性默认都是核心属性, 核心属性不允许被删除、不允许修改约束
| custom | string | 是否是自定义字段: 历史遗留原因不是布尔值定义, 待废弃, 与protected字段含义重复, 优先使用protected字段
| unique | string | 是否唯一: 历史遗留原因不是布尔值定义
| readonly | string | 是否只读: 历史遗留原因不是布尔值定义
| required | string | 是否必填: 历史遗留原因不是布尔值定义
| tag | string[] | 属性分类
| description | string | 似乎没有什么作用的描述
| tips | string | 似乎没有什么作用的提示
| value | property_value.PropertyValue | 属性值类型定义

PropertyValue-

|名称|类型|备注|
|---|---|---|
| type | enum | 数据类型
| regex | value | type是enum时是枚举值数组, struct和structs没有regex, 其他的type时是正则表达式
| default_type | string | 默认值类型( value: 具体的值, function:可执行函数, auto-increment-id:自增ID, series-number:定长序列号)
| default | value | 默认值
| struct_define | struct_define.StructDefine[] | 结构体字段定义: 当type 为 struct 和 structs 时候为必填
| mode | string | 字符串模式定义: 多行文本和普通字符串
| prefix | string | 自增ID和流水号的前缀: 当default_type 是series-number和 auto-increment-id时候为必填
| start_value | int | 自增ID和流水号的起始值
| series_number_length | int | 流水号的固定长度

StructDefine-

|名称|类型|备注|
|---|---|---|
| id | string | 结构体字段ID
| name | string | 结构体字段名称
| type | enum | 数据类型
| regex | string[] | 仅仅在type是enum时有值，并且是字符串数组
| protected | bool | 是否是内置属性: 核心定义的内置属性默认都是核心属性, 核心属性不允许被删除、不允许修改约束

RelationGroup-

|名称|类型|备注|
|---|---|---|
| id | string | ID
| name | string | 名称
| protected | bool | 是否是内置关系分组，内置的关系分组不允许删除

Relation-

|名称|类型|备注|
|---|---|---|
| relation_id | string | 必须全局唯一: 新添加的关系ID字段建议增加下划线前缀
| name | string | 不是必填, 而且在引入了left_description和 right_description 之后这个字段几乎处于废弃状态
| protected | bool | 
| left_object_id | string | 关系左端的模型ID
| left_id | string | 关系左端模型中表达右端模型实例的别名字段: 比如应用的负责人需要在应用的实例中表达出一个字段; 对已有模型添加关系时这个ID需要加下划线前缀避免冲突
| left_description | string | 是与left_id 相反的含义, 但仅用于前端展示
| left_name | string | 是与left_id 对应的含义, 但仅用于前端展示
| left_min | int | 关系左端的资源模型实例至少包含多少数量的关系: 目前来说这个字段是过度设计的字段, 一般填0就好了
| left_max | int | 关系左端的资源模型实例最多包含多少数量的关系: 有数据库级别的索引支持, 一般情况填1 或者 -1, -1表示无限多
| left_groups | string[] | 关系在左端模型的哪些分组里
| left_tags | string[] | 
| right_object_id | string | 关系右端的模型ID
| right_id | string | 关系右端模型中表达左端模型实例的别名字段: 比如应用的负责人需要在应用的实例中表达出一个字段; 对已有模型添加关系时这个ID需要加下划线前缀避免冲突
| right_description | string | 是与right_id 相反的含义, 但仅用于前端展示
| right_name | string | 是与right_id 对应的含义, 但仅用于前端展示
| right_min | int | 关系右端的资源模型实例至少包含多少数量的关系: 目前来说这个字段是过度设计的字段, 一般填0就好了
| right_max | int | 关系右端的资源模型实例最多包含多少数量的关系: 有数据库级别的索引支持, 一般情况填1 或者 -1, -1表示无限多
| right_groups | string[] | 关系在右端模型的哪些分组里
| right_tags | string[] | 

### - 返回码
|返回码|备注|
|---|---|
| 0 | success

### - 请求示例
```json
{
    "description": "fake_description",
    "required": "fake_required",
    "value": {
        "struct_define": [
            {
                "regex": [
                    "fake_regex"
                ],
                "protected": true,
                "type": "int",
                "id": "fake_id",
                "name": "fake_name"
            }
        ],
        "series_number_length": 8,
        "default_type": "fake_default_type",
        "prefix": "fake_prefix",
        "mode": "fake_mode",
        "start_value": 8,
        "type": "int"
    },
    "readonly": "fake_readonly",
    "tag": [
        "fake_tag"
    ],
    "tips": "fake_tips",
    "unique": "fake_unique",
    "name": "fake_name"
}
```

### - 返回示例
```json
{
    "code": 0,
    "data": {
        "category": "fake_category",
        "attrList": [
            {
                "name": "fake_name",
                "required": "fake_required",
                "tag": [
                    "fake_tag"
                ],
                "value": {
                    "struct_define": [
                        {
                            "regex": [
                                "fake_regex"
                            ],
                            "protected": true,
                            "type": "int",
                            "id": "fake_id",
                            "name": "fake_name"
                        }
                    ],
                    "series_number_length": 8,
                    "default_type": "fake_default_type",
                    "prefix": "fake_prefix",
                    "mode": "fake_mode",
                    "start_value": 8,
                    "type": "int"
                },
                "custom": "fake_custom",
                "readonly": "fake_readonly",
                "protected": true,
                "tips": "fake_tips",
                "unique": "fake_unique",
                "id": "fake_id",
                "description": "fake_description"
            }
        ],
        "name": "fake_name",
        "objectId": "fake_objectId",
        "memo": "fake_memo",
        "deleteAuthorizers": [
            "fake_deleteAuthorizers"
        ],
        "updateAuthorizers": [
            "fake_updateAuthorizers"
        ],
        "relation_list": [
            {
                "right_groups": [
                    "fake_right_groups"
                ],
                "right_min": 8,
                "left_object_id": "fake_left_object_id",
                "name": "fake_name",
                "right_id": "fake_right_id",
                "right_max": 8,
                "left_id": "fake_left_id",
                "left_max": 8,
                "left_min": 8,
                "right_description": "fake_right_description",
                "left_name": "fake_left_name",
                "protected": true,
                "left_description": "fake_left_description",
                "right_name": "fake_right_name",
                "relation_id": "fake_relation_id",
                "left_tags": [
                    "fake_left_tags"
                ],
                "right_tags": [
                    "fake_right_tags"
                ],
                "right_object_id": "fake_right_object_id",
                "left_groups": [
                    "fake_left_groups"
                ]
            }
        ],
        "protected": true,
        "relation_groups": [
            {
                "protected": true,
                "id": "fake_id",
                "name": "fake_name"
            }
        ],
        "view": {},
        "icon": "fake_icon"
    },
    "error": "",
    "codeExplain": ""
}
```
## <a id='-update-PUT'></a> update PUT
>更新模型<br>

### - 测试关键字
```
update request 
```
### - 接口访问URL
```
PUT /object/:object_id
```
### - 参数
#### URI 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| object_id | string | 是 |  |  | {'gte': 1}


#### body 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| name | string | 否 | 名称 |  | 
| icon | string | 否 | 图标 |  | 
| category | string | 否 | 分类, 点分表示二级分类 |  | 
| memo | string | 否 | 说明 |  | 
| view | map | 否 | 模型的视图设置 |  | 
| updateAuthorizers | string[] | 否 | 编辑权限白名单 |  | 
| deleteAuthorizers | string[] | 否 | 删除权限白名单 |  | 


### - 返回值说明
|名称|类型|备注|
|---|---|---|
| objectId | string | ID
| name | string | 名称
| icon | string | 图标
| category | string | 分类, 点分表示二级分类
| memo | string | 说明
| protected | bool | true代表是核心模型，是受保护的模型，不允许被删除
| view | map | 模型的视图设置
| attrList | property.Property[] | 属性列表
| relation_groups | relation_group.RelationGroup[] | 关系分组定义
| relation_list | relation.Relation[] | 关系列表
| updateAuthorizers | string[] | 编辑权限白名单
| deleteAuthorizers | string[] | 删除权限白名单


Property-

|名称|类型|备注|
|---|---|---|
| id | string | 属性ID: 对已有模型添加新的属性ID需要加下划线开头避免冲突
| name | string | 属性名称
| protected | bool | 是否是内置属性: 核心定义的内置属性默认都是核心属性, 核心属性不允许被删除、不允许修改约束
| custom | string | 是否是自定义字段: 历史遗留原因不是布尔值定义, 待废弃, 与protected字段含义重复, 优先使用protected字段
| unique | string | 是否唯一: 历史遗留原因不是布尔值定义
| readonly | string | 是否只读: 历史遗留原因不是布尔值定义
| required | string | 是否必填: 历史遗留原因不是布尔值定义
| tag | string[] | 属性分类
| description | string | 似乎没有什么作用的描述
| tips | string | 似乎没有什么作用的提示
| value | property_value.PropertyValue | 属性值类型定义

PropertyValue-

|名称|类型|备注|
|---|---|---|
| type | enum | 数据类型
| regex | value | type是enum时是枚举值数组, struct和structs没有regex, 其他的type时是正则表达式
| default_type | string | 默认值类型( value: 具体的值, function:可执行函数, auto-increment-id:自增ID, series-number:定长序列号)
| default | value | 默认值
| struct_define | struct_define.StructDefine[] | 结构体字段定义: 当type 为 struct 和 structs 时候为必填
| mode | string | 字符串模式定义: 多行文本和普通字符串
| prefix | string | 自增ID和流水号的前缀: 当default_type 是series-number和 auto-increment-id时候为必填
| start_value | int | 自增ID和流水号的起始值
| series_number_length | int | 流水号的固定长度

StructDefine-

|名称|类型|备注|
|---|---|---|
| id | string | 结构体字段ID
| name | string | 结构体字段名称
| type | enum | 数据类型
| regex | string[] | 仅仅在type是enum时有值，并且是字符串数组
| protected | bool | 是否是内置属性: 核心定义的内置属性默认都是核心属性, 核心属性不允许被删除、不允许修改约束

RelationGroup-

|名称|类型|备注|
|---|---|---|
| id | string | ID
| name | string | 名称
| protected | bool | 是否是内置关系分组，内置的关系分组不允许删除

Relation-

|名称|类型|备注|
|---|---|---|
| relation_id | string | 必须全局唯一: 新添加的关系ID字段建议增加下划线前缀
| name | string | 不是必填, 而且在引入了left_description和 right_description 之后这个字段几乎处于废弃状态
| protected | bool | 
| left_object_id | string | 关系左端的模型ID
| left_id | string | 关系左端模型中表达右端模型实例的别名字段: 比如应用的负责人需要在应用的实例中表达出一个字段; 对已有模型添加关系时这个ID需要加下划线前缀避免冲突
| left_description | string | 是与left_id 相反的含义, 但仅用于前端展示
| left_name | string | 是与left_id 对应的含义, 但仅用于前端展示
| left_min | int | 关系左端的资源模型实例至少包含多少数量的关系: 目前来说这个字段是过度设计的字段, 一般填0就好了
| left_max | int | 关系左端的资源模型实例最多包含多少数量的关系: 有数据库级别的索引支持, 一般情况填1 或者 -1, -1表示无限多
| left_groups | string[] | 关系在左端模型的哪些分组里
| left_tags | string[] | 
| right_object_id | string | 关系右端的模型ID
| right_id | string | 关系右端模型中表达左端模型实例的别名字段: 比如应用的负责人需要在应用的实例中表达出一个字段; 对已有模型添加关系时这个ID需要加下划线前缀避免冲突
| right_description | string | 是与right_id 相反的含义, 但仅用于前端展示
| right_name | string | 是与right_id 对应的含义, 但仅用于前端展示
| right_min | int | 关系右端的资源模型实例至少包含多少数量的关系: 目前来说这个字段是过度设计的字段, 一般填0就好了
| right_max | int | 关系右端的资源模型实例最多包含多少数量的关系: 有数据库级别的索引支持, 一般情况填1 或者 -1, -1表示无限多
| right_groups | string[] | 关系在右端模型的哪些分组里
| right_tags | string[] | 

### - 返回码
|返回码|备注|
|---|---|
| 0 | success

### - 请求示例
```json
{
    "category": "fake_category",
    "name": "fake_name",
    "memo": "fake_memo",
    "deleteAuthorizers": [
        "fake_deleteAuthorizers"
    ],
    "updateAuthorizers": [
        "fake_updateAuthorizers"
    ],
    "icon": "fake_icon",
    "view": {}
}
```

### - 返回示例
```json
{
    "code": 0,
    "data": {
        "category": "fake_category",
        "attrList": [
            {
                "name": "fake_name",
                "required": "fake_required",
                "tag": [
                    "fake_tag"
                ],
                "value": {
                    "struct_define": [
                        {
                            "regex": [
                                "fake_regex"
                            ],
                            "protected": true,
                            "type": "int",
                            "id": "fake_id",
                            "name": "fake_name"
                        }
                    ],
                    "series_number_length": 8,
                    "default_type": "fake_default_type",
                    "prefix": "fake_prefix",
                    "mode": "fake_mode",
                    "start_value": 8,
                    "type": "int"
                },
                "custom": "fake_custom",
                "readonly": "fake_readonly",
                "protected": true,
                "tips": "fake_tips",
                "unique": "fake_unique",
                "id": "fake_id",
                "description": "fake_description"
            }
        ],
        "name": "fake_name",
        "objectId": "fake_objectId",
        "memo": "fake_memo",
        "deleteAuthorizers": [
            "fake_deleteAuthorizers"
        ],
        "updateAuthorizers": [
            "fake_updateAuthorizers"
        ],
        "relation_list": [
            {
                "right_groups": [
                    "fake_right_groups"
                ],
                "right_min": 8,
                "left_object_id": "fake_left_object_id",
                "name": "fake_name",
                "right_id": "fake_right_id",
                "right_max": 8,
                "left_id": "fake_left_id",
                "left_max": 8,
                "left_min": 8,
                "right_description": "fake_right_description",
                "left_name": "fake_left_name",
                "protected": true,
                "left_description": "fake_left_description",
                "right_name": "fake_right_name",
                "relation_id": "fake_relation_id",
                "left_tags": [
                    "fake_left_tags"
                ],
                "right_tags": [
                    "fake_right_tags"
                ],
                "right_object_id": "fake_right_object_id",
                "left_groups": [
                    "fake_left_groups"
                ]
            }
        ],
        "protected": true,
        "relation_groups": [
            {
                "protected": true,
                "id": "fake_id",
                "name": "fake_name"
            }
        ],
        "view": {},
        "icon": "fake_icon"
    },
    "error": "",
    "codeExplain": ""
}
```
## <a id='-delete_relation-DELETE'></a> delete_relation DELETE
>删除模型关系<br>

### - 测试关键字
```
delete relation request 
```
### - 接口访问URL
```
DELETE /object_relation/:relation_id
```
### - 参数
#### URI 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| relation_id | string | 是 | 关系ID |  | []




### - 返回码
|返回码|备注|
|---|---|
| 0 | success


## <a id='-set-POST'></a> set POST
>批量设置关系<br>

### - 测试关键字
```
manage instance relation request 
```
### - 接口访问URL
```
POST /object/:object_id/relation/:relation_side_id/set
```
### - 参数
#### URI 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| object_id | string | 是 |  |  | []
| relation_side_id | string | 是 |  |  | []


#### body 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| instance_ids | string[] | 是 | 模型的实例ID列表 |  | []
| related_instance_ids | string[] | 是 | 关联的实例ID列表 |  | []



### - 返回码
|返回码|备注|
|---|---|
| 0 | success

### - 请求示例
```json
{
    "related_instance_ids": [
        "fake_related_instance_ids"
    ],
    "instance_ids": [
        "fake_instance_ids"
    ]
}
```

## <a id='-discovery-POST'></a> discovery POST
>实例关系发现<br>

### - 测试关键字
```
discover instance relation request 
```
### - 接口访问URL
```
POST /object_relation/:relation_id/_autodiscovery/multi
```
### - 参数
#### URI 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| relation_id | string | 是 | 关系id |  | []


#### body 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| match | discovery_match.DiscoverInstanceRelationMatch | 是 | 发现实例的字段列表 |  | []
| data | discovery_data.DiscoverInstanceRelationData[] | 是 | 发现实例的数据列表 |  | []
| strict | bool | 否 | 精确匹配（true: 只允许1:1关系，false: 允许1:n关系，默认true） | True | []

DiscoverInstanceRelationMatch-实例关系发现接口请求 - 发现实例的字段参数

|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| left_match | string[] | 否 | 左侧实例匹配字段列表 |  | 
| right_match | string[] | 否 | 右侧实例匹配字段列表 |  | 
DiscoverInstanceRelationData-实例关系发现接口请求 - 发现实例的数据参数

|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| left_instance | map | 否 | 左侧匹配的实例数据 |  | 
| right_instance | map | 否 | 右侧匹配的实例数据 |  | 


### - 返回码
|返回码|备注|
|---|---|
| 0 | success

### - 请求示例
```json
{
    "strict": true,
    "data": [
        {
            "left_instance": {},
            "right_instance": {}
        }
    ],
    "match": {
        "left_match": [
            "fake_left_match"
        ],
        "right_match": [
            "fake_right_match"
        ]
    }
}
```

### - 返回示例
```json
{
    "code": 0,
    "data": [
        {
            "connected": [
                {
                    "left_instance_id": "fake_left_instance_id",
                    "right_instance_id": "fake_right_instance_id"
                }
            ],
            "message": "fake_message",
            "code": 8,
            "right_object_id": "fake_right_object_id",
            "left_object_id": "fake_left_object_id"
        }
    ],
    "error": "",
    "codeExplain": ""
}
```
## <a id='-remove-POST'></a> remove POST
>批量移除关系<br>

### - 测试关键字
```
manage instance relation request 
```
### - 接口访问URL
```
POST /object/:object_id/relation/:relation_side_id/remove
```
### - 参数
#### URI 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| object_id | string | 是 |  |  | []
| relation_side_id | string | 是 |  |  | []


#### body 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| instance_ids | string[] | 是 | 模型的实例ID列表 |  | []
| related_instance_ids | string[] | 是 | 关联的实例ID列表 |  | []



### - 返回码
|返回码|备注|
|---|---|
| 0 | success

### - 请求示例
```json
{
    "related_instance_ids": [
        "fake_related_instance_ids"
    ],
    "instance_ids": [
        "fake_instance_ids"
    ]
}
```

## <a id='-append-POST'></a> append POST
>批量添加关系<br>

### - 测试关键字
```
manage instance relation request 
```
### - 接口访问URL
```
POST /object/:object_id/relation/:relation_side_id/append
```
### - 参数
#### URI 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| object_id | string | 是 |  |  | []
| relation_side_id | string | 是 |  |  | []


#### body 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| instance_ids | string[] | 是 | 模型的实例ID列表 |  | []
| related_instance_ids | string[] | 是 | 关联的实例ID列表 |  | []



### - 返回码
|返回码|备注|
|---|---|
| 0 | success

### - 请求示例
```json
{
    "related_instance_ids": [
        "fake_related_instance_ids"
    ],
    "instance_ids": [
        "fake_instance_ids"
    ]
}
```

## <a id='-count_relation_instance-GET'></a> count_relation_instance GET
>统计关系实例数量<br>

### - 测试关键字
```
count relation instance request 
```
### - 接口访问URL
```
GET /object_relation/:relation_id/relation_instance/_count_relation_instance
```
### - 参数
#### URI 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| relation_id | string | 是 | 关系id |  | {'gte': 1}




### - 返回码
|返回码|备注|
|---|---|
| 0 | success


## <a id='-delete-DELETE'></a> delete DELETE
>删除关系查询策略<br>

### - 测试关键字
```
delete instance query strategy request 
```
### - 接口访问URL
```
DELETE /object/:object_id/query/strategy/:strategy_id
```
### - 参数
#### URI 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| object_id | string | 是 |  |  | []
| strategy_id | string | 是 |  |  | []



### - 返回值说明
|名称|类型|备注|
|---|---|---|
| id | string | 策略ID
| name | string | 策略名称
| objectId | string | 策略所属模型id
| type | string | 策略类型(org 或者 user)
| instance_type | string | 策略对应的实例类型(instance 或者 relation)
| query | map | 策略内容(包含查询条件和返回的字段,供前端使用，后台逻辑暂时不做校验)
| ctime | string | 创建时间
| creator | string | 创建用户


### - 返回码
|返回码|备注|
|---|---|
| 0 | success


### - 返回示例
```json
{
    "code": 0,
    "data": {
        "name": "fake_name",
        "objectId": "fake_objectId",
        "creator": "fake_creator",
        "instance_type": "fake_instance_type",
        "query": {},
        "type": "fake_type",
        "id": "fake_id",
        "ctime": "fake_ctime"
    },
    "error": "",
    "codeExplain": ""
}
```
## <a id='-get-GET'></a> get GET
>获取查询策略<br>

### - 测试关键字
```
get instance query strategy request 
```
### - 接口访问URL
```
GET /object/:object_id/query/strategy/:strategy_id
```
### - 详细说明
>query字段中的fields字段表示的是模型要返回什么属性, 以及返回的属性的别名ID<br>

### - 参数
#### URI 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| object_id | string | 是 |  |  | []
| strategy_id | string | 是 |  |  | []



### - 返回值说明
|名称|类型|备注|
|---|---|---|
| id | string | 策略ID
| name | string | 策略名称
| objectId | string | 策略所属模型id
| type | string | 策略类型(org 或者 user)
| instance_type | string | 策略对应的实例类型(instance 或者 relation)
| query | map | 策略内容(包含查询条件和返回的字段,供前端使用，后台逻辑暂时不做校验)
| ctime | string | 创建时间
| creator | string | 创建用户


### - 返回码
|返回码|备注|
|---|---|
| 0 | success


### - 返回示例
```json
{
    "code": 0,
    "data": {
        "name": "fake_name",
        "objectId": "fake_objectId",
        "creator": "fake_creator",
        "instance_type": "fake_instance_type",
        "query": {},
        "type": "fake_type",
        "id": "fake_id",
        "ctime": "fake_ctime"
    },
    "error": "",
    "codeExplain": ""
}
```
## <a id='-list-GET'></a> list GET
>按模型获取查询策略列表<br>

### - 测试关键字
```
list instance query strategy request 
```
### - 接口访问URL
```
GET /object/:object_id/query/strategy
```
### - 参数
#### URI 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| object_id | string | 是 |  |  | []

#### query 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| type | string | 否 |  |  | []



### - 返回码
|返回码|备注|
|---|---|
| 0 | success


### - 返回示例
```json
{
    "code": 0,
    "data": [
        {
            "name": "fake_name",
            "objectId": "fake_objectId",
            "creator": "fake_creator",
            "instance_type": "fake_instance_type",
            "query": {},
            "type": "fake_type",
            "id": "fake_id",
            "ctime": "fake_ctime"
        }
    ],
    "error": "",
    "codeExplain": ""
}
```
## <a id='-create-POST'></a> create POST
>创建查询策略<br>

### - 测试关键字
```
create instance query strategy request 
```
### - 接口访问URL
```
POST /object/:object_id/query/strategy
```
### - 参数
#### URI 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| object_id | string | 是 |  |  | []


#### body 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| name | string | 否 | 策略名称 |  | 
| type | string | 否 | 策略类型(org 或者 user) | org | {'pattern': '^(org|user)$'}
| instance_type | string | 否 | 策略对应的实例类型(instance 或者 relation) |  | 
| query | map | 是 | 策略内容(包含查询条件和返回的字段,供前端使用，后台逻辑暂时不做校验) |  | []


### - 返回值说明
|名称|类型|备注|
|---|---|---|
| id | string | 策略ID
| name | string | 策略名称
| objectId | string | 策略所属模型id
| type | string | 策略类型(org 或者 user)
| instance_type | string | 策略对应的实例类型(instance 或者 relation)
| query | map | 策略内容(包含查询条件和返回的字段,供前端使用，后台逻辑暂时不做校验)
| ctime | string | 创建时间
| creator | string | 创建用户


### - 返回码
|返回码|备注|
|---|---|
| 0 | success

### - 请求示例
```json
{
    "instance_type": "fake_instance_type",
    "type": "fake_type",
    "name": "fake_name",
    "query": {}
}
```

### - 返回示例
```json
{
    "code": 0,
    "data": {
        "name": "fake_name",
        "objectId": "fake_objectId",
        "creator": "fake_creator",
        "instance_type": "fake_instance_type",
        "query": {},
        "type": "fake_type",
        "id": "fake_id",
        "ctime": "fake_ctime"
    },
    "error": "",
    "codeExplain": ""
}
```
## <a id='-update-PUT'></a> update PUT
>修改查询策略<br>

### - 测试关键字
```
update instance query strategy request 
```
### - 接口访问URL
```
PUT /object/:object_id/query/strategy/:strategy_id
```
### - 参数
#### URI 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| object_id | string | 是 |  |  | []
| strategy_id | string | 是 |  |  | []


#### body 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| name | string | 是 | 策略名称 |  | []
| type | string | 否 | 策略类型(org 或者 user) |  | 
| instance_type | string | 否 | 策略对应的实例类型(instance 或者 relation) |  | 
| query | map | 否 | 策略内容(包含查询条件和返回的字段,供前端使用，后台逻辑暂时不做校验) |  | 


### - 返回值说明
|名称|类型|备注|
|---|---|---|
| id | string | 策略ID
| name | string | 策略名称
| objectId | string | 策略所属模型id
| type | string | 策略类型(org 或者 user)
| instance_type | string | 策略对应的实例类型(instance 或者 relation)
| query | map | 策略内容(包含查询条件和返回的字段,供前端使用，后台逻辑暂时不做校验)
| ctime | string | 创建时间
| creator | string | 创建用户


### - 返回码
|返回码|备注|
|---|---|
| 0 | success

### - 请求示例
```json
{
    "instance_type": "fake_instance_type",
    "type": "fake_type",
    "name": "fake_name",
    "query": {}
}
```

### - 返回示例
```json
{
    "code": 0,
    "data": {
        "name": "fake_name",
        "objectId": "fake_objectId",
        "creator": "fake_creator",
        "instance_type": "fake_instance_type",
        "query": {},
        "type": "fake_type",
        "id": "fake_id",
        "ctime": "fake_ctime"
    },
    "error": "",
    "codeExplain": ""
}
```
## <a id='-relation_max_check-POST'></a> relation_max_check POST
>搜索实例列表指定关系是否大于等于max约束<br>

### - 测试关键字
```
relation max check request 
```
### - 接口访问URL
```
POST /object/:object_id/instance/_search_relation_max_check
```
### - 详细说明
>一般用于新建实例关系时查询数据用, 会标识出实例数据是否超出关系限定的max(_relation_is_max),支持的查询操作与 [实例搜索接口] 关键字一致<br>

### - 参数
#### URI 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| object_id | string | 是 | 资源模型ID |  | []


#### body 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| relation_id | string | 是 | 资源模型关系ID |  | []
| relation_side_id | string | 是 | left_id或者right_id来指定资源模型在关系的哪一端 |  | []
| query | map | 否 | 查询条件,与[实例搜索接口]的query字段说明一致 |  | 
| sort | map | 否 | 按字段排序, 留空默认按照实例ID降序排序(1表示升序, -1表示降序) |  | 
| permission | string[] | 否 | 按照权限过滤(通用实例都有`read`, `update`, `delete`权限控制, 主机实例在通用实例权限基础上有额外的`operate`权限, 应用实例在通用实例权限基础上有额外的`developClusterOperate`, `testClusterOperate`, `prereleaseClusterOperate`, `productionClusterOperate`权限) |  | 
| page | int | 否 | 页码 | 1 | {'gte': 1}
| page_size | int | 否 | 页大小 | 30 | {'gte': 1, 'lte': 3000}


### - 返回值说明
|名称|类型|备注|
|---|---|---|
| total | int | total
| page | int | page
| page_size | int | page_size
| list | relation_max_check_result.RelationMaxCheckResult[] | list


RelationMaxCheckResult-

|名称|类型|备注|
|---|---|---|
| instanceId | string | 实例Id
| _relation_is_max | bool | _relation_is_max

### - 返回码
|返回码|备注|
|---|---|
| 0 | success

### - 请求示例
```json
{
    "sort": {},
    "permission": [
        "fake_permission"
    ],
    "page_size": 8,
    "relation_side_id": "fake_relation_side_id",
    "relation_id": "fake_relation_id",
    "query": {},
    "page": 8
}
```

### - 返回示例
```json
{
    "code": 0,
    "data": {
        "total": 8,
        "list": [
            {
                "instanceId": "fake_instanceId",
                "_relation_is_max": true
            }
        ],
        "page": 8,
        "page_size": 8
    },
    "error": "",
    "codeExplain": ""
}
```
## <a id='-search-POST'></a> search POST
>实例搜索接口<br>

### - 测试关键字
```
search request 
```
### - 接口访问URL
```
POST /object/:object_id/instance/_search
```
### - 详细说明
>支持属性的查询, 支持内联结构体的属性查询, 支持以left_id或者right_id表达的任意层级关系查询 扩展查询的关键字: `$like`, `$nlike`: 顾名思义, 对应的是数据库的子字符串匹配, 用法为 `{ "name": {"$like": "%easyops%"} }, { "name": {"$nlike": "%easyops%"} }` `$size`: 用于查询关系数量或者数组的长度, 其他的查询会报错或者没有预期效果, 具体可以参考请求示例 `$exists`: 查询字段是否有值, 空值(`null`,`[]`,`""`, 字段不存在)会认为是没有值(属性字段或者关系字段都可以用`$exists`关键字判断) 查询场景举例: 查询APP时, 想根据IP查询query字段可以这么写: `{"clusters.deviceList.ip": {"$in": ["192.168.100.122"]}}`, 查询BUSINESS 时, 想根据IP查询query字段可以这么写: `{"_businesses_APP.clusters.deviceList.ip": {"$in": ["192.168.100.122"]}}` 查询属于多个应用的主机, 请求查询HOST, query字段这么写: `{"_deviceList_CLUSTER.appId": {"$size": {"$gt": 1}}}`<br>

### - 参数
#### URI 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| object_id | string | 是 | 资源模型ID |  | []


#### body 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| page | int | 否 | 页码 | 1 | {'gte': 1}
| page_size | int | 否 | 页大小 | 30 | {'gte': 1, 'lte': 3000}
| query | map | 否 | 查询条件,与[实例搜索接口]的query字段说明一致 |  | 
| fields | map | 否 | 过滤的字段列表, 留空代表返回所有字段(true: 表示指定获取字段, false: 表示指定不获取的字段)(支持关系数据的二级jsonPath格式的指定字段如clusters.name) |  | 
| sort | map | 否 | 按字段排序, 留空默认按照实例ID降序排序(1表示升序, -1表示降序) |  | 
| permission | string[] | 否 | 按照权限过滤(通用实例都有`read`, `update`, `delete`权限控制, 主机实例在通用实例权限基础上有额外的`operate`权限, 应用实例在通用实例权限基础上有额外的`developClusterOperate`, `testClusterOperate`, `prereleaseClusterOperate`, `productionClusterOperate`权限) |  | 
| only_relation_view | bool | 否 | 对于关联的实例数据是否只获取relation_view中指定的属性, 这个字段为true时, 会覆盖fields字段中指定的二级字段设置 | False | []
| only_my_instance | bool | 否 | 是否只获取与自己有关的那部分数据, 默认为false | False | []


### - 返回值说明
|名称|类型|备注|
|---|---|---|
| total | int | total
| page | int | page
| page_size | int | page_size
| list | map[] | 实例列表


### - 返回码
|返回码|备注|
|---|---|
| 0 | success

### - 请求示例
```json
{
    "sort": {},
    "permission": [
        "fake_permission"
    ],
    "fields": {},
    "page_size": 8,
    "only_relation_view": true,
    "only_my_instance": true,
    "query": {},
    "page": 8
}
```

### - 返回示例
```json
{
    "code": 0,
    "data": {
        "total": 8,
        "list": [
            {}
        ],
        "page": 8,
        "page_size": 8
    },
    "error": "",
    "codeExplain": ""
}
```
## <a id='-instance_relation_count-GET'></a> instance_relation_count GET
>单个实例关系统计<br>

### - 测试关键字
```
relation count request 
```
### - 接口访问URL
```
GET /object/:object_id/instance/:instance_id/_relation_count
```
### - 详细说明
>对于APP会额外返回其集群下所有主机的数量(_clusters_deviceList)<br>

### - 参数
#### URI 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| object_id | string | 是 | 资源模型ID |  | []
| instance_id | string | 是 | 实例ID |  | []




### - 返回码
|返回码|备注|
|---|---|
| 0 | success


### - 返回示例
```json
{
    "message": "Success",
    "code": 0,
    "data": {
        "services": 0,
        "clusters": 18,
        "businesses": 1,
        "_clusters_deviceList": 2
    },
    "error": "\u6210\u529f"
}
```
## <a id='-update_v2-PUT'></a> update_v2 PUT
>更新实例v2<br>

### - 测试关键字
```
update instance request 
```
### - 接口访问URL
```
PUT /v2/object/:object_id/instance/:instance_id
```
### - 参数
#### URI 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| object_id | string | 是 | 实例所属的模型ID |  | {'gte': 1}
| instance_id | string | 是 | 实例ID |  | {'gte': 1}


#### body 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
|  |  | 否 |  |  | 



### - 返回码
|返回码|备注|
|---|---|
| 0 | success

### - 请求示例
```json
{}
```

## <a id='-delete-DELETE'></a> delete DELETE
>删除实例<br>

### - 测试关键字
```
delete instance request 
```
### - 接口访问URL
```
DELETE /object/:object_id/instance/:instance_id
```
### - 参数
#### URI 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| object_id | string | 是 | 实例所属的模型ID |  | {'gte': 1}
| instance_id | string | 是 | 实例ID |  | {'gte': 1}




### - 返回码
|返回码|备注|
|---|---|
| 0 | success


## <a id='-get-GET'></a> get GET
>获取单个实例<br>

### - 测试关键字
```
get instance request 
```
### - 接口访问URL
```
GET /object/:object_id/instance/:instance_id
```
### - 参数
#### URI 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| object_id | string | 是 | 实例所属的模型ID |  | {'gte': 1}
| instance_id | string | 是 | 实例ID |  | {'gte': 1}

#### query 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| fields | string | 否 | 指定返回的fields,使用逗号分隔 |  | []



### - 返回码
|返回码|备注|
|---|---|
| 0 | success


## <a id='-search_total-POST'></a> search_total POST
>实例搜索统计实例数量<br>

### - 测试关键字
```
search total request 
```
### - 接口访问URL
```
POST /object/:object_id/instance/_search_total
```
### - 详细说明
>支持属性的查询, 支持内联结构体的属性查询, 支持以left_id或者right_id表达的任意层级关系查询 扩展查询的关键字: `$like`, `$nlike`: 顾名思义, 对应的是数据库的子字符串匹配, 用法为 `{ "name": {"$like": "%easyops%"} }, { "name": {"$nlike": "%easyops%"} }` `$size`: 用于查询关系数量或者数组的长度, 其他的查询会报错或者没有预期效果, 具体可以参考请求示例 `$exists`: 查询字段是否有值, 空值(`null`,`[]`,`""`, 字段不存在)会认为是没有值(属性字段或者关系字段都可以用`$exists`关键字判断) 查询场景举例: 查询APP时, 想根据IP查询query字段可以这么写: `{"clusters.deviceList.ip": {"$in": ["192.168.100.122"]}}`, 查询BUSINESS 时, 想根据IP查询query字段可以这么写: `{"_businesses_APP.clusters.deviceList.ip": {"$in": ["192.168.100.122"]}}` 查询属于多个应用的主机, 请求查询HOST, query字段这么写: `{"_deviceList_CLUSTER.appId": {"$size": {"$gt": 1}}}`<br>

### - 参数
#### URI 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| object_id | string | 是 | 资源模型ID |  | []


#### body 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| query | map | 否 | 查询条件,与[实例搜索接口]的query字段说明一致 |  | 
| permission | string[] | 否 | 按照权限过滤(通用实例都有`read`, `update`, `delete`权限控制, 主机实例在通用实例权限基础上有额外的`operate`权限, 应用实例在通用实例权限基础上有额外的`developClusterOperate`, `testClusterOperate`, `prereleaseClusterOperate`, `productionClusterOperate`权限) |  | 
| only_my_instance | bool | 否 | 是否只获取与自己有关的那部分数据, 默认为false | False | []



### - 返回码
|返回码|备注|
|---|---|
| 0 | success

### - 请求示例
```json
{
    "query": {},
    "only_my_instance": true,
    "permission": [
        "fake_permission"
    ]
}
```

## <a id='-list-GET'></a> list GET
>实例分页列表查询<br>

### - 测试关键字
```
list instance request 
```
### - 接口访问URL
```
GET /object/:object_id/instance
```
### - 参数
#### URI 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| object_id | string | 是 | 实例所属的模型ID |  | {'gte': 1}

#### query 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| page | int | 是 | 页码 | 1 | {'gte': 1}
| page_size | int | 是 | 页大小 | 200 | {'gte': 1, 'lte': 3000}
| only_relation_view | bool | 否 | 对于关联的实例数据是否只获取relation_view中指定的属性 | False | []
| select_relations | string | 否 | 需要返回的关系，多个用逗号分隔 |  | []


### - 返回值说明
|名称|类型|备注|
|---|---|---|
| total | int | total
| page | int | page
| page_size | int | page_size
| list | map[] | 实例列表


### - 返回码
|返回码|备注|
|---|---|
| 0 | success


### - 返回示例
```json
{
    "code": 0,
    "data": {
        "total": 8,
        "list": [
            {}
        ],
        "page": 8,
        "page_size": 8
    },
    "error": "",
    "codeExplain": ""
}
```
## <a id='-aggregate_count_attr-GET'></a> aggregate_count_attr GET
>实例计数统计接口<br>

### - 测试关键字
```
aggregate count attr request 
```
### - 接口访问URL
```
GET /object/:object_id/instance_aggregate/count/:attr_id
```
### - 详细说明
>实例计数统计<br>

### - 参数
#### URI 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| object_id | string | 是 | URL中资源模型ID |  | []
| attr_id | string | 是 | URL中模型属性ID, 支持结构体，用.分隔结构体名称和属性名称，如cpu.brand |  | []

#### query 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| page | int | 否 | 页码 | 1 | {'gte': 1}
| page_size | int | 否 | 页大小 | 30 | {'gte': 1, 'lte': 3000}


### - 返回值说明
|名称|类型|备注|
|---|---|---|
| total | int | 
| page | int | 
| page_size | int | 
| list | aggregate_count_attr_result.AggregateCountAttrResult[] | 


AggregateCountAttrResult-

|名称|类型|备注|
|---|---|---|
| count | int | 
| attr | map | 

### - 返回码
|返回码|备注|
|---|---|
| 0 | success


### - 返回示例
```json
{
    "codeExplain": "",
    "code": 0,
    "data": {
        "total": 1,
        "list": [
            {
                "count": 1,
                "attr": {
                    "cpu.brand": "intel"
                }
            }
        ],
        "page": 1,
        "page_size": 100
    },
    "error": ""
}
```
## <a id='-get_default_value_template-GET'></a> get_default_value_template GET
>获取实例默认值模板<br>

### - 测试关键字
```
get default value template request 
```
### - 接口访问URL
```
GET /object/:object_id/instance_default_value_template
```
### - 参数
#### URI 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| object_id | string | 是 | 实例所属的模型ID |  | {'gte': 1}

#### query 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| exclude_keys | string | 否 | 不获取默认值的字段，用逗号分隔 |  | []



### - 返回码
|返回码|备注|
|---|---|
| 0 | success


## <a id='-create_v2-POST'></a> create_v2 POST
>创建实例v2<br>

### - 测试关键字
```
create instance request 
```
### - 接口访问URL
```
POST /v2/object/:object_id/instance
```
### - 参数
#### URI 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| object_id | string | 是 | 实例所属的模型ID |  | {'gte': 1}


#### body 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
|  |  | 否 |  |  | 



### - 返回码
|返回码|备注|
|---|---|
| 0 | success

### - 请求示例
```json
{}
```

## <a id='-export_relation_instances_v2-POST'></a> export_relation_instances_v2 POST
>导出资源模型路径查询的实例v2<br>

### - 测试关键字
```
path search export request 
```
### - 接口访问URL
```
POST /v2/path/_search/export
```
### - 参数


#### body 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| json | string | 是 | 请求参数json序列化(必填字段path, 可选字段fields_sort:[]string, exportAllFields: bool) |  | {'gte': 1}



### - 返回码
|返回码|备注|
|---|---|
| 0 | success

### - 请求示例
```json
{
    "json": "fake_json"
}
```

## <a id='-export_relation_instances_v4-POST'></a> export_relation_instances_v4 POST
>导出资源模型路径查询的实例v4<br>

### - 测试关键字
```
path search export request 
```
### - 接口访问URL
```
POST /v4/path/_search/export
```
### - 参数


#### body 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| json | string | 是 | 请求参数json序列化(必填字段path, 可选字段fields_sort:[]string, exportAllFields: bool) |  | {'gte': 1}



### - 返回码
|返回码|备注|
|---|---|
| 0 | success

### - 请求示例
```json
{
    "json": "fake_json"
}
```

## <a id='-export_instance-POST'></a> export_instance POST
>实例导出<br>

### - 测试关键字
```
instance search export request 
```
### - 接口访问URL
```
POST /object/:object_id/instance/export
```
### - 参数
#### URI 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| object_id | string | 是 | 资源模型ID |  | {'gte': 1}


#### body 参数
|名称|类型|必选|备注|默认值|校验方法|
|---|---|---|---|---|---|
| json | string | 否 | 请求参数json序列化 | {} | []



### - 返回码
|返回码|备注|
|---|---|
| 0 | success

### - 请求示例
```json
{
    "json": "fake_json"
}
```

