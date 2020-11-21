import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Teamedit from "../views/teamedit.vue";
import Addplayer from "../views/addplayer.vue";
import Userprofile from "../views/userprofile.vue";
import Highlight from "../views/highlights.vue";
import picvid from "../views/picvid.vue";
import rankpage from "../views/rankpage.vue";
import tour from "../views/tour.vue";
import aboutpage from "../views/aboutpage.vue";
import Teamveiw from "../views/teamprofileveiw.vue";
import gallery from "../views/gallery.vue";
import playerpage from "../views/playerpage.vue";
import contest from "../views/contest.vue";
import search from "../views/search.vue";
import guest from "../views/guest.vue";
import singlehighlight from "../views/singlehighlight.vue";
import AnswerEditor from "../views/AnswerEditor.vue";
import matches from "../views/matches.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home
  },

  {
    path: "/guest",
    name: "guest",
    component: guest
  },

  {
    path: "/answer/:id",
    name: "answer-editor",
    component: AnswerEditor,
    props: true
  },


  {
    path: "/Userprofile",
    name: "Userprofile",
    component: Userprofile,
    props: true

  },

  {
    path: "/singlehighlight/:id?",
    name: "singlehighlight",
    component: singlehighlight,
    props: true

  },

  {
    path: "/Teamveiw/:id",
    name: "Teamveiw",
    component: Teamveiw
  },

  {
    path: "/gallery/:id",
    name: "gallery",
    component: gallery
  },

 

  {
    path: "/aboutpage",
    name: "aboutpage",
    component: aboutpage
  },

  {
    path: "/rankpage/:hold",
    name: "rankpage",
    component: rankpage,
    props: true
  },

  {
    path: "/matches/:id",
    name: "matches",
    component: matches
  },


  {
    path: "/tour",
    name: "tour",
    component: tour
  },


  {
    path: "/Highlight",
    name: "Highlight",
    component: Highlight
  },

  {
    path: "/picvid/:com?",
    name: "picvid",
    component: picvid
  },


  {
    path: "/search",
    name: "search",
    component: search
  },




  // {
  //   path: "/about/",
  //   name: "About",
  //   component: About
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   //component: () =>
  //   //import(/* webpackChunkName: "about" */ "../views/About.vue"),
  // },

  
  {
      path: "/Teamedit/:id",
      name: "Teamedit",
      component: Teamedit,
      props: true
    },

    {
      path: "/contest/",
      name: "contest",
      component: contest,
    },

  {
      path: "/addplayer/:id?/",
      name: "Addplayer",
      component: Addplayer,
      props: true
    },

    {
      path: "/playerpage/:id/",
      name: "playerpage",
      component: playerpage,
      props: true
    },



];

const router = new VueRouter({
  mode: "history",
  //base: process.env.BASE_URL,
  routes,

  
});


export default router;
