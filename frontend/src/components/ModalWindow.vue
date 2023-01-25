<template>
  <div class="modal-wrapper">
    <form class="add-form">
      <div class="mb-3">
        <label for="number" class="form-label">Номер заявки</label>
        <input type="number" class="form-control" id="number">
      </div>
      <div class="mb-3">
        <label for="description" class="form-label">Описание</label>
        <input type="text" class="form-control" id="description">
      </div>
      <div class="mb-3">
        <label for="status" class="form-label">Статус</label>
        <input type="radio" class="form-control" id="status">
      </div>
      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
  </div>
</template>

<script>
export default {
  name: "ModalWindow",
  data() {
    return {
      modalVisible: false,
    }
  },
}
</script>

<style scoped>
.modal-wrapper {
  left: 0;
  top: 0;
  z-index: 2;
  width: 100vw;
  height: 100vh;
  position: absolute;
  background-color: rgba(88, 94, 88, 0.6);
}

.add-form {
  background: #e0e0e0;
  margin: 20vh auto;
  max-width: 50vw;
  padding: 2%;
  border-radius: 10px;
}
</style>