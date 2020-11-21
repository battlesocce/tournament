<template>
<div class="ody">
    <div class="container  text-center" ><b> 
        <div class="row fixed-top"   style="-webkit-box-shadow: 0px 1px 2px 0px rgba(50, 50, 50, 0.1);
-moz-box-shadow:    0px 1px 2px 0px rgba(50, 50, 50, 0.1);
box-shadow:         0px 1px 2px 0px rgba(50, 50, 50, 0.1);background-color:white;margin-top:65px; z-index:10;"  >
               
 <div class="col-4 col-lg-4" >
     <div style="margin-bottom:10px; margin-top:15px; cursor:pointer"
      v-on:click="setActive('apphighcom')" :class="{ active: isActive('apphighcom') }"
      @click="selectedComponent = 'apphighcom'">Highlights</div></div>

 <div class="col-4 col-lg-4">
      <div style="margin-bottom:10px; margin-top:15px; cursor:pointer"
       v-on:click="setActive('appgallery_gal')" :class="{ active: isActive('appgallery_gal') }"
       @click="selectedComponent = 'appgallery_gal'" >Photos</div></div>

 <div class="col-4 col-lg-4">
     <div style="margin-bottom:10px; margin-top:15px; cursor:pointer"
      v-on:click="setActive('appmatchvideos')" :class="{ active: isActive('appmatchvideos') }"
     @click="selectedComponent = 'appmatchvideos'" >Matches</div></div>
     </div></b>
     </div> 
<br><br>
                <transition name="slide" mode="out-in">
                <component :is="selectedComponent"/>
                </transition>            
</div>
</template>

<script>

import highcom from '@/components/highcom.vue';
import gallery_gal from '@/components/gallery_gal.vue';
import matchvideos from '@/components/matchvideos.vue';

export default {
    name:"picvid",
      data: function() {
          return {
              selectedComponent: 'apphighcom',
              activeItem: 'apphighcom'
          }
        },
      props: {
    com: {
      type: String,
      required: false
    }
  },
        components: {
            apphighcom: highcom,
            appgallery_gal: gallery_gal,
            appmatchvideos: matchvideos
        },
        methods: {
    isActive: function (menuItem) {
      return this.activeItem === menuItem
    },
    setActive: function (menuItem) {
      this.activeItem = menuItem // no need for Vue.set()
    }
  },
  created(){
     if(this.$route.params.com){
         this.selectedComponent = this.$route.params.com;
         this.activeItem = this.$route.params.com;}
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


</style>