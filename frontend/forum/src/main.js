import Vue from 'vue'
// import Vuex from 'vuex'
import App from './App.vue'
import VueRouter from 'vue-router'
import routes from './router.config.js'
import vuetify from './plugins/vuetify'


// Vue.use(Vuex)

// const store = new Vuex.Store({
//   state: {
//     count: 0
//   },
//   mutations: {
//     increment (state) {
//       state.count++
//     }
//   }
// })

Vue.config.productionTip = false
Vue.use(VueRouter)
const router = new VueRouter({
  mode: 'history',
  routes
})

new Vue({
  render: h => h(App),
  vuetify,
  router,
  // store,
}).$mount('#app')