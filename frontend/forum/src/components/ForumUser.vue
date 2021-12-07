<template>
    <div class="forum-user-com">
        <h3>ForumUsers</h3>
        <table>
            <tr v-for="user in forum_users" v-bind:key="user[0]">
                <td>{{user.uid}}</td>
                <td>{{user.password}}</td>
                <td>{{user.uname}}</td>
                <td>{{user.gender}}</td>
                <td>{{user.email}}</td>
                <td>{{user.signature}}</td>
            </tr>
        </table>
    </div>
</template>

<style>
    .forum-user-com table {
        margin-left: auto;
        margin-right: auto;
        margin-top: 100px;
        margin-bottom: 100px;
        border: 1px black solid;
    }
    .forum-user-com td {
        border: 1px black solid;
        min-width: 100px;
    }
</style>

<script>
import axios from 'axios'
export default {
    name: 'ForumUserView',
    data(){
        return {
            forum_users: [
            ]

        }
    },
    mounted(){
        axios
            .get('http://127.0.0.1:5000/api/v1/object/user/')
            .then(response => (this.forum_users = response.data.objs))
    }
}
</script>