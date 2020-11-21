<template>
<div class="ody">
  <div class="container" v-if="this.teamdata[0]"><br><br><br><br>
<h2 class="text-center fixed-top" style="background-color:white;margin-top:65px; z-index:10;">
  <hr style="width:0%; margin-top:-17px; ">{{this.teamdata[0].tournament_name|capitalize}}</h2></div>
   <b>  <div class="container">
        <div class="row fixed-top text-center " style="-webkit-box-shadow: 0px 1px 2px 0px rgba(50, 50, 50, 0.1);
-moz-box-shadow:0px 1px 2px 0px rgba(50, 50, 50, 0.1);
box-shadow:0px 1px 2px 0px rgba(50, 50, 50, 0.1);background-color:white;margin-top:93px; z-index:10;"  >


<div class="col-3" >
<div style="margin-bottom:5px; margin-top:15px; cursor:pointer"
v-on:click="setActive('apptourrank')" :class="{ active: isActive('apptourrank') }"
@click="selectedComponent = 'apptourrank'">Rank</div></div>


 <div class="col-3" >
     <div style="margin-bottom:5px; margin-top:15px; cursor:pointer"
      v-on:click="setActive('apphighcom')" :class="{ active: isActive('apphighcom') }"
      @click="selectedComponent = 'apphighcom'">Highlight</div></div>

 <div class="col-3">
      <div style="margin-bottom:5px; margin-top:15px; cursor:pointer"
       v-on:click="setActive('appgallery_gal')" :class="{ active: isActive('appgallery_gal') }"
       @click="selectedComponent = 'appgallery_gal'" >Photos</div></div>

 <div class="col-3">
     <div style="margin-bottom:5px; margin-top:15px; cursor:pointer"
      v-on:click="setActive('appmatchvideos')" :class="{ active: isActive('appmatchvideos') }"
     @click="selectedComponent = 'appmatchvideos'" >Videos</div></div>
     </div>
     </div></b> 
<br><br>
                <transition name="slide" mode="out-in" v-if="this.teamdata[0]">
                <component class="mt-3" :is="selectedComponent" :tourname="this.teamdata[0].tournament_name" :hold="this.hold"/>
                </transition>            
</div>
</template>

<script>

import highcom from '@/components/tourdata/highcom.vue';
import gallery_gal from '@/components/tourdata/gallery_gal.vue';
import matchvideos from '@/components/tourdata/matchvideos.vue';
import tourrank from '@/components/tourdata/tourrank.vue';
import { apiService } from "@/common/api.service.js";

export default {
    name:"tourdata",
      data: function() {
          return {
             teamdata:[],
              teamdataall:[],
              selectedComponent: 'apptourrank',
              activeItem: 'apptourrank'
          }
        },
      props: {
     hold: {
      type: Number,
    },
  },
        components: {
            apphighcom: highcom,
            appgallery_gal: gallery_gal,
            appmatchvideos: matchvideos,
            apptourrank: tourrank
        },
        methods: {
           gettourdata() {
      // get the details of a question instance from the REST API and call setPageTitle
      let endpoint = `/api/tournament/${this.hold }/`;
      apiService(endpoint)
 .then(data => {
          if (data) {
            this.teamdataall = data
            this.teamdata=this.teamdataall[0].rank
           
          } else {
             
            this.next = null;
          } 
        })   
    },
    isActive: function (menuItem) {
      return this.activeItem === menuItem
    },
    setActive: function (menuItem) {
      this.activeItem = menuItem // no need for Vue.set()
    }
  },
  created(){
          this.gettourdata() 
  }
}
</script>

<style scoped>
.active{
    color: red;

}

   .slide-leave-active {
        transition: opacity 0.1s ease;
        opacity: 0;
        animation: slide-out 0.1s ease-out forwards;
    }

    .slide-leave {
        opacity: 1;
        transform: translateX(0);
    }

    .slide-enter-active {
        animation: slide-in 0.1s ease-out forwards;
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

    h1{
            font-size:55px;

        }

h2{
            font-size:25px;

        }
h3{
          font-size:35px;
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
            font-size:17px;
        }
h5{
            font-size:20px;

        }
}


</style>