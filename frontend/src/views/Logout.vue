<template>
  <b>Logged out!</b>
</template>

<script>
export default {
  name: 'Logout',

  mounted() {
    this.$cookies.remove("token")
    this.$router.push("/")
  }
}
</script>