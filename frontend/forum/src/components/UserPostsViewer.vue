<template>
    <div class="query-user-post">
        <div><v-chip>{{em_type}}</v-chip></div>
        User: <v-text-field v-model="uid"></v-text-field><v-btn @click="query">Query</v-btn><br/>
        Emotions:{{ emotions}}<br/>
        Counts:{{em_count}}<br/>
        <v-data-table
        :headers="headers"
        :items="rows"
        ></v-data-table>
    </div>
</template>
<script>
import axios from 'axios';
export default {
    name: 'UserPostsViewer',
    data(){
        return {
            rows: [],
            uid: 3545,
            emotions: {},
            em_count: {},
            headers: [
                {
                    'text': 'Post ID',
                    'value': 'pid'
                },
                {
                    'text': 'Title',
                    'value': 'title'
                },
                {
                    'text': 'Content',
                    'value': 'content'
                }
            ],
        };
    },
    computed:{
        em_type(){
            for (var k in this.emotions){
                if (this.emotions[k]>0.3){
                    return k;
                }
            }
            return 'no sure';
        }
    },
    methods:{
        query(){
        axios.get(`http://127.0.0.1:5000/api/v1/query/user_posts/${this.uid}/`).then((resp)=>{
            const raw_rows = resp.data.data[0];
            const h = resp.data.data[1];
            var rows = [];
            const idx = [h.indexOf('pid'), h.indexOf('title'), h.indexOf('content')];
            for (var row of raw_rows){
                rows.push({
                    pid: row[idx[0]],
                    title: row[idx[1]],
                    content: row[idx[2]],
                })
            }
            this.rows = rows;
        })
        axios.get(`http://127.0.0.1:5000/api/v1/ml/infer_user/${this.uid}/`).then((resp)=>{
            const data = resp.data.res;
            var total = {
                anger: 0,
                fear: 0,
                joy: 0,
                love: 0,
                sadness: 0,
                surprise: 0
            }
            var count = {
                anger: 0,
                fear: 0,
                joy: 0,
                love: 0,
                sadness: 0,
                surprise: 0,
                complex: 0,
            }
            for (var em of data){
                var s = 0;
                for (var k in em){
                    s += Math.exp(em[k])
                }
                var max_em = null, max_em_p = 0;
                for (k in em){
                    em[k] = Math.exp(em[k])/s;
                    total[k] += em[k] / data.length;
                    if (em[k] > max_em_p) {
                        max_em_p = em[k];
                        max_em = k;
                    }
                }
                if (max_em_p > 0.5){
                    count[max_em]+=1;
                }
                else{
                    count.complex += 1;
                }
            }
            this.emotions = total;
            this.em_count = count;
        })
    },
    },
    mounted(){
        this.query()
    }
}
</script>