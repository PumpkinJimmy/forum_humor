<template>
    <div class="post-list">
        <v-card 
            v-for="(post, idx) in posts" 
            :key="idx"
            transition="scroll-y-reverse-transition"
            >
            <v-card-title>{{post.title?post.title:'Untitled'}}</v-card-title>
            <v-card-subtitle>Poster: {{ post.poster_uid}}</v-card-subtitle>
            <v-card-text>
                <div>
                    Posted at {{ post.post_time}}<br/>last modified at {{ post.last_modified_time}}
                </div>
                <div>
                    Hot value: {{post.hot_value}}
                </div>
                <div>
                {{post.content}}
                </div>
            </v-card-text>
        </v-card>
    </div>
</template>
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
        axios.get('http://127.0.0.1:5000/api/v1/object/post/?limit=10')
            .then((response)=>{
                this.posts = response.data.objs;
                this.uris = response.data.uris;
            })
    }
}

</script>
