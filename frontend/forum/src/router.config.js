

import PostList from './components/PostList.vue'
import EmotionView from './components/EmotionView'
import UserPostViewer from './components/UserPostsViewer'
import TagViewer from './components/TagViewer'
import Login from './components/Login'
import Panel from './components/Panel'
import UserInfo from './components/UserInfo'
import PostEdit from './components/PostEdit'

const routes = [
    {path: '/', redirect:'/post/'},
    {path: '/post/', component: PostList},
    {path: '/post-edit/', component: PostEdit},
    {path: '/emotion/', component: EmotionView},
    {path: '/userposts/', component: UserPostViewer},
    {path: '/tags/', component: TagViewer},
    {path: '/login/', component: Login},
    {path: '/admin/panel/', component: Panel},
    {path: '/user/:uid/', component: UserInfo, props: true}
]

export default routes