<template src="./html/profile.html">
</template>

<script setup>
import { useAuthStore } from "@/stores/auth"
import { onMounted } from "vue";
const stores = useAuthStore()
onMounted(() => {
  stores.getUserProfile()
})
</script>

