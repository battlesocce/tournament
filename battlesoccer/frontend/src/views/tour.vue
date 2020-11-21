<template>
<div class="ody">
<div class="container-lg"><br><br><br><br>
<h2 class="text-center">Tournaments</h2><br>
<div v-for="tours in tourdata" :key="tours.id">
                <b-row align-v="center">
                  <b-col cols="12" >
                   <router-link 
        :to="{ name: 'rankpage',params:{hold:tours.id} }"
        >  <div class="shadow p-3 mb-4 bg-white rounded" style="opacity:0.9; no-repeat ;  background-size: cover;" v-bind:style="{ 'background-image': 'url(' + tours.tour_coverpic + ')' }">
                <center><h3 style="color: #000000;">{{tours.tour_name|capitalize}}</h3></center>
               
        
        <div class="row" style="margin-bottom:-18px; ">
          <div class="col-auto mr-auto mt-3">
<h5 style="font-weight: bold;color: #000000;">Date:{{tours.tour_date|capitalize}}
          </h5></div>

 <div class="col-auto mt-3" style="float:right">
<h5 style="font-weight: bold;color: #000000;">City:{{tours.tour_city|capitalize}}</h5>
          </div>
          
          </div></div></router-link>
              </b-col>
              </b-row>
</div>
<div class="container text-center">
      <h2 v-show="loadingrank"><div class="lds-ripple"><div></div><div></div></div></h2>
      </div>
      
</div>
</div>
</template>

<script>

import { apiService } from "@/common/api.service.js";

export default{
    name: "tour",

    data() {
    return {
      tourdata:[],
      next: null,
      loadingrank: false,
      flag:false
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
         this.gettourdata();// replace it with your code
        }
        }
      }
    },

    gettourdata() {
      // get the details of a question instance from the REST API and call setPageTitle
      let endpoint = `/api/tournament/`;
      apiService(endpoint)
      setTimeout(() => {
      if (this.next) {
        endpoint = this.next;
      }
      this.loadingrank = true;
      apiService(endpoint)
 .then(data => {
          this.tourdata.push(...data.results);
          this.loadingrank = false;
          if (data.next) {
            this.next = data.next;
          } else {
            this.next = null;
          } }, 2000)
        })   
    },
},
created()
{
  this.gettourdata()
},

}


</script>

<style scoped>
@import '../assets/css/teamrank.css';
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
            font-size:30px;
}
h4{
            font-size:20px;
        }
h5{
            font-size:15px;

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
