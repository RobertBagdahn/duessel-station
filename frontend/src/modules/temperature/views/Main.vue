<template>
  <div class="2xl:px-64 xl:px-30">
    <h1>Temp</h1>

      <!-- Before extracting a custom class -->
      <button @click="onButtonClick" class="py-2 px-4 bg-blue-500 text-white font-semibold rounded-lg shadow-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-400 focus:ring-opacity-75">
        Save changes
      </button>

      <div id="chart">
        <apexchart type="line" height="350" :options="chartOptions" :series="series"></apexchart>
      </div>

  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from "vue";

import { useTemperatureStore } from "@/modules/temperature/store/index";

import { TagIcon } from "@heroicons/vue/20/solid";

function onButtonClick(){
  console.log("Hallo");
  multiplyer.value = multiplyer.value * 2;
}

const multiplyer = ref(1);

const series = computed(() => {
  return [{
      name: "Desktops",
      data: [10*multiplyer.value, 41, 35, 51, 49, 62, 69, 91, 148]
    }]
})
  const chartOptions = {
    chart: {
      height: 350,
      type: 'line',
      zoom: {
        enabled: false
      }
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      curve: 'straight'
    },
    title: {
      text: 'Product Trends by Month',
      align: 'left'
    },
    grid: {
      row: {
        colors: ['#f3f3f3', 'transparent'], // takes an array which will be repeated on columns
        opacity: 0.5
      },
    },
    xaxis: {
      categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep'],
    }
  }

  const temperaturStore = useTemperatureStore();

const temperatures = computed(() => {
  return temperaturStore.temperatures;
});

  onMounted(() => {
  temperaturStore.fetchTemperatures();
});

</script>