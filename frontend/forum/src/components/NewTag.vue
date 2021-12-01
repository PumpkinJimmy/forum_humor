<template>
    <div>
        <div>Tag Name: <input type="text"  v-model="new_data.tname"/></div>
        <div>Hot Value: <input type="text" v-model="new_data.hot_value"/></div>
        <button v-on:click="submit">提交</button>
    </div>
    
</template>

<script>
import axios from 'axios'
export default {
    name: 'NewTagForm',
    data() {
        return {
            new_data: {
                tname: 'OS',
                hot_value: 0
            }
        }
    },
    methods: {
        submit(){
            axios.post(
                'http://127.0.0.1:5000/api/tag',
                this.new_data)
                .then(response=>{
                    alert(JSON.stringify(response.data));
                    this.$router.push({
                        path: '/tag'
                    });
                })
        }
    }
}
</script>