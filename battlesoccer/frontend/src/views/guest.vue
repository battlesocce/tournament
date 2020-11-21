<template>
<div class="ody"><br><br><br><br>
    <div class="container">
        <h1>Welcome to Battle Soccer</h1><br><br>
        <div class="row">
            <div class="cols-12 col-lg-4">     <div class="shadow p-3 mb-5 bg-white rounded">
             <center><img src="https://cdn.dribbble.com/users/4779117/screenshots/14020583/media/2a377b0e61ce9d59f47ef02e8a403e70.jpg" width=90%></center>

        <h2>Sign in with Google to continue as a vistor </h2> 
            <p class="mt-3"><hr><a href="accounts/google/login/" style="text-decoration:none;" ><center class="btn btn-outline-danger btn-lg btn-block">
            <img width="20px" style="margin-top:0px; margin-right:8px" alt="Google sign-in" 
                src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Google_%22G%22_Logo.svg/512px-Google_%22G%22_Logo.svg.png" />
        Login with Google</center></a>
            </div></div>

             <div class="cols-12 col-lg-4">    <div class="shadow p-3 mb-5 bg-white rounded">
             <center><img src="https://image.freepik.com/free-vector/active-happy-children-playing-football-outdoors-isolated-flat-vector-illustration-cartoon-boys-playing-soccer-running-kicking-ball-playground-summer-vacation-sport-game_74855-8208.jpg" width=97%></center><br>

        <h2>Create a Team to join the Battle</h2> 
            <p class="mt-3"><hr><a href="/register/" style="text-decoration:none;" ><center class="btn btn-primary btn-lg btn-block">Create an Team</center></a>
            </div></div>
            
             <div class="cols-12 col-lg-4 "><div class="shadow p-3 mb-5 bg-white rounded">
             <center><img src="https://cdn.dribbble.com/users/4779117/screenshots/14020604/media/c1f79c012d9b89ec4906bee04c5920d0.jpg" width=90%></center>
        <h2>Have a team! Then just Log in to your account </h2> 
            <p class="mt-3"><hr><a href="/accounts/logout/" style="text-decoration:none;" ><center class="btn btn-outline-success btn-lg btn-block">
         Log_in to your Team</center></a>
            </div>
        </div></div>
        </div><br><br><br><br><br><br>
          <footeruse></footeruse>

</div>
</template>

<script>
import footeruse from "@/components/footer.vue";

export default{
    name: "guest",
      components: {
        footeruse,

      }}
</script>

<style scoped>

.ody a{

    font-family: "Quicksand", sans-serif;
        text-decoration: none;


}


h1{
            font-size:55px;
            text-align: center;

        }

h2{
            font-size:25px;

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
            font-size:20px;

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
}
</style>


