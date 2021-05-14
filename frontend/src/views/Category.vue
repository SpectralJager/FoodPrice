<template>
  <div class="info">
    <img :src="category.img_bg_url" alt="">
    <h1 class="info--title">{{category.name}}</h1>
    <p class="info--description">{{category.description}}</p>
  </div>
  <div class="product-list">
    <Product v-for="(product, index) in category.products" :key="index" :product="product"/>
  </div>
</template>

<script>
import Product from '@/components/Product.vue';

export default {
  components: {
    Product,
  },
  props: {
    category_id: String,
  },
  data() {
    return {
      category: {
        name: 'Pizza',
        description: 'Cillum laboris occaecat commodo consequat dolore aute culpa fugiat. Consequat ullamco aliquip minim dolore minim. Occaecat adipisicing anim elit ea ullamco pariatur non laborum est. Fugiat culpa velit do voluptate proident excepteur do officia occaecat do sit.',
        img_bg_url: 'https://images.unsplash.com/photo-1513104890138-7c749659a591?ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8cGl6emF8ZW58MHx8MHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60',
        products: [
          {
            name: 'Pizza1',
            description: 'Pizza1 description',
            count: 0,
            avg_price: 0,
            items: [
              {
                store: 'Store1',
                price: 220.0,
                link: '#',
              },
              {
                store: 'Store2',
                price: 220.0,
                link: '#',
              },
              {
                store: 'Store3',
                price: 220.0,
                link: '#',
              },
            ]
          },
          {
            name: 'Pizza2',
            description: 'Pizza2 description',
            count: 0,
            avg_price: 0,
            items: [
              {
                store: 'Store1',
                price: 220.0,
                link: '#',
              },
              {
                store: 'Store2',
                price: 220.0,
                link: '#',
              },
              {
                store: 'Store3',
                price: 220.0,
                link: '#',
              },
            ]
          },
        ]
      },
    }
  }

}
</script>

<style>

</style>