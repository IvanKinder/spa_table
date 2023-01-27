<template>
  <AppealsTable/>
</template>

<script>
import AppealsTable from "@/components/AppealsTable";

export default {
  name: 'App',
  components: {
    AppealsTable
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
