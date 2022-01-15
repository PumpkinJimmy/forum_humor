<template>
  <v-row justify="center">
    <v-col cols="8">
      <v-row v-for="(post, idx) in posts" :key="idx">
        <v-col cols="1">
          <v-avatar color="primary" size="56">
            <v-icon dark> mdi-account-circle </v-icon>
          </v-avatar>
          <!-- <div>{{post.poster_uid}}</div> -->
        </v-col>
        <v-col cols="11">
          <v-card transition="scroll-y-reverse-transition" class="post">
            <v-card-title>{{
              post.title ? post.title : "Untitled"
            }}</v-card-title>
            <!-- <v-card-subtitle
            ><v-icon small>mdi-account</v-icon>Poster UID:
            {{ post.poster_uid }}</v-card-subtitle
          > -->
            <v-card-text>
              <v-row class="post-info">
                <v-col cols="4">
                  <v-icon small left>mdi-calendar</v-icon>Posted at
                  {{ post.post_time }}
                </v-col>
                <v-col cols="4">
                  <v-icon small left>mdi-calendar</v-icon>Last modified at
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
        </v-col>
      </v-row>
    </v-col>
  </v-row>
</template>
<style scoped>
.post {
  margin-bottom: 20px;
}
.post-info {
  margin-bottom: 20px;
}
.post-footer * {
  color: gray;
  font-size: 0.9em;
}
.post-content {
  text-align: left;
  min-height: 20vh;
}
</style>
<script>
import axios from "axios";
export default {
  name: "PostList",
  data() {
    return {
      posts: [],
      uris: [],
    };
  },
  mounted() {
    axios
      .get(
        "http://127.0.0.1:5000/api/v1/object/post/?limit=10&orderby=hot_value&desc=true"
      )
      .then((response) => {
        this.posts = response.data.objs;
        this.uris = response.data.uris;
      });
  },
};
</script>
