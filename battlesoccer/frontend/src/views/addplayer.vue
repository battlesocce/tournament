<template>
  <div class="ody">
    <br><br><br><br>
    <div class="container-sm">
      <div v-if="!id">
    <h1 >Add player</h1></div>
    <div v-if="id">
    <h1 >Update player</h1></div>
    <br>
  <transition name="fade">
    <div class="alert alert-danger" role="alert" v-if="error">
{{ error }}
</div></transition>
<div v-if="!id">
<transition name="fade">
<div class="alert alert-success" role="alert"  v-if="savingSuccessful" >
  Player added successfully
</div>
</transition></div>
<div v-if="id">
<transition name="fade">
<div class="alert alert-success" role="alert"  v-if="savingSuccessful" >
 updated successfully
</div>
</transition></div>
    <form @submit.prevent="onSubmit">


<div class="form-group input" :class="{invalid: $v.player.$error}">
<label for="usr">Name:</label>
<input type="text"  @input="$v.player.$touch()"
v-model='player'  class="form-control" id="usr" >
<p v-if="!$v.player.required">This field must not be empty.</p>
</div>


<div class="form-group input" :class="{invalid: $v.age.$error}">
<label for="usr">Age:</label>
<input type="text"  @input="$v.age.$touch()"
v-model='age' class="form-control" id="usr">
<p v-if="!$v.age.minVal">You have to be at least {{ $v.age.$params.minVal.min }} years old.</p>
<p v-if="!$v.age.required">This field must not be empty.</p>
</div>


  <div class="form-group input" :class="{invalid: $v.contact.$error}">
  <label for="usr">Contact:</label>
  <input type="text" @input="$v.contact.$touch()" 
   v-model='contact' class="form-control" id="usr">
  <p v-if="!$v.contact.minLen">Invalid contact number</p>
  </div>



  <div class="form-group input" :class="{invalid: $v.profession.$error}">
  <label for="usr">profession:</label>
  <input type="text" @input="$v.profession.$touch()"
   v-model='profession' class="form-control" id="usr">
  <p v-if="!$v.profession.maxLen">Make it crisp</p>
  </div>


  <div class="form-group input" :class="{invalid: $v.instaurl.$error}">
  <label for="usr">Insta_Id:</label>
  <input type="text" @input="$v.instaurl.$touch()"
   v-model='instaurl' class="form-control" id="usr">
  <p v-if="!$v.instaurl.maxLen">Make it crisp</p>
  </div>


<div class="form-group input" :class="{invalid: $v.facebookurl.$error}">
<label for="usr">Facebook_Id:</label>
<input type="text" @input="$v.facebookurl.$touch()"
v-model='facebookurl' class="form-control" id="usr">
<p v-if="!$v.facebookurl.maxLen">Make it crisp</p>
</div>


<div class="form-group input" :class="{invalid: $v.position.$error}">
<label for="usr">Position:</label>
<input type="text" @input="$v.position.$touch()"
v-model='position' class="form-control" id="usr">
<p v-if="!$v.position.maxLen">Make it crisp</p>
</div>


<div class="form-group input" :class="{invalid: $v.description.$error}">
<label for="usr">Description:</label>
<input type="text" @input="$v.description.$touch()"
v-model='description' class="form-control" id="usr">
<p v-if="!$v.description.maxLen">Make it crisp</p>
</div>


      <br>
<button type="submit" :disabled="$v.$invalid" class="btn btn-dark">Add</button>

    </form>
  </div>
  </div>
</template>

<script>
import { required, numeric, minValue,maxLength,minLength} from 'vuelidate/lib/validators'
import { apiService } from "@/common/api.service.js";
export default {
  name: "Addplayer",
  props: {
    id: {
      type: Number,
      required: false
    }
  },
  data() {
    return {
      player: null,
      age: null,
      playerpasscode: null,
      contact: null,
      profession: null,
      facebookurl: null,
      instaurl: null,
      position: null,
      description: null,
      error: null,
      savingSuccessful: false,
      display:null
    }
  },
    validations: {

    player: {
        required,
        maxLen: maxLength(15)
      }, 
    age: {
        required,
        numeric,
        minVal: minValue(16),
        maxLen: maxLength(2)
      },  
    contact: {
        numeric,
        minLen: minLength(10),
        maxLen: maxLength(10)
        
      },
  profession: {
     maxLen: maxLength(35)
  }, 
  instaurl: { 
       maxLen: maxLength(15) 
       }, 
   facebookurl: {
    maxLen: maxLength(15)
  },
  position: {
    maxLen: maxLength(15)
  },  
  description: {
    maxLen: maxLength(255)
  },  
    },
  methods: {
    onSubmit() {
      if(this.id)
      {
        this.display="player update successful"
      }
      if(!this.id)
      {
        this.display="player added successful"
      }
      // Tell the REST API to create or update a Question Instance
      if (!this.player) {
        this.error = "You can't send an empty question!";
     this.savingSuccessful= false;
      } else if (this.player.length > 240) {
       this.savingSuccessful= false;
        this.error = "Ensure this field has no more than 240 characters!";
      } else {
        let endpoint = "/api/player/";
        let method = "POST";
        if (this.id !== undefined) {
          endpoint += `${ this.id }/`;
          method = "PUT";
        }
        apiService(endpoint, method, { player: this.player, 
                                        age: this.age,
                                        playerpasscode: this.playerpasscode,
                                        contact: this.contact,
                                        profession:this.profession,
                                        facebookurl: this.facebookurl,
                                        instaurl: this.instaurl,
                                        position: this.position,
                                        description: this.description,
                                        })
                                       .then(response => {
  console.log('SUCCESS!!');
      this.player= "";
      this.age= "";
      this.playerpasscode= "";
      this.contact= "";
      this.profession= "";
      this.facebookurl= "";
      this.instaurl= "";
      this.position= "";
      this.description= "";
      this.error="";
      this.savingSuccessful= true;
    this.$router.push({
              name: 'Userprofile',
              params: { message:this.display }
            })        
        return response
        

})
      

      }
    }
  },
  async beforeRouteEnter(to, from, next) {
    // if the component will be used to update a question, then get the question's data from the REST API
    if (to.params.id !== undefined) {
      let endpoint = `/api/player/${ to.params.id }/`;
      let data = await apiService(endpoint);
      return next(vm => (vm.player = data.player, 
                         vm.age = data.age,
                         vm.playerpasscode = data.playerpasscode,
                         vm.contact = data.contact,
                         vm.profession = data.profession,
                         vm.facebookurl = data.facebookurl,
                         vm.instaurl = data.instaurl,
                         vm.position = data.position,
                         vm.description = data.description))
                         
} else {
      return next();
    }
  },
}
</script>
<style scoped>

  .input {
    margin: 10px auto;
  }

  .input label {
    display: block;
    color: #4e4e4e;
    margin-bottom: 6px;
  }

  .input.inline label {
    display: inline;
  }

  .input input {
    font: inherit;
    width: 100%;
    padding: 6px 12px;
    box-sizing: border-box;
    border: 1px solid #ccc;
  }

  .input.inline input {
    width: auto;
  }

  .input input:focus {
    outline: none;
    border: 1px solid #521751;
    background-color: #eee;
  }

  .input.invalid label {
    color: red;
  }

  .input.invalid input {
    border: 1px solid red;
    background-color: white;
  }

  .input select {
    border: 1px solid #ccc;
    font: inherit;
  }

 .submit button {
    border: 1px solid #521751;
    color: #521751;
    padding: 10px 20px;
    font: inherit;
    cursor: pointer;
  }

  .submit button:hover,
  .submit button:active {
    background-color: #521751;
    color: white;
  }

  .submit button[disabled],
  .submit button[disabled]:hover,
  .submit button[disabled]:active {
    border: 1px solid #ccc;
    background-color: transparent;
    color: #ccc;
    cursor: not-allowed;}
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