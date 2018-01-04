<template>
  <div class="modal-container">
    <form 
      id="contact-form" 
      class="contact-form modal" 
      action=""
      @submit.prevent="() => !errors.all().length && onSubmit(contact)"
    >
      <h2 class="contact-form__header">{{ msg }}</h2>
      <section class="contact-form__fields">
        <label v-for="[key, val] in formFields">
          {{val}}
          <span v-if="key === 'dob'">
            <input 
              type="text" 
              class="contact-form__input"
              v-on:click="showDatePicker = true" 
              v-model="contact[key]"
              placeholder="Click to Enter your Birthday"
              v-bind:name="key"
              v-validate="'required'"
              key="date-input"
            >
            <transition name="calendar-fade">
              <date-picker 
                color="#3f51b5" 
                @close="showDatePicker = false" 
                v-if="showDatePicker" 
                min="07-04-76"
                v-model="contact[key]"
                class="contact-form__input"
                key="date-picker"
              ></date-picker>
            </transition>
          </span>
          <input
            v-else
            class="contact-form__input"
            v-bind:type="inputTypes[key]"
            v-validate="'required'"
            v-bind:name="key"
            v-model="contact[key]">
          <span class="contact-form__input-error" v-if="key !== 'dob'">{{errors.first(key)}}</span>
        </label>
      </section>
      <section class="contact-form__actions">
        <button class="btn btn__raised contact-form__submit" :disabled="errors.all().length >= 1" type="submit">Save Contact</button>
        <button class="btn contact-form__cancel" @click.prevent="closeForm">Cancel</button>
        <button class="btn contact-form__cancel" @click.prevent="() => onDelete(contact)">Delete</button>
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
      showDatePicker: false,
      inputTypes: {
        'dob': 'date',
        'address': 'text',
        'firstname': 'text',
        'lastname': 'text',
        'phone': 'tel',
        'email': 'email'
      },
      contact: this.update ? this.update : formFields.reduce((contact,[key, val]) => {
        contact[key] = '';
        return contact;
      }, {})
    }
  },
  props: ['closeForm', 'onSubmit', 'onDelete', 'msg', 'update'],
  components: {'date-picker': DatePicker}  
}
</script>