<template>
<div class="ody">
  <div class="home">
  </div>
  <div class="hidden-big"><center>
      </center>
</div>
  <div class="hidden-mob">
<div class="d-sm-flex  align-items-center justify-content-between w-100" style="height: 100vh;">
  <div class="col-md-4 mx-auto mb-4 mb-sm-0 headline">
    <span class="text-secondary text-uppercase"></span>
    <h2 class="display-4 my-4 font-weight-bold">Real Field<span style="color:#32cd32;">Match Making</span></h2>
    <router-link 
        :to="{ name: 'aboutpage' }"
        >
    <div class="btn px-5 py-3 font-weight-bold text-white mt-3 mt-sm-0" style="border-radius: 30px; background-color: #32cd32;" >Learn more</div></router-link>
  </div>
  <!-- in mobile remove the clippath -->
  <div class="col-md-8 h-100 clipped sty">
  </div>
</div>
  </div>
  <div class="row">
  <div data-aos="zoom-in-right" data-aos-duration="800">
 <div class="col-12"><card></card></div></div>
<div class="col-12 col-lg-10 offset-lg-1"><galleryhome/></div>
<div class="col-12"><homeadd/></div>
 <div class="col-12 col-lg-10 offset-lg-1"><videos></videos></div>
 <div class="col-12"><recentteam :teamdata="team"/></div>
 </div>
<about></about>
  <footeruse></footeruse>
  <div class="phone-call"><a href="tel:+918825560028"><img src="https://image.flaticon.com/icons/png/512/131/131133.png" width="26" alt="Call Now" title="Call Now"></a></div>
</div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
import card from "@/components/card.vue";
import videos from "@/components/videos.vue";
import about from "@/components/about.vue";
import footeruse from "@/components/footer.vue";
import recentteam from "@/components/recent_teams.vue";
import homeadd from "@/components/homeadd.vue";
import galleryhome from "@/components/galleryhome.vue";
import Swal from 'sweetalert2'
export default{
  name: "Home",
  data() {
    return {
      team: [],
      player:[],
      error: null,
      requestUser:null,
      loading: false,
      teamown:null,
      id:null,
      contestdata:null,
      
      
    }
  },
       components: {
    card,
    videos,
    about,
    footeruse,
    recentteam,
    homeadd,
    galleryhome
    },

  
methods: {
  arraycheck() {
                    var length = this.contestdata.length;
                    for(var i = 0; i <length; i++) {
                      
                        if(this.contestdata[i].contest_team_id==this.id)
        {
                         return true;
                          
        }
                    }
                    return false;
                },

  contestalert() {
let endpoint = `/api/contest_register/`;
      apiService(endpoint)
        .then(data => {
          if (data) {
            this.contestdata = data;
          } else {
            this.contestdata = null;
          }
   setTimeout(() => { 
   if (!this.arraycheck())
   if(this.teamown){
   if(this.teamown.teamcontact){
{
Swal.fire({
  showConfirmButton: false,
  imageUrl: 'https://cdn5.vectorstock.com/i/thumb-large/84/19/woman-playing-soccer-vector-24058419.jpg',
  imageWidth: 300,
  imageHeight: 300,
  imageAlt: 'Custom image',
  showCloseButton: true,
  html:`<a href=contest/ class="btn btn-outline-dark btn-block">Join contest</a>You have still not enrolled your team for the contest`,
  showClass: {
    popup: 'animate__animated animate__fadeInDown'
  },
  hideClass: {
    popup: 'animate__animated animate__fadeOutUp'
  }
})
   }}}
   },2000)
        })    
},
  datacheck(){
    if(this.teamown){
if(!this.teamown.teamcontact){
      const answers= this.id
Swal.fire({
  showConfirmButton: false,
  imageUrl: 'https://thumbs.dreamstime.com/b/vector-cartoon-girl-character-playing-football-stylized-serious-young-teen-making-exercises-ball-female-woman-athlete-102474484.jpg',
  imageWidth: 300,
  imageHeight: 300,
  imageAlt: 'Custom image',
 html: ` Please fill the team details to join the contest
 <a href=Teamedit/${answers} class="btn btn-outline-dark btn-block">Team Details</a>
 `,
  showClass: {
    popup: 'animate__animated animate__fadeInDown'
  },
  hideClass: {
    popup: 'animate__animated animate__fadeOutUp'
  }
})
}}
  },
getownTeamData() {  
  if (this.id)   {
      // get the details of a question instance from the REST API and call setPageTitle
      let endpoint = `/api/team/${this.id}/`;
      apiService(endpoint)
        .then(data => {
          if (data) {
            this.teamown = data;
          } else {
            this.teamown = null;
          }
        })
   }
   },
     
      getTeamData() {
        
      // get the details of a question instance from the REST API and call setPageTitle
      let endpoint = `/api/team/`;
      apiService(endpoint)
        .then(data => {
          if (data) {
            this.team = data.results;
            this.team = this.team.slice(-4);

          } else {
            this.team = null;
            this.setPageTitle("404 - Page Not Found")
          }
        })
    },
    getplayerData() {
      // get the details of a question instance from the REST API and call setPageTitle
      let endpoint = `/api/player/`;
      apiService(endpoint)
        .then(data => {
          if (data) {
            this.player = data.results;
          } else {
            this.player = null;
            this.setPageTitle("404 - Page Not Found")
          }
        })
    },
    async setUserInfo() {
      // add the username of the logged in user to localStorage
      const data = await apiService("/api/user/");
      const requestUser = data["username"];
      this.requestUser = data["username"];
      const id = data["id"];
      this.id = data["id"];
      window.localStorage.setItem("username", requestUser);
      window.localStorage.setItem("id", id);
    }
    },
  created() {
    this.contestalert()
    this.getTeamData()
    this.getplayerData()
    this.setUserInfo()
  setTimeout(() => {
    this.getownTeamData()
        },1000)  
      setTimeout(() => {
    this.datacheck()
        },2000) 

    },

}
</script>

<style>
@import url('https://fonts.googleapis.com/css?family=Quicksand:400,500,700');
.ody{
  overflow: hidden;
}

h1{
            font-size:55px;

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
            font-size:25px;
}
h4{
            font-size:25px;
        }
h5{
            font-size:20px;

        }


.phone-call {
    width: 50px;
    height: 50px;
    left: 20px;
    bottom: 20px;
    background:lightgreen;
    position: fixed;
    text-align: center;
    color: #ffffff;
    cursor: pointer;
    border-radius: 50%;
    z-index: 99;
  display: inline-block;
  line-height: 50px;
}

.phone-call:before {
    position: absolute;
    content: " ";
    z-index: -1;
    top: -15px;
    left: -15px;
    background-color: lightgreen;
    width: 80px;
    height: 80px;
    border-radius: 100%;
    animation-fill-mode: both;
    -webkit-animation-fill-mode: both;
    opacity: 0.6;
    -webkit-animation: pulse 1s ease-out;
    animation: pulse 1.8s ease-out;
    -webkit-animation-iteration-count: infinite;
    animation-iteration-count: infinite;
}


}

.headline {
  left: 130px;
} 
.clipped {
clip-path: polygon(24% 0, 100% 0, 100% 50%, 100% 100%, 24% 100%, 10% 50%);
}

@media screen and (max-width:1500px)  and (min-width:701px){
  .hidden-big {
    display: none;
    
  }
}
@media screen and (max-width:700px){
  .hidden-mob {
    display: none;
    
  }
.home{
    width: 100%;
    height: 100vh;
    background-image:url('https://i.pinimg.com/originals/11/ba/e8/11bae8258ab02c454ddf553fe2133a10.png') ;
    background-position: center top;
	  background-size:cover;
    background-attachment: fixed;
    background-repeat: no-repeat;
}
.headline {
    left: 20px;
    margin-top:100px;
  } 
  .clipped {
    clip-path: none;
    max-height: 300px !important;
  }
}
.sty{
  min-height: 350px;
  background-position: center;
  background-size: cover;
  background-image:url('~@/assets/img/vectorpaint (1).svg') ;
  background-attachment: fixed;
  background-repeat: no-repeat;
}
.phone-call {
    width: 50px;
    height: 50px;
    left: 20px;
    bottom: 20px;
    background:lightblue;
    position: fixed;
    text-align: center;
    color: #ffffff;
    cursor: pointer;
    border-radius: 50%;
    z-index: 99;
  display: inline-block;
  line-height: 50px;
}

.phone-call:before {
    position: absolute;
    content: " ";
    z-index: -1;
    top: -15px;
    left: -15px;
    background-color: lightblue;
    width: 80px;
    height: 80px;
    border-radius: 100%;
    animation-fill-mode: both;
    -webkit-animation-fill-mode: both;
    opacity: 0.6;
    -webkit-animation: pulse 1s ease-out;
    animation: pulse 1.8s ease-out;
    -webkit-animation-iteration-count: infinite;
    animation-iteration-count: infinite;
}

@-webkit-keyframes pulse {
    0% {
        -webkit-transform: scale(0);
        opacity: 0;
    }
    25% {
        -webkit-transform: scale(0.3);
        opacity: 1;
    }
    50% {
        -webkit-transform: scale(0.6);
        opacity: .6;
    }
    75% {
        -webkit-transform: scale(0.9);
        opacity: .3;
    }
    100% {
        -webkit-transform: scale(1);
        opacity: 0;
    }
}

@keyframes pulse {
    0% {
        transform: scale(0);
        opacity: 0;
    }
    25% {
        transform: scale(0.3);
        opacity: 1;
    }
    50% {
        transform: scale(0.6);
        opacity: .6;
    }
    75% {
        transform: scale(0.9);
        opacity: .3;
    }
    100% {
        transform: scale(1);
        opacity: 0;
    }
}
</style>

