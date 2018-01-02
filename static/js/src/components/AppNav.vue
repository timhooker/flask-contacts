<template>
  <div class="app-nav">
    <nav class="container app-nav__nav">
      <li class="app-nav__logo">
        <router-link to="/">Home</router-link>
      </li>
      <li class="app-nav__item">
        <a href="" class="app-nav__item" @click.prevent="openForm">New Contact</a>
      </li>
    </nav>
  </div>
</template>
<script>
import './app-nav.css';
export default {
  name: 'app-nav',
  props: ['showForm', 'openForm']
}
</script>
