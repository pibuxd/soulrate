<template>
  <form method="POST" @submit.prevent="formSubmit">
    <h3 align="center">Sign up</h3>
        <label for="name">Username</label>
        <input type="text" name="name" v-model="form.name" placeholder="Enter name" />
        <label for="password">Password</label>
        <input type="password" name="password" v-model="form.password" placeholder="Enter password" />
        <input type="submit" value="Sign up">
  </form>
</template>

<script>
export default {
  name: "Signup",

  data() {
    return {
      form: {
          name: '',
          password: '',
        }
    };
  },
  methods: {
    formSubmit() {
      console.log(this.form)
      this.$axios.post('signup', this.form)
      .then(function (response) {
        console.log(response);
      })
      .catch(function (error) {
        console.log(error);
      });
    }
  },
}
</script>