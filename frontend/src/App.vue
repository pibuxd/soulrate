<template>
  <div id="app">
    <div id="nav" v-if="this.$cookies.isKey('token')">
      <router-link to="/">Home</router-link> |
      <router-link to="/logout">Logout</router-link>
    </div>
    <div id="nav" v-else>
      <router-link to="/">Home</router-link> |
      <router-link to="/login">Login</router-link> |
      <router-link to="/signup">Sign up</router-link>
    </div>
    <router-view/>
  </div>
</template>
