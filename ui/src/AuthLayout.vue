<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>
<template>
<!-- ======= Hero Section ======= -->
<section id="hero" class="d-flex align-items-center" style="height: 100vh; background-image: url(/assets/img/lib.jpg); background-position: center; background-repeat: no-repeat; background-size: cover;">

  <div class="container" >
    <div class="row" >
      <div class="col-lg-6 d-flex flex-column justify-content-center pt-4 pt-lg-0 order-2 order-lg-1" data-aos="fade-up" data-aos-delay="200">
        <h1>My Library</h1>
        <h2>Library Management System</h2>
        
      </div>
      <div class="col-lg-6 order-2 order-lg-2 hero-img" >
        <RouterView />
      </div>
    </div>
  </div>

</section><!-- End Hero -->

</template>