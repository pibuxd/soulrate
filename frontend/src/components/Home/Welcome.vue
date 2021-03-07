<template>
  <div>
    <h1>Hi <a id="username"></a>!</h1>
    <h2 v-if="this.$cookies.isKey('token')">your rating is <a id="rating"></a></h2>
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
    }
  },

  created () {
    libHome.requestRating();
  },
}
</script>