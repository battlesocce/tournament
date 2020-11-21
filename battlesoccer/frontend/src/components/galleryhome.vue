<template>
<div class="ody">
     <div class="container">
    <h1>Gallery</h1></div>
    <div class="row">
      <div class="col-12">
     <router-link
        :to="{ name: 'picvid',params: {com:'appgallery_gal'}}"
        >  
   <h4 style="float:right;margin-right:20px;  margin-bottom:10px; color:blue;">see more <i class="fa fa-angle-double-right" style="font-size:24px  margin-bottom:-10px;"></i></h4></router-link>
      </div>
            <div class="col-12">

     <gallery :images="img" :index="index" @close="index = null"></gallery>
  <div class="container-lg">
  <div class="row">
    <div class="col-4 " style="padding:2px"
      v-for="(image, imageIndex) in pics"
      :key="imageIndex"
      @click="index = imageIndex"
    >
      <img :src="image.image" width="100%" class="bg-white " style="border-radius:12px 12px 0px 0px">   
      <h5 class=" shadow-sm bg-white text-center" style="font-weight:600px;margin-top:-17px;"><hr style="width:0%; margin-bottom:6px "><b>
       <router-link 
        :to="{ name: 'rankpage',params:{hold:image.tournament_id} }">
        {{image.property|capitalize}}</router-link>
        </b><hr style="width:0%; margin-top:4px"></h5>
       </div></div>
    </div></div>
</div></div>
</template>

<script>
import VueGallery from 'vue-gallery';
import { apiService } from "@/common/api.service.js";
export default{
  name: "gallerypics",
  data() {
    return {
      pics: {},
      img:[],
      index: null,
      currentIndex :null,
      temporaryValue :null,
      randomIndex:null,
      array:null
    }
  },
      components: {
      'gallery': VueGallery
    },
  methods: {
      getgallery() {
      let endpoint = `/api/gallerypics/`;
      apiService(endpoint)
        .then(data => {
          if (data) {
            this.pics = data;
            this.array = this.pics
             this.currentIndex =this.array.length
            while (0 !== this.currentIndex) {

    // Pick a remaining element...
    this.randomIndex = Math.floor(Math.random() * this.currentIndex);
    this.currentIndex -= 1;

    // And swap it with the current element.
    this.temporaryValue = this.array[this.currentIndex];
    this.array[this.currentIndex] = this.array[this.randomIndex];
   this.array[this.randomIndex] =this. temporaryValue;
  }
  this.pics=this.array.slice(0,9)
 this.pics.map((pic) => {
   this.img.push(pic.image);
});
          } else {
            this.pics = null;
            this.setPageTitle("404 - Page Not Found")
          }
        })
    }
   },
  
 created() {
    this.getgallery()
}
}
</script>
<style scoped>




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
.sm{
    width:100%;
  padding-right: 0px;
padding-left: 0px;
padding-left: 0px;
}
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
            font-size:12px;

        }

.gallery__caption {
  position: absolute;
  bottom: -15px;
  left: 0;
  padding: 25px 15px 15px;
  width: 100%;
  font-family: "Raleway", sans-serif;
  font-size: 10px;
  color: white;
  opacity: 0;
  background: linear-gradient(0deg, rgba(0, 0, 0, 0.5) 0%, rgba(255, 255, 255, 0) 100%);
  transition: 0.3s;
}

}

.gallery {
  transition: 0.3s;
}
.gallery:hover .gallery__image {
  filter: grayscale(1);
}

.gallery__link:hover .gallery__image {
  filter: grayscale(0);
}
.gallery__link:hover .gallery__caption {
  opacity: 1;
}
.gallery__thumb {
  position: relative;
}

.gallery__image {
width:100%;
  padding-right: 0px;
padding-left: 0px;
padding-left: 0px;
  margin-bottom: -16px;
}

.gallery__caption {
  position: absolute;
  bottom: -15px;
  left: 0;
  padding: 25px 15px 15px;
  width: 100%;
  font-family: "Raleway", sans-serif;
  font-size: 16px;
  color: white;
  opacity: 0;
  background: linear-gradient(0deg, rgba(0, 0, 0, 0.5) 0%, rgba(255, 255, 255, 0) 100%);
  transition: 0.3s;
}



</style>
