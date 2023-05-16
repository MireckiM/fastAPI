<template>
  <div class="container" style="margin-top: 40px">
    <div v-if="logging == true">
      <div class="card mx-auto" style="width: 18rem">
        <div class="card-body">
          <h5 class="card-title" style="margin-bottom: 20px">Logowanie</h5>

          <form>
            <div class="form-group">
              <label for="exampleInputEmail1">Nazwa użytkownika</label>
              <input
                type="text"
                class="form-control"
                id="exampleInputEmail1"
                aria-describedby="emailHelp"
                placeholder="Username"
                style="margin-bottom: 20px"
                v-model="username"
              />
            </div>
            <div class="form-group">
              <label for="exampleInputPassword1">Hasło</label>
              <input
                type="password"
                class="form-control"
                id="exampleInputPassword1"
                placeholder="Password"
                style="margin-bottom: 20px"
                v-model="password"
              />
            </div>

            <button
              type="submit"
              class="btn btn-primary"
              style="margin-bottom: 20px"
              @click="login()"
            >
              Zaloguj
            </button>
          </form>
          <a href="#" @click="logging = false" class="card-link">Rejestracja</a>
        </div>
      </div>
    </div>
    <div v-else>
      <div class="card mx-auto" style="width: 18rem">
        <div class="card-body">
          <h5 class="card-title" style="margin-bottom: 20px">Rejestracja</h5>

          <form>
            <div class="form-group">
              <label for="exampleInputEmail1">Nazwa użytkownika</label>
              <input
                type="text"
                class="form-control"
                id="exampleInputEmail1"
                aria-describedby="emailHelp"
                placeholder="Username"
                style="margin-bottom: 20px"
                v-model="username"
              />
            </div>
            <div class="form-group">
              <label for="exampleInputPassword1">Hasło</label>
              <input
                type="password"
                class="form-control"
                id="exampleInputPassword1"
                placeholder="Password"
                style="margin-bottom: 10px"
                v-model="password"
              />
            </div>
            <div class="form-group">
              <label for="exampleInputPassword1">Powtórz hasło</label>
              <input
                type="password"
                class="form-control"
                id="exampleInputPassword1"
                placeholder="Password"
                style="margin-bottom: 20px"
                v-model="password2"
              />
            </div>
            <footer
              v-if="password != password2 && password2 != ''"
              class="blockquote-footer"
              style="color: red"
            >
              Hasła muszą być identyczne!
            </footer>

            <button
              v-if="password == password2 && password2 != '' && username != ''"
              type="submit"
              class="btn btn-primary"
              style="margin-bottom: 20px"
              @click="register()"
            >
              Rejestracja
            </button>
            <button
              v-else
              type="submit"
              class="btn btn-primary"
              style="margin-bottom: 20px"
              disabled
            >
              Rejestracja
            </button>
          </form>

          <a href="#" @click="logging = true" class="card-link">Logowanie</a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "App",
  data() {
    return {
      userLogged: false,
      userTokenized: "",
      logging: true,
      username: "",
      password: "",
      password2: "",
    };
  },
  async created() {
    this.isUserAuthenticated();
  },
  methods: {
    async login() {
      var response = fetch("http://0.0.0.0:8001/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },

        body: JSON.stringify({
          username: this.username,
          password: this.password,
        }),
      }).then((response) => response.json());
      console.log(await response);
      var res = await response;
      //console.log(res["token"]);
      localStorage.setItem("token", res["token"]);
      console.log(localStorage.getItem("token"));
      location.reload();
      /*var auth = await fetch("http://localhost:8001/protected", {
        headers: {
          "Content-Type": "application/json",
          Authorization: "Bearer" + " " + res["token"],
        },
      }).then((auth) => auth.json());
      console.log(auth);
      console.log(auth["name"]);
      */
      /*this.userTokenized = auth["name"];
      if (this.userTokenized == this.username) {
        this.userLogged = true;
      }*/
    },

    isUserAuthenticated() {
      if (localStorage.getItem("token" != null)) {
        this.userLogged = true;
      } else {
        this.userLogged = false;
      }
      console.log(this.userLogged);
      console.log(localStorage.getItem("token"));
    },

    clear() {
      this.username = "";
      this.password = "";
      this.password2 = "";
    },
  },
};
</script>

<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
