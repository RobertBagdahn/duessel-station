<template>
  <div class="2xl:px-64 xl:px-30">
    <div class="mx-auto max-w-7xl sm:px-6 lg:px-8">
      <h1>Sensor daten!</h1>

      <div class="divide-y divide-gray-200 overflow-hidden rounded-lg bg-white shadow">
        <div class="px-4 py-5 sm:px-6">
          <!-- Content goes here -->
          <!-- We use less vertical padding on card headers on desktop than on body sections -->
          
          <div class="grid grid-cols-1 gap-4 sm:grid-cols-2">
            <div v-for="sensorBtn in sensorBtns" :key="sensorBtn.name" class="relative flex items-center space-x-3 rounded-lg border border-gray-300 bg-white px-6 py-5 shadow-sm focus-within:ring-2 focus-within:ring-indigo-500 focus-within:ring-offset-2 hover:border-gray-400">
              <button @click="onDataSelectButtonClick(sensorBtn)">
                <div class="flex-shrink-0">
                  <span :class="[sensorBtn.iconBackground, sensorBtn.iconForeground, 'rounded-lg inline-flex p-3 ring-4 ring-white']">
                    <component :is="sensorBtn.icon" class="h-6 w-6" aria-hidden="true" />
                  </span>
                </div>
                <div class="min-w-0 flex-1">
                  <a href="#" class="focus:outline-none">
                    <span class="absolute inset-0" aria-hidden="true" />
                    <p class="text-xl font-medium text-gray-900">{{ sensorBtn.name }}</p>
                    <p class="truncate text-sm text-gray-500">{{ sensorBtn.description }}</p>
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

          <div>
            <label for="time-range" class="block text-sm font-medium text-gray-700">Zeitdings zurück: </label>
            <div class="mt-1 flex rounded-md shadow-sm">
              <div class="relative flex flex-grow items-stretch focus-within:z-10">
                <div class="pointer-events-none absolute inset-y-0 left-0 flex items-center pl-3">
                  <UsersIcon class="h-5 w-5 text-gray-400" aria-hidden="true" />
                </div>
                <input type="text" v-model="timeRangeInput" name="time-range" id="time-range" class="block w-full rounded-none rounded-l-md border-gray-300 pl-10 focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"/>
              </div>
              <button @click="onTimeRangeButtonClick()" type="button" class="relative -ml-px inline-flex items-center space-x-2 rounded-r-md border border-gray-300 bg-gray-50 px-4 py-2 text-sm font-medium text-gray-700 hover:bg-gray-100 focus:border-indigo-500 focus:outline-none focus:ring-1 focus:ring-indigo-500">
                <BarsArrowUpIcon class="h-5 w-5 text-gray-400" aria-hidden="true" />
                <span>Update</span>
              </button>
            </div>
          </div>

        </div>
      </div>
    </div>
    </div>
  </div>
</template>




<script setup lang="ts">
//IMPORTS
import {
  AcademicCapIcon,
  BanknotesIcon,
  CheckBadgeIcon,
  ClockIcon,
  ReceiptRefundIcon,
  UsersIcon,
} from '@heroicons/vue/24/outline'

import { update, values } from "cypress/types/lodash";


import { 
  useTemperatureStore,
  usePressureStore,
  useHumidityStore,
} from "@/modules/temperature/store/index";


const sensorBtns = [
  {
    name: 'Temperatur',
    description: 'Zeigt die Temperaturdaten an',
    icon: AcademicCapIcon,
    iconForeground: 'text-teal-700',
    iconBackground: 'bg-teal-50',
  },
  {
    name: 'Luftfeuchtigkeit',
    description: 'Zeigt die Luftfeuchtigkeit an',
    icon: UsersIcon,
    iconForeground: 'text-teal-700',
    iconBackground: 'bg-teal-50',
  },
  {
    name: 'Luftdruck',
    description: 'Zeigt den Luftdruck an',
    icon:ClockIcon,
    iconForeground: 'text-teal-700',
    iconBackground: 'bg-teal-50',
  },
]


const temperaturStore = useTemperatureStore();

const temperatures = computed(() => {
  console.log(temperaturStore.temperatures);
  return temperaturStore.temperatures;
});

const pressureStore = usePressureStore();

const pressures = computed(() => {
  console.log(pressureStore.pressures);
  return pressureStore.pressures;
});

const humidityStore = useHumidityStore();

const humidities = computed(() => {
  console.log(humidityStore.humidities);
  return humidityStore.humidities;
});


onMounted(() => {
  updateChartValues(timeRangeInput.value, currentSensorBtnName.value);
});

//FUNCTION FOR BUTTON PUSH
let currentSensorBtnName = ref("Temperatur");

function onDataSelectButtonClick(sensorBtn:object){
  currentSensorBtnName.value = sensorBtn?.name;
  console.log(`auf ${currentSensorBtnName.value} gedrückt`);
  updateChartValues(timeRangeInput.value, currentSensorBtnName.value);
}


const timeRangeInput = ref(20);


function onTimeRangeButtonClick(){
  if(timeRangeInput.value > 1000){
    timeRangeInput.value = 1000;
  }
  else if(timeRangeInput.value < 3){
    timeRangeInput.value = 3;
  }

  console.log(`new number: ${timeRangeInput.value}`);
  updateChartValues(timeRangeInput.value, currentSensorBtnName.value);
}


function updateChartValues(amount:Number, name:String){
  if(currentSensorBtnName.value === "Temperatur"){
    console.log("Temperatur wird aktualisiert");
    temperaturStore.fetchTemperatures();
  }
  else if(currentSensorBtnName.value === "Luftfeuchtigkeit"){
    console.log("Luftfeuchtigkeit wird aktualisiert");
    //humidityStore.fetchHumidities();
    alert("humidity not added yet");
    //add fetch for humidity
  }
  else if(currentSensorBtnName.value === "Luftdruck"){
    console.log("Luftdruck wird aktualisiert");
    pressureStore.fetchPressures();
    //add fetch for luftdruck
  }
  console.log(`Amount: ${amount}; Name: ${name}`);
}


//SHOW THE GRAPH
let series = computed(() => {
  //ergibt irgendwie sinn
  console.log(`${currentSensorBtnName.value} is shown on the y axis`);
  return [{
    name: currentSensorBtnName.value,
    data: temperatures.value.map(a => a.value),
  }]
})


let chartOptions = {
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
    text: (`${currentSensorBtnName.value} über Zeit`),
    align: 'left'
  },
  grid: {
    row: {
      colors: ['#f3f3f3', 'transparent'], // takes an array which will be repeated on columns
      opacity: 0.5
    },
  },
  xaxis: {
    categories: temperatures.value.map(a => a.created),
  }
}

</script>