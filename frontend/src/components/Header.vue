<template>
  <header>
      <div class="logo">
          <span>FPC</span>
      </div>
      <nav class="navbar">
          <span class="navbar--link">
              <router-link to="/">Home</router-link>
          </span>
          <span class="navbar--link">
              <span class="dropdown-toggler">Categories</span>
              <div class="dropdown">
                <router-link to="/Pizza">Pizza</router-link>
                <router-link to="/Sushi">Sushi</router-link>
                <router-link to="/Burger">Burger</router-link>
              </div>
          </span>
          <span class="navbar--link">
              <router-link to="/admin">Admin</router-link>
          </span>
      </nav>
  </header>
</template>

<script>
export default {

}
</script>

<style>

</style>