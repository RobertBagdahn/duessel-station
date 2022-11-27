import { defineStore } from "pinia";

import TemperatureApi from "@//modules/sensorData/services/temperature";
import PressureApi from "@/modules/sensorData/services/pressure";
import HumidityApi from "@/modules/sensorData/services/humidity";

export const useSensorDataStore = defineStore("sensorData", {
  state: () => ({
    _temperatures: [],
    _pressures: [],
    _humidities: [],
  }),

  actions: {
    async fetchTemperatures(params = {}) {
      try {
        const response = await TemperatureApi.fetchAll(params);
        this._temperatures = response.data.results;
      } catch (error) {
        alert(error);
        console.log(error);
      }
    },
    async fetchPressures(params = {}) {
      try {
        const response = await PressureApi.fetchAll(params);
        this._pressures = response.data.results;
      } catch (error) {
        alert(error);
        console.log(error);
      }
    },
    async fetchHumidities(params = {}) {
      try {
        const response = await HumidityApi.fetchAll(params);
        this._humidities = response.data.results;
      } catch (error) {
        alert(error);
        console.log(error);
      }
    },
  },
  getters: {
    temperatures: (state) => {
      return state._temperatures;
    },
    pressures: (state) => {
      return state._pressures;
    },
    humidities: (state) => {
      return state._humidities;
    },
  },
});
