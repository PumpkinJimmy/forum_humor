
// import ObjectListView from './components/ObjectListView.vue'
import ObjectListEditor from './components/ObjectListEditor.vue'

const routes = [
    {path: '/object/:modelName', component: ObjectListEditor, props: true}
]

export default routes