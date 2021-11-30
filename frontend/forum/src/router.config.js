// import HelloWorld from './components/HelloWorld'
import TagView from './components/Tag.vue'

export default {
    router: [
        {path: '/tag', component: TagView},
        {path: '/', redirect: '/tag'}
    ]
}