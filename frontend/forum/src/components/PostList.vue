<template>
    <div class="post-list">
        <v-card 
            v-for="(post, idx) in posts" 
            :key="idx"
            transition="scroll-y-reverse-transition"
            >
            <v-card-title>{{post.title?post.title:'Untitled'}}</v-card-title>
            <v-card-subtitle><v-icon small>mdi-account</v-icon>Poster UID: {{ post.poster_uid}}</v-card-subtitle>
            <v-card-text>
                <v-row class="post-info">
                    <v-col cols=4>
                    <v-icon small>mdi-calendar</v-icon>Posted at {{ post.post_time}}
                    </v-col>
                    <v-col cols=4>
                    <v-icon small>mdi-calendar</v-icon>Last modified at {{ post.last_modified_time}}
                    </v-col>
                    <v-col cols=4>
                    <v-icon small>mdi-fire</v-icon>Hot value: {{post.hot_value}}
                    </v-col>
                </v-row>
                <v-row class="post-content" justify="center">
                    <v-col cols=10>
                {{post.content}}
                    </v-col>
                </v-row>
            </v-card-text>
        </v-card>
    </div>
</template>
<style scoped>
    .post-info{
        margin-bottom: 20px;
    }
    .post-content{
        text-align: left;
    }
</style>
<script>
import axios from 'axios'
export default {
    name: 'PostList',
    data(){
        return {
            posts: [],
            uris: []
        }
    },
    mounted(){
        axios.get('http://127.0.0.1:5000/api/v1/object/post/?limit=10&orderby=pid&desc=true')
            .then((response)=>{
                this.posts = response.data.objs;
                this.uris = response.data.uris;
            })
    }
}

</script>
