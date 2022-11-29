<template>
  <top-menu></top-menu>
  <div class="ui grid">
    <div class="column three wide"><side-menu></side-menu></div>
    <div class="column twelve wide ui container">
      <router-view></router-view>
    </div>
  </div>
</template>
<style scoped>
.ui.grid {
  height: 100%;
}

.ui.table {
}
</style>
<script>
import SideMenu from "./SideMenu.vue";
import TopMenu from "./TopMenu.vue";

export default {
  components: { SideMenu, TopMenu },
  name: "SemanticUI",
  data() {
    return {
      a: 1,
    };
  },
};
</script>
