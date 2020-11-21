<template>
<div class="ody">

 <div>
        <div class="videocover" v-for = "video in filteredList"
        :key="video.pk">
<div class="main main-raised">
      <hr style="width:0%; margin-bottom:2px;">    
      <h2 class="text-center">{{video.tournament_name|capitalize}}</h2>
              <div class="embed-responsive embed-responsive-1by1 mb-3">
  <iframe class="embed-responsive-item" :src="video.matchvideos"
   allow="accelerometer; autoplay;loop;mute;encrypted-media; gyroscope; picture-in-picture" allowfullscreen
   ></iframe>
      </div>
               <h3 class="text-center">{{video.team_a|capitalize}} - {{video.team_b|capitalize}}</h3>
      <hr style="width:0%; margin-bottom:2px;">    

        </div>
        </div>
</div>
          <div class="my-4 container text-center">
      <h2 v-show="loadingmatchvideos"><div class="lds-ripple"><div></div><div></div></div></h2>
      </div>
</div>
</template>

<script>

import { apiService } from "@/common/api.service.js";

export default{
  name: "highcom",
  data() {
    return {
      next: null,
      loadingmatchvideos: false,
      matchvideos: [],
      requestUser:null,
    }
  },
    mounted () {
this.scroll()
  },
       props: {
    tourname: {
      type: String,
    }},
  computed: {
    filteredList() {
       if (!this.tourname) {
      return this.matchvideos;
       }
       else{
      return this.matchvideos.filter(vid=> {
        return vid.tournament_name.toLowerCase().match(this.tourname.toLowerCase())
      })   }
},
  },
   methods: {
          setRequestUser() {
      // the username has been set to localStorage by the App.vue component
      this.requestUser = window.localStorage.getItem("username");
    },
      scroll () {
      window.onscroll = () => {
        let bottomOfWindow = Math.max(window.pageYOffset, document.documentElement.scrollTop, document.body.scrollTop) + window.innerHeight === document.documentElement.offsetHeight

        if (bottomOfWindow) {
          if (this.next) { 
         this.getmatchvideosData();// replace it with your code
        }
        }
      }
    },
      getmatchvideosData() {
      // get the details of a question instance from the REST API and call setPageTitle
      let endpoint = `/api/matchvideos/`;
      setTimeout(() => { 
         if (this.next) {
        endpoint = this.next;
      }
      this.loadingmatchvideos = true;
      apiService(endpoint)
      
 .then(data => {
          this.matchvideos.push(...data.results);
         
  this.loadingmatchvideos = false;
          if (data.next) {
            this.next = data.next;
          } else {
            this.next = null;
          } }, 2000)
        })
    },
    },
  created() {
    this.setRequestUser()
    this.getmatchvideosData()

    }
}
</script>
<style scoped>

.ody a{

    font-family: "Quicksand", sans-serif;
    text-decoration: none;
}
.videocover {
  color:black;
overflow:hidden;
  float:left;
  width:25%;
  padding: 0 0px;
}

iframe{
width:100%;
height:auto;
margin:auto;
font-size:35px;
}


@media only screen and (max-width:950px) {
   .videocover {
    width:100%;
  }
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
            font-size:22px;

        }
h3{
          font-size:18px;
}
h4{
            font-size:20px;
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
            font-size:15px;
        }
h5{
            font-size:20px;

        }
}
.main-raised {
  display:block;
    margin: 20px 10px 0;
    border-radius: 8px;
-webkit-box-shadow: 0px 0px 8px 0px rgba(0,0,0,0.2);
-moz-box-shadow: 0px 0px 8px 0px rgba(0,0,0,0.2);
box-shadow: 0px 0px 8px 0px rgba(0,0,0,0.2);}

</style>