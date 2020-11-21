<template>
<b-col cols="6" sm="6" md="3" lg="3" style="padding:5px"  >
 <div class="shadow bg-white rounded">
 <div data-aos="zoom-in-down">
  <div class="our-team">
    <router-link
        :to="{ name: 'playerpage', params: {id:parseInt(player.id )} }"
        >
    <div class="picture">
      <img :src="player.pic + '?'+ new Date().getTime()">
    </div></router-link>
    <div class="team-content">
      <h4 class="name">{{player.player| capitalize}}</h4>
      <h5 class="tit">{{player.age| capitalize}}</h5>
      
  <div v-if="isUser">
<table>
    <tr>
            <td><p
            class="fa fa-heart" 
            style="font-size:20px;"
            @click="toggleLike"
            :class="{
              'fa fa-heart': userLikedPlayer,
              'fa fa-heart-o': !userLikedPlayer
              }"
            ></p><strong>&nbsp;{{ likesCounter }}</strong>
            </td>

            <td><p @click="triggerDeleteplayer" class="fa fa-trash"  style="font-size:25px;cursor:pointer;"></p>
           </td>
          
         </tr>
</table>
     </div> 
     </div>
             <ul class="social">
            <li><a v-bind:href="'https://www.facebook.com/' + player.facebookurl + '/'"  aria-hidden="true"><i class="fa fa-facebook"></i></a></li>
            <li><a v-bind:href="'https://www.instagram.com/' + player.instaurl + '/'" aria-hidden="true"><i class="fa fa-instagram"></i></a></li>
                    </ul>
</div>
 </div> 
 </div>
</b-col>
</template>

<script>
import Swal from 'sweetalert2'
import { apiService } from "@/common/api.service.js";
export default {
  name: "Player",
  props: {
    player: {
      type: Object,
      required: true
    },
    requestUser: {
      type: String,
      required: true
    },
    user: {
      type: String,
      required: true
    }
  },
  computed: {
    isUser() {
      // return true if the logged in user is also the author of the answer instance
      return this.user === this.requestUser;
    }
  },
    data() {
    return {
      userLikedPlayer: this.player.user_has_voted,
      likesCounter: this.player.likes_count,
      pic: null,
      error: null,
      ran:null
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
      }else{
      this.userLikedPlayer=== false
        ? this.likePlayer()
        : this.unLikePlayer()}
    },
    likePlayer() {
      this.userLikedPlayer = true;
      this.likesCounter += 1;
      let endpoint = `/api/playerlike/${ this.player.id }/like/`;
      apiService(endpoint, "POST")
    },
    unLikePlayer() {
      this.userLikedPlayer = false;
      this.likesCounter -= 1;
      let endpoint = `/api/playerlike/${ this.player.id }/like/`;
      apiService(endpoint, "DELETE")
    },
    triggerDeleteplayer() {
      // emit an event to delete an answer instance
      this.$emit("delete-player", this.player)
    },
  onchange(event){
  this.pic=event.target.files[0]
  this.$emit("update-pic", this.player,this.pic)
  event.target.value = '';

      // Tell the REST API to create or update a Question Instance
   }
  }     
}
</script>


<style scoped>

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


.fa-heart-o {
  color:red;
  cursor: pointer;
}

.fa-heart {
  color: red;
  cursor: pointer;
}

.upload-btn-wrapper {
  position: relative;
  overflow: hidden;
  display: inline-block;
}



.upload-btn-wrapper input[type=file] {
  font-size: 100px;
  position: absolute;
  left: 0;
  top: 0;
  opacity: 0;
}

.router-link {
  color: inherit;
}
table {
  border-collapse: collapse;
  border-spacing: 0;
  width: 100%;
  border: 0px solid #ddd;
}
th, td {
  text-align: center;
  padding: 10px;
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