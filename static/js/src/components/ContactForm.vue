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
          <input
            class="contact-form__input"
            v-bind:type="inputTypes[key]"
            v-validate="key === 'address' ? '' : `required|${validatorTypes[key]}`"
            v-bind:name="key"
            v-on:click="updated=true"
            v-model="contact[key]">
          <span class="contact-form__input-error" v-if="key !== 'dob'">{{errors.first(key)}}</span>
        </label>
      </section>
      <section class="contact-form__actions">
        <button class="btn btn__raised contact-form__submit" :disabled="errors.all().length > 0" type="submit">Save Contact</button>
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
import { Validator } from 'vee-validate';
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
      validatorTypes: {
        'dob': 'date',
        'address': '',
        'firstname': '',
        'lastname': '',
        'phone': '',
        'email': 'email'
      },
      contact: this.update ? this.update : formFields.reduce((contact,[key, val]) => {
        contact[key] = '';
        return contact;
      }, {}),
      updated: false
    }
  },
  props: ['closeForm', 'onSubmit', 'onDelete', 'msg', 'update'],
  components: {'date-picker': DatePicker},
  methods: {
    submit(contact) {
      this.updated && this.onSubmit(this.contact)
    }
  }

}
</script>