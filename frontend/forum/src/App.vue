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
        <v-col cols="8">
          <router-view></router-view>
        </v-col>
        <v-col cols="2">
          <v-card>
          <v-list>
            <v-subheader>Models</v-subheader>
            <v-list-item-group color="primary">
              <v-list-item
              v-for="modelName,idx in models"
              :key="idx"
              @click="route_to($event, `/object/${modelName}/`)"
              >{{modelName}}
              </v-list-item>
            </v-list-item-group>
          </v-list>
          </v-card>
        </v-col>
      </v-row>

      
      <!-- <HelloWorld/> -->
    </v-main>
  </v-app>
</template>

<script>
// import HelloWorld from './components/HelloWorld';
import axios from 'axios'
export default {
  name: "App",

  components: {
    // HelloWorld,
  },

  data: () => ({
    models: []
  }),

  mounted(){
    axios.get('http://127.0.0.1:5000/api/v1/model')
      .then((response)=>{
        this.models = response.data.models
      })
  },

  methods: {
    route_to(ev, loc) {
      this.$router.push(loc);
    },
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
