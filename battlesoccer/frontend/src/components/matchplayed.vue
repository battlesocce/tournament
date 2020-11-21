<template>
  <div class="ody">
<div class="flow">
  <table class="table">
      <tr>
          <th><h4><center>Tour</center></h4></th>
           <th><h4><center>Goals</center></h4></th>
          <th><h4><center>Played</center></h4></th>
          <th><h4><center>Won</center></h4></th>
          <th><h4><center>Lost</center></h4></th>
      </tr>
    <tbody  v-for="teampresent in team"
      :key="teampresent.id">
      <tr v-if="teampresent.own.id==id">
             
         <td><router-link 
        :to="{ name: 'matches' ,params: {id:teampresent}}">
        <h5 style="color:darkblue;"><center>{{teampresent.tournament_name}}</center></h5></router-link></td>
          <td><h3><center>{{teampresent.teamgoals}}</center></h3></td>
          <td><h3><center>{{teampresent.matchs_played}}</center></h3></td>
          <td><h3><center>{{teampresent.match_won}}</center></h3></td>
          <td><h3><center>{{teampresent.match_lost}}</center></h3></td>
              
      </tr>
   </tbody>
  </table> 
            </div>

<br>
        </div> 
</template>

<script>
import { apiService } from "@/common/api.service.js";
export default{
  name: "matchplayed",
  
  data() {
    return {
      team: {},
      error: null
    }
  },
  props: {
    id: {
      type: Number,
      required: true
    },
  },
   methods: {
      getmatchdetails() {
      let endpoint = `/api/teamrankall/`;
      apiService(endpoint)
        .then(data => {
          if (data) {
            this.team = data;
          } else {
            this.team = null;
            this.setPageTitle("404 - Page Not Found")
          }
        })
    }
   },
 created() {
    this.getmatchdetails()
    },

}
</script>
<style scoped>
@import '../assets/css/details.css';
body {

    font-family: "Quicksand", sans-serif;

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

 .v-lazy-image {
    filter: blur(10px);
    transition: filter 0.7s;
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
            font-size:25px;
}
h4{
            font-size:23px;
        }
h5{
            font-size:20px;

        }
}
</style>
