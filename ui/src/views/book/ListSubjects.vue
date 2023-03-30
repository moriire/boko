<script setup>
  import { onMounted, ref } from "vue";
  import { useBookStore } from "@/stores/books"
  const ubook = useBookStore();
  let searchinput = ref("");
  onMounted(() => {
    ubook.getSubjects()
  });
  function searchSub(){
    return ubook.subjects.filter((subject) => 
      subject.name.toLowerCase().includes(searchinput.value.toLowerCase()
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
          <input type="search" class="form-control" placeholder="Search" @input="searchSub" v-model="searchinput">
        </div>
      </div>
      <div class="row content justify-content-center">

        <div class="col-lg-8">
          <table class="table table-striped">
            <thead>
              <tr>
                <th>#</th>
                <td>Title</td>
                <td>Created on</td>
                <td colspan="3">Actions</td>
              </tr>
            </thead>
            <tbody>
              <tr v-if="searchSub().length===0">
                <td colspan="6">Search not found</td>
              </tr>
              <tr v-for="(sub, index) in searchSub()" v-bind:key="index">
                <th>{{ index+1 }}</th>
                <td>{{ sub.name }}</td>
                <td>{{ sub.created_on }}</td>
                <!--td><button class="btn btn-danger">-</button></td>
                <td><button class="btn btn-primary">+</button></td-->
                <td><button class="btn btn-danger" @click="ubook.delSubjects(sub.id)">Del</button></td>
              </tr>
            </tbody>
            <tfooter>

            </tfooter>
          </table>
        </div>
        <div class="col-lg-4">
          <div class="card">
            <div class="card-header text-center"><h2>Add Subject</h2></div>
            <form @submit.prevent="ubook.addSubjects" class="card-body bg-primary">
              <div class="input-group">
                <input type="text" class="form-control" placeholder="Subject Name" v-model="ubook.subForm.name" required>
              </div>
              <div class="input-group">
                <textarea class="form-control" placeholder="Subject Description" v-model="ubook.subForm.desc"></textarea>
              </div>
              
              <div class="input-group">
                <input type="submit" value="Add Subject">
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