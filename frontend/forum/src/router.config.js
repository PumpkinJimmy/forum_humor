
// import ObjectListView from './components/ObjectListView.vue'
import ObjectListEditor from './components/ObjectListEditor.vue'
import PostList from './components/PostList.vue'

const routes = [
    {path: '/object/:modelName', component: ObjectListEditor, props: true},
    {path: '/post/', component: PostList}
]

export default routes