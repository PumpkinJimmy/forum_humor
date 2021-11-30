<template>
    <div>
        <h3>Tags</h3>
        <table>
            <tr v-for="tag in tags" v-bind:key="tag">
                <td>{{tag.tname}}</td>
                <td>{{tag.hot_value}}</td>
            </tr>
        </table>
    </div>
</template>

<style>
    table {
        margin-left: auto;
        margin-right: auto;
        margin-top: 100px;
        margin-bottom: 100px;
    }
</style>

<script>
import axios from 'axios'
export default {
    name: 'TagView',
    data(){
        return {
            tags: []
        }
    },
    mounted(){
        axios
            .get('http://127.0.0.1:5000/api/tag')
            .then(response => (this.tags = response.data.data))
    }
}
</script>