<template src="../../html/password-change.html">  
</template>

<script>
import alertify from 'alertifyjs';

export default {
  name: 'LoginView', 
  inject: ["stores", "alertifyjs"],//, "isLoading"],
  data() {
   return {
    form: {},
    loginError: ""
   }
  },
  methods: {
        async loginForm() { 
        const { new_password1, new_password2} = this.form; 
        const res = await this.stores.changePassword(new_password1, new_password2)
        if (res.data.status === 401){
          this.stores.logout()
        }
        else if(res.data.status === 400){
          this.alertifyjs.error("Invalid username or password")
        }
    }
  },
}
</script>

