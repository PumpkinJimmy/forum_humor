<template>
  <v-row justify="center">
    <v-col cols="8">
      <v-card class="post-edit">
        <v-card-text>
          <v-card-title>
            <v-row><v-col cols="12">发帖</v-col></v-row>
          </v-card-title>
          <v-row
            ><v-col cols="3">
              <v-avatar color="primary" size="56">
                <v-icon dark> mdi-account-circle </v-icon>
                
              </v-avatar>
              <div class="username">{{ user.username }}</div>
              <emotion-label></emotion-label>
            </v-col>
            <v-col cols="9">
              <v-text-field label="Title" v-model="title"></v-text-field>
              <v-textarea outlined label="Content" v-model="content"> </v-textarea>
            </v-col>
          </v-row>
          <v-row justify="end" align="center">
            <v-col cols="2"> 添加标签 </v-col>
            <v-col cols="7">
              <v-text-field label="Tags" v-model="tags_raw"> </v-text-field>
            </v-col>
          </v-row>
          <v-row justify="end">
            <v-col cols="3"><v-btn class="primary" depressed block @click="submitPost">提交</v-btn></v-col>
            <v-col cols="3"><v-btn depressed block>放弃</v-btn></v-col>
          </v-row>
        </v-card-text>
      </v-card>
    </v-col>
  </v-row>
</template>
<style scoped>
.username{
  margin: 2vh;
  font-size: 1.3em;
}
</style>
<script>
import axios from 'axios';
import EmotionLabel from './EmotionLabel.vue';
export default {
  components: { EmotionLabel },
  name: "PostEdit",
  data() {
    return {
      title: '',
      content: '',
      tags_raw: '',
    };
  },
  mounted(){
    if (!this.user){
      this.$router.push('/login/');
    }
  },
  computed: {
    user(){
      return this.$store.state.user;
    }
  },
  methods:{
    
    submitPost(){
      var data = {
        'post_time': new Date() / 1000,
        'last_modified_time': new Date() / 1000,
        'poster_uid': this.user.uid,
        'title': this.title.trim(),
        'content': this.content,
        'tags': this.tags_raw.trim().split(' '),
        'hot_value': 1
      }
      console.log(data);
      axios.post(`http://${this.$store.state.api}/api/v1/post/add/`, data)
        .then((resp)=>{
          console.log(resp)
          this.$router.push('/post/');
        })
        .catch((err)=>{
          console.log(err)
        })
    }
  }
};
</script>