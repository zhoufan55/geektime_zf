<template>
  <div class="ui menu inverted">
    <a class="item">项目列表</a>
    <router-link class="item active" to="/testcase/all">测试管理</router-link>
    <a class="item">环境管理</a>
    <a class="item">测试能力管理</a>
    <a class="item">测试趋势分析</a>
    <div class="right menu">
      <a class="item">个人中心</a>
    </div>
  </div>
</template>

<script>
export default {
  name: "TopMenu",
};
</script>