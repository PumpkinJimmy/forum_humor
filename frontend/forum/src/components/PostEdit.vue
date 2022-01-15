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
              <div>User Name</div>
            </v-col>
            <v-col cols="9">
              <v-text-field label="Title"></v-text-field>
              <v-textarea outlined label="Content"> </v-textarea>
            </v-col>
          </v-row>
          <v-row justify="end">
            <v-col cols="2"> 添加标签 </v-col>
            <v-col cols="7">
              <v-text-field label="Tags"> </v-text-field>
            </v-col>
          </v-row>
          <v-row justify="end">
            <v-col cols="3"><v-btn class="primary" depressed block>提交</v-btn></v-col>
            <v-col cols="3"><v-btn depressed block>放弃</v-btn></v-col>
          </v-row>
        </v-card-text>
      </v-card>
    </v-col>
  </v-row>
</template>
<script>
export default {
  name: "PostEdit",
  data() {
    return {};
  },
};
</script>