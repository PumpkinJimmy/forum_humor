# 笔记
## DB
- **不要用Python字符串模板来构造请求**。正确的`curs.execute`使用可以自动转义（见SQL注入测试），但Python模板不会。
- 在执行`commit`或者关闭连接之前的**所有`curs.execute/executemany`的操作会视作一个事务里的，随时可以`rollback`**