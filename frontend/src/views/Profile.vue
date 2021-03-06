<template>
  <div>
    <div v-if="this.$cookies.isKey('token')">
      <div v-if="rating == null">
        <p><b>{{ $route.params.name }}</b> not found</p>
      </div>
      <div v-else>
        <GetUser />
      </div>
    </div>
    <div v-else>
      <p><b>You have to be logged to evaluate</b></p>
    </div>
  </div>

</template>

<script>
import GetUser from "../components/Profile/GetUser.vue"
export default {
  name: 'Profile',
  
  components: {
    GetUser,
  },

  data: function () {
    return {
      rating: null,
    }
  },

  created() {
    this.$axios.get('rating/' + this.$route.params.name)
      .then(response => {
        this.rating = response.data.rating
      })
      .catch(err => {
        console.log(err)
      })
  },
}
</script>
