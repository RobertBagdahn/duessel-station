export default [
  {
    path: "/temperatur",
    name: "TemperaturMain",
    component: () => import(/* webpackChunkName: "TemperaturMain" */ "@/modules/temperature/views/Main.vue")
  },
];
