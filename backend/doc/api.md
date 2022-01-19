对象元数据：
- `/api/v1/model/`
- `/api/v1/model/<model:model>/`

对象CRUD：
- `/api/v1/object/<model:model>/`
- `/api/v1/object/<model:model>/<key:pk>/`

登录服务：
- `/api/v1/auth/login/`
- `/api/v1/auth/login_status/`

面向具体业务的查询：
- `/api/v1/query/user_posts/<key:pk>/`
- `/api/v1/query/tag_access/<string:tname>/`

情感推断服务：
- `/api/v1/ml/infer_all/`
- `/api/v1/ml/infer_user/<string:uid>/`

点击记录服务：
- `/api/v1/log/tag_access//<string:tname>`

话题热度统计服务：
- `/api/v1/hot/tag_hot/<string:tname>/`