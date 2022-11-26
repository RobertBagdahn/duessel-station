<template>
  <div class="2xl:px-64 xl:px-30">
    <div class="mx-auto max-w-7xl sm:px-6 lg:px-8">
      <h1>Sensor daten!</h1>

      <div class="divide-y divide-gray-200 overflow-hidden rounded-lg bg-white shadow">
        <div class="px-4 py-5 sm:px-6">
          <!-- Content goes here -->
          <!-- We use less vertical padding on card headers on desktop than on body sections -->
          
          <div class="grid grid-cols-1 gap-4 sm:grid-cols-2">
            <div v-for="sensorBtn in sensorBtns" :key="sensorBtn.id" class="relative flex items-center space-x-3 rounded-lg border border-gray-300 bg-white px-6 py-5 shadow-sm focus-within:ring-2 focus-within:ring-indigo-500 focus-within:ring-offset-2 hover:border-gray-400">
              <button @click="onButtonClick(sensorBtn.id)">
                <div class="flex-shrink-0">
                  <span :class="[sensorBtn.iconBackground, sensorBtn.iconForeground, 'rounded-lg inline-flex p-3 ring-4 ring-white']">
                    <component :is="sensorBtn.icon" class="h-6 w-6" aria-hidden="true" />
                  </span>
                </div>
                <div class="min-w-0 flex-1">
                  <a href="#" class="focus:outline-none">
                    <span class="absolute inset-0" aria-hidden="true" />
                    <p class="text-xl font-medium text-gray-900">{{ sensorBtn.name }}</p>
                    <p class="truncate text-sm text-gray-500">{{ sensorBtn.role }}</p>
                  </a>
                </div>
              </button>
            </div>
          </div>
        

        <div class="px-4 py-5 sm:p-6">
          <!-- Content goes here -->
          <div id="chart">
            <apexchart type="line" height="350" :options="chartOptions" :series="series"></apexchart>
          </div>
        </div>
      </div>
    </div>
    </div>
  </div>
</template>





<script setup lang="ts">
import { TagIcon } from "@heroicons/vue/20/solid";

import {
  AcademicCapIcon,
  BanknotesIcon,
  CheckBadgeIcon,
  ClockIcon,
  ReceiptRefundIcon,
  UsersIcon,
} from '@heroicons/vue/24/outline'
import { values } from "cypress/types/lodash";


const sensorBtns = [
  {
    name: 'Temperatur',
    id: 'temp',
    role: 'Zeigt die Temperaturdaten an',
    icon: AcademicCapIcon,
    iconForeground: 'text-teal-700',
    iconBackground: 'bg-teal-50',
  },
  {
    name: 'Luftfeuchtigkeit',
    id: 'humid',
    role: 'Zeigt die Luftfeuchtigkeit an',
    icon: UsersIcon,
    iconForeground: 'text-teal-700',
    iconBackground: 'bg-teal-50',
  },
  {
    name: 'Luftdruck',
    id: 'pres',
    role: 'Zeigt den Luftdruck an',
    icon:ClockIcon,
    iconForeground: 'text-teal-700',
    iconBackground: 'bg-teal-50',
  },
]


//Ist das gemüse richtig definiert?
const currentSensorData = "";
function onButtonClick(id:string){
  alert(`Gedrückt ${id}`) ;

  //warum kann ich das so nicht setzen? weil es const ist?
  currentSensorData = id;
}


const series = computed(() => {
  //ergibt irgendwie sinn
  if (currentSensorData === "temp"){
    return [{
      name: "Temperaturen",
      data: [10, 41, 35, 51, 49, 62, 69, 91, 148]
    }]
  }

  if (currentSensorData === "humid"){
    return [{
      name: "Luftfeuchtigkeit",
      data: [40, 41, 43, 41, 50, 40, 44, 49, 55, 53]
    }]
  }

  if (currentSensorData === "pres"){
    return [{
      name: "Luftdruck",
      data: [20, 21, 25, 24, 22, 19, 20, 18, 17, 15, 10]
    }]
  }
  
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

</script>