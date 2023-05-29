<template>
  <div class="container" style="margin-top: 40px">
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
        <tr v-for="book in books" :key="book.id" @dblclick="$data.book = book">
          <td>{{ book.title }}</td>
          <td>{{ book.pages }}</td>
          <td>{{ book.client_id }}</td>
        </tr>
      </tbody>
    </table>
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
      token: localStorage.getItem("token"),
    };
  },
  async created() {
    await this.getBooks();
    await this.getClients();
  },
  methods: {
    submitForm() {} /*{
        if (this.book.id === undefined) {
          this.addBook();
        } else {
          this.editBook();
        }
      },*/,

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
          Authorization: "Bearer" + " " + this.token,
          "Access-Control-Allow-Origin": "*",
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
