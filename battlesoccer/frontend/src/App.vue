<template>
  <div>
    <transition> 
    <div v-if="loading">
    <preloader/>
</div></transition>
   <div v-if="!loading"> 
    <NavbarComponent/>
    <transition name="fade" mode="out-in" appear> 
    <router-view/></transition>
<a id="back2Top" title="Back to top" href="#">&#10148;</a>

   </div>

  </div>
</template>

<script>
import $ from 'jquery'
import Swal from 'sweetalert2'
import { apiService } from "@/common/api.service.js";
import NavbarComponent from "@/components/Navbar.vue";
import preloader from "@/components/preloader.vue";
export default {
  name: "App",
  components: {
    NavbarComponent,
    preloader

  },
  data() {
    return {
      loading: false,
      requestUser:null

    }
  },
  
  methods:{
    test(){
      if (!this.requestUser) {
 Swal.fire({
  showCloseButton: true, 
  position: 'top-end',
  showConfirmButton: false,
  html:'Are you a spectator?<a href="accounts/google/login/" class="btn btn-light btn-block"><i class="fa fa-google mr-2" aria-hidden="true" ></i>Login with Google</a>Or<br>Want a Team?<a href="/register/" class="btn btn-light  btn-block"><i class="fa fa-plus mr-2" aria-hidden="true" ></i>Create a Team</a>'
})
          }
if (this.requestUser) {
 Swal.fire({
 toast: true,
  position: 'top-end',
  showConfirmButton: false,
  timerProgressBar: true,
  timer: 2000,
 icon: 'success',
  text: 'Signed in successfully'
  })
          }
    },
        async setUserInfo() {
          this.loading = true;
      // add the username of the logged in user to localStorage
      const data = await apiService("/api/user/");
      const requestUser = data["username"];
      this.requestUser = data["username"];
      const id = data["id"];
      window.localStorage.setItem("username", requestUser);
      window.localStorage.setItem("id", id);
      setTimeout(() => {
            this.loading = false;
          }, 1000)
    }
  },
mounted(){
$(window).scroll(function() {
    var height = $(window).scrollTop();
    if (height > 100) {
        $('#back2Top').fadeIn();
    } else {
        $('#back2Top').fadeOut();
    }
});
$(document).ready(function() {
    $("#back2Top").click(function(event) {
        event.preventDefault();
        $("html, body").animate({ scrollTop: 0 }, "slow");
        return false;
    });

});
},
    created() {
          this.setUserInfo()
          setTimeout(() => {
  this.test() }, 3000)
    },
         
          
    }
</script>
<style>

.ody {

    font-family: "Quicksand", sans-serif;
}
.fade-enter-active, .fade-leave-active {
  transition: opacity 0.3s
}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0
}
.flow
{
overflow-x: auto;
}
.flow::-webkit-scrollbar {
  width: 1px;
}
.flow::-webkit-scrollbar-thumb {
  background-color: LightGray;
  border-radius: 50px;
  border: 7px solid white;
  cursor: pointer;
}
* {
  scrollbar-width: thin;
  scrollbar-color: LightGray white;
}
*::-webkit-scrollbar {
  width: 10px;
}
*::-webkit-scrollbar-track {
  background: white;
}
*::-webkit-scrollbar-thumb {
  background-color: LightGray;
  border-radius: 50px;
  border: 3px solid white;
  cursor: pointer;
}
 
  /*  .slide-leave-active {
        transition: opacity 1s ease;
        opacity: 0;
        animation: slide-out 1s ease-out forwards;
    }

    .slide-leave {
        opacity: 1;
        transform: translateX(0);
    }

    .slide-enter-active {
        animation: slide-in 1s ease-out forwards;
    }

    @keyframes slide-out {
        0% {
            transform: translateY(0);
        }
        100% {
            transform: translateY(-30px);
        }
    }

    @keyframes slide-in {
        0% {
            transform: translateY(-30px);
        }
        100% {
            transform: translateY(0);
        }
    }
*/
#back2Top {
    width: 50px;
    line-height: 50px;
    overflow: hidden;
    z-index: 999;
    display: none;
    cursor: pointer;
    -moz-transform: rotate(270deg);
    -webkit-transform: rotate(270deg);
    -o-transform: rotate(270deg);
    -ms-transform: rotate(270deg);
    transform: rotate(270deg);
    position: fixed;
    bottom: 20px;
    right: 5px;
    border-radius: 50%;
    background-color:white;
    color: black;
    text-align: center;
    font-size: 30px;
    text-decoration: none;
}
#back2Top:hover {
    background-color: white;
    color: black;
}
</style>
