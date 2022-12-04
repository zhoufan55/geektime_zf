<template>
  <div class="ui middle aligned center aligned grid bg-gray-200">
    <div class="column">
      <h2 class="ui teal image header">
        <img
          src="https://ceshiren.com/uploads/default/original/1X/809c63f904a37bc0c6f029bbaf4903c27f03ea8a.png"
          class="image"
        />
        <div class="content">Log-in to your account</div>
      </h2>
      <form class="ui large form">
        <div class="ui stacked segment">
          <div class="field">
            <div class="ui left icon input">
              <i class="user icon"></i>
              <input
                v-model="username"
                type="text"
                name="email"
                placeholder="E-mail address"
              />
            </div>
          </div>
          <div class="field">
            <div class="ui left icon input">
              <i class="lock icon"></i>
              <input
                v-model="password"
                type="password"
                name="password"
                placeholder="Password"
              />
            </div>
          </div>
          <div class="ui fluid large teal submit button" @click="login">
            Login
          </div>
        </div>

        <div class="ui error message"></div>
      </form>

      <div class="ui message">New to us? <a href="#">Sign Up</a></div>
    </div>
  </div>

  <div class="flex flex-row">
    <div class="basis-1/4">01</div>
    <div class="basis-1/4">02</div>
    <div class="basis-1/2">03</div>
  </div>
</template>

<style scoped>
.ui.grid {
  height: 100%;
}
.ui .column {
  max-width: 450px;
}
</style>

<script>
import http from "@/http";

export default {
  name: "LoginForm",
  data() {
    return {
      username: "test_zhoufan",
      password: "test_zhoufan",
    };
  },
  methods: {
    async login() {
      console.log(this.username + this.password);
      const res = await http.post("/login", {
        username: this.username,
        password: this.password,
      });
      if (res.data.errcode === 0) {
        let token = res.data.token;
        localStorage.token = token;
        this.$router.push("/testcase/all");
      }
    },
  },
};
</script>