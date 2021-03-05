<template>
  <div>
    <div v-if="rating == null">
      <p><b>{{ $route.params.name }}</b> not found</p>
    </div>
    <div v-else>
      <h2>Rating of user {{ $route.params.name }} is {{ rating }}</h2>
      <ButtonUprate />
      <ButtonDownrate />
    </div>
  </div>
</template>

<script>
import ButtonUprate from '../components/ChangeRating/ButtonUprate.vue'
import ButtonDownrate from '../components/ChangeRating/ButtonDownrate.vue'

export default {
  name: 'Profile',

  components: {
    ButtonUprate,
    ButtonDownrate,
  },
  
  data: function () {
    return {
      rating: null,
    }
  },
  created () {
    this.$axios.get('rating/' + this.$route.params.name)
      .then(response => {
        this.rating = response.data.rating
      })
      .catch(err => {
        console.log(err)
      })
  }

}
</script>
