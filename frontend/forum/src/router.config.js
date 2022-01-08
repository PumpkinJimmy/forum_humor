
import ObjectListEditor from './components/ObjectListEditor.vue'
import PostList from './components/PostList.vue'
import EmotionView from './components/EmotionView'
import UserPostViewer from './components/UserPostsViewer'
import TagViewer from './components/TagViewer'
import Login from './components/Login'

const routes = [
    {path: '/object/:modelName', component: ObjectListEditor, props: true},
    {path: '/post/', component: PostList},
    {path: '/emotion/', component: EmotionView},
    {path: '/userposts/', component: UserPostViewer},
    {path: '/tags/', component: TagViewer},
    {path: '/login/', component: Login}
]

export default routes