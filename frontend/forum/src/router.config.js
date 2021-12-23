// import HelloWorld from './components/HelloWorld'
// import TagView from './components/Tag.vue'
// import ObjectListView from './components/ObjectListView.vue'
import ObjectListEditor from './components/ObjectListEditor.vue'
// import ForumUserView from './components/ForumUser.vue'
// import NewTagForm from './components/NewTag'
// import UpdateTagForm from './components/UpdateTag'

const routes = [
    {path: '/object/:modelName', component: ObjectListEditor, props: true}
    // {path: '/object/:modelName', component: ObjectListView, props: true}
    // {path: '/tag', component: ObjectListView, props: {'modelName': 'tag'}},
    // {path: '/forum_user', component: ObjectListView, props:{'modelName': 'user'}},
    // {path: '/new_tag', component: NewTagForm},
    // {path: '/tag_update', component: UpdateTagForm},
]

export default routes