<template>
    <div>
      <br>
       <div class="container"><br>
<h1>Team Enrolled</h1>  </div> 
<br>
<div class="container-lg">
      <transition-group name=slide class="row">
<div class="col-6 col-lg-3" style="padding:5px;" v-for="teamd in team" :key="teamd.id"><div data-aos="zoom-in-down">
  <div class="shadow bg-white rounded">
        <router-link
        :to="{ name: 'Teamveiw', params: { id: teamd.own.id } }"
        >
  <div class="our-team">
    <div class="picture">
      <img :src="teamd.own.logo + '?'+ new Date().getTime()">
         </div>

    <div class="team-content">
      <h4 class="name">{{teamd.own.teamname| capitalize}}</h4>
    </div>

  </div>
        </router-link></div></div>
</div>
      </transition-group>
</div>
<div class="container text-center">
      <h2 v-show="loadingteam"><div class="lds-ripple"><div></div><div></div></div></h2>

      </div>


    </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
export default {
    name:"enrolledteams",
      data() {
    return {
      team: [],
      next: null,
      loadingteam: false,
    }
      },
          mounted () {
this.scroll()
  },
 
      methods: {
         scroll () {
      window.onscroll = () => {
        let bottomOfWindow = Math.max(window.pageYOffset, document.documentElement.scrollTop, document.body.scrollTop) + window.innerHeight === document.documentElement.offsetHeight

        if (bottomOfWindow) {
          if (this.next) { 
         this.getTeamData();// replace it with your code
        }
        }
      }
    },
      getTeamData() {
      // get the details of a question instance from the REST API and call setPageTitle
      let endpoint = `/api/contest/`;
      apiService(endpoint)
       setTimeout(() => {
if (this.next) {
        endpoint = this.next;
      }
      this.loadingteam = true;
      apiService(endpoint)
 .then(data => {
          this.team.push(...data.results);
          this.loadingteam = false;
          if (data.next) {
            this.next = data.next;
          } else {
            this.next = null;
          }}, 2000)
        })
    },
      },
  created() {
    this.getTeamData()
  }

}

</script>

<style scoped>
  .ody a{

    font-family: "Quicksand", sans-serif;
    text-decoration: none;    
}
.lds-ripple {
  display: inline-block;
  position: relative;
  width: 80px;
  height: 80px;
}
.lds-ripple div {
  position: absolute;
  border: 4px solid black;
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
            font-size:20px;
        }
h5{
            font-size:20px;

        }
}

</style>