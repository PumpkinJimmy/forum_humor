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
            <v-tabs>
              <v-tab>帖子</v-tab>
              <v-tab>群组</v-tab>
              <v-tab>关注话题</v-tab>
              <v-tab>情绪分析</v-tab>
              <v-tab>热度分析</v-tab>
            </v-tabs>
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
      user: {},
    };
  },
  methods: {
    requestUserInfo() {
      axios
        .get(`http://192.168.43.205:5000/api/v1/object/user/${this.uid}/`)
        .then((resp) => {
          this.user = resp.data.obj;
        });
    },
  },
  mounted() {
    this.requestUserInfo();
  },
  watch: {
    uid() {
      this.requestUserInfo();
    },
  },
};
</script>