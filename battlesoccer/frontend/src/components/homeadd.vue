<template>
<div clas="ody">
   <article id="banner" class="jumbotron jumbotron-fluid">
    <div class="font-italic pl-4 mt-4 text-light">
      <h1 class="display-1 font-italic">
        Battle
        <span class="badge badge-primary shadow">Soccer</span>
      </h1>

      <p class="lead mt-5">
       Where passionate people with talent meet oppurtunity.
      </p>
    </div>
  </article>
</div>
</template>
<script>
export default {
    name:"homeadd"
}
</script>
<style scoped>
#banner {
 background:
   url("https://i.postimg.cc/FzSHSbhQ/img-soccer.jpg") no-repeat;
  background-size: cover;
  height: 400px;
  background-position: 0 0;
  
}

@media screen and (max-width:768px){
  
 #banner {
  background-size: cover;
  height: 300px;
  background-position: right bottom;
    background-attachment: fixed;
} 
  
#banner h1{
  font-size: 3.2rem !important;
}
 
  #banner p{
    padding:0.5rem;
    text-align: center;
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