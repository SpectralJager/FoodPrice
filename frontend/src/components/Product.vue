<template>
  <div class="product">
    <h3 class="product--title">{{product.name}}</h3>
    <p class="product--description">{{product.description}}</p>
    <span class="product--count">Count: {{product.count}}</span>
    <span class="product--avg-price">Avg.Price: {{product.avg_price}}</span>
    <table>
      <thead>
        <th>#</th>
        <th>Store</th>
        <th>Price</th>
        <th>Link</th>
      </thead>
      <tbody>
        <tr v-for="(item, index) in product.items" :key="index">
          <td>{{ index+1 }}</td>
          <td>{{ item.store }}</td>
          <td>{{ item.price }}</td>
          <td><a :href="item.link">Click</a></td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  props: {
    product: Object,
  }

}
</script>

<style>

</style>