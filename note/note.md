# 笔记
## DB
- **不要用Python字符串模板来构造请求**。正确的`curs.execute`使用可以自动转义（见SQL注入测试），但Python模板不会。
- 在执行`commit`或者关闭连接之前的**所有`curs.execute/executemany`的操作会视作一个事务里的，随时可以`rollback`**
- `curs.execute`中可以有命名格式化参数直接使用dict

## Vue
- 常用`v-`
  - `v-if` 条件
  - `v-for` 循环
  - `v-on:click` `@click` 事件（此处是点击事件）
  - `v-bind:attr='var'` `:attr='var'` 单项绑定 
  - `v-model="var"` `#var`（表单）双向绑定
- 利用vue-router实现的多页跳转存在问题：组件之间数据不互通。解决方案是使用Vuex。
- Vuex相比全局变量的优势在于Vuex实现了Vue的响应式数据更新框架，可以同步变化，而全局变量不行
- **不要在methods中使用箭头函数**。因为箭头函数绑定的是全局对象上下文，而朴素定义的函数会有Vue自动绑定的this可使用。
- 组件参数：`props`
- 侦听器`watch`与计算属性`computed`类似，但除非是精细的行为控制，否则`computed`更方便

## Vuetify
常用组件说明：
- `v-badge` （图标右上角）提示点
- `v-dialog` 对话框
- `v-button` 按钮
- `v-row` `v-col` 响应式栅格系统
- `v-data-table` 全功能的数据表格
- `v-list` `v-list-item` `v-list-item-group` 列表（可用作菜单）
- `v-card` 卡片。Material Design中突起的东西

## Vue Router
- 传参: `props = Object`
- 当两个不同路由导向同一个组件时，Vue router不会新建组件而是**复用组件**。这样带来的问题是：组件声明周期钩子（如`mounted, created`）不会再被调用。使用`watch:{ $route(from ,to) { do something } }`监控路由变化

## 异步问题
如果回调依赖上下文状态，就会产生异步问题：
- 考虑一个对话框，发起异步请求，回调中处理返回
- 回调函数依赖请求时刻的某个上下文变量
- 但窗口关闭之后将那个依赖的变量的值改变了
- 回调处理出问题了

## Timestamp坑
- Postgresql: 以秒为单位的整数
- Python: 以秒为单位的浮点数(提供更高的精度)
- Javascript: 以毫秒为单位的整数(啊这)