<template>
   <div class="ody">
       <br><br>
   <div v-if="!stepall">
<br><br><br><br><br><br><br><br>
    <div class="svg-container">    
    <svg class="ft-green-tick" xmlns="http://www.w3.org/2000/svg" height="100" width="100" viewBox="0 0 48 48" aria-hidden="true">
        <circle class="circle" fill="#5bb543" cx="24" cy="24" r="22"/>
        <path class="tick" fill="none" stroke="#FFF" stroke-width="6" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10" d="M14 27l5.917 4.917L34 17"/>
    </svg>
</div>

<center><h1 class="mt-3">Registration successful!!</h1></center><h2 class="mt-3 text-muted container-fluid text-center">Your team has been enrolled for the contest</h2>
  </div>
       <div v-if="stepall" class="container-lg">
    <section>
        <div class="text-center mb-5">
            <h2><span>STEPS</span></h2><br>
            <h2 class="font-weight-bold display-4 ">How It <span style="color: #9B5DE5">Works?</span></h2>
        </div>
        <div  class="col-12 col-md-8 mx-auto" style="padding:5px">
          <div v-if=!this.step1 >
              <div class="alert alert-primary" role="alert">
  Step one complete,Now make your payment and wait for the confirmation.
</div>  
              </div>
            <div v-if=this.step1>
              
                <div class="bg-light position-relative px-3 my-5">
                    <div class="font-weight-bold circle text-white rounded-circle d-flex align-items-center justify-content-center mx-auto position-relative border border-white"
                         style="width: 60px;height: 60px;top: -30px;border-width: 4px !important; background-color: #9B5DE5">
                        1
                    </div>
                    <div class="px-3 text-center pb-3">
                         <div class="container-lg">
    <h1>Register Your Team Here</h1>   
     <form>
<br>
<form @submit.prevent="onSubmit">
<div class="form-group">
  <label for="usr">Team_name:</label>
  <input type="text" v-model="contest_teamname" 
  class="form-control" required  readonly>
</div>

<div class="form-group input" :class="{invalid: $v.contest_adminname.$error}">
    <label for="usr">Admin_name:</label>
  <input type="text" @input="$v.contest_adminname.$touch()" v-model="contest_adminname"
    class="form-control" required>
  <p v-if="!$v.contest_adminname.required">This field must not be empty.</p>
</div>

<div class="form-group input" :class="{invalid: $v.contest_teamcontact.$error}">
<label for="usr">Admin_contact:</label>
<input type="text" @input="$v.contest_teamcontact.$touch()" v-model="contest_teamcontact"
   class="form-control" required >
  <p v-if="!$v.contest_teamcontact.required">This field must not be empty.</p>
  <p v-if="!$v.contest_teamcontact.minLen">Invalid contact number.</p>
  
</div>

      <br>
      <div v-if="is_team">
<button type="submit" :disabled="$v.$invalid" class="btn btn-dark">Register</button></div>

<div v-if="!is_team">
  <a href=/register/ class="btn btn-outline-dark btn-block">Create team</a>
</div>


</form>
<br><br>
    </form>
  </div>
                    </div>
                </div>
            </div>
            <div class="">
                <div class="bg-light position-relative px-3 my-5">
                    <div class="font-weight-bold circle text-white rounded-circle d-flex align-items-center justify-content-center mx-auto position-relative border border-white"
                         style="width: 60px;height: 60px;top: -30px;border-width: 4px !important; background-color: #9B5DE5">
                        2
                    </div>
                    <div class="px-3 text-center pb-3">
                      <div class="hidden-big">
                        <h1>Make payment through your mobile</h1><br>
                        <a href="upi://pay?pa=kaamil312@oksbi&pn=KAAMIL MOHMAMMED&cu=INR&am=1000&mam=1000" class="btn btn-outline-dark btn-lg btn-block"><i class="fa fa-google-wallet mr-2" style="font-size:24px"></i>Pay using UPI</a>
                    </div>

                    <div class="hidden-small">
                        <h1>Scan to make Payment</h1><br>
                        <img src="@/assets/img/qr.png" width="40%">
                    </div>
                    </div>
                </div>
            </div>
            <div class="">
                <div class="bg-light position-relative px-3 my-5">
                    <div class="font-weight-bold circle text-white rounded-circle d-flex align-items-center justify-content-center mx-auto position-relative border border-white"
                         style="width: 60px;height: 60px;top: -30px;border-width: 4px !important; background-color: #9B5DE5">
                        3
                    </div>
                    <div class="px-3 text-center pb-3">
                        <h1>Send the confirmation</h1><br>
                        <h3>Take a "screenshot" of SUCCESS Transaction and send it by clicking the whatsapp icon at bottom.</h3>
                    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.5.0/css/font-awesome.min.css">
<a href="https://api.whatsapp.com/send?phone=+919384116478&text=Hola%21%20Quisiera%20m%C3%A1s%20informaci%C3%B3n%20sobre%20Varela%202."  target="_blank">
<i class="fa fa-whatsapp" style="font-size:32px;"></i>
</a>
                    </div>
                </div>
            </div>
        </div>
    </section>
</div>

  </div>
</template>

<script>
import { required, numeric,maxLength,minLength} from 'vuelidate/lib/validators'
import Swal from 'sweetalert2'
import { apiService } from "@/common/api.service.js";
export default {
    name:"joincontest",
    data() {
    return {
      contest_teamname: null,
      contest_adminname: null,
      contest_teamcontact: null,
      team:{},
      id:null,
      requestUser:null,
      is_team:null,
      contestdata:null,
      step1:true,
      stepall:true,
      enrolledteam: [],

      }
    },
    validations: {

    contest_adminname: {
        required,
        maxLen: maxLength(15)
      },

   contest_teamcontact: {
        numeric,
        minLen: minLength(10),
        maxLen: maxLength(10)
        
      },

    },

     methods: {
        start() {
        this.$confetti.start();
      },

stop() {
        this.$confetti.stop();
      },

       
    

arraycheckcontest() {
                    var length = this.enrolledteam.length;
                    for(var i = 0; i <length; i++) {
                        if(this.enrolledteam[i].own.id== this.id)
        {
                         return true;
                          
        }
                    }
                    return false;
                },

  contestcheck() {
let endpoint = `/api/contestcheck/`;
      apiService(endpoint)
        .then(data => {
          if (data) {
            this.enrolledteam = data;
          } else {
            this.enrolledteam = null;
          }  
   if (this.arraycheckcontest())
{
this.stepall=false;
if(!this.stepall){
         this.start()

         setTimeout(() => {
           this. stop()
         },2000)



       }
}  }) 
},
arraycheck() {
                    var length = this.contestdata.length;
                    for(var i = 0; i <length; i++) {
                        if(this.contestdata[i].contest_team_id== this.id)
        {
                         return true;
                          
        }
                    }
                    return false;
                },

  contestalert() {
let endpoint = `/api/contest_register/`;
      apiService(endpoint)
        .then(data => {
          if (data) {
            this.contestdata = data;
          } else {
            this.contestdata = null;
          }  
   if (this.arraycheck())
{
this.step1=false;
       
}  }) 
},
       setUserInfo() {
       let endpoint = `/api/user/`;
      apiService(endpoint)
        .then(data => {
      this.requestUser = data["username"];
      this.is_team = data["is_team"];
        })
    },
        getTeamData() {  
      this.id = window.localStorage.getItem("id");
      this.id=parseInt(this.id)
      if(this.id){
        
      let endpoint = `/api/team/${this.id}/`;
      apiService(endpoint)
        .then(data => {
          if (data) {
            this.team = data;
            this.contest_teamname=this.team.teamname
          } else {
            this.team = null;
          }
        })
    setTimeout(() => {      
        if(this.requestUser && !this.is_team){
 Swal.fire({
  showConfirmButton: false,
  imageUrl: 'https://cdn5.vectorstock.com/i/thumb-large/84/19/woman-playing-soccer-vector-24058419.jpg',
  imageWidth: 300,
  imageHeight: 300,
  imageAlt: 'Custom image',
  showCloseButton: true,
  html:`Create your team to join contest<br>
   <a href=/register/ class="btn btn-outline-dark btn-block">Create team</a>
`,  showClass: {
    popup: 'animate__animated animate__fadeInDown'
  },
  hideClass: {
    popup: 'animate__animated animate__fadeOutUp'
  }
})

    }},1500)}
        },
    onSubmit() {
      if (!this.contest_teamname) {
        this.error = "You can't send an empty question!";
      }else {
        let endpoint = "/api/contest_register/";
        let method = "POST";
        apiService(endpoint, method, { contest_teamname:     this.contest_teamname, 
                                       contest_adminname:    this.contest_adminname,
                                       contest_teamcontact : this.contest_teamcontact,
                                       contest_team_id : this.team.id,
                                        })
                                       .then(response => {
      console.log('SUCCESS!!');
      this.step1=false;
      Swal.fire({
  icon: 'success',
  title: 'Your work has been saved',
  html: "Go to step 2", 
  showConfirmButton: true,
  timer: 1500
})
      this.contest_teamname= "";
      this.contest_adminname= "";
      this.contest_teamcontact= "";   
      return response  
})

      
      }
    }
     },
     created() {
    this.contestcheck()
    this.contestalert()
    this.getTeamData()
    this. setUserInfo()
   setTimeout(() => { 
    if(!this.requestUser){
 Swal.fire({
  showConfirmButton: false,
  imageUrl: 'https://cdn5.vectorstock.com/i/thumb-large/84/19/woman-playing-soccer-vector-24058419.jpg',
  imageWidth: 300,
  imageHeight: 300,
  imageAlt: 'Custom image',
  showCloseButton: true,
  html:`Create your team to join contest<br>
   <a href=/register/ class="btn btn-outline-dark btn-block">Create team</a>
`,
  showClass: {
    popup: 'animate__animated animate__fadeInDown'
  },
  hideClass: {
    popup: 'animate__animated animate__fadeOutUp'
  }
})

    }},1000)
     }
}

</script>

<style scoped>
  
    h1{
            font-size:40px;

        }

h2{
            font-size:30px;

        }
h3{
          font-size:20px;
}


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
    background-color: white; }

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

    @media only screen and (max-width:500px) {
   .hidden-small {
    display: none;
  }
    }
@media screen and (max-width:1500px)  and (min-width:501px){
  .hidden-big {
    display: none;
  }
}
@media only screen and (max-width:700px) {

h1{
            font-size:25px;

        }
h2{
            font-size:20px;

        }
h3{
            font-size:15px;
}

}





@supports (animation: grow .5s cubic-bezier(.25, .25, .25, 1) forwards) {
	 .tick {
		 stroke-opacity: 0;
		 stroke-dasharray: 29px;
		 stroke-dashoffset: 29px;
		 animation: draw 0.5s cubic-bezier(0.25, 0.25, 0.25, 1) forwards;
		 animation-delay: 0.6s;
	}
	 .circle {
		 fill-opacity: 0;
		 stroke: #219a00;
		 stroke-width: 16px;
		 transform-origin: center;
		 transform: scale(0);
		 animation: grow 1s cubic-bezier(0.25, 0.25, 0.25, 1.25) forwards;
	}
}

 @keyframes grow {
	 60% {
		 transform: scale(0.8);
		 stroke-width: 4px;
		 fill-opacity: 0;
	}
	 100% {
		 transform: scale(0.9);
		 stroke-width: 8px;
		 fill-opacity: 1;
		 fill: #219a00;
	}
}
 @keyframes draw {
	 0%, 100% {
		 stroke-opacity: 1;
	}
	 100% {
		 stroke-dashoffset: 0;
	}
}
 :root {
	 --theme-color: var(--color-purple);
}

 
</style>