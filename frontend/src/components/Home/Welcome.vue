<template>
  <div>
    <h1>Hi {{ username }}!</h1>
    <h2 v-if="this.$cookies.isKey('token')">your rating is {{ rating }}</h2>
  </div>
</template>

<script>
import libHome from '../../assets/js/home.js';

export default {
  name: 'Welcome',

  data: function () {
    return {
      username: '',
      rating: null,
      x: true,
    }
  },

  methods: {
    delay(ms) {
      return new Promise(resolve => setTimeout(resolve, ms));
    },

    async requestRating() {
      var resp = await libHome.requestHome()
      this.username = resp.username
      this.rating = resp.rating
    },
  },

  async created () {
    this.x = true;

    while(this.x){
      this.requestRating();
      await this.delay(4000)
    }
  },

  destroyed() {
    this.x = false;
    console.log("destroyed")
  },
}
</script>