<template>
<div class="ody">
        <div class="container">
    <h1><center>Top Teams</center></h1>
  </div>
<div class="row">
  <div class="col-12 col-lg-6 offset-lg-3">
<div class="container-fluid">
  <div class="main main-raised">
<div data-aos="flip-left" data-aos-duration="800">
<div class="table_ranking row1  text-center">
 <div class="col-4 ranking r2 animated">
        <router-link
        :to="{ name: 'Teamveiw', params: { id: rank2.own.id } }"
        >
  <div class="header">
   <h3>{{rank2.own.teamname}}</h3>
  </div>
 <div class="block1">
      <h2><img :src="rank2.own.logo" class="res"/></h2>
   <p><strong>Goals</strong></p>
   <p>{{rank2.teamgoals}}</p>
  </div>
  <div class="block2">
   <p><strong>Played</strong></p>
   <p>{{rank2.matchs_played}}</p>
  </div>
  <div class="block3">
   <p><strong>Won</strong></p>
   <p>{{rank2.match_won}}</p>
  </div>
  <div class="block4">
   <div class="place">2</div>
  </div>
  </router-link>
 </div>


 <div class="col-4 ranking r1 animated first ">
<router-link
        :to="{ name: 'Teamveiw', params: { id: rank1.own.id } }">
          <div class="header">
   <h3>{{rank1.own.teamname}}</h3>
  </div>
 <div class="block1">
      <h2><img :src="rank1.own.logo" class="res1"/></h2>
   <p><strong>Goals</strong></p>
   <p>{{rank1.teamgoals}}</p>
  </div>
  <div class="block2">
   <p><strong>Played</strong></p>
   <p>{{rank1.matchs_played}}</p>
  </div>
  <div class="block3">
   <p><strong>Won</strong></p>
   <p>{{rank1.match_won}}</p>
  </div>
  <div class="block4">
   <div class="place">1</div>
  </div>
</router-link>
 </div>

 <div class="col-4 ranking r3 animated">
<router-link
        :to="{ name: 'Teamveiw', params: { id: rank3.own.id } }">
  <div class="header">
   <h3>{{rank3.own.teamname}}</h3>
  </div>
 <div class="block1">
      <h2><img :src="rank3.own.logo" class="res"/></h2>
   <p><strong>Goals</strong></p>
   <p>{{rank3.teamgoals}}</p>
  </div>
  <div class="block2">
   <p><strong>Played</strong></p>
   <p>{{rank3.matchs_played}}</p>
  </div>
  <div class="block3">
   <p><strong>Won</strong></p>
   <p>{{rank3.match_won}}</p>
  </div>
  <div class="block4">
   <div class="place">3</div>
  </div>
</router-link>
 </div>
</div>
</div>
 </div>
  </div>
</div>
</div>
<br><br>
</div>
</template>

<script>

import { apiService } from "@/common/api.service.js";

export default{
    name: "rankboard",

    data() {
    return {
      teamrank:[],
      rank1:{},
      rank2:{},
      rank3:{},
    }
    },
methods: {
    getTeamRank() {
      // get the details of a question instance from the REST API and call setPageTitle
      let endpoint = `/api/teamrank/`;
      apiService(endpoint)
        .then(data => {
          if (data) {
            this.loading = true;
            this.teamrank = data.results;
            this.rank1=this.teamrank[0];
            this.rank2=this.teamrank[1];
            this.rank3=this.teamrank[2];
          } 
          else {
            this.setPageTitle("404 - Page Not Found")
          }
        })    
    },
},
created()
{
  this.getTeamRank()
},

}


</script>

<style scoped>

@import '../assets/css/teamrank.css';
@import '../assets/css/rankcard.css';

.ody a{

    font-family: "Quicksand", sans-serif;
        text-decoration: none;


}

.ody{
  overflow: hidden;

}

.row1 {
  display: flex;
  flex-wrap: wrap;
  margin-right: 0px;
  margin-left: 0px;
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
}
</style>

