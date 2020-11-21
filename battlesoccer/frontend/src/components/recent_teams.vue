<template>
<div>
  <center><hr>
 <div class="card">
      <div class="card-image">
        <div class="background-image" :style="{'background-image': `url(${require('@/assets/img/card.jpg')})`}"></div>
        <div class="publication-details">
            Next Battle on
          <span class="date"><i class="fas fa-calendar-alt"></i> Dec 05, 2020</span>
        </div>
      </div>

      <div class="card-content">
        <h2 >Battle Takedown</h2>
        <h3 class="subtitle">Join the Real battle now</h3>
        <router-link 
        :to="{ name: 'contest'}" >
        <div class="cta1">
          <a href="">Read more &rarr;</a>
        </div></router-link>
      </div> 
 </div>

</center><br>
  <div class="container">
    <div  style="margin-bottom:40px;" >
<h1><br>Recently added Teams</h1></div>
<div class="row" >
<div class="col-6 col-lg-3" style="padding:6px;" v-for="teamd in teamdata" :key="teamd.id"><div data-aos="zoom-in-down">
        <div class="shadow rounded">
        <router-link
        :to="{ name: 'Teamveiw', params: { id: teamd.id } }"
        >
  <div class="our-team">
    <div class="picture">
      <img :src="teamd.logo + '?'+ new Date().getTime()">
         </div>

    <div class="team-content">
      <h4 class="name">{{teamd.teamname| capitalize}}</h4>
    </div>
  
  </div>
        </router-link></div>
</div>
</div></div>
  </div>
</div>
</template>

<script>


export default{
name: "recentteam",
props: {
    teamdata: {
      type: Array,
      required: true
    },
    }
}

</script>

<style scoped>
@import '../assets/css/userprofile.css';
@import '../assets/css/about.css';
.right2 {
  color:black;
  float:left;
  width:100%;
  padding:18px;
  margin-top:10px;
  text-align:center;
}

.background-image {
  width: 100%;
  height: 100%;
  position: absolute;
  top: 0;
  left: 0;
  background-size: cover;
  z-index: 0;
  transition: transform 5s;
 

}
hr {
  border: 0;
  clear:both;
  display:block;
  width: 96%;               
  background-color:white;
  height: 1px;
}
.ody a{

    font-family: "Quicksand", sans-serif;
        text-decoration: none;


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
            font-size:25px;

        }
h3{
            font-size:20px;
}
h4{
            font-size:20px;
        }
h5{
            font-size:20px;

        }
}
.main-raised1 {
  display:block;
-webkit-box-shadow: 0px 0px 8px 0px rgba(0,0,0,0.1);
-moz-box-shadow: 0px 0px 8px 0px rgba(0,0,0,0.1);
box-shadow: 0px 0px 8px 0px rgba(0,0,0,0.1);}

</style>
