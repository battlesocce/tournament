<template>
  <div class="ody" v-if='team.coverpic'>
    <vue-snotify></vue-snotify> 
<div class="profile-page">
    <div><v-lazy-image :src="team.coverpic" class="responsive shadow-sm p-1  bg-white rounded"
     style="margin-top:75px;" />
    </div>
    <div class="main main-raised">
		<div class="profile-content">
            <div class="container">
                <div class="row">
	                <div class="col-md-6 ml-auto mr-auto">
        	           <div class="profile">
	                        <div class="avatar">
                          <div class="upload-btn-wrapper">
  <button class="btn btn-just-icon btn-link btn-twitter"><li class="fa fa-user-o"></li></button>
  <input type="file" name="myfile"  v-on:input="onchange"/>
</div>
                        <v-lazy-image :src="team.logo" class="img-raised rounded-circle img-fluid"
    src-placeholder="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcR508iDAmSEkkOWUuK7SsEbpflpVR1TKl1ljQ&usqp=CAU"
     />	                                                  <div class="upload-btn-wrapper">
  <button class="btn btn-just-icon btn-link btn-twitter"><li class="fa fa-picture-o"></li></button>
  <input type="file" name="myfileprofile"  v-on:input="onchangeprofile"/>
</div>
                          </div>
	                        <div class="name">
	                            <h2>{{team.teamname | capitalize}}</h2>
								                <router-link class="btn btn-just-icon btn-link btn-twitter"
        :to="{ name: 'Teamedit' ,params: {id:id}}"
        ><i class="fa fa-edit"></i></router-link>
                                 <router-link class="btn btn-just-icon btn-link btn-twitter"
        :to="{ name: 'Addplayer' }"
        ><i class="fa fa-plus"></i></router-link>
        <div class="btn btn-just-icon btn-link btn-twitter"
        @click='onclick'
        ><i class="fa fa-info"></i></div>
        <router-link class="btn btn-just-icon btn-link btn-twitter"
        :to="{ name: 'gallery',params: {id:id} }"
        ><i class="fa fa-file-video-o"></i></router-link>
	                        </div>
	                    </div>
    	            </div>
                </div>
                    <h3><center>{{team.teamquotes| capitalize}}</center></h3>
                <br>
            </div>
            <div v-for="(teampresent,index) in teamrankall" :key=index>
              <div v-if="teampresent.teamown==team.teamname">

 <div class="flow">
                <table class="table">
      <tr>
          <th><h4><center>Goals</center></h4></th>
          <th><h4><center>Played</center></h4></th>
          <th><h4><center>Won</center></h4></th>
          <th><h4><center>Lost</center></h4></th>
      </tr>
    <tbody>
      <tr>
          <td><h3><center>{{teampresent.teamgoals}}</center></h3></td>
          <td><h3><center>{{teampresent.matchs_played}}</center></h3></td>
          <td><h3><center>{{teampresent.match_won}}</center></h3></td>
          <td><h3><center>{{teampresent.match_lost}}</center></h3></td>
      </tr>
   </tbody>
  </table>
   </div>            </div></div>
		</div>
    </div>
</div>
<br>
<div class="container-sm">
  <br>
  <transition name='fade' mode="out-in">
 <div class="alert alert-success" v-if="message" role="alert">
  {{message}}
</div> 
  </transition>
  <transition-group name='slide' mode="out-in">
<div v-if ="flag" key=1> 
      <matchplayed :id='id'/>
</div>
<div key=2>
      <transition-group name=slide class="row">
         <Player 
        v-for="player in team.players"
        :player="player"
        :user="team.user"
        :requestUser="requestUser"
        :key="player.id"
        @delete-player="deleteplayer"
        @update-pic="updatepic"
      /></transition-group></div>
  </transition-group>
</div>        

        </div>
</template>
<script>

import { CSRF_TOKEN } from "@/common/csrf_token.js"
import axios from 'axios'
import swal from 'sweetalert';
import Swal from 'sweetalert2'
import { apiService } from "@/common/api.service.js";
import Player from "@/components/player.vue";
import matchplayed from "@/components/matchplayed.vue";
export default{
  name: "Userprofile",
     components: {
    Player,
    matchplayed
  },
  data() {
    return {
      flag:false,
      team: {},
      requestUser:null,
      id:null,
      logo: null,
      coverpic: null,
      error: null,
      message:null,
      teamrankall:null,
    }
  },
   methods: {
     playeralert() {
Swal.fire({
  showConfirmButton: false,
  imageUrl: 'https://cdn.dribbble.com/users/2898003/screenshots/14096752/_1__soccer-01_4x.png?compress=1&resize=400x300',
  imageWidth: 600,
  imageHeight: 300,
  showCloseButton: true,
  imageAlt: 'Custom image',
  title:"Add player",
  html:'Click on the <i class="fa fa-plus"></i> icon to add players' ,
  showClass: {
    popup: 'animate__animated animate__fadeInDown'
  },
  hideClass: {
    popup: 'animate__animated animate__fadeOutUp'
  }
})
           
},
     onclick() {
        this.flag=!this.flag
       },
     setRequestUser() {
      // the username has been set to localStorage by the App.vue component
      this.requestUser = window.localStorage.getItem("username");
    },
    getTeamRank() {
      let endpoint = `/api/totalteamrankall/`;
      apiService(endpoint)
.then(data => {
          if (data) {
            this.teamrankall = data;
          } else {
            this.teamrankall = null;
          }
        })
    },
      getTeamData() {       
      this.id = window.localStorage.getItem("id");
      this.id=parseInt(this.id)
      // get the details of a question instance from the REST API and call setPageTitle
      let endpoint = `/api/team/${this.id}/`;
      apiService(endpoint)
        .then(data => {
          if (data) {
            this.team = data;
          if(!this.team.players[0]){
            this.playeralert()
          }
          } else {
            this.team = null;
            this.setPageTitle("404 - Page Not Found")
          }
        })
setTimeout(() => {
  this.message = "" }, 4000)
    },
 onchange(event){
  this.logo=event.target.files[0]
  console.log(this.logo);
      // Tell the REST API to create or update a Question Instance
      if (!this.logo) {
        this.error = "You can't send an empty question!";
      }  else {
      const formData = new FormData()
     formData.append('logo', this.logo)
     axios.put( '/api/avatar/',
  formData,
  {
    headers: {
         "Access-Control-Allow-Origin" : "*",
        'Content-Type': 'multipart/form-data',
        "X-CSRFTOKEN": CSRF_TOKEN

    }
  }
).then(function(){
  console.log('SUCCESS!!');
})
.catch(function(){
  console.log('FAILURE!!');
});
setTimeout(() => {
 this.getTeamData()
        },2000)
}
    },
    onchangeprofile(event){
  this.coverpic=event.target.files[0]
      // Tell the REST API to create or update a Question Instance
      if (!this.coverpic) {
        this.error = "You can't send an empty question!";
      }  else {
      const formData = new FormData()
     formData.append('coverpic', this.coverpic)
     axios.put( '/api/avatar/',
  formData,
  {
    headers: {
         "Access-Control-Allow-Origin" : "*",
        'Content-Type': 'multipart/form-data',
        "X-CSRFTOKEN": CSRF_TOKEN

    }
  }
).then(function(){
  console.log('SUCCESS!!');
})
.catch(function(){
  console.log('FAILURE!!');
});
setTimeout(() => {
 this.getTeamData()
         Swal.fire({
 toast: true,
  showConfirmButton: false,
  timerProgressBar: true,
  timer: 2000,
  position: 'center-right',
 icon: 'success',
  text: "Cover picture update Successful"
  });
        },2000)
}
    },

    async deleteplayer(player) {
      swal({
  title: "Are you sure?",
  text: "Once deleted, you will not be able to recover this player profile!",
  icon: "warning",
  buttons: true,
  dangerMode: true,
})
.then((willDelete) => {
  if (willDelete) {
    let endpoint = `/api/player/${player.id}/`;

      try {
         apiService(endpoint, "DELETE")
        this.$delete(this.team.players,this.team.players.indexOf(player))
      }
      catch (err) {
        console.log(err)
      }
    swal("Poof! Your imaginary file has been deleted!", {
      icon: "success",
    });
  } else {
    swal("Your profile  is safe!");
  }
});
      // delete a given answer from the answers array and make a delete request to the REST API
      
    },
async updatepic(player,pic) {
if (!pic) {
        this.error = "You can't send an empty question!";
      }  else {
      const formData = new FormData()
     formData.append('pic', pic)
     axios.put( `/api/playerpic/${ player.id }/`,
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
 this.getTeamData()
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
    }
},
 created() {
    this.message = this.$route.params.message;
    this.getTeamData()
    this.setRequestUser()
    this.getTeamRank()
    if(this.message)
    {
       Swal.fire({
 toast: true,
  showConfirmButton: false,
  timerProgressBar: true,
  timer: 2000,
  position: 'center-right',
 icon: 'success',
  html: `${this.message}`
  });
    
    }
    },
  mounted () {
window.scrollTo(0, 0);
  window.addEventListener("scroll", this.lazyLoad);
  }


}
</script>
<style scoped>
@import '../assets/css/details.css';

.fa-heart-o {
  color:red;
  cursor: pointer;
}

.fa-heart {
  color: red;
  cursor: pointer;
}

@media screen and (max-width:600px) {


.profile-page .profile img {
    max-width: 120px;
    width: 100%;
    margin: 0 auto;
    -webkit-transform: translate3d(0,-40%,0);
    -moz-transform: translate3d(0,-40%,0);
    -o-transform: translate3d(0,-40%,0);
    -ms-transform: translate3d(0,-40%,0);
    transform: translate3d(0,-40%,0);
}

}
.upload-btn-wrapper {
  position: relative;
  overflow: hidden;
  display: inline-block;
  

}



.upload-btn-wrapper input[type=file] {
  font-size: 100px;
  position: absolute;
  left: 0;
  top: 0;
  opacity: 0;
}

 .slide-leave-active {
        transition: opacity 1s ease;
        opacity: 0;
        animation: slide-out 1s ease-out forwards;
        position: absolute;
    }

    .slide-leave {
        opacity: 1;
        transform: translateX(0);
    }

    .slide-enter-active {
        animation: slide-in 1s ease-out forwards;
    }

    .slide-move
    {
      transition: transform 1s;
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
 .v-lazy-image {
    filter: blur(10px);
    transition: filter 0.7s;
  }
  .v-lazy-image-loaded {
    filter: blur(0);
  }

    h1{
            font-size:75px;

        }

h2{
            font-size:45px;

        }
h3{
          font-size:35px;
}
h4{
            font-size:25px;
        }

h5{
            font-size:20px;
        }
@media only screen and (max-width:700px) {
h1{
            font-size:40px;

        }
h2{
            font-size:30px;

        }
h3{
            font-size:20px;
}
h4{
            font-size:25px;
        }
h5{
            font-size:20px;

        }
}


</style>
