<template>
  <div>
    <nav class="navbar navbar-dark bg-dark">
      <a
        class="navbar-brand"
        href="#"
        style="margin-left: 3%"
        v-if="token != null"
        >Witaj {{ username }}</a
      >
      <button
        v-if="token != null"
        class="btn btn-outline-danger"
        type="button"
        style="margin-right: 3%"
        @click="logout()"
      >
        Wyloguj
      </button>
    </nav>
    <div class="container-fluid">
      <div v-if="token == null">
        <HelloWorld />
      </div>
      <div v-else>
        <HelloBooks />
      </div>
    </div>
  </div>
</template>

<script>
import HelloWorld from "./components/HelloWorld.vue";
import HelloBooks from "./components/HelloBooks.vue";

export default {
  name: "App",
  components: {
    HelloWorld,
    HelloBooks,
  },
  data() {
    return {
      token: localStorage.getItem("token"),
      username: "",
    };
  },
  async created() {
    this.getToken();
    this.getUser();
  },
  methods: {
    getToken() {
      if (this.token != null) {
        console.log("Użytkownik zalogowany");
        console.log(localStorage.getItem("token"));
      } else {
        console.log("Użytkownik niezalogowany");
      }
    },
    async getUser() {
      if (this.token != null) {
        var response = await fetch("http://localhost:8001/protected", {
          headers: {
            "Content-Type": "application/json",
            Authorization: "Bearer" + " " + this.token,
          },
        }).then((auth) => auth.json());
        console.log(response);
        this.username = response["name"];
      }
    },
    logout() {
      localStorage.removeItem("token");
      this.token = null;
      this.username = "";
    },
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
