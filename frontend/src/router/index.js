import Vue from 'vue'
import VueRouter from 'vue-router'

import Home from '../views/Home.vue'
import Profile from '../views/Profile.vue'
import Login from '../views/Login.vue'
import Signup from '../views/Signup.vue'
import Logout from '../views/Logout.vue'
import NotFound from '../views/NotFound.vue'

Vue.use(VueRouter)

const routes = [{
        path: '/',
        name: 'Home',
        component: Home
    },
    {
        path: '/login',
        name: 'Login',
        component: Login,
    },
    {
        path: '/logout',
        name: 'Logout',
        component: Logout,
    },
    {
        path: '/signup',
        name: 'Signup',
        component: Signup,
    },
    {
        path: '/404',
        name: 'NotFound',
        component: NotFound,
    },
    {
        path: '/:name',
        name: 'Profile',
        component: Profile,
    },

]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router