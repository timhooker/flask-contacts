<template>
  <form id="contact-form" action="">
    <h1>{{ msg }}</h1>
    <label for="">Name
      <input type="text">
    </label>
    <label for="">Email
      <input type="email">
    </label>
  </form>
</template>

<script>
export default {
  name: 'contact-form',
  props: ['msg']
}
</script>