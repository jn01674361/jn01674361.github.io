<template>
  <p>{{ bluehello }}</p>
</template>

<script>
export default {
  data() {
    return {
      bluehello: 'Hello World!'
    }
  }
}
</script>

<style scoped>
  p {
    color: blue;
  }
</style>