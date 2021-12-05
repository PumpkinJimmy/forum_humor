# 后端接口文档（待完善）
- 查询对象列表

- 查询对象
  
  URI: `/api/v1/<obj>/<primary_key...>`

  Method: `GET`

  Response: 
  
  | key name | type   | comment                             |
  | -------- | ------ | ----------------------------------- |
  | status   | String |                                     |
  | object   | Object | Structure depends on Specified obj. |

- 增加对象
  
  URI: `/api/v1/<obj>`

  Method: `POST`

  Request:

    | key name | type   | comment          |
    | -------- | ------ | ---------------- |
    | status   | String |                  |
    | uri      | String | New object's uri |

- 修改对象


- 删除对象
  
  URI: `/api/v1/<obj>/<primary_key...>`

  Method: `DELETE`

  Response:

