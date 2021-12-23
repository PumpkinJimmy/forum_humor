# serial 类型的原理
原理：
1. 随原表附加一个表
2. 附加的表中只有一行，**这一行记录了最近一次产生的id**
3. 提供一个函数`nextval`，**每次调用这个函数都会返回最近一次的id+1，并令表中记录的值+1**
4. 然后**将`nextval`的返回值作为自增字段的默认值**。
5. 这样，只要使用`default`即可令给定字段自动增加1，不用自己设置

说明：
1. 附加的表不可以直接更改
2. 提供一些列函数用于修改这个表的值
3. `nextval`返回并自增；`lastval`返回最近一次值；`setval`设置最近一次值；