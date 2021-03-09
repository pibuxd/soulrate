<template>
  <div>
    <h2>Rating of user {{ $route.params.name }} is {{ rating }} </h2>
    <button type="uprate" @click="uprate">Uprate</button>
    <button type="downrate" @click="downrate">Downrate</button>
  </div>
</template>

<script>
import libRating from '../../assets/js/rating.js';

export default {
  data: function () {
    return {
      rating: null,
      x: true
    }
  },

  methods: {
    delay(ms) {
      return new Promise(resolve => setTimeout(resolve, ms));
    },

    async requestRating() {
      var resp = await libRating.requestRating(this.$route.params.name)
      this.rating = resp.rating
    },

    async uprate() {
      await libRating.uprate(this.$route.params.name)
      this.requestRating()
    },

     async downrate() {
      await libRating.downrate(this.$route.params.name)
      this.requestRating()
    },
  },

  async created () {
    this.x = true

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

