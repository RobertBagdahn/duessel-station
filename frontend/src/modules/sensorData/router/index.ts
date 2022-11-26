export default [
  {
    path: "/sensorData",
    name: "SensorDataMain",
    component: () => import(/* webpackChunkName: "SensorDataMain" */ "@/modules/sensorData/views/Main.vue")
  },
];
