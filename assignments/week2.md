LXY & WP的任务：
1. 为ER图增加实体：Tag的点击日志
2. 建表。
   
   需要了解一下知识：
   1. 更多数据类型：日期、时间、长文本（text）、浮点数、Blob、枚举类型，等等
   2. 自增ID `serial`
   3. openGauss的约束书写
   4. 触发器的编写（用于自动触发日志记录）
   
   需要完成以下部分：
   1. 表本体
   2. 主键
   3. 非空约束、unique约束
   4. check约束
   5. 外键约束
   6. 其他自定义约束
   
   可能用得到的文档链接：
   1. [openGauss SQL参考](https://opengauss.org/zh/docs/latest/docs/Developerguide/SQL%E5%8F%82%E8%80%83.html)
   2. [连接openGauss数据库](https://opengauss.org/zh/docs/latest/docs/Quickstart/gsql%E5%AE%A2%E6%88%B7%E7%AB%AF%E8%BF%9E%E6%8E%A5.html)
   3. [gs_ctl命令的使用](https://opengauss.org/zh/docs/latest/docs/Toolreference/gs_ctl.html)
   4. [PostgreSQL官方文档](https://www.postgresql.org/docs/14/index.html)
   5. [openGauss 管理员指南](https://opengauss.org/zh/docs/latest/docs/Administratorguide/Administratorguide.html)
   6. [openGauss 开发者指南](https://opengauss.org/zh/docs/latest/docs/Developerguide/Developerguide.html)


3. 了解openGauss中运行SQL脚本的方法
4. 了解openGauss中导入数据的方法
5. **编写建表的SQL脚本**
6. **测试编写的SQL脚本**
7. 将测试好的SQL DDL脚本和测试脚本上传Github

WP的任务：
1. 了解openGauss基本服务管理（如何启动服务，如何连接，如何关闭防火墙）

LYH的任务：
1. 收集文本情感分析方面的数据集（Kaggle之类的）