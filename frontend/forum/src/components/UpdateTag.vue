<template>
    <div>
        <div>Current Editing Tag: {{ form_data.old_key.tname }}</div>
        <div>Tag Name: <input type="text"  v-model="form_data.new_value.tname"/></div>
        <div>Hot Value: <input type="text" v-model="form_data.new_value.hot_value"/></div>
        <button v-on:click="submit">提交更改</button>
        <button v-on:click="del">删除对象</button>
    </div>
    
</template>

<script>
// FIXME: Improper RESTful PUT
import axios from 'axios';
export default {
    name: 'UpdateTagForm',
    data() {
        return {
            form_data:{
                old_key: {},
                new_value: {}
            }
        }
    },
    methods: {
        submit(){
            axios.put('http://127.0.0.1:5000/api/tag', this.form_data)
            .then((response)=>{
                alert(JSON.stringify(response.data))
                this.$router.push({
                    path: '/tag'
                })
            })
        },
        del(){
            axios.delete('http://127.0.0.1:5000/api/tag/' + this.form_data.old_key.tname)
            .then((response)=>{
                alert(JSON.stringify(response.data))
                this.$router.push({
                    path: '/tag'
                })
            })
        }
    },
    mounted(){
        this.form_data.old_key = this.$route.query.key;
        
    }
}
</script>