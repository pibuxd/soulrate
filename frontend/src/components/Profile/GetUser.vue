<template>
  <div>
    <h2>Rating of user {{ $route.params.name }} is {{ rating }} </h2>
    <button type="uprate" @click="uprate">Uprate</button>
    <button type="downrate" @click="downrate">Uprate</button>
    </div>
</template>

<script>
export default {
  data: function () {
    return {
      rating: null,
    }
  },

  methods: {
    async requestRating() {
      var x = true
      while(x){
        await this.$axios.get('rating/' + this.$route.params.name)
          .then(response => {
            this.rating = response.data.rating
          })
          .catch(err => {
            console.log(err)
          })

        await new Promise(resolve => setTimeout(resolve, 2000))
      }
    },
    getRating() {
      this.$axios.get('rating/' + this.$route.params.name)
          .then(response => {
            this.rating = response.data.rating
          })
          .catch(err => {
            console.log(err)
          })
    },
    uprate() {
      this.$axios.get('uprate/' + this.$route.params.name, {withCredentials: true})
        .then(response => {
          console.log(response)
          this.getRating();
        })
        .catch(err => {
          console.log(err)
        })
    },
    downrate() {
      this.$axios.get('downrate/' + this.$route.params.name, {withCredentials: true})
        .then(response => {
          console.log(response)
          this.getRating();
        })
        .catch(err => {
          console.log(err)
        })
    }
  },

  created () {
    this.requestRating();
  }
}
</script>

