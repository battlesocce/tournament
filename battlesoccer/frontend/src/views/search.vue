<template>
<div class="ody">
  <br><br><br><br>
        <div class="row fixed-top"   style="
        background-color:white;margin-top:58px; z-index:10;"  >
<div class="col-12"><hr style="width:0%; margin-bottom:-10px;"></div>
  <div class="col-8 col-lg-6 offset-lg-4 offset-2" style='padding:3px;'>
<input type="text" class="form-control form-control-lg"  :value='search'
@input='evt=>search=evt.target.value'
  ref="search" placeholder="Search here"></div>
  <div class="col-2" style='padding:2px;'>

</div></div>

<div class="container text-center "><b> 
        <div class="row fixed-top" style="-webkit-box-shadow: 0px 1px 2px 0px rgba(50, 50, 50, 0.1);-moz-box-shadow:0px 1px 2px 0px rgba(50, 50, 50, 0.1);
box-shadow:0px 1px 2px 0px rgba(50, 50, 50, 0.1); background-color:white;margin-top:118px; z-index:10;"  >
               
<div class="col-3 col-lg-3">
      <div style="margin-bottom:7px; margin-top:7px; cursor:pointer;"
       v-on:click="setActive('appsearchteam')" :class="{ active: isActive('appsearchteam') }"
      @click="selectedComponent = 'appsearchteam'">Team</div> </div>

 <div class="col-3 col-lg-3" >
     <div style="margin-bottom:7px; margin-top:7px; cursor:pointer"
      v-on:click="setActive('appsearchplayer')" :class="{ active: isActive('appsearchplayer') }"
      @click="selectedComponent = 'appsearchplayer'">Player</div></div>

 <div class="col-3 col-lg-3">
      <div style="margin-bottom:7px; margin-top:7px; cursor:pointer"
       v-on:click="setActive('appsearchhighlight')" :class="{ active: isActive('appsearchhighlight') }"
       @click="selectedComponent = 'appsearchhighlight'" >Highlights</div></div>

 <div class="col-3 col-lg-3">
     <div style="margin-bottom:7px; margin-top:7px; cursor:pointer"
      v-on:click="setActive('appsearchbattle')" :class="{ active: isActive('appsearchbattle') }"
     @click="selectedComponent = 'appsearchbattle'">Battle</div></div>


</div></b>
     </div>


<transition name="slide" mode="out-in">
                <component :is="selectedComponent" :search="this.search"/>
                </transition>
</div>
</template>  

<script>
import searchteams from '@/components/search/searchteam.vue';
import searchplayer from '@/components/search/searchplayer.vue';
import searchhighlight from '@/components/search/searchhighlight.vue';
import searchbattle from '@/components/search/searchbattle.vue';

export default {
  name: "search",
data() {
    return {
      search:null,
      selectedComponent: 'appsearchteam',
      activeItem: 'appsearchteam'
    }
},
components: {
            appsearchteam: searchteams,
            appsearchplayer: searchplayer,
            appsearchhighlight: searchhighlight,
            appsearchbattle: searchbattle,
},
  methods: {
     focusInput() {
      this.$refs.search.focus();
    },
    isActive: function (menuItem) {
      return this.activeItem === menuItem
    },
    setActive: function (menuItem) {
      this.activeItem = menuItem // no need for Vue.set()
    }
  },
 mounted() {
    this.focusInput();
    

  },
}
</script>


<style scoped>
.ody a{

    font-family: "Quicksand", sans-serif;
        text-decoration: none;
        


}
.ody {

    font-family: "Quicksand", sans-serif;
        text-decoration: none;
        


}

.our-team .social {
  width: 100%;
  padding: 0;
  margin: 0;
  background-color: #1369ce;
  position: absolute;
  bottom: -100px;
  left: 0;
  transition: all 0.5s ease 0s;
}

.our-team:hover .social {
  bottom: 0;
}

.our-team .social li {
  display: inline-block;
}

.our-team .social li a {
  margin: 5px;
  display: block;
  padding: 3px;
  font-size:20px;
  color: white;
  transition: all 0.3s ease 0s;
  text-decoration: none;
}

.our-team .social li a:hover {
  color: black;
}


.row1 {
  display: flex;
  flex-wrap: wrap;
  margin-right: 0px;
  margin-left: 0px;
}

input[type="submit"]:hover {
  opacity: 0.8;
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
.active{
    color: red;

}
</style>