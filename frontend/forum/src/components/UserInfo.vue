<template>
  <v-row justify="center">
    <v-col cols="8">
      <div class="user-info">
        <v-card class="card">
          <v-row>
            <v-col cols="1">
              <v-avatar color="primary" size="56">
                <v-icon dark> mdi-account-circle </v-icon>
              </v-avatar>
            </v-col>
            <v-col cols="3">
              <div>{{ user.uname }}<v-chip>Unknown</v-chip></div>
              <div>{{ user.email }}</div>
            </v-col>
          </v-row>
          <v-row>
            <v-tabs v-model="tab">
              <v-tab href="#tab-posts">帖子</v-tab>
              <v-tab href="#tab-groups">群组</v-tab>
              <v-tab href="#tab-tags">关注话题</v-tab>
              <v-tab href="#tab-emotion">情绪分析</v-tab>
              <v-tab href="#tab-hot">热度分析</v-tab>
            </v-tabs>
          </v-row>
          <v-row>
            <v-col cols="12">
          <v-tabs-items v-model="tab">
            <v-tab-item value="tab-posts">
              <div v-for="(post, idx) of posts" :key="idx">
                {{post}}
              </div>
            </v-tab-item>
            <v-tab-item value="tab-groups">
              <div>hehe</div>
            </v-tab-item>
            <v-tab-item value="tab-tags">
              <div>hehe</div>
            </v-tab-item>
            <v-tab-item value="tab-emotion">
              <div>hehe</div>
            </v-tab-item>
            <v-tab-item value="tab-hot">
              <div>hehe</div>
            </v-tab-item>
          </v-tabs-items>
            </v-col>
          </v-row>
        </v-card>
        <v-spacer></v-spacer>
        <v-card class="card">
          {{ user }}
        </v-card>
      </div>
    </v-col>
  </v-row>
</template>

<style scoped>
.card {
  margin-bottom: 5vh;
  padding: 7vmin;
}
</style>

<script>
import axios from "axios";
export default {
  name: "UserInfo",
  props: ["uid"],
  data() {
    return {
      tab: null,
      posts: [],
      headers: []
    };
  },
  methods: {
    requestUserInfo() {
      axios.get(`http://${this.$store.state.api}/api/v1/query/user_posts/${this.user.uid}/`)
      .then((resp)=>{
        this.posts = resp.data.data[0];
        this.headers = resp.data.data[1];
      })
      // axios
      //   .get(`http://${this.$store.state.api}/api/v1/object/user/${this.user.uid}/`)
      //   .then((resp) => {
      //     this.user = resp.data.obj;
      //     
      //   });
    },
  },
  mounted() {
    this.requestUserInfo();
  },
  computed: {
    user(){
      return this.$store.state.user;
    }
  },
};
</script>