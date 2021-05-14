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

<style>

</style>