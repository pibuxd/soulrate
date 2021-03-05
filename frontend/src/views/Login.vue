<template>
  <form method="POST" @submit.prevent="formSubmit">
    <h3 align="center">Login</h3>
        <label for="name">Username</label>
        <input type="text" name="name" v-model="form.name" placeholder="Enter name" />
        <label for="password">Password</label>
        <input type="password" name="password" v-model="form.password" placeholder="Enter password" />
        <input type="submit" value="Login">
  </form>
</template>

<script>
export default {
  name: "Login",

  data() {
    return {
      form: {
          name: '',
          password: '',
        },
      token: '',
    };
  },
  methods: {
    formSubmit() {
      console.log(this.form)
      
      this.$axios.post('login', this.form)
      .then(response => {
        this.token = response.data.token
      })
      .catch(function (error) {
        console.log(error);
      })
      .finally(() => {
        this.$cookies.set("token", this.token)
        this.$router.push("/")
      })
    }
  },
}
</script>