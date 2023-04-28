<template>
  <div class="container-fluid">
    <nav class="navbar navbar-light" style="background-color: #e3f2fd">
      <div class="container-fluid">
        <div class="row">
          <div class="col"></div>
          <!--<form class="form-inline d-flex justify-content-between">
            <input
              class="form-control mr-sm-2"
              type="search"
              placeholder="Search"
              aria-label="Search"
            />

            <button class="btn btn-outline-success my-2 my-sm-0" type="submit">
              Search
            </button>
          </form>-->
        </div>
      </div>
    </nav>
    <HelloWorld />
  </div>
</template>

<script>
import HelloWorld from "./components/HelloWorld.vue";

export default {
  name: "App",
  components: {
    HelloWorld,
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
