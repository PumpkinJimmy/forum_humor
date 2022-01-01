
// import ObjectListView from './components/ObjectListView.vue'
import ObjectListEditor from './components/ObjectListEditor.vue'
import PostList from './components/PostList.vue'
import EmotionView from './components/EmotionView'

const routes = [
    {path: '/object/:modelName', component: ObjectListEditor, props: true},
    {path: '/post/', component: PostList},
    {path: '/emotion/', component: EmotionView}
]

export default routes