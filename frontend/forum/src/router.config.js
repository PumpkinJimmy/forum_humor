// import HelloWorld from './components/HelloWorld'
import TagView from './components/Tag.vue'
import ForumUserView from './components/ForumUser.vue'
import NewTagForm from './components/NewTag'

const routes = [
    {path: '/tag', component: TagView},
    {path: '/forum_user', component: ForumUserView},
    {path: '/new_tag', component: NewTagForm},
]

export default routes