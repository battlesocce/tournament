<template>
<div class="ody"><br><br><br><br><br><br>
<div class="profile-page">
     <div class="main main-raised">
		 <div class="profile-content">
            <div class="container">
                <div class="row">
	                <div class="col-md-6 ml-auto mr-auto">
        	           <div class="profile">
	                        <div class="avatar" v-if="players.pic">     
                            <v-lazy-image :src="players.pic" class="res"
    src-placeholder="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcR508iDAmSEkkOWUuK7SsEbpflpVR1TKl1ljQ&usqp=CAU"
     />
                        </div>
                         <div class="name">
	                            <h2 style="margin-top:-50px;">{{players.player| capitalize}}</h2></div>
        	        <router-link v-if="isUser" class='router-link' 
            :to="{ name: 'Addplayer',
             params: { id: players.id } }"
             ><i class="fa fa-edit btn btn-just-icon btn-twitter"  style="margin-top:-60px" ></i>
            </router-link>
            <div v-if="isUser"  class="upload-btn-wrapper">
  <button class="btn"><i class="fa fa-camera btn btn-just-icon btn-twitter"></i></button>
  <input type="file" name="myfile"  v-on:input="onchange"/>
</div>  
                  </div>
                </div>
            </div>
     <center><h4 v-if="players.description">{{players.description|capitalize}}</h4></center><br>
     <div class="row">
       <div class="col-3">
    <table>
      <th>
            <a v-bind:href="'https://www.facebook.com/' + players.facebookurl + '/'"  aria-hidden="true"><i class="fa fa-facebook" style="font-size:22px"></i></a></th>
          <th><a v-bind:href="'https://www.instagram.com/' + players.instaurl + '/'" aria-hidden="true"><i class="fa fa-instagram" style="font-size:22px"></i></a></th>
                   </table></div>
       <div class="col-6">
   <h3 class="text-muted text-center" style="margin-top:-20px">{{players.teamname|capitalize}}</h3>
       </div>
       <div class="col-3 text-center">
<p
            class="fa fa-heart" 
            style="font-size:25px;"
            @click="toggleLike"
            :class="{
              'fa fa-heart': userLikedPlayer,
              'fa fa-heart-o': !userLikedPlayer
              }"
            ></p><strong>&nbsp;{{ likesCounter }}</strong></div>
     </div><br>
     <div class="shadow p-1 mb-1 bg-white rounded">
<div class="row mt-2">
     <div class="col-2 offset-1" style="padding :1px;">
                                <center>
                                  <img src="@/assets/img/Reward.png"  v-if="this.bestplayer" alt="Avatar" class=circle1>
                            <img src="@/assets/img/Reward.png"  v-if="!this.bestplayer" style="opacity:0.5" alt="Avatar" class=circle1></center>
         </div>
          <div class="col-2" style="padding :1px;">
                       <center>    
                          <img src="https://www.battlesoccer.in/static/img/Reward%20(1).b103c29b.png" alt="Avatar" v-if="this.goalkeaper" class=circle1>
                           <img src="https://www.battlesoccer.in/static/img/Reward%20(1).b103c29b.png" alt="Avatar" v-if="!this.goalkeaper" style="opacity:0.5" class=circle1></center>

         </div>
          <div class="col-2" style="padding :1px;">
                         <center>   <img src="https://www.battlesoccer.in/static/img/Reward%20(2).d60369c6.png"  v-if="this.highgoal" alt="Avatar" class=circle1>
                         <img src="https://www.battlesoccer.in/static/img/Reward%20(2).d60369c6.png" alt="Avatar"  v-if="!this.highgoal" style="opacity:0.5" class=circle1>
                         </center>
         </div>
          <div class="col-2" style="padding :1px;">
                         <center>   <img src="https://www.battlesoccer.in/static/img/Reward%20(3).27cfb1a1.png" v-if="this.moves" alt="Avatar" class=circle1>
                         <img src="https://www.battlesoccer.in/static/img/Reward%20(3).27cfb1a1.png" v-if="!this.moves" style="opacity:0.5" alt="Avatar" class=circle1></center>
         </div>
          <div class="col-2" style="padding :1px;">
                         <center>   <img src="https://www.battlesoccer.in/static/img/Reward%20(5).799283aa.png"  v-if="this.fairplay" alt="Avatar" class=circle1>
                          <img src="https://www.battlesoccer.in/static/img/Reward%20(5).799283aa.png" v-if="!this.fairplay" style="opacity:0.5" alt="Avatar" class=circle1></center>
          </div>
</div>

<div class="row mt-1">
     <div class="col-2 offset-1" style="padding :1px;">
                         <center v-if="this.bestplayer>=2" > <b><h5>*({{this.bestplayer}})</h5></b></center>
         </div>
          <div class="col-2" style="padding :1px;">
                          <center v-if="this.goalkeaper>=2"><b><h5>*({{this.goalkeaper}})</h5></b></center>
         </div>
          <div class="col-2" style="padding :1px;">
                          <center v-if="this.highgoal>=2"><b><h5>*({{this.highgoal}})</h5></b></center>
         </div>
          <div class="col-2" style="padding :1px;">
                          <center v-if="this.moves>=2"> <b><h5>*({{this.moves}})</h5></b></center>
         </div>
          <div class="col-2" style="padding :1px;">
                         <center v-if="this.fairplay>=2"><b><h5>*({{this.fairplay}})</h5></b></center>
          </div>
</div>
     </div><br>
    <div class="wrap  text-center">
    <div class="col-lg-2 col-6 " style="padding-left:8px;padding-right:8px;" >
      <div class="main-raised1">
    <h3> <hr style="width:0%">Age </h3><br><h4 class="text-muted"><div v-if="players.age">{{players.age| capitalize}}</div></h4>
    <h5 class="text-muted"><div v-if="!players.age">Not available</div></h5><br>
    </div></div>


     <div class="col-lg-2 col-6 "  style="padding-left:8px;padding-right:8px;"  >
      <div class="main-raised1">
    <h3><hr style="width:0%"> Profession </h3><br><h4 class="text-muted"><div v-if="players.profession">{{players.profession| capitalize}}</div></h4>
    <h5 class="text-muted"><div v-if="!players.profession">Not available</div></h5><br>
    </div></div>

<div class=" col-0 col-lg-4"  >
</div>
         <div class="col-lg-2 col-6 "  style="padding-left:8px;padding-right:8px;"  >
          <div class="main-raised1"> 
    <h3><hr style="width:0%"> Position </h3><br><h4 class="text-muted"><div v-if="players.position">{{players.position| capitalize}}</div></h4>
    <h5 class="text-muted"><div v-if="!players.position">Not available</div></h5><br>
    </div></div>

         <div class="col-lg-2 col-6 "  style="padding-left:8px;padding-right:8px;" >
           <div class="main-raised1 ">
    <h3> <hr style="width:0%">Likes </h3><br><h4 class="text-muted"><div v-if="players.likes_count">{{this.likesCounter| capitalize}}<i class="fa fa-heart ml-2"></i></div></h4>
    <h5 class="text-muted"><div v-if="!players.likes_count">Not available</div></h5><br>
    </div></div>

    </div>
    <div class="row text-center">
<div class="col-12 col-lg-6 offset-lg-3">
          <div class="main-raised1"> 
    <h3><hr style="width:0%"> Goals </h3><br><h4 class="text-muted"><div v-if="players.goals">{{players.goals| capitalize}}</div></h4>
    <h5 class="text-muted"><div v-if="!players.goals">Not available</div></h5><br>
    </div></div>
</div><br><br>
	    </div>
    </div>
</div> 
    </div>
   <br><br> 
</div>
</template>

<script>
import Swal from 'sweetalert2'
import axios from 'axios'
import { CSRF_TOKEN } from "@/common/csrf_token.js"
import { apiService } from "@/common/api.service.js";
export default {
  name: "playerpage",
    data() {
    return {
      userLikedPlayer: null,
      likesCounter: null,
      players:{},
     pic: null,
     userid:null,
     playeruser:null,
     tourdata:[],
     goalkeaper:null,
     bestplayer:null,
     highgoal:null,
     moves:null,
     fairplay:null,


    }}, 
  props: {
    id: {
      type: [Number, String],
      required: false
    }
  },

  computed: {
    isUser() {    
      return this.playeruser == this.userid
    }
  },
methods: {

  award(){
    for (let i = 0; i < this.tourdata.length; i++)
    {
      if(this.tourdata[i].tour_player==this.players.id)
      {
        this.bestplayer=this.bestplayer+1
          }
      if(this.tourdata[i].tour_goalkeaper==this.players.id)
      {
       this.goalkeaper=this.goalkeaper+1
          }
      if(this.tourdata[i].tour_highgoals==this.players.id)
      {
        this.highgoal=this.highgoal+1
    }
    
      if(this.tourdata[i].tour_fairplay==this.players.id)
      {
          this.fairplay=this.fairplay+1
    }
      if(this.tourdata[i].tour_moves==this.players.id)
      {
          this.moves=this.moves+1
    }
    }
  },
   gettourdata() {
      let endpoint = `/api/alltournament/`;
      apiService(endpoint)
        .then(data => {
          if (data) {
            this.tourdata = data;
            } else {
            this.tourdata = null;
            this.setPageTitle("404 - Page Not Found")
          }
        })
    },
test(){
      if (!this.requestUser) {
 Swal.fire({
  position: 'top-end',
  showConfirmButton: false,
  html:'Are you a spectator?<a href="accounts/google/login/" class="btn btn-light btn-block"><i class="fa fa-google mr-2" aria-hidden="true" ></i>Login with Google</a>Or<br>Want a Team?<a href="/register/" class="btn btn-light  btn-block"><i class="fa fa-plus mr-2" aria-hidden="true" ></i>Create a Team</a>'
})
          }
    },
  toggleLike() {
    if (!this.requestUser) {
        this.test()
      }else{
      this.userLikedPlayer=== false
        ? this.likePlayer()
        : this.unLikePlayer()}
    },
    likePlayer() {
      this.userLikedPlayer = true;
      this.likesCounter += 1;
      let endpoint = `/api/playerlike/${ this.id }/like/`;
      apiService(endpoint, "POST")
    },
    unLikePlayer() {
      this.userLikedPlayer = false;
      this.likesCounter -= 1;
      let endpoint = `/api/playerlike/${ this.id }/like/`;
      apiService(endpoint, "DELETE")
    },
onchange() {
 this.pic=event.target.files[0]
 event.target.value = '';
if (!this.pic) {
        this.error = "You can't send an empty question!";
      }  else {
      const formData = new FormData()
     formData.append('pic',this.pic)
     axios.put( `/api/playerpic/${this.id }/`,
  formData,
  {
    headers: {
         "Access-Control-Allow-Origin" : "*",
        'Content-Type': 'multipart/form-data',
        "X-CSRFTOKEN": CSRF_TOKEN

    }
  }
)
.then(function(){
  console.log('SUCCESS!!');
})
.catch(function(){
  console.log('FAILURE!!');
});
setTimeout(() => {
 this.getplayerData()
 Swal.fire({
 toast: true,
  showConfirmButton: false,
  timerProgressBar: true,
  timer: 2000,
  position: 'center-right',
 icon: 'success',
  text: "Profile picture updated successful "
  });
        },2000)
      }
    },
      getplayerData() {
      // get the details of a question instance from the REST API and call setPageTitle
      let endpoint = `/api/player/${this.id}/`;
      apiService(endpoint)
        .then(data => {
          if (data) {
            this.players = data;
      this.userLikedPlayer = this.players.user_has_voted
      this.likesCounter = this.players.likes_count
      this.playeruser=this.players.own.user
          } else {
            this.players = null;
            this.setPageTitle("404 - Page Not Found")
          }
        })
    }
},
    created() {
    
    this.userid = window.localStorage.getItem("id");
    this.getplayerData()
    this.gettourdata()
    setTimeout(() => {
    this.award()},1000)
 this.requestUser = window.localStorage.getItem("username");
    }    
}
</script>


<style scoped>
@import '../assets/css/details.css';

.ody a{

    font-family: "Quicksand", sans-serif;
        text-decoration: none;


}
.ody {

    font-family: "Quicksand", sans-serif;
        text-decoration: none;


}
.profile-page .profile img {
    max-width: 250px;
    width: 100%;
    margin: 0 auto;
    -webkit-transform: translate3d(0,-40%,0);
    -moz-transform: translate3d(0,-40%,0);
    -o-transform: translate3d(0,-40%,0);
    -ms-transform: translate3d(0,-40%,0);
    transform: translate3d(0,-40%,0);
}
.res{
	width:25%;
	height:auto;
	margin: auto;
	border-radius: 50%;


}
.wrap {
	display: flex;
	flex-wrap: wrap;
	margin-right:-15px;
	margin-left:-15px;
  }
 .circle1 {
  border-radius: 50%;
  width:40%;
  height:auto;
}

@media screen and (max-width:600px) {
 
    .res{
	width:100%;
	height:auto;
	margin: auto;
	border-radius: 50%;

}

.profile-page .profile img {
    max-width: 180px;
    width: 100%;
    margin: 0 auto;
    -webkit-transform: translate3d(0,-40%,0);
    -moz-transform: translate3d(0,-40%,0);
    -o-transform: translate3d(0,-40%,0);
    -ms-transform: translate3d(0,-40%,0);
    transform: translate3d(0,-40%,0);
}
.wrap {
	display: flex;
	flex-wrap: wrap;
	margin-right:-15px;
	margin-left:-15px;
  }

}
.responsive{
width:100%;
height:auto;

}

.upload-btn-wrapper {
  position: relative;
  overflow: hidden;
  display: inline-block;
}



.upload-btn-wrapper input[type=file] {
  font-size: 80px;
  position: absolute;
  left: 0;
  top: 0;
  opacity: 0;
}
h1{
            font-size:55px;

        }

h2{
            font-size:30px;

        }
h3{
          font-size:20px;
}
h4{
            font-size:20px;
        }

h5{
            font-size:16px;
            font-weight: 700;
        }
@media only screen and (max-width:700px) {
 .circle1 {
  border-radius: 75%;
  width:100%;
  height:auto;
}
h1{
            font-size:40px;

        }
h2{
            font-size:30px;

        }
h3{
            font-size:22px;
}
h4{
            font-size:21px;
        }
h5{
            font-size:16px;
        font-weight: 700;
        }
}
.main-raised1 {
  display:block;
    border-radius: 8px;
-webkit-box-shadow: 0px 0px 8px 0px rgba(0,0,0,0.3);
-moz-box-shadow: 0px 0px 8px 0px rgba(0,0,0,0.3);
box-shadow: 0px 0px 8px 0px rgba(0,0,0,0.3);}

.fa-heart-o {
  color:red;
  cursor: pointer;
}

.fa-heart {
  color: red;
  cursor: pointer;
}


</style>