<template>
  <v-row justify="center">
    <v-col cols="8">
      <v-card class="tag-viewer">
        <v-card-title>标签一览</v-card-title>
        <v-row class="tag-list-header" justify="space-between">
          <v-col cols="3"> 标签 </v-col>
          <v-col> 累计点击量 </v-col>
          <v-col cols="7"> 热度 </v-col>
        </v-row>
        <hr />
        <div v-for="(tag, idx) of tags" :key="idx">
          <v-row
            class="tag-list-row"
            justify="space-between"
            @click="tagAccess(tag[0])"
          >
            <v-col cols="3">
              <v-chip class="primary"> # {{ tag[0] }} </v-chip>
            </v-col>
            <v-col>
              <div>{{ tag[1] }}</div>
            </v-col>
            <v-col cols="7">
              <hot-plot :tname="tag[0]" ratio="3" strokeWidth="5"></hot-plot>
            </v-col>
          </v-row>
          <hr />
        </div>
      </v-card>
    </v-col>
  </v-row>
</template>

<style scoped>
.tag-viewer {
  padding: 5vmin;
  min-height: 80vh;
}
.tag-list-row svg {
  max-height: 5vh;
}
.tag-list-row {
  padding-top: 2vh;
  padding-bottom: 2vh;
}
.tag-list-header {
  padding-top: 2vh;
  padding-bottom: 2vh;
}
hr {
  color: white;
}
</style>

<script>
import axios from "axios";
import HotPlot from "./HotPlot.vue";
export default {
  components: { HotPlot },
  name: "TagViewer",
  data() {
    return {
      tags: [],
    };
  },
  mounted() {
    this.query_tags();
  },
  methods: {
    query_tags() {
      axios
        .get(`http://${this.$store.state.api}/api/v1/query/tag_access/`)
        .then((resp) => {
          this.tags = resp.data.res;
        });
    },
    tagAccess(tname) {
      const uid = 2;
      axios
        .get(
          `http://${this.$store.state.api}/api/v1/log/tag_access/?uid=${uid}&tname=${tname}`
        )
        .then((resp) => {
          console.log(resp.data);
          this.query_tags();
        });
    },
  },
};
</script>