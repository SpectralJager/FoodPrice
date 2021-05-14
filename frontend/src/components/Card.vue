<template>
  <div class="card">
    <img class="card--img" :src="category.img_bg_url" :alt="category.name + ' img'">
    <div class="card--content">
      <h2 class="title">{{ category.name }}</h2>
      <p class="description">
          {{ category.description }}
      </p>
    </div>
    <div class="card--footer">
      <a href="#" class="btn"><router-link :to="'/' + category.name" :category_id="category.name">Show products</router-link></a>
    </div>
  </div>
</template>

<script>
export default {
    props: {
        category: Object,
    }
}
</script>

<style lang="scss">
.card{
  height: 600px;
  widows: 100%;
  border: 1px solid black;
  border-radius: 2rem;
  overflow: hidden;
  &--img{
    width: 100%;
    height: 50%;
  }
  &--content{
    padding: 5%;
    height: 40%;
    .title{
      font-size: 2rem;
      margin-bottom: 1.5rem;
    }
    .description{
      font-size: 1rem;
    }

  }
  &--footer{
    background: linear-gradient(20deg, #fbd07c, #f7f779);
    height: 10%;
    color: #000;
    font-size: 1.5rem;
    font-weight: 700;
    display: flex;
    align-items: center;
    justify-content: center;
  }
}
</style>