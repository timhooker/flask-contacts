<template>
  <div className="contact">
    <h1>{{ name }}!!</h1>
  </div>
</template>

<script>
export default {
  name: 'contact-form',
  props: ['msg']
}
</script>

// "firstname": "Jim",
// "lastname": "Hopper",
// "dob": date(1940,6,6).isoformat(),
// "address": "555 somewhere ln",
// "phone": "555-555-5555",
// "email": "jim@example.com"