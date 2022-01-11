<template>
    <div class="user-info">
        <v-card class="card">
            <v-row>
                <v-col cols="4">
        <v-avatar color="primary" size="56">
            <v-icon dark>
                mdi-account-circle
            </v-icon>
        </v-avatar>
                </v-col>
                <v-col cols="8">
                    {{user.uname}}
                </v-col>
            </v-row>
        </v-card>
        <v-spacer></v-spacer>
        <v-card class="card">
        {{ user }}
        </v-card>
    </div>
</template>

<style scoped>
    .card {
        margin-bottom: 5vh;
        padding: 7vmin;
    }
</style>

<script>
import axios from 'axios';
export default {
    name: 'UserInfo',
    props: ['uid'],
    data(){
        return {
            user: {}
        }
    },
    methods: {
        requestUserInfo(){
            axios.get(`http://127.0.0.1:5000/api/v1/object/user/${this.uid}/`)
                .then((resp)=>{
                    this.user = resp.data.obj;
                });
        }
    },
    mounted(){
        this.requestUserInfo();
    },
    watch: {
        uid(){
            this.requestUserInfo();
        }
    }
}
</script>