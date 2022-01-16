import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import routes from './router.config.js'
import vuetify from './plugins/vuetify'
import Vuex from 'vuex'
import axios from 'axios'


Vue.config.productionTip = false


Vue.use(Vuex)

const store = new Vuex.Store({
  state: {
    user: null,
    api: 'localhost:5000'
    // api: '172.26.13.146:5000'
  },
  mutations: {
    setUser(state, user){
      state.user = user
    }
  },
  actions:{
    login(context, {username, password}){
      axios.post(`http://${context.state.api}/api/v1/auth/login/`, {
              username: username,
              password: password,
          })
          .then((resp)=>{
              context.commit('setUser', resp.data.user);
              console.log(context.state.user);
          })
    }
  }
})

Vue.use(VueRouter)
const router = new VueRouter({
  mode: 'history',
  routes
})

new Vue({
  render: h => h(App),
  vuetify,
  router,
  store,
}).$mount('#app')