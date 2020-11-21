<template>
<div clas="ody">
<div class="right3">
<div class="footer1">
    <div class="gooey-animations"></div>
    <h1>
    <a href="https://www.facebook.com/battlesoccer.india" class="btn btn-just-icon btn-link btn-twitter" ><i class="fa fa-facebook"></i></a>
    <a href="https://twitter.com/BattlesoccerI" class="btn btn-just-icon btn-link btn-twitter" ><i class="fa fa-youtube"></i></a>
    <a href="https://www.instagram.com/battlesoccer_india/" class="btn btn-just-icon btn-link btn-twitter" ><i class="fa fa-instagram"></i></a>
    <a href="https://www.youtube.com/channel/UCIXe1NrFsq9v2kwszsqEoCw?view_as=subscriber" class="btn btn-just-icon btn-link btn-twitter" ><i class="fa fa-twitter"></i></a>
        <br>
  @ Battle<span>Soccer.in</span>
  </h1>
</div>
<svg xmlns="http://www.w3.org/2000/svg" version="1.1">
  <defs>
    <filter id="goo">
      <feGaussianBlur in="SourceGraphic" stdDeviation="15" result="blur" />
      <feColorMatrix in="blur" mode="matrix" values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 15 -7" result="goo" />
      <feBlend in="SourceGraphic" in2="goo" />
  	</filter>
  </defs>
</svg>


<svg viewbox="0 0 1440 328"  width="100%">
    <defs>
        <clipPath id="wave" clipPathUnits="objectBoundingBox" transform="scale(0.00069444444, 0.00304878048)">
            <path d="M504.452 27.7002C163.193 -42.9551 25.9595 38.071 0 87.4161V328H1440V27.7002C1270.34 57.14 845.711 98.3556 504.452 27.7002Z"/>
        </clipPath>
    </defs>
</svg>
    </div>

</div>
</template>
<script>
import $ from 'jquery'

export default {
    name:"footers",
     mounted () {
         function generateBalls() {
  for (var i = 0; i < Math.floor(window.innerWidth / 20); i++) {
    $(".gooey-animations").append(`
    <div class="ball"></div>
  `);
    var colors = ["#28323B", "#FFA036"];
    $(".ball")
      .eq(i)
      .css({
        bottom: "0px",
        left: Math.random() * window.innerWidth - 100,
        "animation-delay": Math.random() * 5 + "s",
        transform: "translateY(" + Math.random() * 10 + "px)",
        "background-color": colors[i % 2]
      });
  }
}
generateBalls();

window.addEventListener("resize", function () {
  $(".gooey-animations .ball").remove();
  generateBalls();
});


     }}
</script>
<style scoped>
@import '../assets/css/footer.css';
html,
.ody {

    font-family: "Quicksand", sans-serif;

}

</style>