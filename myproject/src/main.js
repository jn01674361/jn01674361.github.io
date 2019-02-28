// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import Rating from './components/Rating.vue'
import Agent0 from './components/Agent0.vue'
import router from './router'

Vue.config.productionTip = false
/* eslint-disable no-new */
Vue.use(router)
new Vue({
  el: '#Rating',
  router,
  components: { Rating },
  template: '<Rating/>'
})
new Vue({
  el: '#Agent0',
  router,
  components: { Agent0 },
  template: '<Agent0/>'
})
