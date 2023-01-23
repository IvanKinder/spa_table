<template>
  <div class="hello">
    {{ appealsList }}
  </div>
</template>

<script>
export default {
  name: 'AppealsTable',
  data() {
    return {
      appealsList: []
    }
  },
  mounted() {
    fetch('http://127.0.0.1:8000/appeals/').then((response) => {
      return response.json();
    }).then((data) => {
      console.log(data);
    });
  }
}
</script>

<style scoped>
</style>
