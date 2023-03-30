import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from "axios"
const BASE = "http://127.0.0.1:8000"
import { useAuthStore } from "@/stores/auth"
export const useBookStore = defineStore('counter', () => {
  const auth = useAuthStore();
  const searchinput = ref("");
  const books = ref([]);
  const subjects = ref([]);
  const subForm = ref({name: "", desc:""});
  const bookForm = ref({title:"", subject:1, copies: 1, shelved_by: auth.stores.data.user.pk});
  const doubleCount = computed(() => count.value * 2);
  function getSubjects() {
    axios.get(`${BASE}/v1/api/subject/`)
    .then(res => {
      this.subjects = res.data
    })
    .catch(e=>{
      console.log(e.response)
    })
  }
  function addSubjects() {
    axios.post(`${BASE}/v1/api/subject/`, this.subForm)
    .then(res=>{
      this.getSubjects()
    })
    .catch(e=>{
      console.log(e.response)
    })
  }
  function delSubjects(pk) {
    axios.delete(`${BASE}/v1/api/subject/${pk}/`)
    .then(res=>{
      this.getSubjects(),
      alert("deleted")
    })
    .catch(e=>{
      console.log(e.response)
    })
  }
  function getBooks() {
    axios.get(`${BASE}/v1/api/book/`)
    .then(res => {
      this.books = res.data
    })
    .catch(e=>{
      console.log(e.response)
    })
  }
  function addBooks() {
    axios.post(`${BASE}/v1/api/book/`, this.bookForm)
    .then(res=>{
      this.getBooks()
    })
    .catch(e=>{
      console.log(e.response)
    })
  }
  function delBooks(pk) {
    axios.delete(`${BASE}/v1/api/book/${pk}/`)
    .then(res=>{
      this.getBooks(),
      alert("deleted")
    })
    .catch(e=>{
      console.log(e.response)
    })
  }
  function incCount(pk) {
    axios.patch(`${BASE}/v1/api/book/${pk}/`, {copies: this.bookForm.copies++})
    .then(res =>{
      this.getBooks()
    })
    .catch(e=>{
      console.log(e.response)
    })
  }
  function decCount(pk) {
    axios.patch(`${BASE}/v1/api/book/${pk}/`, {copies: this.bookForm.copies--})
    .then(res =>{
      this.getBooks()
    })
    .catch(e=>{
      console.log(e.response)
    })
  }
  return { incCount, decCount, subForm, getSubjects, addSubjects, delSubjects, subjects, bookForm, books, getBooks, addBooks, delBooks }
})
