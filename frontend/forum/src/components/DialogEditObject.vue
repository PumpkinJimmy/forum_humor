<template>
  <v-dialog v-model="value" max-width="500px">
    <v-card>
      <v-card-title>
        <span class="text-h5">{{op == 'create' ? "Create Object" : "Edit Object"}}</span>
      </v-card-title>

      <v-card-text>
        <v-container>
          <v-row
          v-for="(finfo,idx) in model.fields"
          :key="idx">
          <v-col cols="12">
            <v-text-field 
            v-if="(finfo['type']=='char')"
            :label="finfo.label"
            v-model="obj[finfo.name]"
            >
            {{obj[finfo.name]}}
            </v-text-field>

            <v-text-field
            v-if="finfo['type']=='email'"
            :label="finfo.label"
            :rules="[rules.email]"
            v-model="obj[finfo.name]">

            </v-text-field>

            <v-text-field
            v-if="finfo['type']=='integer'"
            :label="finfo.label"
            v-model="obj[finfo.name]">
            </v-text-field>


            <v-text-field
            v-if="finfo['type']=='auto'"
            :label="finfo.label"
            v-model="obj[finfo.name]">
            </v-text-field>

            <v-text-field
            v-if="finfo['type']=='password'"
            :label="finfo.label"
            v-model="obj[finfo.name]">
            </v-text-field>

            <v-select
            v-if="finfo['type']=='enum'"
            :label="finfo.label"
            :items="finfo.options"
            v-model="obj[finfo.name]"
            >
            </v-select>

            <v-text-field
            v-if="finfo['type']=='foreign'"
            :label="finfo.label"
            v-model="obj[finfo.name]"
            >
            </v-text-field>

            <v-file-input 
            v-if="(finfo['type'] == 'image') || (finfo['type']=='file')"
            :label="finfo.label"
            ></v-file-input>

            <v-input
            v-if="finfo['type'] == 'datetime'"
            :label="finfo.label"
            >
            <datepicker :date="tmp"></datepicker>
            </v-input>
           
          </v-col>
          </v-row>
        </v-container>
      </v-card-text>

      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="normal" text @click="close"> Cancel </v-btn>
        <v-btn color="primary" text @click="save"> Save </v-btn>
        <v-btn v-if="op == 'update'" color="error" text @click="del"> Delete </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
import Datepicker from 'vue-datepicker';
export default {
  name: "DialogEditObject",
  props: ["model", "value", "type", "init_obj", "op"],
  components:{
    datepicker: Datepicker
  },
  data(){
    return {
      tmp: {},
      obj: {},
      componentType:{
        email: 'V-text-field',
        enum: 'v-text-field',
        password: 'v-text-field',
        image: 'v-textarea',
        auto: 'v-text-field',
        char: 'v-text-field',
        integer: 'v-text-field',
      },
      rules: {
          required: value => !!value || 'Required.',
          counter: value => value.length <= 20 || 'Max 20 characters',
          email: value => {
            const pattern = /(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))/
            return pattern.test(value) || 'Invalid e-mail.'
          },
        },
    }
  },
  watch: {
      value(bool){
          this.$emit('input', bool);
      },
      init_obj(obj){
        this.obj = {};
        Object.assign(this.obj, obj);
      }
  },
  methods:{
    copyData(d){
      return JSON.parse(JSON.stringify(d));
    },
    close(){
      this.value = false;
    },
    save(){
      if (this.op == 'create'){
        this.$emit('create', this.copyData(this.obj));
      }
      else this.$emit('update', this.copyData(this.obj));
      this.value = false;
    },
    del(){
      if (this.op != 'create'){
        this.$emit('del', this.copyData(this.obj)); 
      }
      this.value = false;
    }
  }
};
</script>
