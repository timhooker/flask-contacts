<template>
  <div id="app" class="container">
    <app-nav :openForm="() => showForm=true"></app-nav>
    <div class="app-header">
      <h2>Contacts</h2>
    </div>
    <div class="app-body">
      <router-view />
      <contact-list 
        :newForm="() => showForm=true"
        :editForm="contact => {
          update = contact;
          formMsg='Edit Contact';
          showForm=true;
        }"
        v-bind:contacts="contacts" />
      <contact-form 
        :closeForm="() => {
          showForm = false;
          update = null;
        }" 
        v-if="showForm" 
        v-bind:msg="formMsg"
        v-bind:update="update"
        :submit="contact => { 
          showForm = false;
          newContact(contact);
          updateContacts();
        }" 
      />

    </div>
  </div>
</template>

<script>
import { getContacts, createContact } from './api/contacts';
import AppNav from './components/AppNav';
import Contact from './components/Contact';
import ContactList from './components/ContactList';
import ContactForm from './components/ContactForm';
import router from './router';
import './components/contact-list.css';
import './app.css';
export default {
  name: 'app',
  data () {
    return { 
      update: null,
      contacts: [],
      showForm: false,
      formMsg: 'Create New Contact'
    };
  },
  mounted() {
    getContacts().then(res => {
      this.contacts = res;
    })
  },
  components: { 
    'contact-form': ContactForm,
    'contact-list': ContactList,
    'app-nav': AppNav
  },
  methods: {
    newContact: contact => {
      return createContact(contact).then(res => {
        router.push({name: 'contact', params: { id: contact.id, contact: contact }})
      })
    },
    updateContacts() {
      window.setTimeout(() => {
        getContacts().then(res => {
          this.contacts = res;
        })
      }, 200)
    }
  },
}
</script>