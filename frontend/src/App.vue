<template>
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
  <div class="container-fluid">
    <span class="navbar-brand"><router-link to="/">FoodPrice</router-link></span>
    <button 
      class="navbar-toggler" 
      type="button" 
      data-bs-toggle="collapse" 
      data-bs-target="#navbarSupportedContent" 
      aria-controls="navbarSupportedContent" 
      aria-expanded="false" 
      aria-label="Toggle navigation"
    >
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <router-link to="/">Home</router-link>
        </li>
        <li class="nav-item">
            <router-link to="/panel">Panel</router-link>
        </li>
      </ul>
    </div>
  </div>
</nav>
  <router-view/>
</template>

<script>
export default {
}
</script>


<style lang="scss">
a{
  text-decoration: none;
  color: inherit;
}
*,*::before,*::after{
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
.nav-item{
  margin: 0 1rem;
  color: hsla(120, 100%, 97%, .8);
}

</style>
