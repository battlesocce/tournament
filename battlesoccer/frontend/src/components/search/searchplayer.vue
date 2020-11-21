<template>
<div class="ody">
  <br><br><br><br>
<div class="container-lg">
      <transition-group name=slide class="row" >
<div class="col-6 col-lg-3" style="padding:5px;" v-for="p in filteredListplayer" :key ="p.id"><div data-aos="zoom-in-down">
                  <div class="shadow  bg-white rounded">
  <div class="our-team"> <router-link
        :to="{ name: 'playerpage', params: { id: p.id } }"
        >
    <div class="picture">
      <img :src="p.pic + '?'+ new Date().getTime()">
    </div>
    <div class="team-content">
      <h4 class="name">{{p.player| capitalize}}</h4>
     </div> <br></router-link>
              <ul class="social">
            <li><a v-bind:href="'https://www.facebook.com/' + p.facebookurl + '/'"  aria-hidden="true"><i class="fa fa-facebook"></i></a></li>
            <li><a v-bind:href="'https://www.instagram.com/' + p.instaurl + '/'" aria-hidden="true"><i class="fa fa-instagram"></i></a></li>
                    </ul>
</div>
</div></div></div>
      </transition-group
      ></div>
<div class="my-4 container text-center">
      <h2 v-show="loadingplayer"><div class="lds-ripple"><div></div><div></div></div></h2>
      </div>
</div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
export default {
  name: "searchplayer",
data() {
    return {
      
      teamsearch: [],
      player:[],
      show:null,
      next: null,
      next1: null,
      loadingplayer: false,
      loadingteamsearch: false
    }
},
props: {
    search: {
      type: String,
    }},
 computed: {
    filteredList() {
       if (!this.search) {
      return this.teamsearch;
       }
       else{
      return this.teamsearch.filter(teams => {
        return teams.teamname.toLowerCase().match(this.search.toLowerCase())
      })
       }
},
    filteredListplayer() {
             if (!this.search) {
      return this.player;
       }
       else{
      return this.player.filter(players => {
        return players.player.toLowerCase().match(this.search.toLowerCase())
      })
    }}
  },
  mounted () {
this.scroll()
  },
     methods: {
        scroll () {
      window.onscroll = () => {
        let bottomOfWindow = Math.max(window.pageYOffset, document.documentElement.scrollTop, document.body.scrollTop) + window.innerHeight === document.documentElement.offsetHeight

        if (bottomOfWindow) {
          if (this.next1) { 
         this.getplayerData();// replace it with your code
        }
        }
      }
    },
      
getTeamData() {
      // get the details of a question instance from the REST API and call setPageTitle
      let endpoint = `/api/team/`;
      if (this.next) {
        endpoint = this.next;
      }
      this.loadingteamsearch = true;
      setTimeout(() => {
      apiService(endpoint)
 .then(data => {
          this.teamsearch.push(...data.results);
          this.loadingteamsearch = false;
          if (data.next) {
            this.next = data.next;
          } else {
            this.next = null;
          }}, 2000)
        })
    },
      getplayerData() {
      // get the details of a question instance from the REST API and call setPageTitle
      let endpoint = `/api/player/`;
        if (this.next1) {
        endpoint = this.next1;
      }
      this.loadingplayer = true;
      setTimeout(() => {
      apiService(endpoint)
 .then(data => {
          this.player.push(...data.results);
          this.loadingplayer = false;
          if (data.next) {
            this.next1 = data.next;
          } else {
            this.next1 = null;
          }}, 2000)
        })
    },
     },
  created() {
    this.getplayerData()

    },

}
</script>


<style scoped>
@import '../../assets/css/userprofile.css';

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

#wrap {
  margin: 15px 15px;
  display: inline-block;
  position: relative;
  height: 60px;
  float: right;
  padding: 0;
  position: relative;
}


input[type="text"] {
  height: 60px;
  font-size: 35px;
  display: inline-block;
  font-weight: 100;
  border: none;
  outline: none;
  color: #555;
  padding: 30px;
  padding-right: 5px;
  position: absolute;
  top: 0;
  right: 0;
  background: none;
  z-index: 1;
  transition: width 0.4s cubic-bezier(0, 0.795, 0, 1);
  cursor: pointer;
  width:550px;
  z-index: 0;
  border-bottom: 1px solid #bbb;
  cursor: text;
}



@media only screen and (max-width:550px) {

   input[type="text"] {
     font-size: 18px;
      width:320px;
     padding-right:3px;
  }

  .close {
  margin-left:10px;
}
}

input[type="submit"] {
  height: 47px;
  width: 43px;
  display: inline-block;
  color: red;
  float: right;
  background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAMAAABg3Am1AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAADNQTFRFU1NT9fX1lJSUXl5e1dXVfn5+c3Nz6urqv7+/tLS0iYmJqampn5+fysrK39/faWlp////Vi4ZywAAABF0Uk5T/////////////////////wAlrZliAAABLklEQVR42rSWWRbDIAhFHeOUtN3/ags1zaA4cHrKZ8JFRHwoXkwTvwGP1Qo0bYObAPwiLmbNAHBWFBZlD9j0JxflDViIObNHG/Do8PRHTJk0TezAhv7qloK0JJEBh+F8+U/hopIELOWfiZUCDOZD1RADOQKA75oq4cvVkcT+OdHnqqpQCITWAjnWVgGQUWz12lJuGwGoaWgBKzRVBcCypgUkOAoWgBX/L0CmxN40u6xwcIJ1cOzWYDffp3axsQOyvdkXiH9FKRFwPRHYZUaXMgPLeiW7QhbDRciyLXJaKheCuLbiVoqx1DVRyH26yb0hsuoOFEPsoz+BVE0MRlZNjGZcRQyHYkmMp2hBTIzdkzCTc/pLqOnBrk7/yZdAOq/q5NPBH1f7x7fGP4C3AAMAQrhzX9zhcGsAAAAASUVORK5CYII=)
  center center no-repeat;
  text-indent: -10000px;
  border: none;
  position: absolute;
  top: 0;
  right: 0;
  z-index: 0;
  cursor: pointer;
  opacity: 0.4;
  cursor: pointer;
  transition: opacity 0.4s ease;

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
            font-size:17px;
        }
h5{
            font-size:20px;

        }
}
</style>