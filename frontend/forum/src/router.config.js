
import ObjectListEditor from './components/ObjectListEditor.vue'
import PostList from './components/PostList.vue'
import EmotionView from './components/EmotionView'
import UserPostViewer from './components/UserPostsViewer'

const routes = [
    {path: '/object/:modelName', component: ObjectListEditor, props: true},
    {path: '/post/', component: PostList},
    {path: '/emotion/', component: EmotionView},
    {path: '/userposts/', component: UserPostViewer}
]

export default routes