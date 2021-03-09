<template>
  <div>
    <Welcome />
    <SearchBar />
  </div>
</template>

<script>
import SearchBar from '../components/SearchBar/SearchBar.vue'
import Welcome from '../components/Home/Welcome.vue'

export default {
  name: 'Home',

  components: {
    SearchBar,
    Welcome,
  },

  created () {
    var isToken = this.$cookies.isKey('token')

    if(!isToken) {
      this.$router.push("/login")
    }
  },

}
</script>
