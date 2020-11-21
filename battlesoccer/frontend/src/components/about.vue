<template>
<div class="dy" style="margin-top:-70px">
  <div class="container py-5 my-5">
<!--  copy here  -->
  <div class="col-md-10 mx-auto">
    <img  style="width: 60px;" src="@/assets/img/load.svg" alt=""><h1 style="font-weight:400; color: #9B5DE5;">BattleSoccer</h1>
    <p class="text-secondary pl-4 border-left py-2 my-3 position-relative">
      <span  class="position-absolute" style="background-color: #9B5DE5; top: 50%; left:0; transform: translate(-60%,-50%); height: 60px; width: 2px;"></span>
                 Many of you might have the question what is battlesocer? Well to keep it simple, we are a community of passionate football players and fans where everyone who loves the sport is a part of.
                 There is no we without you. </p>
  </div>
</div>
<br>
</div>
</template>
<script>
export default {
    name:"about"
}
</script>
<style scoped>
 @import '../assets/css/about.css';

@import url("https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap");

dy {
  font-family: "Poppins", sans-serif !important;
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