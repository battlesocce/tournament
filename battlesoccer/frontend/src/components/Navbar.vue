<template>
<div class="ody">
<nav class="nav slide" >
        <div class="contain">
            <div class="logo scroll">
                 <router-link
        :to="{ name: 'Home' }" 
        ><img src="@/assets/img/load.svg"  class="si"/> Battle Soccer</router-link>        
            </div> 
        <router-link 
        :to="{ name: 'search' }"
        ><li class="fa fa-search  btn btn-just-icon btn-twitter" style="float:right; margin-right:70px; margin-top:14px;"></li></router-link> 
            
              <div id="mainListDiv" class="main_list">
                <div class="tog" >
                <ul class="navlinks">
        <li class=" btm">

          <router-link v-if="requestUser && is_team"
        :to="{ name: 'Userprofile' }" 
        >Profile</router-link>

         
            <router-link v-if="!requestUser"
        :to="{ name: 'guest' }" 
        >Guest</router-link>
        
        <div @click="guest()" v-if="!is_team">
         <a style="cursor:pointer;">{{this.requestUser}}</a>
        </div>
        </li>
        
<li><router-link 
        :to="{ name: 'contest' }"
        >Contest</router-link></li>

         <li><router-link
        :to="{ name: 'picvid' }"
        >Gallery</router-link></li>

          <li><router-link 
        :to="{ name: 'tour' }"
        >Tournaments</router-link></li>

        <li><router-link 
        :to="{ name: 'aboutpage' }"
        >About</router-link></li>

      <li><div v-if="requestUser" >
      <a href="/accounts/logout/">Log out</a></div>

      <div v-if="!requestUser" >
      <a href="/accounts/logout/">Sign In</a></div></li>

                </ul>
            </div></div>
            <span class="navTrigger">
                <img src="@/assets/img/nav.png" width="40px" style="margin-top:-40px; margin-right:10px;">
            </span>
        </div>
    </nav>
    <div class='thetop'></div>
    </div>
</template>

<script>
import Swal from 'sweetalert2'
import $ from 'jquery'
import { apiService } from "@/common/api.service.js";
export default {
  name: "NavbarComponent",
    data() {
    return {
      requestUser:null, 
      is_team:null
    }},
  methods: {
    guest(){
Swal.fire({
  showConfirmButton: false,
  imageUrl: 'https://cdn5.vectorstock.com/i/thumb-large/84/19/woman-playing-soccer-vector-24058419.jpg',
  imageWidth: 300,
  imageHeight: 300,
  imageAlt: 'Custom image',
  showCloseButton: true,
  html:`You have been logged in as a Guest<br>
   <a href=/register/ class="btn btn-outline-dark btn-block">Create team</a>
`,
  showClass: {
    popup: 'animate__animated animate__fadeInDown'
  },
  hideClass: {
    popup: 'animate__animated animate__fadeOutUp'
  }
})
    },
    async setUserInfo() {
      const data = await apiService("/api/user/");
      this.requestUser = data["username"];
      this.is_team = data["is_team"];

    }
    },
  mounted () {
              $(window).scroll(function() {
            if ($(document).scrollTop() > 0) {
                $('.nav').addClass('affix');
                console.log("OK");
            } else {
                $('.nav').removeClass('affix');
            }
        });
 $('.navTrigger').click(function () {
    $(this).toggleClass('active');
    console.log("Clicked menu");
    $("#mainListDiv").toggleClass("show_list");
    $("#mainListDiv").fadeIn();
});

 $('.tog').click(function () {
    $(this).toggleClass('active');
    console.log("Clicked menu");
    $("#mainListDiv").toggleClass("show_list");
    $("#mainListDiv").fadeIn();

});


$(function(){$(".scroll").click(function(){$("html,body").animate({scrollTop:$(".thetop").offset().top},"1000");return false})})



},
created() {
    this.setUserInfo()
    },
};

</script>

<style>
.ody a{

    font-family: "Quicksand", sans-serif;
        text-decoration: none;
        color:inherit;


}
@media only screen and (max-width:700px) {

.btm{
  margin-top:95px;
}
}

.ody {

    font-family: "Quicksand", sans-serif;
        text-decoration: none;
        color:inherit;


}
@import '../assets/css/navbar.css';
</style>