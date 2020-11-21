<template>
  <div class="Teamedit">
    <br><br><br><br>
    <div class="container">
    <h1 class="display-4">Team edit</h1>   
     <form @submit.prevent="onSubmit">
<br>
<div class="form-group input" :class="{invalid: $v.teamname.$error}">
  <label for="usr">Team_name:</label>
  <input type="text" @input="$v.teamname.$touch()"
   v-model='teamname' class="form-control" id="usr">
    <p v-if="!$v.teamname.maxLen">Make it crisp</p> 
<p v-if="!$v.teamname.required">This field must not be empty.</p>
</div>

<div class="form-group input" :class="{invalid: $v.teamquotes.$error}">
  <label for="usr">Team_quotes:</label>
  <input type="text" @input="$v.teamquotes.$touch()"
   v-model='teamquotes' class="form-control" id="usr">
    <p v-if="!$v.teamquotes.maxLen">Invaild Contact</p>
</div>

<div class="form-group input" :class="{invalid: $v.teamcontact.$error}">
  <label for="usr">Team_contact:</label>
  <input type="text" @input="$v.teamcontact.$touch()" 
    v-model='teamcontact' class="form-control" id="usr">
  <p v-if="!$v.teamcontact.maxLen">Invaild Contact</p>
<p v-if="!$v.teamcontact.required">This field must not be empty.</p>
</div>
<div class="form-group input">
<label for="cars">Choose your city:</label>
<select  v-model='teamcity'  class="form-control" required>
  <option class="form-control" value="madurai">madurai</option>
  <option class="form-control" value="Chennai">Chennai</option>
  <option class="form-control" value="Dindigul">Dindigul</option>
<option class="form-control" value="Ariyalur">Ariyalur</option>
<option class="form-control" value="Chengalpattu">Chengalpattu</option>
<option class="form-control" value="Chennai">Chennai</option>
<option class="form-control" value="Coimbatore">Coimbatore</option>
<option class="form-control" value="Cuddalore">Cuddalore</option>
<option class="form-control" value="Dharmapuri">Dharmapuri</option>
<option class="form-control" value="Dindigul">Dindigul</option>
<option class="form-control" value="Erode">Erode</option>
<option class="form-control" value="Kallakurichi">Kallakurichi</option>
<option class="form-control" value="Kanchipuram">Kanchipuram</option>
<option class="form-control" value="Kanniyakumari">Kanniyakumari</option>
<option class="form-control" value="Karur">Karur</option>
<option class="form-control" value="Krishnagiri">Krishnagiri</option>
<option class="form-control" value="Madurai">Madurai</option>
<option class="form-control" value="Mayiladuthurai">Mayiladuthurai</option>
<option class="form-control" value="Nagapattinam">Nagapattinam</option>
<option class="form-control" value="Namakkal">Namakkal</option>
<option class="form-control" value="Nilgiris">Nilgiris</option>
<option class="form-control" value="Perambalur">Perambalur</option>
<option class="form-control" value="Pudukkottai">Pudukkottai</option>
<option class="form-control" value="Ramanathapuram">Ramanathapuram</option>
<option class="form-control" value="Ranipet">Ranipet</option>
<option class="form-control" value="Salem">Salem</option>
<option class="form-control" value="Sivagangai">Sivagangai</option>
<option class="form-control" value="Tenkasi">Tenkasi</option>
<option class="form-control" value="Thanjavur">Thanjavur</option>
<option class="form-control" value="Theni">Theni</option>
<option class="form-control" value="Thoothukudi">Thoothukudi</option>
<option class="form-control" value="Tiruchirappalli">Tiruchirappalli</option>
<option class="form-control" value="Tirunelveli">Tirunelveli</option>
<option class="form-control" value="Tirupattur">Tirupattur</option>
<option class="form-control" value="Tiruppur">Tiruppur</option>
<option class="form-control" value="Tiruvallur">Tiruvallur</option>
<option class="form-control" value="Tiruvannamalai">Tiruvannamalai</option>
<option class="form-control" value="Tiruvarur">Tiruvarur</option>
<option class="form-control" value="Vellore">Vellore</option>
<option class="form-control" value="Viluppuram">Viluppuram</option>
<option class="form-control" value="Virudhunagar">Virudhunagar</option>


</select>
</div>
      <br>
<button type="submit" :disabled="$v.$invalid" class="btn btn-dark">Sumbit</button>

    </form>
    <p v-if="error" class="muted mt-2">{{ error }}</p>
  </div>
  </div>
</template>
<script>
import { required, numeric,maxLength,minLength} from 'vuelidate/lib/validators'
import { apiService } from "@/common/api.service.js";
export default {
  name: "Teamedit",
  props: {
    id: {
      type: [Number,String],
      required: false
    }
  },
  data() {
    return {
      teamname: null,
      teamquotes:null,
      teamcontact:null,
      teamcity:null,
      error: null
    }
  },
validations: {
  teamname: {
        required,
        maxLen: maxLength(15)
      }, 
   teamcontact: {
        numeric,
        required,
        minLen: minLength(10),
        maxLen: maxLength(10)
      },
  teamquotes: {
        maxLen: maxLength(255)
      }, 
      
      },
  methods: {
    onSubmit() {
      // Tell the REST API to create or update a Question Instance
      if (!this.teamname) {
        this.error = "You can't send an empty question!";
      } else if (this.teamname.length > 240) {
        this.error = "Ensure this field has no more than 240 characters!";
      } else {
        let endpoint = "/api/team/";
        let method = "POST";
        if (this.id !== undefined) {
          endpoint += `${ this.id }/`;
          method = "PUT";
        }
        apiService(endpoint, method, { teamname: this.teamname,
                                        teamquotes: this.teamquotes,
                                        teamcontact:this.teamcontact,
                                        teamcity:this.teamcity,
                                        })
        
            this.$router.push({
              name: 'Userprofile',
              params: {message:"Team edit successful"}
            })
        
      }
    }
  },
  async beforeRouteEnter(to, from, next) {
    // if the component will be used to update a question, then get the question's data from the REST API
    if (to.params.id !== undefined) {
      let endpoint = `/api/team/${ to.params.id }/`;
      let data = await apiService(endpoint);
      return next(vm => (vm.teamname = data.teamname,
                        vm.teamquotes=data.teamquotes,
                        vm.teamcontact=data.teamcontact,
                        vm.teamcity=data.teamcity))
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
    background-color:white;
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