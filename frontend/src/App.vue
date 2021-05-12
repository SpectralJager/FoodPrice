<template>
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
  <div class="container-fluid">
    <span class="navbar-brand"><router-link to="/">FoPriC</router-link></span>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <span class="nav-link"><router-link to="/">Home</router-link></span>
        </li>
        <li class="nav-item">
          <span class="nav-link"><router-link to="/about">About</router-link></span>
        </li>
      </ul>
    </div>
  </div>
</nav>
<router-view/>
</template>

<style lang="scss">
a{
  color: inherit;
  text-decoration: none;
}

.navbar{
  margin-bottom: 2rem;
}
</style>
