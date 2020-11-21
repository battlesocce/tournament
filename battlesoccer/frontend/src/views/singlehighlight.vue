<template>
<div class=ody v-if="video.own">
<br><br><br><br>
<div class="row">
<div class="col-12 col-lg-4 offset-lg-4">
  <div class="main main-raised">
<hr style="width:0%; margin-bottom:3px;">
<h2 class="text-center">{{video.own.teamname}}</h2>
<div class="embed-responsive embed-responsive-1by1 mb-3 ">
  <iframe class="embed-responsive-item" :src="video.highlight"
   allow="accelerometer; autoplay;loop;mute;encrypted-media; gyroscope; picture-in-picture" allowfullscreen
   ></iframe>
</div>
<a class="ml-2" :href="'whatsapp://send?text=https://www.battlesoccer.in/singlehighlight/' + this.video.id + '/' " data-action="share/whatsapp/share"><img src="https://www.iconfinder.com/data/icons/internet-2020/1080/whatsappicon-512.png" style="margin-top:-10px;" width="35px"></a>
<p
            class="fa fa-heart ml-2" 
            style="font-size:25px;"
            @click="toggleLike"
            :class="{
              'fa fa-heart': userLikedAnswer,
              'fa fa-heart-o': !userLikedAnswer
              }"
            ></p><strong>&nbsp;{{ likesCounter }}</strong>
</div>
</div>
</div>
<div class="row">
<div class="col-12 col-lg-4 offset-lg-4">
<form  @submit.prevent="onSubmit">
<div class="form__group field ">
<input type="input" class="form-control"  placeholder="comment" v-model="newAnswerBody" required />
<center><button type="submit" class="btn btn-sm btn-dark">Submit</button></center></div>
</form>
<br>
    <div class="container">
      <AnswerComponent 
        v-for="answer in answers"
        :answer="answer"
        :requestUser="requestUser"
        :key="answer.id"
        @delete-answer="deleteAnswer"
      /></div></div></div>

          <div class="my-4 container text-center">
      <h2 v-show="loadingAnswers"><div class="lds-ripple"><div></div><div></div></div></h2>
      </div>

    </div>

</template>

<script>
import { apiService } from "@/common/api.service.js";
import AnswerComponent from "@/components/Answer.vue";
import Swal from 'sweetalert2'
export default {
  name: "singlehighlight",
   props: {
    id: {
      type: Number,
      required: true
      
    }
   },
  data() {
    return {
        requestUser :null,
        video:{},
        answers: [],
        next: null,
        loadingAnswers: false,
        newAnswerBody: null, 
        showForm: false,
        userLikedAnswer: null,
        likesCounter: null
        
    }
  },
  components: {
    AnswerComponent,
  },
      mounted () {
this.scroll()
  },
  methods: {
    test(){
      if (!this.requestUser) {
 Swal.fire({
  position: 'top-end',
  showConfirmButton: false,
  html:'Are you new to our WebApp?<a href="accounts/google/login/" class="btn btn-light btn-block"><i class="fa fa-google mr-2" aria-hidden="true" ></i>Login with Google</a>Or<br>Want a Team?<a href="/register/" class="btn btn-light  btn-block"><i class="fa fa-plus mr-2" aria-hidden="true" ></i>Create a Team</a>'
})
          }
    },
    scroll () {
      window.onscroll = () => {
        let bottomOfWindow = Math.max(window.pageYOffset, document.documentElement.scrollTop, document.body.scrollTop) + window.innerHeight === document.documentElement.offsetHeight

        if (bottomOfWindow) {
          if (this.next) { 
         this.gethighlightAnswers();// replace it with your code
        }
        }
      }
    },
    setRequestUser() {
      // the username has been set to localStorage by the App.vue component
      this.requestUser = window.localStorage.getItem("username");
    },
    gethighlight() {
      // get the details of a question instance from the REST API and call setPageTitle
      let endpoint = `/api/highlights/${this.id}/`;
      apiService(endpoint)
        .then(data => {
          if (data) {
            this.video = data[0];
            this.userLikedAnswer = this.video.user_has_voted,
            this.likesCounter = this.video.likes_count
          } else {
            this.video = null;
            this.setPageTitle("404 - Page Not Found")
          }

        })
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
  
    gethighlightAnswers() {
      // get a page of answers for a single question from the REST API's paginated 'Questions Endpoint'
      let endpoint = `/api/highlights/${this.id}/answers/`;
      if (this.next) {
        endpoint = this.next;
      }
      this.loadingAnswers = true;
      apiService(endpoint)
        .then(data => {
          this.answers.push(...data.results);
          this.loadingAnswers = false;
          if (data.next) {
            this.next = data.next;
          } else {
            this.next = null;
          }
        })
    },
    onSubmit() {
       if (!this.requestUser) {
         this.test()}
         else{
      // Tell the REST API to create a new answer for this question based on the user input, then update some data properties
      if (this.newAnswerBody) {
        let endpoint = `/api/highlights/${this.id}/answer/`;
        apiService(endpoint, "POST", { body: this.newAnswerBody })
          .then(data => {
            this.answers.unshift(data)
          })
        this.newAnswerBody = null;
        if (this.error) {
          this.error = null;
        }
      } else {
        this.error = "You can't send an empty answer!";
      }}
    },
    async deleteAnswer(answer) {
      // delete a given answer from the answers array and make a delete request to the REST API
      let endpoint = `/api/answers/${answer.id}/`;
      try {
        await apiService(endpoint, "DELETE")
        this.$delete(this.answers, this.answers.indexOf(answer))
      }
      catch (err) {
        console.log(err)
      }
    }
  },
  created() {
    this.gethighlight()
    this.gethighlightAnswers()
    this.setRequestUser()
    this.id = this.$route.params.id;
    
  }
}
</script>

<style scoped>
.author-name {
  font-weight: bold;
  color: #DC3545;
}

.answer-added {
  font-weight: bold;
  color: green;
}

.error {
  font-weight: bold;
  color: red; 
}
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
.fa-heart-o {
  color:red;
  cursor: pointer;

}

.fa-heart {
  color: red;
  cursor: pointer;
}  


iframe{
width:100%;
height:auto;
margin:auto;
font-size:35px;
}


@media only screen and (max-width:950px) {
   .videocover {
    width:100%;
  }
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
            font-size:35px;

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

.form__group {
	 position: relative;
	 padding: 15px 0 0;
	 margin-top: 10px;
	 width: 100%;
}
 .form__field {
	 font-family: inherit;
	 width: 100%;
	 border: 0;
	 border-bottom: 2px solid #9b9b9b;
	 outline: 0;
	 font-size: 1.3rem;
	 color: black;
	 padding: 7px 0;
	 background: transparent;
	 transition: border-color 0.2s;
}
 .form__field::placeholder {
	 color: transparent;
}
 .form__field:placeholder-shown ~ .form__label {
	 font-size: 1.3rem;
	 cursor: text;
	 top: 20px;
}
 .form__label {
	 position: absolute;
	 top: 0;
	 display: block;
	 transition: 0.2s;
	 font-size: 1rem;
	 color: #9b9b9b;
}
 .form__field:focus {
	 padding-bottom: 6px;
	 font-weight: 700;
	 border-width: 3px;
	 border-image: linear-gradient(to right, #11998e, #38ef7d);
	 border-image-slice: 1;
}
 .form__field:focus ~ .form__label {
	 position: absolute;
	 top: 0;
	 display: block;
	 transition: 0.2s;
	 font-size: 1rem;
	 color: #11998e;
	 font-weight: 700;
}
/* reset input */
 .form__field:required, .form__field:invalid {
	 box-shadow: none;
}
.main-raised {
  display:block;
    margin: 20px 10px 0;
    border-radius: 8px;
-webkit-box-shadow: 0px 0px 8px 0px rgba(0,0,0,0.2);
-moz-box-shadow: 0px 0px 8px 0px rgba(0,0,0,0.2);
box-shadow: 0px 0px 8px 0px rgba(0,0,0,0.2);}


</style>
