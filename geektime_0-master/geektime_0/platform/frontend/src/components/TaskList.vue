<template>
  <table class="ui compact celled definition table">
    <thead class="full-width">
      <tr>
        <th></th>
        <th v-for="item in keys" :key="item">{{ item }}</th>
        <th>preview</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="item in values" :key="item">
        <td class="collapsing">
          <div class="ui fitted slider checkbox">
            <input type="checkbox" /> <label></label>
          </div>
        </td>
        <td v-for="cell in item" :key="cell"><a :href="cell">{{ cell }}</a></td>
        <td>
          
          <iframe
            class="ui embed"
            :src="item[1]"
          ></iframe>
        </td>
      </tr>
    </tbody>
    <tfoot class="full-width">
      <tr>
        <th></th>
        <th colspan="4">
          <div
            class="ui right floated small primary labeled icon button"
            @click="dataitem"
          >
            <i class="user icon"></i> Add
          </div>
        </th>
      </tr>
    </tfoot>
  </table>
</template>

<script>
import http from "@/http";
export default {
  name: "TaskList",
  data() {
    return {
      data: [],
    };
  },
  computed: {
    keys() {
      if (this.data.length > 0) {
        return Object.keys(this.data[0]);
      } else {
        return [];
      }
    },
    values() {
      if (this.data.length == 0) {
        return [];
      }
      let keys = Object.keys(this.data[0]);
      let values = [];
      this.data.forEach((item) => {
        let r = [];
        for (let i = 0; i < keys.length; i++) {
          r.push(item[keys[i]]);
        }
        values.push(r);
      });
      return values;
    },
  },
  async mounted() {
    let res = await http.get("/task");
    if (res.data.errcode === 0) {
      let testcases = res.data.data;
      console.log(testcases);
      this.data = testcases;
      testcases.forEach((testcase) => {
        console.log(testcase);
      });
    }
  },

  methods: {
    dataitem() {
      this.$router.push("/task/edit");
    },
  },
};
</script>