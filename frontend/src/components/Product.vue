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
  <hr>
</template>

<script>
export default {
  props: {
    product: Object,
  }

}
</script>

<style lang="scss">
.product{
  widows: 100%;
  &--title{
    font-size: 2rem;
  }
  &--description{
    font-size: 1.25rem;
  }
  span{
    display: block;
  }
  table{
    margin-top: 1rem;
    border-collapse: collapse;
    border-spacing: 0;
    width: 100%;
    border: 1px solid #ddd;
    thead{
      background-color: #121212;
      color: #fff;
      font-size: 1.25rem;
      font-weight: 700;
    }
    th, td {
      text-align: left;
      padding: 16px;
    }
    tr:nth-child(even) {
      background-color: #f2f2f2;
    }
  }

}
</style>