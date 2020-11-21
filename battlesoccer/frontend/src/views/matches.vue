<template>
  <div class="ody"><br><br><br>
  <div class="container-lg" v-if="team[0]">
<h2 class="mt-2"><center>{{team[0].tournament_name|capitalize}}</center></h2>
<h3 class="text-muted mt-4 mb-4"><center>{{team[0].team_a|capitalize}}</center></h3>
<div class="flow ">
  <table v-if = "id.tournament_name" class="table">
     <tr>
          <th><h4><center>Opponent</center></h4></th>
          <th><h4><center>team goals</center></h4></th>
          <th><h4><center>Opponent goals</center></h4></th>
          <th><h4><center>Winner</center></h4></th>
          <th><h4><center>Date</center></h4></th>
          <th><h4><center>Time</center></h4></th>
     </tr> 
    <tbody  v-for="teampresent in team"
      :key="teampresent.id">
      <tr v-if="(id.teamown == teampresent.team_a || id.teamown == teampresent.team_b) && id.tournament_name == teampresent.tournament_name">
             
          <td><h3><center>{{teampresent.team_b}}</center></h3></td>
          <td><h3><center>{{teampresent.team_a_goals}}</center></h3></td>
          <td><h3><center>{{teampresent.team_b_goals}}</center></h3></td>
          <td><h3><center>{{teampresent.winner}}</center></h3></td>
          <td><h3><center>{{teampresent.date}}</center></h3></td>
          <td><h3><center>{{teampresent.time}}</center></h3></td>
              
      </tr>
   </tbody>
  </table> 
            </div>

<br></div>
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
   methods: {
      getmatchdetails() {
      let endpoint = `/api/matchplayed/`;
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
  this.id = this.$route.params.id;
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
          font-size:30px;
}
h4{
            font-size:30px;
            font-weight: 600;
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
            font-size:22px;
}
h4{
            font-size:22px;
        }
h5{
            font-size:20px;

        }
}
</style>
