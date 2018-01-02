
import Vue from 'vue';
import Router from 'vue-router';
import Contact from '../components/Contact';

const routes = [
  { path: '/contact/:id', name: 'contact', component: Contact, props: true },
]

// const routes = routerOptions.map(route => {
//   return {
//     ...route,
//     component: () => import(`../components/${route.component}.vue`)
//   }
// })

Vue.use(Router)

export default new Router({
  routes
})