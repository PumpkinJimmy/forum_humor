<template>
    <div>
        <h3>Tags</h3>
        <table>
            <tr v-for="(tag, idx) in rows" v-bind:key="idx" v-on:click="selectRow(idx)">
                <td v-for="(k, j) in header" v-bind:key="j">{{ tag[k] }}</td>
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
    tr:hover {
        background-color: yellow;
    }
</style>

<script>
import axios from 'axios'
export default {
    name: 'TagView',
    data(){
        return {
            rows: [
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
            ],
            uris: [],
            header: []
        }
    },
    mounted(){
        axios
            .get('http://127.0.0.1:5000/api/v1/object/tag/')
            .then(response => {
                this.rows = response.data.objs;
                this.uris = response.data.uris;
            });
        axios.get('http://127.0.0.1:5000/api/v1/form/tag/')
            .then(response => {
                this.header = response.data.layout;
            });
    },
    methods: {
        selectRow(idx){
            // alert(JSON.stringify(k));
            this.$router.push({
                path: '/tag_update', 
                query: {
                    uri: this.uris[idx]
                }
            })
        }
    }
}
</script>