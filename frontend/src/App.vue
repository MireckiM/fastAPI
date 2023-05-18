<template>
  <div>
    <nav class="navbar navbar-dark bg-dark">
      <a
        class="navbar-brand"
        href="#"
        style="margin-left: 3%"
        v-if="username != undefined"
        >Witaj {{ username }}</a
      >
      <button
        v-if="username != undefined"
        class="btn btn-outline-danger"
        type="button"
        style="margin-right: 3%"
        @click="logout()"
      >
        Wyloguj
      </button>
    </nav>
    <div class="container-fluid">
      <div v-if="this.username == undefined">
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
      authDetail: "",
    };
  },
  async created() {
    this.getToken();
    this.getUser();
    //this.isAuthenticated();
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
      //if (this.token != null ) {
      var response = await fetch("http://localhost:8001/protected", {
        headers: {
          "Content-Type": "application/json",
          Authorization: "Bearer" + " " + this.token,
        },
      }).then((auth) => auth.json());
      this.authDetail = response.detail;
      this.username = response["name"];
      console.log("username = " + this.username);
      console.log("authdetail = " + this.authDetail);
      //}
    },
    /*async isAuthenticated() {
      var response = await fetch("http://0.0.0.0:8001/users/me", {
        headers: {
          accept: "application/json",
        },
      }).then((response) => response.json());
      console.log("isAuth");
      console.log(response);
    },*/
    logout() {
      localStorage.removeItem("token");
      this.token = null;
      this.username = "";
      location.reload();
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
