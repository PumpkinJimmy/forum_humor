<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <tag-view></tag-view>
    <router-link to="/tag">Tags</router-link>
    <router-view></router-view>
  </div>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
import TagView from './components/Tag.vue'
export default {
  name: 'App',
  components:{
    TagView
  }
  // components: {
  //   HelloWorld
  // }
}
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
</style>
