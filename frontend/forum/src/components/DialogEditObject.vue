<template>
  <v-dialog v-model="value" max-width="500px">
    <v-card>
      <v-card-title>
        <span class="text-h5">{{
          op == "create" ? "Create Object" : "Edit Object"
        }}</span>
      </v-card-title>

      <v-card-text>
        <v-container>
          <v-row v-for="(finfo, idx) in model.fields" :key="idx">
            <v-col cols="12">
              <v-text-field
                v-if="finfo['type'] == 'char'"
                :label="finfo.label"
                v-model="obj[finfo.name]"
              >
                {{ obj[finfo.name] }}
              </v-text-field>

              <v-textarea
                v-if="finfo['type'] == 'text'"
                :label="finfo.label"
                v-model="obj[finfo.name]"
              >
                {{ obj[finfo.name] }}
              </v-textarea>

              <v-text-field
                v-if="finfo['type'] == 'email'"
                :label="finfo.label"
                :rules="[rules.email]"
                v-model="obj[finfo.name]"
              >
              </v-text-field>

              <v-text-field
                v-if="finfo['type'] == 'integer'"
                :label="finfo.label"
                v-model="obj[finfo.name]"
              >
              </v-text-field>

              <v-text-field
                v-if="finfo['type'] == 'auto'"
                :label="finfo.label"
                v-model="obj[finfo.name]"
              >
              </v-text-field>

              <v-text-field
                v-if="finfo['type'] == 'password'"
                :label="finfo.label"
                v-model="obj[finfo.name]"
              >
              </v-text-field>

              <v-select
                v-if="finfo['type'] == 'enum'"
                :label="finfo.label"
                :items="finfo.options"
                v-model="obj[finfo.name]"
              >
              </v-select>

              <v-text-field
                v-if="finfo['type'] == 'foreign'"
                :label="finfo.label"
                v-model="obj[finfo.name]"
              >
              </v-text-field>

              <v-file-input
                v-if="finfo['type'] == 'image' || finfo['type'] == 'file'"
                :label="finfo.label"
              ></v-file-input>

              <v-input v-if="finfo['type'] == 'datetime'" :label="finfo.label">
                <v-menu
                  v-model="date_menus[finfo.name]"
                  :close-on-content-click="false"
                  :nudge-right="40"
                  transition="scale-transition"
                  offset-y
                  min-width="auto"
                  
                >
                  <template v-slot:activator="{ on, attrs }">
                    <v-text-field
                      v-model="dates[finfo.name]"
                      label="Picker without buttons"
                      prepend-icon="mdi-calendar"
                      readonly
                      v-bind="attrs"
                      v-on="on"
                    ></v-text-field>
                  </template>
                  <v-date-picker
                    v-model="dates[finfo.name]"
                    @change="date_menus[finfo.name] = false"
                    min="2000-01-01"
                    max="2077-12-31"
                  ></v-date-picker>
                </v-menu>
              </v-input>
              <!-- 
              <v-text-field
                v-if="finfo['type'] == 'datetime'"
                :label="finfo.label"
                :value="fromTimestamp(obj[finfo.name])"
              >
              </v-text-field>
              <v-date-picker
                v-if="finfo['type'] == 'datetime'"
                :label="finfo.label"
                @change="onChangeDate"
                no-title
              >
              </v-date-picker> -->
            </v-col>
          </v-row>
        </v-container>
      </v-card-text>

      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="normal" text @click="close"> Cancel </v-btn>
        <v-btn color="primary" text @click="save"> Save </v-btn>
        <v-btn v-if="op == 'update'" color="error" text @click="del">
          Delete
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
import moment from 'moment';
export default {
  name: "DialogEditObject",
  props: ["model", "value", "type", "init_obj", "op"],
  components: {
    // datepicker: Datepicker
  },
  data() {
    return {
      date: null,
      dates: {},
      date_menus: {},
      obj: {},
      menu: null,
      componentType: {
        email: "V-text-field",
        enum: "v-text-field",
        password: "v-text-field",
        image: "v-textarea",
        auto: "v-text-field",
        char: "v-text-field",
        integer: "v-text-field",
      },
      rules: {
        required: (value) => !!value || "Required.",
        counter: (value) => value.length <= 20 || "Max 20 characters",
        email: (value) => {
          const pattern =
            /(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))/;
          return pattern.test(value) || "Invalid e-mail.";
        },
      },
    };
  },
  watch: {
    value(bool) {
      this.$emit("input", bool);
      if (bool){
        for (var k in this.model.fields){
          var finfo = this.model.fields[k];
          console.log(finfo.type);
          if (finfo.type=='datetime'){
            if (this.init_obj[finfo.name]){
              this.dates[finfo.name] = moment(this.init_obj[finfo.name]*1000).format('YYYY-MM-DD');
            }
            
          }
        }
      }
      
    },
    init_obj(obj) {
      this.obj = {};
      Object.assign(this.obj, obj);
      console.log(this.obj);
    },
  },
  methods: {
    copyData(d) {
      return JSON.parse(JSON.stringify(d));
    },
    close() {
      this.value = false;
    },
    save() {
      for (var name in this.dates){
        this.obj[name] = moment(this.dates[name], 'YYYY-MM-DD').valueOf()/1000;
      }
      if (this.op == "create") {
        this.$emit("create", this.copyData(this.obj));
      } 
      else this.$emit("update", this.copyData(this.obj));
      this.dates = {}
      this.date_menus = {}
      this.value = false;
    },
    del() {
      if (this.op != "create") {
        this.$emit("del", this.copyData(this.obj));
      }
      this.value = false;
    },
    fromTimestamp(t) {
      var tmp = new Date(t * 1000);
      return tmp.toLocaleString();
    },
    onChangeDate(date) {
      console.log(date);
    },
  },
};
</script>
