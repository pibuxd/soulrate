<template>
  <button type="uprate" @click="uprate">Uprate</button>
</template>

<script>
export default {
  name: "ButtonUprate",

  methods: {
    uprate() {
      this.$axios.get('uprate/' + this.$route.params.name, {withCredentials: true})
        .then(response => {
          console.log(response)
        })
        .catch(err => {
          console.log(err)
        })
    }
  }
}
</script>
