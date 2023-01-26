<template>
  <div class="hello">
    <ModalWindow ref="modal"></ModalWindow>
    <p>Список Обращений</p>
    <div class="top-bar">
      <div class="btn-group" role="group" aria-label="Button group">
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
    <div class="table" id="table">
      <div
          class="row"
          v-for="appeal in appealsList"
          :key="appeal.id">
        <div class="col">
          {{ appeal.number }}
        </div>
        <div class="col">
          {{ appeal.created_at }}
        </div>
        <div class="col">
          {{ appeal.description }}
        </div>
        <div class="col">
          {{ appeal.creator }}
        </div>
        <div class="col">
          {{ appeal.status }}
        </div>
      </div>
    </div>
    <nav aria-label="Page navigation">
      <ul class="pagination">
        <li class="page-item">
          <button type="button"
                  class="btn disabled"
                  @click="setPage(page - 1)"
                  id="prevBtn">&laquo;
          </button>
        </li>
        <li v-for="page in pages" :key="page">
          <button type="button"
                  class="btn"
                  @click="setPage(page)"
                  :id="page">{{ page }}
          </button>
        </li>
        <li class="page-item">
          <button type="button"
                  class="btn"
                  @click="setPage(page + 1)"
                  id="nextBtn">&raquo;
          </button>
        </li>
      </ul>
    </nav>
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
      orderBy: '',
      pagesCount: 0,
      page: 1,
      searchLike: null,
    }
  },
  methods: {
    getAppeals(params) {
      if (Object.hasOwn(params, 'orderBy')) {
        this.orderBy = params.orderBy;
        this.$refs.searchField.value = '';
        this.searchLike = null;
      }
      if (Object.hasOwn(params, 'filterBy')) {
        this.filterBy = params.filterBy;
        this.$refs.searchField.value = '';
        this.searchLike = null;
      }
      fetch(`http://127.0.0.1:8000/appeals/?filterBy=${this.filterBy}&orderBy=${this.orderBy}&page=${this.page}&search=${this.searchLike}`).then((response) => {
        return response.json();
      }).then((data) => {
        this.appealsList = data.data;
        this.pagesCount = data.pagesCount;
      });
    },
    searchByNumber(e) {
      this.searchLike = e.target.value;
      this.getAppeals({});
    },
    onAddClick() {
      this.$refs.modal.modalVisible = true;
      this.$refs.modal.parentComponent = this;
    },
    setPage(page) {
      const prevBtn = document.getElementById('prevBtn');
      const nextBtn = document.getElementById('nextBtn');
      const table = document.getElementById('table');

      table.scrollTo(0, 0);

      if (document.getElementById(this.page)) {
        document.getElementById(this.page).classList.remove('disabled');
      }

      if (page === 1) {
        prevBtn.classList.add('disabled');
      } else {
        prevBtn.classList.remove('disabled');
      }
      if (page === this.pagesCount || this.pagesCount === 1) {
        nextBtn.classList.add('disabled');
      } else {
        nextBtn.classList.remove('disabled');
      }
      this.page = page;

      if (document.getElementById(this.page)) {
        document.getElementById(this.page).classList.add('disabled');
      }
      this.getAppeals({});
    },
  },
  computed: {
    pages() {
      const pagesList = [];

      for (let i = 1; i < this.pagesCount + 1; i++) {
        pagesList.push(i);
      }

      return pagesList
    }
  },
  mounted() {
    this.getAppeals({});
  },
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
  height: 30vh;
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

.pagination {
  display: inline-flex;
}

.page-link {
  color: black
}
</style>
