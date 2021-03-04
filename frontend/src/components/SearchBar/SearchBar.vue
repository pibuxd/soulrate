<template>
  <header>
    <h3>{{ text }}</h3>
    <ButtonSubmit />
  </header>
</template>

<script>
import ButtonSubmit from './ButtonSubmit.vue'

export default {
  name: 'SearchBar',
  props: {
    text: String,
  },
  components: {
    ButtonSubmit,
  },
}
</script>

<style scoped>
  @import '/css/style.css';

  header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
  }
</style>