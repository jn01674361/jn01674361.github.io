<template>
  <div class="Agent0">
    <iframe
      allow="microphone;"
      width="700"
      height="500"
      text-align="center"
      src="https://console.dialogflow.com/api-client/demo/embedded/c480f8ac-06eb-4aeb-9794-be0219f64243">
    </iframe>
  </div>
</template>
<script>
export default {
  name: 'Agent0',
  data () {
    return {
      msg: 'Agent0 is upp and running'
    }
  }
}
</script>
<style>
  .center {
  text-align: center;
  border: 3px solid green;
  }
</style>
