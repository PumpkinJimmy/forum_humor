# 后端接口文档（待完善）
- 查询对象列表

- 查询对象
  
  API: `/api/v1/object/<model>/<primary key...>/`

  Method: `GET`

  Response: 
  
  | key name | type   | comment                             |
  | -------- | ------ | ----------------------------------- |
  | status   | String |                                     |
  | obj      | Object | Structure depends on Specified obj. |

- 增加对象
  
  API: `/api/v1/object/<model>/`

  Method: `POST`

  Response:

    | key name | type   | comment          |
    | -------- | ------ | ---------------- |
    | status   | String |                  |

- 修改对象
  
  API: `/api/v1/object/<model>/<primary key...>/`

  Method: `PUT`

  Response:
  
  | key name | type   | comment |
  | -------- | ------ | ------- |
  | status   | String |         |


- 删除对象
  
  URI: `/api/v1/object/<model>/<primary_key...>`

  Method: `DELETE`

  Response:

  | key name | type   | comment |
  | -------- | ------ | ------- |
  | status   | String |         |

- 查询对象列表
  
  API: `/api/v1/object/<model>/`

  Method: `GET`

  Response:

    | key name | type   | comment         |
    | -------- | ------ | --------------- |
    | status   | String |                 |
    | objs     | Array  | Array of Object |
    | uris     | Array  | Array of String |
