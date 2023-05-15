<template>
  <div class="container" style="margin-top: 20px">
    <div v-if="userLogged == true">
      <h3>Użytkownicy</h3>
      <form @submit.prevent="submitForm" style="margin-top: 20px">
        <div class="form-group row mb-4">
          <div class="row">
            <div class="col-2"></div>
            <div class="col">
              <input
                type="text"
                class="form-control col-3 mx-2"
                placeholder="Imię"
                v-model="client.name"
              />
            </div>

            <div class="col">
              <input
                type="text"
                class="form-control col-3 mx-2"
                placeholder="Wiek"
                v-model="client.age"
              />
            </div>

            <div class="col-2"></div>
          </div>
          <div class="row">
            <div class="col-3"></div>
            <div class="col">
              <button
                class="btn btn-success"
                style="margin-top: 20px; width: 100%"
                @click="addClient(client)"
              >
                Dodaj użytkownika
              </button>
            </div>
            <div class="col-3"></div>
          </div>
        </div>
      </form>

      <table class="table">
        <thead>
          <th>ID</th>
          <th>Klient</th>
          <th>Wiek</th>
        </thead>
        <tbody>
          <tr
            v-for="client in clients"
            :key="client.id"
            @dblclick="$data.client = client"
          >
            <td>{{ client.id }}</td>
            <td>{{ client.name }}</td>
            <td>{{ client.age }}</td>
          </tr>
        </tbody>
      </table>

      <hr class="hr hr-blurry" />

      <h3>Książki</h3>
      <form @submit.prevent="submitForm" style="margin-top: 20px">
        <div class="form-group row mb-4">
          <div class="row">
            <div class="col-2"></div>
            <div class="col">
              <input
                type="text"
                class="form-control col-3 mx-2"
                placeholder="Tytuł"
                v-model="book.title"
              />
            </div>

            <div class="col">
              <input
                type="text"
                class="form-control col-3 mx-2"
                placeholder="Strony"
                v-model="book.pages"
              />
            </div>
            <div class="col">
              <input
                type="number"
                class="form-control col-3 mx-2"
                placeholder="ID klienta"
                v-model="book.client_id"
              />
            </div>
            <div class="col-2"></div>
          </div>
          <div class="row">
            <div class="col-3"></div>
            <div class="col">
              <button
                class="btn btn-success"
                style="margin-top: 20px; width: 100%"
                @click="addBook(book)"
              >
                Dodaj książkę
              </button>
            </div>
            <div class="col-3"></div>
          </div>
        </div>
      </form>

      <table class="table">
        <thead>
          <th>Tytuł</th>
          <th>Strony</th>
          <th>Klient</th>
        </thead>
        <tbody>
          <tr
            v-for="book in books"
            :key="book.id"
            @dblclick="$data.book = book"
          >
            <td>{{ book.title }}</td>
            <td>{{ book.pages }}</td>
            <td>{{ book.client_id }}</td>
          </tr>
        </tbody>
      </table>
    </div>
    <div v-else>
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
            <a href="#" @click="logging = false" class="card-link"
              >Rejestracja</a
            >
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
                v-if="
                  password == password2 && password2 != '' && username != ''
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
  </div>
</template>

<script>
export default {
  name: "App",
  data() {
    return {
      books: [],
      book: {},
      clients: [],
      client: {},
      userLogged: false,
      userTokenized: "",
      logging: true,
      username: "",
      password: "",
      password2: "",
    };
  },
  async created() {
    await this.getBooks();
    await this.getClients();
    await this.isUserAuthenticated();
  },
  methods: {
    submitForm() {} /*{
      if (this.book.id === undefined) {
        this.addBook();
      } else {
        this.editBook();
      }
    },*/,
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

      var auth = await fetch("http://localhost:8001/protected", {
        headers: {
          "Content-Type": "application/json",
          Authorization: "Bearer" + " " + res["token"],
        },
      }).then((auth) => auth.json());
      console.log(auth);
      console.log(auth["name"]);
      this.userTokenized = auth["name"];
      if (this.userTokenized == this.username) {
        this.userLogged = true;
      }
    },

    isUserAuthenticated(){
      if (localStorage.getItem("token" != null)){
        this.userLogged = true;
      }else{
        this.userLogged = false;
      }
      console.log(this.userLogged);
      console.log(localStorage.getItem("token"));
    },

    register() {
      var response = fetch("http://0.0.0.0:8001/register", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },

        body: JSON.stringify({
          username: this.username,
          password: this.password,
        }),
      });
      console.log("ok");
      console.log(response);
      //location.reload();
    },
    async getBooks() {
      var response = await fetch("http://0.0.0.0:8001/books/");
      console.log(response);
      this.books = await response.json();
    },
    async getClients() {
      var response = await fetch("http://0.0.0.0:8001/clients/");
      console.log(response);
      this.clients = await response.json();
    },
    async addBook() {
      await this.getBooks();
      this.book.pages = Number(this.book.pages);
      var response = await fetch("http://0.0.0.0:8001/add-book/", {
        method: "post",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(this.book),
      });
      console.log(response);
      await this.getBooks();
    },
    async addClient() {
      await this.getClients();
      this.client.age = Number(this.client.age);
      var response = await fetch("http://0.0.0.0:8001/add-client/", {
        method: "post",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(this.client),
      });
      console.log(response);
      await this.getClients();
    },
    async editBook() {},
    async deleteBook() {},
    clear() {
      this.book.title = "";
      this.book.author = "";
      this.book.pages = "";
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
