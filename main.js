import Vue from 'vue'
import App from './App.vue'
import Router from '.vue-router'

// Vue.config.productionTip = false

// new Vue({
//   render: h => h(App),
// }).$mount('#app')

Vue.use(Router)

const routes = [
  { path: '/tags', component: TagView }
]

const router = new VueRouter({
  routes
})

const app = new Vue({
  router
}).$mount('#app')