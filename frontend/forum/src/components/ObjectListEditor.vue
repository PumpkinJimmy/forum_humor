<template>
  <div class="crud-view elevation-2">
    <v-alert 
    :type="alertType"
    v-model="alerting"
    dismissible
    transition="slide-y-transition"
    >
    {{ alertMsg }}
    </v-alert>
    <dialog-edit-object
    v-model="dialogEdit"
    :model="model"
    :init_obj="editItem"
    :op="editOp"
    @create="create"
    @update="update"
    @del="del">
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
      uris: [],
      headers: [],
      model: {},
      serverLength: 100,
      loading: false,
      dialogEdit: false,
      form: [],
      editItem: {
      },
      editIdx: -1,
      editOp: 'create',
      alerting: false,
      alertMsg: "",
      alertType: "success",
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
    getModelInfo(){
      axios
        .get(`http://192.168.43.205:5000/api/v1/model/${this.modelName}/`)
        .then((response) => {
          this.model = response.data.model_info;
          this.headers = [];
          const fields = this.model.fields;
          fields.sort((a,b)=>(a.idx>b.idx));
          for (var field of fields){
            this.headers.push({
              text: field.label,
              value: field.name
            })
          }
        })
        .catch((err) => {
          console.error(err);
          this.formFailAlert = true;
        });
    },
    getObjects(limit, offset, orderby, desc) {
      if (this.serverLength == 0) return;
      var api;
      if (limit == undefined) {
        api = `http://192.168.43.205:5000/api/v1/object/${this.modelName}/?`;
      } else {
        api = `http://192.168.43.205:5000/api/v1/object/${this.modelName}/?offset=${offset}&limit=${limit}`;
      }
      if (orderby){
        api += `&orderby=${orderby}`
      }
      if (desc){
        api += `&desc=true`
      }
      axios.get(api).then((response) => {
        this.rows = response.data.objs;
        this.uris = response.data.uris;
      });
    },
    renderEditor() {
      this.loading = true;
      axios
        .get(
          `http://192.168.43.205:5000/api/v1/object/${this.modelName}/?count_only=true`
        )
        .then((response) => {
          this.serverLength = response.data.count;
          this.getModelInfo();
          this.getObjects(15, 0);
          this.loading = false;
        })
        .catch(() => {
          this.serverLength = 0;
          this.getModelInfo();
          this.loading = false;

        });
        
    },
    copyData(d){
      return JSON.parse(JSON.stringify(d));
    },
    onNew(){
      this.editIdx = -1;
      this.editItem = this.copyData(this.model.default);
      this.editOp = 'create';
      this.dialogEdit = true;
    },
    onClickRow(item,other) {
      this.editOp = 'update';
      this.editIdx = other.index;
      this.editItem = this.copyData(this.rows[other.index]);
      this.dialogEdit = true;
    },
    onPaginate(options) {
      const { page, itemsPerPage, sortBy,sortDesc } = options;
      const offset = itemsPerPage * (page - 1);
      const limit = itemsPerPage;
      
      this.getObjects(limit, offset, sortBy[0], sortDesc[0]);
    },
    reset(){
      this.editIdx = -1;
      this.editItem = {};
    },
    create(obj){
      axios.post(`http://192.168.43.205:5000/api/v1/object/${this.modelName}/`, obj)
        .then((response)=>{
          console.log(`Create status: ${response.data.status}`);
          this.alertType = response.data.status
          this.alertMsg = `Create status: ${response.data.status}`
          this.alerting = true
          this.reset();
          this.renderEditor();
        })
        .catch((err)=>{
          this.alertType = "error"
          this.alertMsg = err.message
          this.alerting = true
          this.reset()
        })
    },
    update(obj){
      axios.put(`http://192.168.43.205:5000${this.uris[this.editIdx]}`, obj)
          .then((response)=>{
            console.log(`Update status: ${response.data.status}`)
            if (response.data.status == 'success'){
              this.alertType = "success"
              this.alertMsg = `Update status: ${response.data.status}`
              this.alerting = true
              Object.assign(this.rows[this.editIdx], obj);
              this.uris[this.editIdx] = response.data.uri;
            }
            else{
              this.alertType = "error"
              this.alertMsg = `Update status: ${response.data.status}`
              this.alerting = true
            }
            this.reset();
          })
          .catch((err)=>{
            console.log("Update failed")
            this.alertType = "error"
            this.alertMsg = err.message
            this.alerting = true
            this.reset();
          })
    },
    del(){
      axios.delete(`http://192.168.43.205:5000${this.uris[this.editIdx]}`)
        .then((response)=>{
            console.log(`Delete status: ${response.data.status}`)
            this.alertType = "success"
            this.alertMsg = `Delete status: ${response.data.status}`
            this.alerting = true
            this.reset();
            this.renderEditor();
          })
          .catch((err)=>{
            console.log("Delete failed")
            console.log(err)
            this.alertType = "error"
            this.alertMsg = err.message
            this.alerting = true
            this.reset();
          })
    }
  },
  computed: {},
  watch: {
    modelName() {
      this.reset();
      this.renderEditor();
    },
  },
};
</script>
