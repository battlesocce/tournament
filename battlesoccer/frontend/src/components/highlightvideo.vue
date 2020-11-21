<template>
  <div class="ody">
    <div class="main main-raised">
      <hr style="width:0%; margin-bottom:3px;">    <router-link
        :to="{ name: 'Teamveiw', params: { id: video.own.id} }"
        >  
      <h2 class="text-center">{{video.own.teamname|capitalize}}</h2></router-link>
              <div class="embed-responsive embed-responsive-1by1 mb-3">
  <iframe class="embed-responsive-item" :src="video.highlight"
   allow="accelerometer; autoplay;loop;mute;encrypted-media; gyroscope; picture-in-picture" allowfullscreen
   ></iframe>
      </div>
    <router-link class="ml-2"
        :to="{ name: 'singlehighlight', params: { id: video.id} }"
        ><img src="https://static.thenounproject.com/png/638755-200.png" width="40px" style="margin-top:-10px;"></router-link>
<a :href="'whatsapp://send?text=https://www.battlesoccer.in/singlehighlight/' + this.video.id + '/' " data-action="share/whatsapp/share"><img src="https://www.iconfinder.com/data/icons/internet-2020/1080/whatsappicon-512.png" width="35px" style="margin-top:-10px;"></a>
            <p
            class="fa fa-heart ml-2" 
            style="font-size:25px;"
            @click="toggleLike"
            :class="{
              'fa fa-heart': userLikedAnswer,
              'fa fa-heart-o': !userLikedAnswer
              }"
            ></p><strong>&nbsp;{{ likesCounter }}</strong>
       <router-link
        :to="{ name: 'Teamveiw', params: { id: video.own.id} }"
        ></router-link>
    </div>
    <br>
  </div>
</template>

<script>
import Swal from 'sweetalert2'
import { apiService } from "@/common/api.service.js";
export default {
  name: "highlightvideo",
  props: {
    video: {
      type: Object,
      required: true
    },
     requestUser: {
      type: String,
      required: true
    },
  },
  data() {
    return {
      userLikedAnswer: this.video.user_has_voted,
      likesCounter: this.video.likes_count
    }
  },
  methods: {
     test(){
      if (!this.requestUser) {
 Swal.fire({
  position: 'top-end',
  showConfirmButton: false,
  html:'Are you a spectator?<a href="accounts/google/login/" class="btn btn-light btn-block"><i class="fa fa-google mr-2" aria-hidden="true" ></i>Login with Google</a>Or<br>Want a Team?<a href="/register/" class="btn btn-light  btn-block"><i class="fa fa-plus mr-2" aria-hidden="true" ></i>Create a Team</a>'
})
          }
    },
    toggleLike() {
      if (!this.requestUser) {
        this.test()
      }
      else{
      this.userLikedAnswer === false
        ? this.likeAnswer()
        : this.unLikeAnswer()}
    },
    likeAnswer() {
      this.userLikedAnswer = true;
      this.likesCounter += 1;
      let endpoint = `/api/highlights/${ this.video.id }/like/`;
      apiService(endpoint, "POST")
    },
    unLikeAnswer() {
      this.userLikedAnswer = false;
      this.likesCounter -= 1;
      let endpoint = `/api/highlights/${ this.video.id }/like/`;
      apiService(endpoint, "DELETE")
    },
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

.fa-heart-o {
  color:red;
  cursor: pointer;

}

.fa-heart {
  color: red;
  cursor: pointer;
}  

@media only screen and (max-width:950px) {
   .videocover {
    width:100%;
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
            font-size:25px;
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