<template>
  <div class="crud-view elevation-2">
    <dialog-edit-object
    v-model="dialogEdit"
    :form="form"
    :type="dialogType">
    </dialog-edit-object>
    <v-row justify="center">
      <v-col cols="12">
        <v-data-table
          :headers="headers"
          :items="rows"
          :server-items-length="serverLength"
          :loading="loading"
          @click:row="onClickRow"
          @update:options="onPaginate"
          class="elevation-1"
        >
          <template v-slot:top>
            <v-toolbar flat>
              <v-toolbar-title>{{ modelName }}</v-toolbar-title>
              <v-divider class="mx-4" inset vertical></v-divider>
              <v-spacer></v-spacer>
              <v-btn class="mx-2" small fab color="indigo"
              @click="onNew">
                <v-icon dark> mdi-plus </v-icon>
              </v-btn>
            </v-toolbar>
          </template>
          <template v-slot:no-data>
            <v-btn color="primary" @click="initialize"> Reset </v-btn>
          </template>
        </v-data-table>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import axios from "axios";
import DialogEditObject from "./DialogEditObject.vue";
export default {
  name: "ObjectListEdior",
  props: ["modelName"],
  components: {
    DialogEditObject,
  },
  data() {
    return {
      rows: [],
      headers: [],
      model: {},
      serverLength: 100,
      loading: false,
      dialogEdit: false,
      dialogType: 'create',
      form: [],
      default_headers: [
        {
          text: "Tag Name",
          value: "tname",
        },
        {
          text: "Hot Value",
          value: "hot_value",
        },
      ],
      default_rows: [
        {
          tname: "A",
          hot_value: 10,
          uri: 1,
        },
        {
          tname: "B",
          hot_value: 20,
          uri: 2,
        },
        {
          tname: "Arknight",
          hot_value: 100,
          uri: 3,
        },
        {
          tname: "Yuan Shen",
          hot_value: 10000,
          uri: 4,
        },
      ],
    };
  },
  mounted() {
    this.renderEditor();
  },
  methods: {
    getObjects(limit, offset) {
      if (this.serverLength == 0) return;
      this.loading = true;
      var api;
      if (limit == undefined) {
        api = `http://127.0.0.1:5000/api/v1/object/${this.modelName}/`;
      } else {
        api = `http://127.0.0.1:5000/api/v1/object/${this.modelName}/?offset=${offset}&limit=${limit}`;
      }
      axios.get(api).then((response) => {
        this.rows = response.data.objs;
        var uris = response.data.uris;
        for (var i = 0; i < uris.length; i++) {
          this.rows[i].idx = i;
        }
        axios
        .get(`http://127.0.0.1:5000/api/v1/form/${this.modelName}/`)
        .then((response) => {
          this.model = response.data.model;
        })
        .catch((err) => {
          console.error(err);
          this.formFailAlert = true;
          this.model.attrs = Object.keys(this.rows[0]);
          this.headers = this.model.attrs.map((a) => {
            return {
              text: a,
              value: a,
            };
          });
        });
        this.loading = false;
      });
    },
    renderEditor() {
      axios
        .get(
          `http://127.0.0.1:5000/api/v1/object/${this.modelName}/?count_only=true`
        )
        .then((response) => {
          this.serverLength = response.data.count;
          this.getObjects(15, 0);
        })
        .catch(() => {
          this.serverLength = 0;
        });
        
    },
    onNew(){
      this.dialogType = "create";
      const keys = Object.keys(this.rows[0]);
      this.form = Object.fromEntries(keys.map((k)=>[k,null]));
      this.dialogEdit = true;
    },
    onClickRow(item) {
      this.dialogType = "edit";
      this.form = this.rows[item.idx];
      this.dialogEdit = true;
    },
    onPaginate(options) {
      const { page, itemsPerPage } = options;
      const offset = itemsPerPage * (page - 1);
      const limit = itemsPerPage;
      
      this.getObjects(limit, offset);
    },
  },
  computed: {},
  watch: {
    modelName() {
      this.renderEditor();
    },
  },
};
</script>
