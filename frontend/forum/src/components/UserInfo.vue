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
        </v-card>
        <v-spacer></v-spacer>
        <v-card class="card">
          <v-row>
            <v-col cols="12">
              <v-tabs-items v-model="tab">
                <v-tab-item value="tab-posts">
                  
                  <div v-for="(post, idx) in posts" :key="idx">
                    <v-card
                      transition="scroll-y-reverse-transition"
                      class="post elevation-1"
                    >
                      <v-card-title>{{
                        post.title ? post.title : "Untitled"
                      }}</v-card-title>
                      <v-card-text>
                        <v-row class="post-info">
                          <v-col cols="4">
                            <v-icon small left>mdi-calendar</v-icon>Posted at
                            {{ post.post_time }}
                          </v-col>
                          <v-col cols="4">
                            <v-icon small left>mdi-calendar</v-icon>Last
                            modified at
                            {{ post.last_modified_time }}
                          </v-col>
                          <v-col cols="4">
                            <v-icon small left>mdi-fire</v-icon>Hot value:
                            {{ post.hot_value }}
                          </v-col>
                        </v-row>
                        <v-row class="post-content" justify="center">
                          <v-col cols="10">
                            {{ post.content }}
                          </v-col>
                        </v-row>
                      </v-card-text>
                      <v-card-actions>
                        <v-row class="post-footer">
                          <v-col cols="4"><v-icon>mdi-tag</v-icon>Tag</v-col>
                          <v-col cols="2"><v-btn text>热度(10)</v-btn></v-col>
                          <v-col cols="2"><v-btn text>评论(5)</v-btn></v-col>
                          <v-col cols="2"><v-btn text>查看全文</v-btn></v-col>
                          <v-col cols="2">
                            <v-btn class="ma-2" text icon color="red lighten-2">
                              <v-icon>mdi-thumb-up</v-icon>
                            </v-btn>
                          </v-col>
                        </v-row>
                      </v-card-actions>
                    </v-card>
                  </div>
                  
                </v-tab-item>
                <v-tab-item value="tab-groups">
                  <div>hehe</div>
                </v-tab-item>
                <v-tab-item value="tab-tags">
                  <div>hehe</div>
                </v-tab-item>
                <v-tab-item value="tab-emotion">
                  <emotion-pie :emotion="emotion"></emotion-pie>
                </v-tab-item>
                <v-tab-item value="tab-hot">
                  <div>hehe</div>
                </v-tab-item>
              </v-tabs-items>
            </v-col>
          </v-row>
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

.post{
  margin-bottom: 5vh;
}
</style>

<script>
import axios from "axios";
import EmotionPie from './EmotionPie.vue';
export default {
  name: "UserInfo",
  props: ["uid"],
  data() {
    return {
      tab: null,
      posts: [],
      headers: [],
      emotion: {},
    };
  },
  components:{ EmotionPie},
  methods: {
    requestUserInfo() {
      axios
        .get(
          `http://${this.$store.state.api}/api/v1/query/user_posts/${this.user.uid}/`
        )
        .then((resp) => {
          this.posts = resp.data.data[0];
          this.headers = resp.data.data[1];
        });
      axios
        .get(
          `http://${this.$store.state.api}/api/v1/ml/infer_user/${this.user.uid}/`
        )
        .then((resp)=>{
          alert(resp.data);
          this.emotion = resp.data.res[0];
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
    user() {
      return this.$store.state.user;
    },
  },
};
</script>