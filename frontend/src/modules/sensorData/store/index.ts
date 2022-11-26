import { defineStore } from "pinia";

import TemperaturApi from "@//modules/sensorData/services/temperatur";
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
        const response = await TemperaturApi.fetchAll(params);
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
    pressure: (state) => {
      return state._pressures;
    },
    humidities: (state) => {
      return state._humidities;
    },
  },
});
