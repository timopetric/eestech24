<template>
    <div class="card-container">
      <div v-for="(row, index) in rows" :key="index" class="card-row">
        <div class="card" v-for="(prediction, idx) in row" :key="idx">
          <h2>{{ prediction.location }}</h2>
          <p>Napoved za jutrišnji dan: {{ prediction.numPeople }}</p>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        loading: true,
        predictions: []
      };
    },
    computed: {
      rows() {
        // Split predictions into chunks of three
        return this.chunkArray(this.predictions, 3);
      }
    },
    mounted() {
      // Fetch data from your backend or use mock data
      this.fetchPredictions();
    },
    methods: {
      fetchPredictions() {
        // Mock data for demonstration
        // TODO change this to fetch data from your backend
        setTimeout(() => {
          this.predictions = [
            { location: 'Mountain A', numPeople: 100 },
            { location: 'Mountain B', numPeople: 50 },
            { location: 'Mountain C', numPeople: 80 },
            { location: 'Mountain D', numPeople: 120 },
            { location: 'Mountain E', numPeople: 70 },
            { location: 'Mountain F', numPeople: 90 }
          ];
          this.loading = false;
        }, 500);
      },
      chunkArray(array, size) {
        // Split array into chunks of specified size
        const result = [];
        for (let i = 0; i < array.length; i += size) {
          result.push(array.slice(i, i + size));
        }
        return result;
      }
    }
  };
  </script>
  
  <style>
  .card-container {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  
  .card-row {
    display: flex;
    justify-content: space-between;
    width: 100%;
    margin-bottom: 20px;
  }
  
  .card {
    background-color: rgb(25, 153, 25);
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    width: calc(33.33% - 20px);
  }
  
  h2 {
    margin-top: 0;
  }
  
  p {
    margin-bottom: 0;
  }
  </style>
  