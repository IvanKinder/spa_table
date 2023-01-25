<template>
  <div class="hello">
    <ModalWindow ref="modal"></ModalWindow>
    <p>Список Обращений</p>
    <div class="top-bar">
      <div class="btn-group" role="group" aria-label="Button group with nested dropdown">
        <button type="button" class="btn btn-light first-btn" @click="getAppeals({
          filterBy: 'status-0'
        })">Открытые
        </button>
        <button type="button" class="btn btn-light middle-btn" @click="getAppeals({
          filterBy: 'status-2'
        })">Закрытые
        </button>
        <button type="button" class="btn btn-light last-btn" @click="getAppeals({
          filterBy: ''
        })">Все
        </button>
      </div>
      <ul class="nav">
        <li class="nav-item search-field">
          <input type="search"
                 class="form-control"
                 @input="searchByNumber"
                 id="search"
                 placeholder="search by number"
                 ref="searchField">
        </li>
        <li class="nav-item">
          <button type="button" class="btn btn-light" @click="onAddClick">Добавить</button>
        </li>
      </ul>
    </div>
    <div class="container">
      <div class="row">
        <div class="col">
          <button type="button"
                  class="btn dropdown-toggle"
                  data-bs-toggle="dropdown"
                  role="button"
                  aria-expanded="false">Номер заявки
          </button>
          <ul class="dropdown-menu">
            <li>
              <button type="button"
                      class="btn dropdown-item"
                      @click="getAppeals({
                        orderBy: 'number'
                      })">По возрастанию
              </button>
            </li>
            <li>
              <button type="button"
                      class="btn dropdown-item"
                      @click="getAppeals({
                        orderBy: '-number'
                      })">По убыванию
              </button>
            </li>
          </ul>
        </div>
        <div class="col">
          <button type="button" class="btn dropdown-toggle" data-bs-toggle="dropdown" role="button"
                  aria-expanded="false">Дата создания
          </button>
          <ul class="dropdown-menu">
            <li>
              <button type="button"
                      class="btn dropdown-item"
                      @click="getAppeals({
                        orderBy: 'created_at'
                      })">По возрастанию
              </button>
            </li>
            <li>
              <button type="button"
                      class="btn dropdown-item"
                      @click="getAppeals({
                        orderBy: '-created_at'
                      })">По убыванию
              </button>
            </li>
          </ul>
        </div>
        <div class="col">
          Описание
        </div>
        <div class="col">
          Создатель
        </div>
        <div class="col">
          <button type="button"
                  class="btn dropdown-toggle"
                  data-bs-toggle="dropdown"
                  role="button"
                  aria-expanded="false">Статус
          </button>
          <ul class="dropdown-menu">
            <li>
              <button type="button"
                      class="btn dropdown-item"
                      @click="getAppeals({
                        orderBy: 'status'
                      })">По возрастанию
              </button>
            </li>
            <li>
              <button type="button"
                      class="btn dropdown-item"
                      @click="getAppeals({
                        orderBy: '-status'
                      })">По убыванию
              </button>
            </li>
          </ul>
        </div>
      </div>
    </div>
    <div class="table">
      <div
          class="row"
          v-for="appeal in appealsList"
          :key="appeal.fields.id">
        <div class="col">
          {{ appeal.fields.number }}
        </div>
        <div class="col">
          {{ appeal.fields.created_at }}
        </div>
        <div class="col">
          {{ appeal.fields.description }}
        </div>
        <div class="col">
          {{ appeal.fields.creator }}
        </div>
        <div class="col">
          {{ appeal.fields.status }}
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ModalWindow from "@/components/ModalWindow";

export default {
  name: 'AppealsTable',
  components: {
    ModalWindow,
  },
  data() {
    return {
      appealsList: [],
      filterBy: '',
      orderBy: ''
    }
  },
  methods: {
    getAppeals(params) {
      this.$refs.searchField.value = '';

      if (Object.hasOwn(params, 'orderBy')) {
        this.orderBy = params.orderBy;
      }
      if (Object.hasOwn(params, 'filterBy')) {
        this.filterBy = params.filterBy;
      }
      fetch(`http://127.0.0.1:8000/appeals/?filterBy=${this.filterBy}&orderBy=${this.orderBy}`).then((response) => {
        return response.json();
      }).then((data) => {
        this.appealsList = data.data;
      });
    },
    searchByNumber(e) {
      fetch(`http://127.0.0.1:8000/appeals/?search=${e.target.value}&filterBy=${this.filterBy}&orderBy=${this.orderBy}`).then((response) => {
        return response.json();
      }).then((data) => {
        this.appealsList = data.data;
      });
    },
    onAddClick() {
      this.$refs.modal.modalVisible = true;
      this.$refs.modal.parentComponent = this;
    },
  },
  mounted() {
    this.getAppeals({});
  }
}
</script>

<style scoped>
p {
  text-align: left;
}

.hello {
  margin: 5%
}

.table {
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  max-height: 30vh;
  overflow: auto;
}

.row {
  margin: 1%;
}

.btn-light {
  background: #F1F6FB;
}

.form-control {
  position: relative;
  z-index: 1;
}

.nav-item {
  background: white;
}

.top-bar {
  margin-top: 2vh;
  display: flex;
  justify-content: space-between;
}
</style>
