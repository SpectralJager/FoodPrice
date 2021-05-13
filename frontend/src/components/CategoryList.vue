<template>
<div class="table-responsive">
    <table class="table table-dark table-striped">
    <thead>
        <tr>
        <th scope="col">#</th>
        <th scope="col">Name</th>
        <th scope="col">Description</th>
        <th scope="col">Count</th>
        <th scope="col"></th>
        </tr>
    </thead>
    <tbody>
        <tr v-for="(category, index) in categories" :key="index">
        <th scope="row">1</th>
        <td>{{ category.name }}</td>
        <td>{{ category.description }}</td>
        <td>{{ category.items.length }}</td>
        <td>
            <button class="btn btn-success" @click="showItems(category)">Items</button>
        </td>
        </tr>
    </tbody>
    </table>
    <div v-if="show_items" class="mt-5">
        <button class="btn btn-secondary" @click="hideItems">Hide</button>
        <ItemsList :items="items" />
    </div>
</div>
</template>

<script>
import ItemsList from '@/components/ItemsList.vue';
export default {
    components: {
        ItemsList,
    },
    props: {
        categories: Object,
    },
    data(){
        return {
            show_items: false,
            items: {},
        }
    },
    methods: {
        showItems(category){
            this.show_items = true;
            this.items = category.items;
        },
        hideItems(){
            this.show_items = false;
        }
    }
}
</script>

<style>

</style>