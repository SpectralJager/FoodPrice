<template>
  <div class="modal" id="ProductModal" tabindex="-1">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">Product</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
        </div>
        <div class="modal-body">
          <form>
            <div class="mb-3">
              <label class="form-label">Product name</label>
              <input type="text" class="form-control" placeholder="Product name">
            </div>
            <div class="mb-3">
              <label class="form-label">Description of product</label>
              <textarea class="form-control" rows="3"></textarea>
            </div>
            <div class="mb-3">
              <label class="form-label">Img url of product</label>
              <input type="text" class="form-control" >
            </div>
          </form>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
          <button type="button" class="btn btn-success" @click="saveProduct">Save</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Modal',
}
</script>

<style lang="scss">
.modal{
  color: black;
  display: block;
}
</style>