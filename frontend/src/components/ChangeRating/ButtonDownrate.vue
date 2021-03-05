<template>
  <button type="downrate" @click="downrate">Downrate</button>
</template>

<script>
export default {
  name: "ButtonDownrate",

  methods: {
    downrate() {
      this.$axios.get('downrate/' + this.$route.params.name, {withCredentials: true})
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
