<template>
  <v-row justify="center">
    <v-col cols="8">
      <v-card class="tag-viewer">
        <v-card-title class="text-h3">话题一览</v-card-title>
        <v-chip
          v-for="(tag, idx) of tags"
          :key="idx"
          @click="tagAccess(tag[0])"
        >
          #{{ tag[0] }}
          <v-avatar right class="green">
            {{ tag[1] }}
          </v-avatar>
        </v-chip>
      </v-card>
    </v-col>
  </v-row>
</template>

<style scoped>
.tag-viewer {
  padding: 5vmin;
  min-height: 80vh;
}
</style>

<script>
import axios from "axios";
export default {
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
        .get("http://127.0.0.1:5000/api/v1/query/tag_access/")
        .then((resp) => {
          this.tags = resp.data.res;
        });
    },
    tagAccess(tname) {
      const uid = 2;
      axios
        .get(
          `http://127.0.0.1:5000/api/v1/log/tag_access/?uid=${uid}&tname=${tname}`
        )
        .then((resp) => {
          console.log(resp.data);
          this.query_tags();
        });
    },
  },
};
</script>