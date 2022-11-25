export default [
  {
    path: "/temperatur",
    name: "TemperaturMain",
    component: () => import(/* webpackChunkName: "TemperaturMain" */ "@/modules/temperatur/views/Main.vue")
  },
];
