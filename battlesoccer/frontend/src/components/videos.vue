<template>
<div clas="ody">
<br>
 <div class="container">
    <h1>Highlights</h1></div>
    <div class="container-fluid">
      
       <div class="row"> 
         <div class="col-12">

           <router-link
        :to="{ name: 'picvid',params: {com:'apphighcom'}}"
        >  
   <h5 style="float:right;margin-right:15px; margin-bottom:10px; color:blue;">see more <i class="fa fa-angle-double-right" style="font-size:24px  margin-bottom:-10px;"></i></h5></router-link>
         </div>
         <div class="col-6 col-lg-3 " style="padding:4px;" v-for = "video in highligths"
        :key="video.pk">
        <div class="main-raised1">
              <div class="embed-responsive embed-responsive-1by1">
  <iframe class="embed-responsive-item" :src="video.highlight" 
   allow="accelerometer; autoplay;loop; encrypted-media; gyroscope; picture-in-picture" allowfullscreen
   ></iframe>
</div> 
    <router-link
        :to="{ name: 'Teamveiw', params: { id: video.own.id} }"
        >      
 <center><h4 class="mt-2">{{video.teamname| capitalize}}</h4></center></router-link>
              <hr style="width:0%; margin-top:-2px;">
        </div></div>
          </div></div></div>
</template>

<script>

import { apiService } from "@/common/api.service.js";
export default{
  name: "videos",
  data() {
    return {
      highligths: [],
    }
  },
   methods: {
      gethighligthsData() {
      // get the details of a question instance from the REST API and call setPageTitle
      let endpoint = `/api/highlights/`;
      apiService(endpoint)
        .then(data => {
          if (data) {
            this.highligths = data.results;
            this.highligths = this.highligths.slice(0,4);
          } else {
            this.highligths = null;
            this.setPageTitle("404 - Page Not Found")
          }
        })
    },
    },
  created() {
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

video{
width:100%;
margin:auto;
font-size:35px;

}


@media only screen and (max-width:950px) {
   .videocover {
    width:50%;
    

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
            font-size:17px;
        }
h5{
            font-size:17px;

        }
}
.main-raised1 {
  display:block;
    border-radius: 8px;
-webkit-box-shadow: 0px 0px 8px 0px rgba(0,0,0,0.2);
-moz-box-shadow: 0px 0px 8px 0px rgba(0,0,0,0.2);
box-shadow: 0px 0px 8px 0px rgba(0,0,0,0.2);}


</style>
