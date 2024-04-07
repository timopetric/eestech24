<template>
  <div class="card-container">
    <div v-for="(row, index) in rows" :key="index" class="card-row">
      <div :class="['card', getStatusClass(prediction)]" v-for="(prediction, idx) in row" :key="idx">
        <h2>{{ getLocation((index*3)+ idx) }}</h2>
        <p>Napoved za jutrišnji dan: {{ getStatusString(prediction) }}</p>
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
    // Fetch data from your backend
    this.fetchPredictions();
  },
  methods: {
    async fetchPredictions() {
      try {
        const response = await fetch('http://127.0.0.1:8000/predict/2023-06-14'); // Update the URL with your actual API endpoint
        const data = await response.json();
        this.predictions = data.predictions;
        console.log(this.predictions)
        this.loading = false;
      } catch (error) {
        console.error('Error fetching predictions:', error);
      }
    },
    chunkArray(array, size) {
      // Split array into chunks of specified size
      const result = [];
      for (let i = 0; i < array.length; i += size) {
        result.push(array.slice(i, i + size));
      }
      return result;
    },
    getStatusClass(status) {
      // Return the appropriate class based on the status
      if (status === 2) {
        return 'card-visoka';
      } else if (status === 1) {
        return 'card-srednja';
      } else if (status === 0) {
        return 'card-nizka';
      } else if (status === 3) {
        return 'card-nipodatka';
      }
      return '';
    },
    getStatusString(status) {
      if (status === 2) {
        return 'visoka';
      } else if (status === 1) {
        return 'srednja';
      } else if (status === 0) {
        return 'nizka';
      } else if (status === 3) {
        return 'ni podatka';
      }
      return '';
    }, 
    getLocation(prediction) {
      const locationDict = {
        0: "Kum",
        1: "Lovrenška jezera",
        2: "Osp",
        3: "Storžič",
        4: "Triglavski narodni park",
        5: "Vršič",
      };
      const locationIndex = locationDict[prediction];
      const locations = Object.keys(locationDict);
      console.log(locationIndex)
      return locationIndex;
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
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  width: calc(33.33% - 20px);
}

.card-visoka {
  background-color: red;
}

.card-srednja {
  background-color: orange;
}

.card-nizka {
  background-color: green;
}

.card-nipodatka {
  background-color: gray;
}

h2 {
  margin-top: 0;
}

p {
  margin-bottom: 0;
}
</style>
