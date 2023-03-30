<template src="./html/pages-login.html">  
</template>

<script setup>
import { useAuthStore } from "@/stores/auth"
//import { ref, reactive, computed } from "vue"
//import alertify from 'alertifyjs';
 const stores = useAuthStore()

  const loginAction =  async () => { 
        const { email, password } = stores.loginForm; 
        const res = await stores.login(email, password)
        if (res === "invalid-user"){
          alert("Invalid username or password")
        }
    }
  

</script>

