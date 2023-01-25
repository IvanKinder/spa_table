<template>
  <div class="modal-wrapper" v-if="modalVisible">
    <form class="add-form">
      <div class="mb-3">
        <label for="number" class="form-label">Номер заявки</label>
        <input type="number" class="form-control" id="number" v-model="appealNumber">
      </div>
      <div class="mb-3">
        <label for="description" class="form-label">Описание</label>
        <div class="form-outline">
          <textarea class="form-control" id="description" rows="4" v-model="description"></textarea>
        </div>
      </div>
      <button type="submit" class="btn btn-primary" @click="onAppealAdd">Submit</button>
    </form>
  </div>
</template>

<script>
export default {
  name: "ModalWindow",
  data() {
    return {
      modalVisible: false,
      appealNumber: null,
      description: null,
      parentComponent: null
    }
  },
  methods: {
    onAppealAdd() {
      fetch(`http://127.0.0.1:8000/appeals/`, {
        method: 'POST',
        body: JSON.stringify({
          appealNumber: this.appealNumber,
          description: this.description,
        })
      }).then((response) => {
        return response.json();
      }).then((data) => {
        console.log(data);
        this.parentComponent.getAppeals({});
        this.modalVisible = false;
      });
    }
  }
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
  max-width: 40vw;
  padding: 2%;
  border-radius: 10px;
}
</style>