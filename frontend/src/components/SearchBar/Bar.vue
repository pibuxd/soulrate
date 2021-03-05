<template>
  <form autocomplete="off" @submit.prevent="redirect">
    <input type="text" name="name" v-model="name" placeholder="Enter username" />
    <button type="submit">Search</button>
  </form>
</template>

<script>
//import jd from '../../assets/js/search.js';

export default {
  name: 'Bar',

  data() {
    return {
      name: '',
    };
  },

  mounted() {
    //getRating('{{ username }}')
    //jd.asyncGetRating('{{ username }}', 2)
    var usernames = ["xd", "jd"];
    console.log(usernames)
    //jd.autocomplete(document.getElementById("myInput"), usernames);
  },

  methods: {
    redirect() {
      this.$router.push("/"+this.name)
    }
  }

}
</script>

