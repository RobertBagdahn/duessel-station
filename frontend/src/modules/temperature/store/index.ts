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



import PressureApi from "@/modules/temperature/services/temperature";


export const usePressureStore = defineStore("temperature", {
  state: () => ({
    _temperatures: [],
  }),

  actions: {
    async fetchTemperatures(params = {}) {
      try {
        const response = await PressureApi.fetchAll(params);
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



import HumidityApi from "@/modules/temperature/services/temperature";


export const useHumidityStore = defineStore("temperature", {
  state: () => ({
    _temperatures: [],
  }),

  actions: {
    async fetchTemperatures(params = {}) {
      try {
        const response = await HumidityApi.fetchAll(params);
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
