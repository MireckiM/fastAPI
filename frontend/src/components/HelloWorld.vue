<template>
  <div class="container" style="margin-top: 20px;">
    <h3>Biblioteka app</h3>
    <form @submit.prevent="submitForm" style="margin-top: 20px;">
    <div class="form-group row mb-4">
      <input
        type="text"
        class="form-control col-3 mx-2"
        placeholder="Tytuł"
        
      />
      <input
        type="text"
        class="form-control col-3 mx-2"
        placeholder="Autor"
        
      />
      <input
        type="text"
        class="form-control col-3 mx-2"
        placeholder="Strony"
        
      />
      <input
        type="number"
        class="form-control col-3 mx-2"
        placeholder="ID klienta"
        
      />
      <button class="btn btn-success ml-3" style="margin-top: 20px">Dodaj</button>
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
      //var response = await fetch("http://127.0.0.1:8000/api/books/");
      //this.books = await response.json();
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
