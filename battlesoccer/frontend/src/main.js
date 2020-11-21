import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import Vuelidate from 'vuelidate'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import AOS from 'aos'
import 'aos/dist/aos.css'
import VueConfetti from 'vue-confetti'
import Lightbox from 'vue-my-photos'
Vue.component('lightbox', Lightbox);
  Vue.use(VueConfetti)

import VueSweetalert2 from 'vue-sweetalert2';

Vue.use(VueSweetalert2, options);

 
// If you don't need the styles, do not connect
import 'sweetalert2/dist/sweetalert2.min.css';
import 'vue-snotify/styles/material.css'

import Snotify, { SnotifyPosition } from 'vue-snotify'

const options = {
  confirmButtonColor: '#41b882',
  cancelButtonColor: '#ff7674',
  toast: {
    position: SnotifyPosition.rightTop
  }
}

Vue.use(Snotify, options)


Vue.use(BootstrapVue)
Vue.use(IconsPlugin)
import { VLazyImagePlugin } from "v-lazy-image";
Vue.use(Vuelidate)
Vue.directive('$model', {
  bind: function (el, binding, vnode) {
      el.oninput = () => (vnode.context[binding.expression] = el.value)
  }
})
Vue.use(VLazyImagePlugin);
// using CommonJS modules
import vueScrollBehavior from 'vue-scroll-behavior'

Vue.use(vueScrollBehavior, {
  router: router,    // The router instance
  maxLength: 100,    // Saved history List max length
  ignore: [/\/boo/, /\/zoo/]    // ignore some routes, they will directly scroll to the top
})

Vue.filter('capitalize', function (value) {
  if (!value) return ''
  value = value.toString()
  return value.charAt(0).toUpperCase() + value.slice(1)
})

new Vue({
  router,
  created () {
    AOS.init()
  },
  render: h => h(App)
  }).$mount("#app");
