<template>
  <div>
    <h2>Rating of user {{ $route.params.name }} is <a id="rating"></a> </h2>
    <button type="uprate" @click="uprate">Uprate</button>
    <button type="downrate" @click="downrate">Downrate</button>
    </div>
</template>

<script>
import libRating from '../../assets/js/rating.js';

export default {
  data: function () {
    return {
      rating: null
    }
  },

  methods: {
    uprate() {
      libRating.uprate(this.$route.params.name)
    },
    downrate() {
      libRating.downrate(this.$route.params.name)
    },
  },

  created () {
    libRating.requestRating(this.$route.params.name);
  }
}
</script>

