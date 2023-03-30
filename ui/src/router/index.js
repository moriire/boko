import { createRouter, createWebHistory } from 'vue-router'
import AuthLayout from '@/AuthLayout.vue'
import GenLayout from '@/GenLayout.vue'
import LoginView from '@/views/account/LoginView.vue'
import RegisterView from '@/views/account/RegisterView.vue'
import ProfileView from '@/views/account/ProfileView.vue'
import ListBooks from '@/views/book/ListBooks.vue'
import ListSubjects from '@/views/book/ListSubjects.vue'

var check= localStorage.getItem("access_token_time"),
refreshTime=  localStorage.getItem("refresh_token_time");

function guardMyroute(to, from, next)
{
  let start = check? new Date(check).getTime(): 0,
  end = start - new Date().getTime(),
  refreshEnd = new Date(refreshTime).getTime() - new Date().getTime()
  console.log(start)
  console.log(end)
  if(end > 0 && refreshEnd>0) {
  //checkTime(globals.state.data.access_token)
    next()
  } else if(end<0 && refreshEnd>0){
    stores.refreshToken(),
    next()
  }
  else{
    next({ path: `/login?redirect=${to.path}` }); // go to '/login';
 }
}

function guardAuth(to, from, next){
  var start = check? new Date(check.access_token_expiration).getTime(): 0,
  end = start - new Date().getTime();
  if((end < 0) && (to.name==="home")){
    next(false)
  } else{
    next()
 }
}
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  linkActiveClass: "active",
  routes: [
    {
      path: '/',
      name: 'home',
      beforeEnter:guardAuth,
      component: AuthLayout,
      children: [
          {
            path: '',
            alias: 'login',
            name: 'login',
            component: LoginView,
            meta: {title: "Login", subtitle: "Add & Manage Subject Categories"},
          },
          {
            path: 'register',
            name: 'register',
            component: RegisterView,
            meta: {title: "Sign up", subtitle: "Add & Manage Subject Categories"},
          },
          {
            path: 'profile',
            name: 'profile',
            beforeEnter: guardMyroute,
            component: ProfileView,
            meta: {title: "Profile", subtitle: "Manage Categories"}
          },
          
      ]
        
    },
    {
      path: '/books',
      name: 'gen',
      beforeEnter: guardMyroute,
      component: GenLayout,
      children: [
          {
            path: '',
            name: 'list-books',
            component: ListBooks,
            meta: {title: "Books", subtitle: "Add & Manage Books"}
          }
          
      ]
        
    },
    {
      path: '/subjects',
      name: 'subject',
      beforeEnter: guardMyroute,
      component: GenLayout,
      children: [
          {
            path: '',
            name: 'list-subjects',
            component: ListSubjects,
            meta: {title: "Subject", subtitle: "Add & Manage Subject Categories"}
          }
          
      ]
        
    }
  ]
})

export default router
router.afterEach((to) =>{
  document.title = `${to.meta.title} | My Library`
  document.getElementById("title").innerHTML = to.meta.title
  document.getElementById("subtitle").innerHTML = to.meta.subtitle
})