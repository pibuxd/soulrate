<template>
  <div>
    <h1>Hi {{ username }}!</h1>
    <h2 v-if="this.$cookies.isKey('token')">your rating is <b>{{ rating }}</b></h2>
  </div>
</template>

<script>
export default {
  name: 'Welcome',

  data: function () {
    return {
      username: '',
      rating: null,
    }
  },
  created () {
    this.$axios.get('http://0.0.0.0:5000/api/home', {withCredentials: true})
      .then(response => {
        this.username = response.data.username
        this.rating = response.data.rating
        console.log(response)
      })
      .catch(err => {
        console.log(err)
      })
  }
}
</script>