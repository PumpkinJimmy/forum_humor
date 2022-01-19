<template>
    <v-list class="elevation-1">
        <v-header>帖子热门排行榜</v-header>
        <v-list-item
        v-for="(post, idx) in posts"
        :key="idx"
        
        >
        {{ post.title}}
        </v-list-item>
    </v-list>
</template>

<script>
export default {
    name: 'HotBoard',
    data(){
        return {
            posts:[
                {
                    title: 'Hey, Guys!',
                },
                {
                    title: 'Hey, Gay!',
                },
                {
                    title: 'Dick',
                }
            ]
        }
    }
}
</script>