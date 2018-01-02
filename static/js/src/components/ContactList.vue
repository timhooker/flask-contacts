<template>
  <ul class="contact-list">
    <button v-on:click="newForm" class="btn btn__raised contact-list__btn-new">New</button>
    <li class="contact-list__item" v-for="contact in contacts">
      <h3 class="contact-list__item__name">{{contact.firstname}} {{contact.lastname}}</h3>
      <p class="contact-list__item__detail">{{contact.email}}</p>
      <router-link class="contact-list__item__link" :to="{name: 'contact', params: { id: contact.id, contact: contact }}">View</router-link>
      <button v-on:click="() => editForm(contact)" class="contact-list__item__link">Edit</button>
    </li>
  </ul>
</template>
<script>
export default {
  name: 'contact-list',
  props: ['contacts', 'newForm', 'editForm']
}
</script>

