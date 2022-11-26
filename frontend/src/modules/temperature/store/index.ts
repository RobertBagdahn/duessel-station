import { defineStore } from "pinia";

import TemperaturApi from "@/modules/temperature/services/temperature";


export const useTemperatureStore = defineStore("temperature", {
  state: () => ({
    _temperatures: [],
  }),

  actions: {
    async fetchTemperatures(params = {}) {
      try {
        const response = await TemperaturApi.fetchAll(params);
        this._temperatures = response.data;
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
  },
});



import PressureApi from "@/modules/temperature/services/pressure";


export const usePressureStore = defineStore("pressure", {
  state: () => ({
    _pressures: [],
  }),

  actions: {
    async fetchPressures(params = {}) {
      try {
        const response = await PressureApi.fetchAll(params);
        this._pressures = response.data;
      } catch (error) {
        alert(error);
        console.log(error);
      }
    },
  },
  getters: {
    pressures: (state) => {
      return state._pressures;
    },
  },
});



import HumidityApi from "@/modules/temperature/services/humidity";


export const useHumidityStore = defineStore("humidity", {
  state: () => ({
    _humidities: [],
  }),

  actions: {
    async fetchHumidities(params = {}) {
      try {
        const response = await HumidityApi.fetchAll(params);
        this._humidities = response.data;
      } catch (error) {
        alert(error);
        console.log(error);
      }
    },
  },
  getters: {
    humidities: (state) => {
      return state._humidities;
    },
  },
});
