<template>
  <div class="single-answer">
    <p class="text-muted">
      <strong>{{ answer.author }}</strong> &#8901; {{ answer.created_at }}
    </p>
    <p>{{ answer.body }}</p>
    <div v-if="isAnswerAuthor">
      <router-link
        :to="{ name: 'answer-editor', params: { id: answer.id } }"
        class="btn btn-sm btn-outline-secondary mr-1"
        >Edit
      </router-link>
      <button
        class="btn btn-sm btn-outline-danger"
        @click="triggerDeleteAnswer"
        >Delete
      </button>
    </div>
    <div v-else>      
<p
            class="fa fa-heart ml-2" 
            style="font-size:18px;"
            @click="toggleLike"
            :class="{
              'fa fa-heart': userLikedAnswer,
              'fa fa-heart-o': !userLikedAnswer
              }"
            ></p><strong>&nbsp;{{ likesCounter }}</strong>
    </div>
    <hr>
  </div>
</template>

<script>
import Swal from 'sweetalert2'
import { apiService } from "@/common/api.service.js";
export default {
  name: "AnswerComponent",
  props: {
    answer: {
      type: Object,
      required: true
    },

    requestUser: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      userLikedAnswer: this.answer.user_has_voted,
      likesCounter: this.answer.likes_count
    }
  },
  computed: {
    isAnswerAuthor() {
      // return true if the logged in user is also the author of the answer instance
      return this.answer.author === this.requestUser;
    }
  },
  methods: {
    test(){
      if (!this.requestUser) {
 Swal.fire({
  position: 'top-end',
  showConfirmButton: false,
  html:'Are you vistor?<a href="accounts/google/login/" class="btn btn-light btn-block"><i class="fa fa-google mr-2" aria-hidden="true" ></i>Login with Google</a>Or<br>Want a Team?<a href="/register/" class="btn btn-light  btn-block"><i class="fa fa-plus mr-2" aria-hidden="true" ></i>Create a Team</a>'
})
          }
    },
    toggleLike() {
      if (!this.requestUser) {
        this.test()}
        else{
      this.userLikedAnswer === false
        ? this.likeAnswer()
        : this.unLikeAnswer()
        }
    },
    likeAnswer() {
      this.userLikedAnswer = true;
      this.likesCounter += 1;
      let endpoint = `/api/answers/${ this.answer.id }/like/`;
      apiService(endpoint, "POST")
    },
    unLikeAnswer() {
      this.userLikedAnswer = false;
      this.likesCounter -= 1;
      let endpoint = `/api/answers/${ this.answer.id }/like/`;
      apiService(endpoint, "DELETE")
    },
    triggerDeleteAnswer() {
      // emit an event to delete an answer instance
      this.$emit("delete-answer", this.answer)
    }
  }
}
</script>
<style scoped>
.fa-heart-o {
  color:red;
  cursor: pointer;
}

.fa-heart {
  color: red;
  cursor: pointer;
}  
</style>

