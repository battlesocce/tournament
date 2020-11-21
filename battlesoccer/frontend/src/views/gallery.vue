<template>
<body>
 <br><br><br>
 <div class="container">
    <h1 class="display-4">Gallery</h1>   
 </div>
    <br>
 <highlightvideo class="videocover" v-for = "video in team.videos"
        :video="video"
        :requestUser="requestUser"
        :key="video.pk"/>


</body>
</template>

<script>
import highlightvideo from "@/components/highlightvideo.vue";

import { apiService } from "@/common/api.service.js";
export default{
  name: "gallery",
    components: {
highlightvideo
  },
  data() {
    return {
      team: {},
      requestUser:null,
    }
  },
  methods: {
         setRequestUser() {
      // the username has been set to localStorage by the App.vue component
      this.requestUser = window.localStorage.getItem("username");
    },
      getgallery() {
      let endpoint = `/api/team/${this.id}/`;
      apiService(endpoint)
        .then(data => {
          if (data) {
            this.team = data;
          } else {
            this.team = null;
            this.setPageTitle("404 - Page Not Found")
          }
        })
    }
   },
 created() {
    this.id = this.$route.params.id;
    this.getgallery(),
    this.setRequestUser()
    },
}
</script>
<style scoped>
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
    width:100%;
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
