<template>
<div class="container mx-auto my-3 p-5 bg-secondary text-light">
    <h1>Controle panel</h1>
</div>
<div class="container">
    <CategoryList :categories="categories"/>
</div>
</template>

<script>
import CategoryList from '@/components/CategoryList.vue';
export default {
    components: {
        CategoryList,
    },
    data() {
        return {
            categories: [
                {
                    name: 'Pizza',
                    description: 'Tasty pizza for tasty price!',
                    items: [
                        {
                            name: '1',
                            description: '1',
                            price: 220.0
                        },
                        {
                            name: '2',
                            description: '2',
                            price: 320.0
                        },
                        {
                            name: '3',
                            description: '3',
                            price: 420.0
                        }
                    ]
                },
                {
                    name: 'Sushi',
                    description: 'Tasty sushi for tasty price!',
                    items: [
                        {
                            name: 'Sushi 1',
                            description: '1',
                            price: 220.0
                        },
                        {
                            name: 'Sushi 2',
                            description: '2',
                            price: 320.0
                        },
                    ]
                }
            ]
        }
    },

}
</script>

<style>

</style>