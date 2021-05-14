<template>
  <header>
      <div class="logo">
          <span>FoodPrice</span>
      </div>
      <nav class="navbar">
          <span class="navbar--link">
              <router-link to="/">Home</router-link>
          </span>
          <span class="navbar--link dropdown">
              <span class="dropdown-toggler">Categories</span>
              <div class="dropdown--content">
                <router-link to="/Pizza">Pizza</router-link>
                <router-link to="/Sushi">Sushi</router-link>
                <router-link to="/Burger">Burger</router-link>
              </div>
          </span>
      </nav>
  </header>
</template>

<script>
export default {
  data() {
    return {
      showDropdown: false,
    }
  }
}
</script>

<style lang="scss">
header{
  width: 100%;
  height: 64px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 10%;
  background: linear-gradient(30deg, #ef709b, #fa9372);
  .logo{
    font-size: 1.5rem;
    color: #fff;
    font-weight: 700;
    letter-spacing: .3rem;
  }
  .navbar{
    display: flex;
    justify-content: space-around;
    width: 250px;
    color: #fff;
    &--link{
      font-size: 1.2rem;
    }
    .dropdown{
      position: relative;
      &--content{
        position: absolute;
        display: none;
        flex-direction: column;
        align-items: center;
        justify-content: space-around;
        height: 8rem;
        width: 6rem;
        padding: 1% 0;
        background-color: #595cff;
      }
      &:hover{
        .dropdown--content{
          display: flex;
        }
      }
    }
  }
}
</style>