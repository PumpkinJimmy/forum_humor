# forum_humor

论坛信息系统.

可以计算用户的幽默度.

Features:
- Backend
  - 基于Flask的App
  - 基于`psycopg2`的openGauss数据库客户端
  - 基于`psycopg2`的线程池与会话语义
  - Python实现的简易ORM
    - 支持`select, insert, update, delete`操作
    - 支持条件查询、排序、分页
  - 基于Python元类的ORM Model API
    - 对接存储模型和业务语义的`Model & Field`接口
    - 支持`Field`:
      - `AutoField`
      - `CharField`
      - `IntegerField`
      - `EmialField`
      - `EnumField`
      - `PasswordField`
      - `BlobField`
      - `FileField`
      - `ImageField`
  - RESTful通用对象访问接口
  - 基于Transformer的语言情感分类
  - 基于Numpy的窗口式热度统计
  
- Frontend
  - 基于Vue & Vue Router & Vuetify的单页后台管理框架应用
    - 基于Vue的前后端分离界面
    - 基于Vue Router的单页应用路由
    - 基于Vuetify的Material Design响应式跨端界面
    - 基于后端Model元信息的通用动态表单
  - 表单组件
    - 头像选择预览组件
    - 日历式日期选择组件
    - 基于正则表达式与Model元信息的表单验证

- Database
  - 数据库：openGauss
  - 基本数据类型
    - Serial 自增主键
    - Timestamp 日期、时间
    - Blob 大容量二进制存储
  - 权限管理：有限权限的后端用户`forum_backend`
  - 主键索引
  - 数据导入：基于CSV的大量测试数据导入
  - 基于触发器的点击日志

Dependencies:
- Database
  - openGauss

- Python3.7
  - psycopg2
  - flask
  - flask-CORS
  - numpy
  - pytorch>=1.8
  - gensim
  

- frontent
  - Vue
  - Vue CLI
  - Vue Router
  - Vuetify
  - axios
  - moment.js

剩余目标特性:
- Database
  - 触发器实现日志
- Backend
  - 基础登录
  - 用户帖子聚合（为了情感分析）
  - Tag内容聚合
  - 完整的情感分析支持
  - 点击记录
  - 热度统计
  
- Frontend
  - 头像显示
  - 帖子界面
  - 登录界面
  - 发帖操作
  - Tag内容聚合页面
  - 情感可视化（饼状图和自动人物标签）
  - 热度可视化（曲线图）


日后再谈：
- 应用部署
- Redis加速
- Websocket聊天功能
- 评论功能
- 鉴权
- 加盐哈希密码存储
- Flink流统计
- 社交图推荐
- 分布式集群
- CDN