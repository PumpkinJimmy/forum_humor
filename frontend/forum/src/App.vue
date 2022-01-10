<template>
  <v-app>
    <v-app-bar app color="primary" dark>
      <div class="d-flex align-center">
        Forum Humor
      </div>

      <v-spacer></v-spacer>

      <v-btn
        href="https://github.com/PumpkinJimmy/forum_humor"
        target="_blank"
        text
      >
        <span class="mr-2">View on Github</span>
        <v-icon>mdi-open-in-new</v-icon>
      </v-btn>
    </v-app-bar>

    <v-main>
      <v-row justify="center">
        <v-col cols="10">
          <router-view></router-view>
        </v-col>
      </v-row>
    </v-main>
  </v-app>
</template>

<script>

export default {
  name: "App",
  data: () => ({
    models: []
  }),
  methods: {
  },
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
</style>
