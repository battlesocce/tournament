<template>
<div class="ody">
<div>
  <div class="row">
    <div class="col-12">
      <article class="blog-card">
        <div class="blog-card__background">
          <div class="card__background--wrapper">
            <div class="card__background--main" :style="{'background-image': `url(${require('@/assets/img/card.jpg')})`}">             
             <div class="card__background--layer"></div>
            </div>
          </div>
        </div>
        <div class="blog-card__head">
          <span class="date__box">
            <span class="date__day">5</span>
            <span class="date__month">DEC</span>
          </span>
        </div>
        <div class="blog-card__info">
          <h2>Battle Takedown</h2>
            <br>
          <p>
              Football is much more than just a game where you score a goal or win a match. It's a relationship where only passion and hope prevails.Love the colours you wear, for that crest you touch right above your heart when you pray and for those boots you lace up in the hope that your legs pump harder than your heart does.Keep your hopes high and join our contest to face off with the top teams and enjoy the game to the core.
          </p>
          <router-link 
        :to="{ name: 'contest'}" class="btn1 btn1--with-icon"><i class="btn1-icon fa fa-long-arrow-right"></i>READ MORE</router-link>
        </div>
      </article>
    </div></div></div>
  </div>
</template>

<script>
export default {
  name: "card",
}
</script>


<style scoped>


@import '../assets/css/card.css';
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