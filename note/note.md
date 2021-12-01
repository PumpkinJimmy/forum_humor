# 笔记
## DB
- **不要用Python字符串模板来构造请求**。正确的`curs.execute`使用可以自动转义（见SQL注入测试），但Python模板不会。
- 在执行`commit`或者关闭连接之前的**所有`curs.execute/executemany`的操作会视作一个事务里的，随时可以`rollback`**
- `curs.execute`中可以有命名格式化参数直接使用dict

## Vue
- 常用`v-`
  - `v-if` 条件
  - `v-for` 循环
  - `v-model` （表单）双向绑定
  - `v-on:click` 事件（此处是点击事件）
  - `v-bind:var` 绑定

- 利用vue-router实现的多页跳转存在问题：组件之间数据不互通。解决方案是使用Vuex。
- Vuex相比全局变量的优势在于Vuex实现了Vue的响应式数据更新框架，可以同步变化，而全局变量不行