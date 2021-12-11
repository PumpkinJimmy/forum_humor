<template>
  <div class="object-view">
    <v-row>
      <v-col cols="12">
        <v-alert :value="formFailAlert" type="error">
          Model meta data unaccessiable. Form below may unavailable.
        </v-alert>
      </v-col>
    </v-row>
    <v-row justify="center">
      <v-col cols="12">
        <h3>Tags</h3>
      </v-col>
    </v-row>
    <v-row justify="center">
      <v-col cols="8">
        <v-data-table :headers="headers" :items="rows" class="elevation-1">
          <template v-slot:top>
            <v-toolbar flat>
              <v-toolbar-title>{{ formTitle }}</v-toolbar-title>
              <v-divider class="mx-4" inset vertical></v-divider>
              <v-spacer></v-spacer>
              <v-dialog v-model="dialog" max-width="500px">
                <template v-slot:activator="{ on, attrs }">
                  <v-btn
                    color="primary"
                    dark
                    class="mb-2"
                    v-bind="attrs"
                    v-on="on"
                  >
                    New Item
                  </v-btn>
                </template>
                <v-card>
                  <v-card-title>
                    <span class="text-h5">New Object</span>
                  </v-card-title>

                  <v-card-text>
                    <v-container>
                      <v-row>
                        <v-col
                          v-for="(attr, idx) in model.attrs"
                          :key="idx"
                          cols="12"
                          sm="6"
                          md="4"
                        >
                          <v-text-field
                            v-model="editedItem[attr]"
                            :label="attr"
                          ></v-text-field>
                        </v-col>
                      </v-row>
                    </v-container>
                  </v-card-text>

                  <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="blue darken-1" text @click="close">
                      Cancel
                    </v-btn>
                    <v-btn color="blue darken-1" text @click="save">
                      Save
                    </v-btn>
                  </v-card-actions>
                </v-card>
              </v-dialog>
              <v-dialog v-model="dialogDelete" max-width="500px">
                <v-card>
                  <v-card-title class="text-h5"
                    >Are you sure you want to delete this item?</v-card-title
                  >
                  <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="blue darken-1" text @click="closeDelete"
                      >Cancel</v-btn
                    >
                    <v-btn color="blue darken-1" text @click="deleteItemConfirm"
                      >OK</v-btn
                    >
                    <v-spacer></v-spacer>
                  </v-card-actions>
                </v-card>
              </v-dialog>
            </v-toolbar>
          </template>
          <template v-slot:item.actions="{ item }">
            <v-icon small class="mr-2" @click="editItem(item)">
              mdi-pencil
            </v-icon>
            <v-icon small @click="deleteItem(item)"> mdi-delete </v-icon>
          </template>
          <template v-slot:no-data>
            <v-btn color="primary" @click="initialize"> Reset </v-btn>
          </template>
        </v-data-table>
      </v-col>
    </v-row>
  </div>
</template>

<style>
</style>

<script>
import axios from "axios";
export default {
  name: "ObjectListView",
  props: ['modelName'],
  data() {
    return {
      rows: [
        {
          tname: "A",
          hot_value: 10,
        },
        {
          tname: "B",
          hot_value: 20,
        },
        {
          tname: "Arknight",
          hot_value: 100,
        },
        {
          tname: "Yuan Shen",
          hot_value: 10000,
        },
      ],
      uris: [],
      headers: [],
      dialog: false,
      dialogDelete: false,
      editedIndex: -1,
      editedItem: {
        tname: "",
        hot_value: 0,
      },
      defaultItem: {
        tname: "",
        hot_value: 0,
      },
      model: {},
      formFailAlert: false,
    };
  },
  mounted() {
    this.renderView();
  },
  methods: {
    renderView(){
      axios.get(`http://127.0.0.1:5000/api/v1/object/${this.modelName}/`).then((response) => {
      this.rows = response.data.objs;
      this.uris = response.data.uris;
    });
    axios
      .get(`http://127.0.0.1:5000/api/v1/form/${this.modelName}/`)
      .then((response) => {
        this.model = response.data.model;
      })
      .catch((err) => {
        console.error(err);
        this.formFailAlert = true;
        this.model.attrs = Object.keys(this.rows[0]);
        this.headers = this.model.attrs
          .map((a) => {
            return {
              text: a,
              value: a,
            };
          })
          .concat([
            {
              text: "Actions",
              value: "actions",
            },
          ]);
      });
    },
    selectRow(idx) {
      // alert(JSON.stringify(k));
      this.$router.push({
        path: "/tag_update",
        query: {
          uri: this.uris[idx],
        },
      });
    },
    editItem(item) {
      this.editedIndex = this.rows.indexOf(item);
      this.editedItem = Object.assign({}, item);
      this.dialog = true;
    },

    deleteItem(item) {
      this.editedIndex = this.rows.indexOf(item);
      this.editedItem = Object.assign({}, item);
      this.dialogDelete = true;
    },

    deleteItemConfirm() {
      this.rows.splice(this.editedIndex, 1);
      this.closeDelete();
    },

    close() {
      this.dialog = false;
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
      });
    },

    closeDelete() {
      this.dialogDelete = false;
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
      });
    },

    save() {
      if (this.editedIndex > -1) {
        Object.assign(this.rows[this.editedIndex], this.editedItem);
      } else {
        this.rows.push(this.editedItem);
      }
      this.close();
    },
  },
  computed: {
    formTitle() {
      return this.editedIndex === -1 ? "New Item" : "Edit Item";
    },
  },

  watch: {
    dialog(val) {
      val || this.close();
    },
    dialogDelete(val) {
      val || this.closeDelete();
    },
    modelName(){
      this.renderView()
    }
  },

  created() {
    //   this.initialize()
  },
};
</script>