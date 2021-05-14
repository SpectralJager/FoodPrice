<template>
  <div class="card-list">
    <Card v-for="(category, index) in categories" :key="index" :category="category"/>
  </div>
</template>

<script>
import Card from "@/components/Card.vue";

export default {
  name: 'Home',
  components: {
    Card,
  },
  data() {
    return {
      categories: [
        {
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
        {
          name: 'Sushi',
          description: 'Cillum laboris occaecat commodo consequat dolore aute culpa fugiat. Consequat ullamco aliquip minim dolore minim. Occaecat adipisicing anim elit ea ullamco pariatur non laborum est. Fugiat culpa velit do voluptate proident excepteur do officia occaecat do sit.',
          img_bg_url: 'https://images.unsplash.com/photo-1513104890138-7c749659a591?ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8cGl6emF8ZW58MHx8MHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60',
          products: [

          ]
        },
        {
          name: 'Burger',
          description: 'Cillum laboris occaecat commodo consequat dolore aute culpa fugiat. Consequat ullamco aliquip minim dolore minim. Occaecat adipisicing anim elit ea ullamco pariatur non laborum est. Fugiat culpa velit do voluptate proident excepteur do officia occaecat do sit.',
          img_bg_url: 'https://images.unsplash.com/photo-1513104890138-7c749659a591?ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8cGl6emF8ZW58MHx8MHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60',
          products: [

          ]
        },
      ]
    }
  }
}
</script>
<style lang="scss">

</style>
