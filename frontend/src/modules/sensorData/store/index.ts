import { defineStore } from "pinia";

import TemperaturApi from "@//modules/temperatur/services/temperatur.ts";


export const useRecipeStore = defineStore("recipe", {
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
