<template>
<div class="ody">
 <br><br><br><br>
 <div class="container">
    <h1>Highlights</h1>   
 </div><br>
 <div>
        <highlightvideo class="videocover" v-for = "video in highligths"
        :video="video"
        :requestUser="requestUser"
        :key="video.pk"/>
</div>
          <div class="my-4 container text-center">
      <h2 v-show="loadinghighlight"><div class="lds-ripple"><div></div><div></div></div></h2>
      </div>
</div>
</template>

<script>

import { apiService } from "@/common/api.service.js";
import highlightvideo from "@/components/highlightvideo.vue";

export default{
  name: "Highlight",
  components: {
highlightvideo
  },
  data() {
    return {
      next: null,
      loadinghighlight: false,
      highligths: [],
      requestUser:null,
    }
  },
    mounted () {
this.scroll()
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
         this.gethighligthsData();// replace it with your code
        }
        }
      }
    },
      gethighligthsData() {
      // get the details of a question instance from the REST API and call setPageTitle
      let endpoint = `/api/highlights/`;
      setTimeout(() => { 
         if (this.next) {
        endpoint = this.next;
      }
      this.loadinghighlight = true;
      apiService(endpoint)
      
 .then(data => {
          this.highligths.push(...data.results);
         
  this.loadinghighlight = false;
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
    this.gethighligthsData()

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
  padding: 0 4px;
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