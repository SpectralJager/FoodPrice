<template>
  <div class="container mt-5">
    <table class="table table-dark table-hover">
      <thead>
        <tr>
          <th>#</th>
          <th>Name</th>
          <th>Description</th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(product, index) in products" :key="index">
          <td>{{ index }}</td>
          <td>{{ product.name }}</td>
          <td>{{ product.description }}</td>
          <td>
            <div class="btn-group float-end">
              <button class="btn btn-warning" data-bs-toggle="modal" data-bs-target="#ProductModal" @click="this.$parent.editProduct">Edit</button>
              <button class="btn btn-danger" @click="this.$parent.deleteProduct">Delete</button>
            </div>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>

export default {
  name: 'ProductList',
  props: {
    products: Object,
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss">

</style>
