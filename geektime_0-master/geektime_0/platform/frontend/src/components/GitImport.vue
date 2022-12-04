<template>
  <form class="ui form">
    <div class="field">
      <label>Git地址</label>
      <input
        v-model="url"
        type="text"
        name="first-name"
        placeholder="{{this.url}}"
      />
    </div>
    <button class="ui button" type="submit" @click="gitImport">开始导入</button>
  </form>
</template>

<script>
import http from "@/http";
export default {
  name: "GitImport",
  data() {
    return {
      url: "https://github.com/zhoufan55/geektime_zf.git",
    };
  },
  methods: {
    async gitImport() {
      let res = await http.put("/testcase", null, {
        params: { git: this.url },
      });
      console.log(res);
      this.$router.push('/testcase/all')
    },
  },
};
</script>