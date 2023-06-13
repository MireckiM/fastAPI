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
                v-model="usermodel.username"
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
                v-model="usermodel.password"
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
              v-if="usermodel.password != password2 && password2 != ''"
              class="blockquote-footer"
              style="color: red"
            >
              Hasła muszą być identyczne!
            </footer>

            <button
              v-if="
                usermodel.password == password2 &&
                password2 != '' &&
                usermodel.password != ''
              "
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
      user: "",
      usermodel: {},
      users: {},
      usernames: [],
    };
  },
  async created() {
    this.getUsers();
  },
  methods: {
    async getUsers() {
      var response = await fetch("http://0.0.0.0:8001/users/");
      console.log(response);
      this.users = await response.json();
    },
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

      /*var response2 = await fetch("http://localhost:8001/protected", {
        headers: {
          "Content-Type": "application/json",
          Authorization: "Bearer" + " " + res["token"],
        },
      }).then((response2) => response2.json());

      if (this.username == response2["name"]) {
        localStorage.setItem("token", res["token"]);
        console.log(localStorage.getItem("token"));
      } else {
        console.log("nie otrzymano tokenu");
      }*/
    },

    async register() {
      let taken = 0;
      for (let i = 0; i < this.users.length; ++i) {
        if (this.users[i].username == this.usermodel.username) {
          taken = 1;
        }
      }
      if (taken == 0) {
        var response = await fetch("http://0.0.0.0:8001/add-user", {
          method: "post",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(this.usermodel),
          /*body: JSON.stringify({
          username: this.username,
          password: this.password,
        }*/
        }).then((response) => response.json());
        console.log("ok");
        console.log(response);
        //location.reload();
      } else {
        console.log("Username is taken");
      }
    },

    async getUser() {
      var response = await fetch("http://localhost:8001/protected", {
        headers: {
          "Content-Type": "application/json",
          Authorization: "Bearer" + " " + this.token,
        },
      }).then((response) => response.json());

      //this.user = response["name"];
      //console.log("username = " + this.username);
      return response["name"];
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
