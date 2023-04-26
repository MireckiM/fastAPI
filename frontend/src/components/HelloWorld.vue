<template>
  <div class="container" style="margin-top: 20px">
    <h3>Biblioteka app</h3>
    <form @submit.prevent="submitForm" style="margin-top: 20px">
      <div class="form-group row mb-4">
        <div class="row">
          <div class="col-2"></div>
          <div class="col">
            <input
              type="text"
              class="form-control col-3 mx-2"
              placeholder="Tytuł"
            />
          </div>
          <div class="col">
            <input
              type="text"
              class="form-control col-3 mx-2"
              placeholder="Autor"
            />
          </div>
          <div class="col">
            <input
              type="text"
              class="form-control col-3 mx-2"
              placeholder="Strony"
            />
          </div>
          <div class="col">
            <input
              type="number"
              class="form-control col-3 mx-2"
              placeholder="ID klienta"
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
            >
              Dodaj
            </button>
          </div>
          <div class="col-3"></div>
        </div>
      </div>
    </form>

    <table class="table">
      <thead>
        <th>Tytuł</th>
        <th>Autor</th>
        <th>Strony</th>
        <th>Klient</th>
      </thead>
      <tbody>
        <tr v-for="book in books" :key="book.id" @dblclick="$data.book = book">
          <td>{{ book.title }}</td>
          <td>{{ book.author }}</td>
          <td>{{ book.pages }}</td>
          <td>{{ book.client_id }}</td>
          <td>
            <button
              class="btn btn-danger btn-sm mx-1"
              @click="deleteBook(book)"
            >
              X
            </button>
          </td>
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
    };
  },
  async created() {
    await this.getBooks();
  },
  methods: {
    submitForm() {},
    async getBooks() {
      var response = await fetch("http://0.0.0.0:8001/books/");
      this.books = await response.json();
    },
    async addBook() {},
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
