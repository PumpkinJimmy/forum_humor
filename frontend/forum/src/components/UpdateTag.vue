<template>
    <div>
        <div>Current Editing Tag: {{ pk }}</div>
        <div>Tag Name: <input type="text"  v-model="new_value.tname"/></div>
        <div>Hot Value: <input type="text" v-model="new_value.hot_value"/></div>
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
            pk: null,
            new_value: {}
        }
    },
    methods: {
        submit(){
            axios.put('http://127.0.0.1:5000' + this.uri, this.new_value)
            .then((response)=>{
                alert(JSON.stringify(response.data))
                this.$router.push({
                    path: '/tag'
                })
            })
        },
        del(){
            axios.delete('http://127.0.0.1:5000' + this.uri)
            .then((response)=>{
                alert(JSON.stringify(response.data))
                this.$router.push({
                    path: '/tag'
                })
            })
        }
    },
    mounted(){
        // FIXME: use VUEX cache instead of repeated query
        this.uri = this.$route.query.uri
        axios.get('http://127.0.0.1:5000' + this.uri)
            .then(response=>{
                this.new_value = response.data.row
            })
        
    }
}
</script>