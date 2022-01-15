<template>
  <v-app>
    <v-app-bar app color="primary" dark hide-on-scroll>
      <v-icon left>mdi-reddit</v-icon>
      <v-toolbar-title>Forum Humor</v-toolbar-title>

      <v-spacer></v-spacer>

      <router-link :to="user_link">
        <v-btn text>
          <v-icon left>mdi-account-circle</v-icon>
          <span>{{ user ? user : "登录" }}</span>
        </v-btn>
      </router-link>

      <router-link to="/post/">
        <v-btn text>
          <v-icon left>mdi-note</v-icon>
          <span>帖子</span>
        </v-btn>
      </router-link>

      <router-link to="/post-edit/">
        <v-btn text>
          <v-icon left>mdi-lead-pencil</v-icon>
          <span>创作</span>
        </v-btn>
      </router-link>

      <v-btn text>
        <v-icon left>mdi-account-group</v-icon>
        <span>群组</span>
      </v-btn>

      <router-link to="/tags/">
        <v-btn text>
          <v-icon left>mdi-tag</v-icon>
          <span>话题</span>
        </v-btn>
      </router-link>

      <router-link to="/admin/panel/">
        <v-btn text>
          <v-icon left>mdi-database</v-icon>
          <span>管理</span>
        </v-btn>
      </router-link>

      <v-btn
        href="https://github.com/PumpkinJimmy/forum_humor"
        target="_blank"
        text
      >
        <v-icon>mdi-open-in-new</v-icon>
        <span class="mr-2">View on Github</span>
      </v-btn>
    </v-app-bar>

    <v-main class="main">
      <v-row justify="center">
        <v-col cols="10">
          <router-view></router-view>
        </v-col>
        <!-- <v-col cols="2">
          <HotBoard></HotBoard>
        </v-col> -->
      </v-row>
    </v-main>
  </v-app>
</template>

<script>
// import HotBoard from './components/HotBoard'
import axios from "axios";
// import bus from "./bus.js";
export default {
  name: "App",
  data: () => ({
    models: [],
  }),

  // components:{
  //   HotBoard
  // },
  mounted() {
    console.log(this.$store.state);
    // var self = this;
    // bus.$on("login", function (val) {
    //   self.user = val;
    // });
    axios
      .get("http://192.168.43.205:5000/api/v1/auth/login_status/")
      .then((resp) => {
        if (resp.data.status == "ok") {
          this.user = resp.data.username;
        }
      });
  },
  computed: {
    user(){
      return this.$store.state.user;
    },
    user_link() {
      if (this.user) {
        return `/user/${this.user}/`;
      } else {
        return "/login/";
      }
    },
  },
  methods: {},
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
div.links {
  display: flex;
  width: 100%;
  justify-content: space-around;
  flex-direction: row;
  border: 2px black solid;
}
.main {
  background-color: rgb(218, 224, 230);
}
</style>
