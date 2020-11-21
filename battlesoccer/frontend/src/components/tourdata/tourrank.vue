<template>
<div class="ody">
  <div class="text-center shadow p-1 mb-1 bg-white rounded" v-if="!flag"><br><br>
    <img src="https://img.freepik.com/free-vector/soccer-football-player-running-with-ball-field-goalkeeper-front-gate-judge-observe-game-athlete-stadium-championship-league-cartoon-illustration_277904-4855.jpg?size=626&ext=jpg" 
    class="sic">
   <h3>Let us fill the rankboard with your goals</h3></div>
<div v-if="flag">
  <div v-if="this.rank3.own">
           <div class="conatiner">
<div class="container-sm">
<div class="row">
  <div class="col-12">
<div class="row text-center">
<b-col cols="4" style="padding:4px;">
<br><br><br><br><br><br>
<h3>2</h3>
<router-link
        :to="{ name: 'Teamveiw', params: { id: rank2.own.id } }"
        >
 <div data-aos="fade-down-right">
   <v-lazy-image :src="rank2.own.logo" class="respo"/>
 </div>
   <br>
<h4>{{rank2.own.teamname|capitalize}}</h4><br></router-link>
</b-col>

<b-col cols="4" style="padding:4px;">
<h3>1</h3><br>
<router-link
        :to="{ name: 'Teamveiw', params: { id: rank1.own.id } }"
        >
<div data-aos="flip-left">       
<v-lazy-image  :src="rank1.own.logo" class="resp"/></div><br>
<h4>{{rank1.own.teamname|capitalize}}</h4><br></router-link>
</b-col>

<b-col cols="4" style="padding:4px;">
<br><br><br><br><br><br>
<h3>3</h3>
<router-link
        :to="{ name: 'Teamveiw', params: { id: rank3.own.id } }"
        >
<div data-aos="fade-down-left">
  <v-lazy-image  :src="rank3.own.logo" class="respo"/></div><br>
<h4>{{rank3.own.teamname|capitalize}}</h4><br></router-link>
</b-col>

<hr>
<br><br>
</div>
</div>  
<div class="col-12">
  <div class="shadow p-1 mb-1 bg-white rounded" >
<div class="row mt-1">
     <div class="col-2 offset-1" style="padding:1px;"><router-link
        :to="{ name: 'playerpage', params: { id:this.teamdataall[0].tour_player } }"
        >
          <center>
            <img src="@/assets/img/Reward.png" alt="Avatar" class=circle1></center></router-link>
         </div>
          <div class="col-2" style="padding :1px;"><router-link
        :to="{ name: 'playerpage', params: { id:this.teamdataall[0].tour_goalkeaper } }"
        >
                       <center>     <img src="https://www.battlesoccer.in/static/img/Reward%20(1).b103c29b.png" alt="Avatar" class=circle1></center></router-link>
         </div>
          <div class="col-2" style="padding :1px;"><router-link
        :to="{ name: 'playerpage', params: { id:this.teamdataall[0].tour_highgoals } }"
        >
                         <center>   <img src="https://www.battlesoccer.in/static/img/Reward%20(2).d60369c6.png" alt="Avatar" class=circle1></center></router-link>
         </div>
          <div class="col-2" style="padding :1px;"><router-link
        :to="{ name: 'playerpage', params: { id:this.teamdataall[0].tour_fairplay } }"
        >
                         <center>   <img src="https://www.battlesoccer.in/static/img/Reward%20(3).27cfb1a1.png" alt="Avatar" class=circle1></center></router-link>
         </div>
          <div class="col-2" style="padding :1px;"><router-link
        :to="{ name: 'playerpage', params: { id:this.teamdataall[0].tour_moves} }"
        >
                         <center>   <img src="https://www.battlesoccer.in/static/img/Reward%20(5).799283aa.png" alt="Avatar" class=circle1></center></router-link>
          </div>
</div>
  
  <div class="row mt-1">
    
     <div class="col-2 offset-1" style="padding :1px;"><router-link
        :to="{ name: 'playerpage', params: { id:this.teamdataall[0].tour_player } }"
        >
          <center><h5>Best player</h5>
            <b>{{this.teamdataall[0].tour_player_detail}}</b></center></router-link>
         </div>
          <div class="col-2" style="padding :1px;"><router-link
        :to="{ name: 'playerpage', params: { id:this.teamdataall[0].tour_goalkeaper } }"
        >
          <center><h5>Best keeper</h5>
            <b>{{this.teamdataall[0].tour_goalkeaper_detail}}</b></center></router-link>
         </div>
          <div class="col-2" style="padding :1px;"><router-link
        :to="{ name: 'playerpage', params: { id:this.teamdataall[0].tour_highgoals } }"
        >
          <center><h5>Goal scorer</h5>
            <b>{{this.teamdataall[0].tour_highgoals_detail}}</b></center></router-link>
         </div>
          <div class="col-2" style="padding :1px;"><router-link
        :to="{ name: 'playerpage', params: { id:this.teamdataall[0].tour_fairplay } }"
        >
          <center><h5>Fairpaly</h5>
       <b>{{this.teamdataall[0].tour_fairplay_detail}}</b></center></router-link>
         </div>
          <div class="col-2" style="padding :1px;"><router-link
        :to="{ name: 'playerpage', params: { id:this.teamdataall[0].tour_moves} }"
        >
          <center><b><h5>Best move</h5>
            {{this.teamdataall[0].tour_moves_detail}}</b></center></router-link>
          </div>
</div>
  </div>

</div>
</div>
</div>

          <div class="container-lg"><br>
<hr>
<div v-for="(ranks,index) in teamdata" :key="index">
                <b-row align-v="center">
                  <b-col cols="12" lg="10" offset-lg="1" >
                 <div class="shadow  bg-white rounded" style="opacity:1; no-repeat ; background-color: rgba(255,255,255, 0.6); background-size: cover;" v-bind:style="{ 'background-image': 'url(' + ranks.own.coverpic + ')' } ">
                  <div class="shadow p-3 mb-2  rounded" style="background-color: rgba(255,255,255, 0.5);">
                  <b-row align-v="center" >
                  <b-col cols="4"> 
                <router-link
        :to="{ name: 'Teamveiw', params: { id: ranks.own.id } }"
        >    
                <div data-aos="zoom-in-up">
                 <center><img :src="ranks.own.logo" class="respo mb-3"/></center></div>
             <h3 class="text-center">{{ranks.own.teamname|capitalize}}</h3>
                </router-link>
                </b-col>
              <b-col cols="8">
                <b-row >
                  <b-col cols="6" offset="3">
                  <h2 class=text-center style="font-weight: bold;color: #000000;"><b>#{{index+1}}</b></h2>
                  </b-col>
                </b-row> <br>
                    <br>
                    
      <b-row style="" align-v="center">
         <b-col cols="4"><h4 style="font-weight: bold;color: #000000;" data-aos="flip-left"><center>{{ranks.teamgoals}}</center></h4></b-col>
         <b-col cols="4" ><h4 style="font-weight: bold;color: #000000;" data-aos="flip-left"><center>{{ranks.matchs_played}}</center></h4></b-col>
         <b-col cols="4" ><h4 style="font-weight: bold;color: #000000;" data-aos="flip-left"><center>{{ranks.match_won}}</center></h4></b-col>
</b-row>
 <b-row  align-v="center">
        <b-col cols="4"><b><h4 style="font-weight: bold;color: #000000;"><center>Goals</center></h4></b></b-col>
          <b-col cols="4"><b><h4 style="font-weight: bold;color: #000000;"><center>Play</center></h4></b></b-col>
          <b-col cols="4"><b><h4 style="font-weight: bold;color: #000000;"><center>Won</center></h4></b></b-col>
     </b-row>
              </b-col>
              </b-row>
              </div></div>
              </b-col>
              </b-row>
              <hr>
              </div>
</div>
</div></div>
<br>

</div>
</div>
</template>
<script>
import { apiService } from "@/common/api.service.js";

export default{
    name: "tourrank",
     props: {
    hold: {
      type: [Number,String]
    },
 },
data() {
    return {
      teamdata:[],
      teamdataall:[],
      teamrank:[],
      rank1:{},
      rank2:{},
      rank3:{},
      flag:true,
      holds:null,
      temp:null
    }
    },


  methods: {  
    gettourdata() {
      // get the details of a question instance from the REST API and call setPageTitle
      if(!this.hold){
        this.temp=this.holds
      }
      else{
        this.temp=this.hold
      }
       let endpoint = `/api/tournament/${this.temp }/`;
      apiService(endpoint)
 .then(data => {
          if (data) {
            this.teamdataall = data
            this.teamdata=this.teamdataall[0].rank
            this.teamrank=this.teamdata.slice(0,4)
            this.rank1=this.teamrank[0];
            this.rank2=this.teamrank[1];
            this.rank3=this.teamrank[2]; 
             if(!this.rank1.own){
              this.flag=false
            }
          } else {
             if(!this.rank1.own){
              this.flag=false}
            this.next = null;
          } 
        })   
    },
},
created()
{console.log(this.hold)
            this.holds = this.$route.params.hold;
            console.log(this.holds)
           this.gettourdata() 
},

}


</script>

<style scoped>
@import '../../assets/css/teamrank.css';
@import '../../assets/css/rankcard.css';

.ody a{

    font-family: "Quicksand", sans-serif;
    text-decoration: none;
}

.sic{
 width: 60%; 
}

.ody{
  overflow:hidden;

}
.lds-ripple {
  display: inline-block;
  position: relative;
  width: 80px;
  height: 80px;
}
.lds-ripple div {
  position: absolute;
  border: 4px solid #fff;
  opacity: 1;
  border-radius: 50%;
  animation: lds-ripple 1s cubic-bezier(0, 0.2, 0.8, 1) infinite;
}
.lds-ripple div:nth-child(2) {
  animation-delay: -0.5s;
}
@keyframes lds-ripple {
  0% {
    top: 36px;
    left: 36px;
    width: 0;
    height: 0;
    opacity: 1;
  }
  100% {
    top: 0px;
    left: 0px;
    width: 72px;
    height: 72px;
    opacity: 0;
  }
}

 .circle1 {
  border-radius: 50%;
  width:55%;
  height:auto;
}

h1{
            font-size:55px;

        }

h2{
            font-size:45px;

        }
h3{
          font-size:24px;
}
h4{
            font-size:20px;
        }

h5{
            font-size:15px;
        }
@media only screen and (max-width:700px) {
   .circle1 {
  border-radius: 75%;
  width:100%;
  height:auto;
}
  .sic{
 width: 75%; 
}
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
            font-size:17px;
        }
h5{
            font-size:8px;

        }
}

.main-raised {
  width:65px;
  height:45px;
  border-radius: 10%;
-webkit-box-shadow: 0px 0px 8px 0px rgba(0,0,0,0.3);
-moz-box-shadow: 0px 0px 8px 0px rgba(0,0,0,0.3);
box-shadow: 0px 0px 8px 0px rgba(0,0,0,0.3);
  font-size: 30px;
  text-align: center;
float:left
}

  </style>
