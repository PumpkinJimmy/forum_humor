<template>
    <div class="tag-viewer">
        <v-chip v-for="(tag, idx) of tags" :key="idx" @click="tagAccess(tag[0])"
         >
            #{{ tag[0] }} 
            <v-avatar
            right
            class="green"
            >
                {{ tag[1] }}
            </v-avatar>
        </v-chip>
    </div>
</template>

<script>
import axios from 'axios';
export default {
    name: 'TagViewer',
    data(){
        return {
            tags: [],
        }
    },
    mounted(){
        this.query_tags();
    },
    methods:{
        query_tags(){
            axios.get('http://127.0.0.1:5000/api/v1/query/tag_access/')
            .then((resp)=>{
                this.tags = resp.data.res;
            })
        },
        tagAccess(tname){
            
            const uid = 2;
            axios.get(`http://127.0.0.1:5000/api/v1/log/tag_access/?uid=${uid}&tname=${tname}`)
                .then((resp)=>{
                    console.log(resp.data);
                    this.query_tags();
                })
        }
    }
}
</script>