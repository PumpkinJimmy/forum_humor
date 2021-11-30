import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import routerConfig from './router.config.js'
// // Vue.config.productionTip = false
Vue.use(VueRouter)
const router = new VueRouter(routerConfig)

new Vue({
  render: h => h(App),
  router
}).$mount('#app')