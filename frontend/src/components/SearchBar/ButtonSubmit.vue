<template>
  <button @click="search()" type="submit">Search</button>
</template>

<script>
  import jd from '../../assets/js/jd.js';

  export default {
    name: 'ButtonSubmit',
  
    methods: {
      search() {
        jd.jd();
        jd.f()
      },
      
    },
  }
</script>
