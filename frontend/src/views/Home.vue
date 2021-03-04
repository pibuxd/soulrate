<template>
  <SearchBar text="Search for a user:"/>
</template>

<script>
import SearchBar from './components/SearchBar/SearchBar.vue'

export default {
  name: 'Home',
  components: {
    SearchBar,
  },
}
</script>