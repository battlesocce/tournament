<template>
  <div class="ody" v-if='team.coverpic'>
<div class="profile-page">
    <div v-if='team.coverpic'>
<v-lazy-image :src="team.coverpic"  class="responsive shadow-sm p-1  bg-white rounded"
     style="margin-top:75px;" />    </div>
    <div class="main main-raised">
		<div class="profile-content">
            <div class="container">
                <div class="row">
	                <div class="col-md-6 ml-auto mr-auto">
        	           <div class="profile">
	                        <div class="avatar" v-if='team.logo'>
                            <v-lazy-image :src="team.logo" class="img-raised rounded-circle img-fluid"
    src-placeholder="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcR508iDAmSEkkOWUuK7SsEbpflpVR1TKl1ljQ&usqp=CAU"
     />
                          </div>
	                        <div class="name">
	                            <h2>{{team.teamname | capitalize}}</h2>
<div class="btn btn-just-icon btn-link btn-twitter"
        @click='onclick'
        ><i class="fa fa-info"></i></div>
        <router-link class="btn btn-just-icon btn-link btn-twitter"
        :to="{ name: 'gallery',params: {id:id} }"
        ><i class="fa fa-file-video-o"></i></router-link>	                        </div>
	                    </div>
    	            </div>
                </div>
                    <h3><center>{{team.teamquotes| capitalize}}</center></h3>
                <br>
            </div>
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
<br>
<transition-group name='slide' mode="out-in">
<div v-if ="flag" key=1> 
      <matchplayed :id='id'/>
</div>
<div key=2>
<div class="container-sm">
  <br>
        <b-row>
         <Playerveiw
        v-for="player in team.players"
        :player="player"
        :key="player.id"
      />
      </b-row>
</div>
</div>
</transition-group>
        </div> 
</template>

<script>
import { apiService } from "@/common/api.service.js";
import Playerveiw from "@/components/profileplayer.vue";
import matchplayed from "@/components/matchplayed.vue";

export default{
  name: "Teamveiw",
     components: {
    Playerveiw,
    matchplayed

  },
  data() {
    return {
      team: {},
      id:null,
      flag:false,
      teamrankall:null,

    }
  },
   methods: {
          onclick() {
        this.flag=!this.flag
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
      // get the details of a question instance from the REST API and call setPageTitle
      let endpoint = `/api/team/${this.id}/`;
      apiService(endpoint)
        .then(data => {
          if (data) {
            this.team = data;
          } else {
            this.team = null;
            this.setPageTitle("404 - Page Not Found")
          }
        })
    },
   }, 
 created() {
this.id = this.$route.params.id;
this.id=parseInt(this.id)
    this.getTeamData()
    this.getTeamRank()
    },

}

</script>
<style scoped>
@import '../assets/css/details.css';
.ody{

    font-family: "Quicksand", sans-serif;
        text-decoration: none;


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
.ody {

    font-family: "Quicksand", sans-serif;
        text-decoration: none;


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
    filter: blur(20px);
    transition: filter 0.8s;
  }
  .v-lazy-image-loaded {
    filter: blur(0);
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
