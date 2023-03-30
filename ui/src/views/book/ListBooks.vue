<script setup>
  import { onMounted, ref } from "vue";
  import { useBookStore } from "@/stores/books"
  const searchinput = ref("");
  const ubook = useBookStore();
  onMounted(()=>{
    ubook.getBooks(),
    ubook.getSubjects()
  });
  function searchBook(){
    return ubook.books.filter((book) => 
      book.title.toLowerCase().includes(searchinput.value.toLowerCase()
    ))
  }
</script>
<template>
  
<main id="main">
  <!-- ======= Aall Books Section ======= -->
  <section id="about" class="about">
    <div class="container" data-aos="fade-up">
      <div class="row justify-content-center">
        <div class="col-md-8 input-group">
          <input type="search" class="form-control" placeholder="Search" @input="searchBook" v-model="searchinput">
        </div>
      </div>

      <div class="row content justify-content-center">
        <div class="col-lg-8">
          <table class="table table-striped">
            <thead>
              <tr>
                <th>#</th>
                <td>Title</td>
                <td>Copies</td>
                <td colspan="3">Actions</td>
              </tr>
            </thead>
            <tbody>
              <tr v-if="searchBook().length===0">
                <td colspan="6">Search not found</td>
              </tr>
              <tr v-for="(book, index) in searchBook()" v-bind:key="index">
                <th>{{ index+1 }}</th>
                <td>{{ book.title }}</td>
                <td>{{ book.copies }}</td>
                <td><button class="btn btn-danger" @click="ubook.decCount(book.id)">-</button></td>
                <td><button class="btn btn-primary" @click="ubook.incCount(book.id)">+</button></td>
                <td><button class="btn btn-danger" @click="ubook.delBooks(book.id)">Del</button></td>
              </tr>
            </tbody>
            
          </table>
        </div>
        <div class="col-lg-4">
          <div class="card">
            <div class="card-header text-center"><h2>Add Book</h2></div>
            <form @submit.prevent="ubook.addBooks" class="card-body bg-primary">
              <div class="input-group">
                <input type="text" class="form-control" placeholder="title" v-model="ubook.bookForm.title">
              </div>
              <div class="input-group">
                <input type="number" :min="1" :max="100" class="form-control" placeholder="Copies" v-model="ubook.bookForm.copies">
              </div>
              <div class="input-group">
                <select class="form-select form-control" v-model="ubook.bookForm.subject">
                  <option disabled selected value="1">Subjects</option>
                  <option v-for="(subject, index) in ubook.subjects" v-bind:key="index" :value="subject.id">{{ subject.name }}</option>
                </select>
              </div>
              <div class="input-group">
                <input type="submit" value="submit">
              </div>
            </form>
          </div>
        </div>
      </div>

    </div>
  </section><!-- End All books Section -->

</main><!-- End #main -->
</template>

<style scoped>
div.input-group{
  margin: 15px 0;
}
input[type="search"]{
  outline: 2px dashed blue;
  margin: 10px 0 30px 0;
}
</style>
