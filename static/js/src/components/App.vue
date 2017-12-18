<template>
  <div id="app">
    <h1>{{ msg }}</h1>
    <h2>Essential Links!</h2>
    <input v-model="msg">
    <contact-form v-bind:msg="msg"></contact-form>
  </div>
</template>

<script>
import ContactForm from './ContactForm.vue';

export default {
  name: 'app',
  data () {
    return {
      msg: 'OK, it\'s time to write something!!!',
      contact: {
        name: '',
        email: ''
      }
    };
  },
  components: { 'contact-form': ContactForm }
}
</script>


