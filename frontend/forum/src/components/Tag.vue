<template>
    <div>
        <h3>Tags</h3>
        <table>
            <tr v-for="tag in tags" v-bind:key="tag[0]">
                <td>{{tag.tname}}</td>
                <td>{{tag.hot_value}}</td>
            </tr>
        </table>
        <router-link to='/new_tag'><button>New Tag</button></router-link>
    </div>
</template>

<style>
    table {
        margin-left: auto;
        margin-right: auto;
        margin-top: 100px;
        margin-bottom: 100px;
        border: 1px black solid;
    }
    td {
        border: 1px black solid;
        min-width: 100px;
    }
</style>

<script>
import axios from 'axios'
export default {
    name: 'TagView',
    data(){
        return {
            tags: [
                {
                    tname: 'A',
                    hot_value: 10
                },
                {
                    tname: 'B',
                    hot_value: 20
                },
                {
                    tname: 'Arknight',
                    hot_value: 100
                },
                {
                    tname: 'Yuan Shen',
                    hot_value: 10000
                }
            ]

        }
    },
    mounted(){
        axios
            .get('http://127.0.0.1:5000/api/tag')
            .then(response => (this.tags = response.data.data))
    },
    methods: {
    }
}
</script>