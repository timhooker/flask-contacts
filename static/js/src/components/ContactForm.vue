<template>
  <div class="modal-container">
    <form 
      id="contact-form" 
      class="contact-form modal" 
      action=""
      @submit.prevent="() => submit(contact)"
    >
      <h2 class="contact-form__header">{{ msg }}</h2>
      <section class="contact-form__fields">
        <label v-for="[key, val] in formFields">
          {{val}}
          <span v-if="key === 'dob'">
            <input 
              type="text" 
              v-on:click="showDatePicker = true" 
              v-model="contact[key]"
              placeholder="Click to Enter your Birthday"
              key="date"
            >
            <transition name="calendar-fade">
              <date-picker 
                color="#3f51b5" 
                @close="showDatePicker = false" 
                v-if="showDatePicker" 
                v-model="contact[key]"
              ></date-picker>
            </transition>
          </span>
          <input v-else-if="key === 'phone'" type="tel" v-model="contact[key]">
          <input v-else type="text" v-model="contact[key]">
        </label>
      </section>
      <section class="contact-form__actions">
        <button class="btn btn__raised contact-form__submit" type="submit">Save Contact</button>
        <button class="btn contact-form__cancel" @click.prevent="closeForm">Cancel</button>
      </section>
    </form>
  </div>
</template>

<script>
/**
  Contact Form
  All in one place for this form just to keep it more simple.
  Using formField array w/ tuples for ensuring keys are the same as backend although
  it does create a bit more data wrangling.
 */

import './contact-form.css';
import DatePicker from 'vue-md-date-picker';
const formFields = [
  ['firstname', 'First Name'], 
  ['lastname', 'Last Name'], 
  ['dob', 'Birth Date'], 
  ['address', 'Address'], 
  ['phone', 'Phone'], 
  ['email', 'Email']
];
const contact = formFields.reduce((contact,[key, val]) => {
  contact[key] = '';
  return contact;
}, {})

export default {
  name: 'contact-form',
  data() {
    return {
      formFields,
      contact: this.update ? this.update : formFields.reduce((contact,[key, val]) => {
        contact[key] = '';
        return contact;
      }, {}),
      showDatePicker: false
    }
  },
  props: ['closeForm', 'submit', 'msg', 'update'],
  components: {'date-picker': DatePicker}  
}
</script>