<template>
  <v-data-table
    :headers="headers"
    :items="users"
    :items-per-page="5"
    class="elevation-1"
  ></v-data-table>
</template>
<script>
import axios from 'axios'

export default {
    data(){
        return {
            headers: [
                {text: "UID", value: 'uid'},
                {text: "Name", value: 'name'},
                {text: "Humor", value: 'humor'},
                {text: "Tag", value: 'tag'},
            ],
            users: []
        }
    },
    mounted(){
        // this.users = [
        //     {uid: '001',
        //     name: 'dxj',
        //     humor: 10,
        //     tag: 'anime'},
        //     {uid: '002',
        //     name: 'dq',
        //     humor: 20,
        //     tag: 'all'},
        // ]
        axios
            .get('http://localhost:5000/api/allusers')
            .then(response => {
                console.log(response.data.users)
                this.users = response.data.users
            })
            // .get('http://localhost:5000/api/allusers')
            
    }
}
</script>
