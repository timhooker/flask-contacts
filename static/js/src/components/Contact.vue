<template>
  <div class="contact" v-if="contact">
    <h1>{{ `${contact.firstname} ${contact.lastname}` }}</h1>
    
    <ul class="contact-props">
      <li>{{contact.dob}}</li>
      <li>{{contact.address}}</li>
      <li>{{contact.phone}}</li>
      <li>{{contact.email}}</li>
    </ul>
    <router-link to="/">Done</router-link>
  </div>
</template>

<script>
import * as styles from './contact.css';
export default {
  name: 'contact',
  props: ['contact', 'id']
}
</script>