<template>
  <form autocomplete="off" @submit.prevent="redirect">
    <input type="text" v-model="name">
    <button type="submit">Search</button>
  </form>
</template>

<script>
//import libSearch from '../../assets/js/search.js';
import libHome from '../../assets/js/home.js';

export default {
  name: 'Bar',

  data() {
    return {
      name: '',
    };
  },

  async mounted() {
    var resp = await libHome.requestHome();
    var usernames =  resp.names
    console.log(usernames)

  },

  methods: {
    redirect() {
      this.$router.push("/"+this.name)
    }
  }

}
</script>

