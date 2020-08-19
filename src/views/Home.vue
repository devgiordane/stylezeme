<template>
  <div class="home">
    <Gerador />
    <Menu />
  </div>
</template>

<script>
// @ is an alias to /src
import Gerador from "@/components/Gerador.vue";
import Menu from "@/components/Menu.vue";

export default {
  name: "Home",
  components: {
    Gerador,
    Menu
  }
};
</script>
