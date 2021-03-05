<template>
  <div>
    <h2>Search for a user:</h2>
    <Bar />
  </div>
</template>

<script>
import Bar from './Bar.vue'

export default {
  name: 'SearchBar',
  props: {
    text: String,
  },
  components: {
    Bar,
  },
}
</script>