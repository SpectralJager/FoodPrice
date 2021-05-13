<template>
<table class="table table-info table-striped">
  <thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">Name</th>
      <th scope="col">Description</th>
      <th scope="col">Price</th>
    </tr>
  </thead>
  <tbody>
    <tr v-for="(item, index) in items" :key="index">
      <th scope="row">{{ index+1 }}</th>
      <td>{{ item.name }}</td>
      <td>{{ item.description }}</td>
      <td>{{ item.price }}</td>
    </tr>
  </tbody>
</table>
</template>

<script>
export default {
    props: {
        items: Object,
    }

}
</script>

<style>

</style>