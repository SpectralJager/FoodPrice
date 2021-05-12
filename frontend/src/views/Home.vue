<template>
  <div class="home">
    <h1 class="title">Your products list</h1>
    <button type="button" class="btn btn-primary" @click="showModal = true">
      Add Product
    </button>
    <ProductsList :products="products"/>
  </div>
  <div class="container-fluid" v-if="showModal">
    <Modal /> 
  </div>
</template>

<script>
// @ is an alias to /src
import ProductsList from '@/components/ProductsList.vue'
import Modal from '@/components/Modal.vue';

export default {
  name: 'Home',
  data() {
    return {
      showModal: false,
      name: '',
      description: '',
      img_url: '',
      products: []
    }
  },
  watch: {
    showModal(n, o) {
      console.log(this.showModal);
    }
  },
  methods: {
    sendProducts() {
      this.products.push({
        name: this.name,
        description: this.description,
        img_url: this.img_url
      });
      this.name = '';
      this.description = '';
      this.img_url = '';
    },
    editProduct(){
      console.log('edit');
    },
    deleteProduct(){
      console.log('delete');
    }
  },
  components: {
    ProductsList,
    Modal
  }
}
</script>
<style lang="scss">
h1{
  border-bottom: 1px solid black;
  padding-bottom: 1rem;
  display: inline-block;
}
.home{
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
</style>
