<template>
  <div class="hello">
    <ModalWindow v-if="addAppealWindow"></ModalWindow>
    <h2>Список Обращений</h2>
    <ul class="nav">
      <li class="nav-item">
        <button type="button" class="btn btn-light" @click="getOpenedAppeals">Открытые</button>
      </li>
      <li class="nav-item">
        <button type="button" class="btn btn-light" @click="getClosedAppeals">Закрытые</button>
      </li>
      <li class="nav-item">
        <button type="button" class="btn btn-light" @click="getAllAppeals">Все</button>
      </li>
      <li class="nav-item">
        <input type="search" class="form-control" @input="searchByNumber" id="search" placeholder="search by number">
      </li>
      <li class="nav-item dropdown">
        <button type="button" class="btn btn-light nav-link dropdown-toggle" data-bs-toggle="dropdown" role="button" aria-expanded="false">Сортировка</button>
        <ul class="dropdown-menu">
          <li><button type="button" class="btn btn-light dropdown-item" @click="getSortedAppeals('created_at')">По дате</button></li>
          <li><button type="button" class="btn btn-light dropdown-item" @click="getSortedAppeals('status')">По статусу</button></li>
        </ul>
      </li>
      <li class="nav-item">
        <button type="button" class="btn btn-light" @click="onAddClick">Добавить</button>
      </li>
      <div class="container">
        <div class="row">
          <div class="col">
            Номер заявки
          </div>
          <div class="col">
            Дата создания
          </div>
          <div class="col">
            Описание
          </div>
          <div class="col">
            Создатель
          </div>
          <div class="col">
            Статус
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
    </ul>
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
      addAppealWindow: false
    }
  },
  methods: {
    getAllAppeals() {
      fetch('http://127.0.0.1:8000/appeals/?filter=&search=').then((response) => {
        return response.json();
      }).then((data) => {
        this.appealsList = data.data;
      });
    },
    getOpenedAppeals() {
      fetch('http://127.0.0.1:8000/appeals/?filter=0&search=').then((response) => {
        return response.json();
      }).then((data) => {
        this.appealsList = data.data;
      });
    },
    getClosedAppeals() {
      fetch('http://127.0.0.1:8000/appeals/?filter=2&search=').then((response) => {
        return response.json();
      }).then((data) => {
        this.appealsList = data.data;
      });
    },
    getSortedAppeals(filter_param) {
      fetch(`http://127.0.0.1:8000/appeals/?filter=${filter_param}&search=`).then((response) => {
        return response.json();
      }).then((data) => {
        this.appealsList = data.data;
      });
    },
    searchByNumber(e) {
      fetch(`http://127.0.0.1:8000/appeals/?filter=&search=${e.target.value}`).then((response) => {
        return response.json();
      }).then((data) => {
        this.appealsList = data.data;
      });
    },
    onAddClick() {
      this.addAppealWindow = true;
      // const today = new Date();
      // this.appealsList.unshift({
      //   fields: {
      //     created_at : today.toDateString(),
      //     creator : 1,
      //     description : '',
      //     number : 0,
      //     status : 0
      //   }
      // });
    },
  },
  mounted() {
    this.getAllAppeals();
  }
}
</script>

<style scoped>
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

.dropdown {
  background: #f8f9fa
}

.btn-light, .dropdown-toggle {
  height: 40px;
  color: black;
}

.form-control {
    position: relative;
    z-index: 1;
}
</style>
