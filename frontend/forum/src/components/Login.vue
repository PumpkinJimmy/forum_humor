<template>
  <div class="login">
    <v-row justify="center">
      <v-col cols="5">
        <v-card>
          <v-card-title>Login</v-card-title>
          <v-card-text>
              Current login: {{ login_user }}
            <v-text-field label="Username" v-model="username"></v-text-field>
            <v-text-field label="Password" v-model="password" type="password"></v-text-field>
          </v-card-text>
          <v-card-actions class="pt-0">

            <v-btn @click="login" color="primary">Login</v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>
<script>
import axios from 'axios'
export default {
  name: "Login",
  data() {
    return {
      username: null,
      password: null,
      login_user: null,
    };
  },
  mounted(){
      axios.defaults.withCredentials=true;
      axios.get('http://127.0.0.1:5000/api/v1/auth/login_status/')
        .then((resp)=>{
            this.login_user = resp.data.username;
            console.log(resp.data);
        })
  },
  methods:{
      login(){
          axios.post('http://127.0.0.1:5000/api/v1/auth/login/', {
              username: this.username,
              password: this.password
          })
          .then((resp)=>{
              this.login_user = resp.data.username;
          })
      }
  }
};
</script>