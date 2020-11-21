<template>
  <div class="container">
    <br><br><br><br><br>
    <form @submit.prevent="onSubmit">
      <textarea 
        v-model="answerBody" 
        class="form-control" 
        rows="3"
      ></textarea>
      <br>
      <button 
        type="submit" 
        class="btn btn-light"
        >submit
      </button>
    </form>
    <p v-if="error" class="muted mt-2">{{ error }}</p>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
export default {
  name: "AnswerEditor",
  props: {
    id: {
      type: Number,
      required: true
    }
  },
  data() {
    return {
      highlight_id: null,
      answerBody: null,
      error: null
    }
  },
  methods: {
    onSubmit() {
      if (this.answerBody) {
        let endpoint = `/api/answers/${this.id}/`;
        apiService(endpoint, "PUT", { body: this.answerBody })
          .then(() => {
            this.$router.push({
              name: "singlehighlight",
              params: { id: this.highlight_id }
            })
          })
      } else {
        this.error = "You can't submit an empty answer!";
      }
    }
  },
  async beforeRouteEnter(to, from, next) {
    // get the answer's data from the REST API and set two data properties for the component
    let endpoint = `/api/answers/${to.params.id}/`;
    let data = await apiService(endpoint);
    return next(vm => (
      vm.answerBody = data.body,
      vm.highlight_id = data.highlight_id
    ));
  }
};
</script>
