<template>
  <div class="card-container">
    <div v-for="(row, index) in rows" :key="index" class="card-row">
      <div :class="['card', getStatusClass(prediction.status)]" v-for="(prediction, idx) in row" :key="idx">
        <h2>{{ prediction.location }}</h2>
        <p>Napoved za jutrišnji dan: {{ getStatusString(prediction.status) }}</p>
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
          { location: 'Mountain A', numPeople: 100, status: 0 },
          { location: 'Mountain B', numPeople: 50, status: 1 },
          { location: 'Mountain C', numPeople: 80, status: 2 },
          { location: 'Mountain D', numPeople: 120, status: 3 },
          { location: 'Mountain E', numPeople: 70, status: 1 },
          { location: 'Mountain F', numPeople: 90, status: 2 }
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