<template>
    <div class="ui vertical menu">
      <a class="active item"> 测试用例 </a>
      <a class="item"> 测试套件 </a>
      <router-link to="/task/all" class="item"> 测试任务 </router-link>
      <a class="item"> 测试执行记录 </a>
      <a class="item"> 测试结果 </a>
      <a class="item"> 测试报告 </a>
    </div>
</template>

<style scoped>
.ui.menu {
  background: #f5f5f5;
  height: 100%;
}
</style>

<script>
export default {
  name: "SideMenu",
};
</script>