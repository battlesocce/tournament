<template>
<div class="ody">
<gallery :images="img" :index="index" @close="index = null"></gallery>
  <div class="container-lg">
  <div class="row">
    <div class="col-4 col-lg-3" style="padding:2px"
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
    </div>
</div>
</template>

<script>
import VueGallery from 'vue-gallery';
import { apiService } from "@/common/api.service.js";
export default{
  name: "gallery_gal",
  data() {
    return {
      pics: [],
       img:[],
      index: null,
      currentIndex :null,
      temporaryValue :null,
      randomIndex:null,
      array:null
    }
  },
     props: {
    tourname: {
      type: String,
    }},
      components: {
      'gallery': VueGallery
    },
  computed: {
    filteredList() {
       if (!this.tourname) {
      return this.pics;
       }
       else{
      return this.pics.filter(pice=> {
        return pice.property.toLowerCase().match(this.tourname.toLowerCase())
      })   }
},
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
   this.array[this.randomIndex] = this. temporaryValue;
  }
  this.pics=this.array
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
            font-size:25px;
        }
h5{
            font-size:12px;

        }
}
</style>
