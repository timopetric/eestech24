<template>
    <div class="map-container">
      <img
        src="../assets/slovenia-hd-map-3744772488.jpg"
        alt="Slovenia Map"
        style="max-width: 100%; height: auto;"
      />
      <div class="pin" style="top: 35%; left: 20%;">
        <div class="pin-label">Nizka</div>
      </div>
      <div class="pin" style="top: 38%; left: 15%;">
        <div class="pin-label">Nizka</div>
      </div>
      <div class="pin" style="top: 85%; left: 15%;">
        <div class="pin-label">Srednja</div>
      </div>
      <div class="pin" style="top: 40%; left: 35%;">
        <div class="pin-label">Visoka</div>
      </div>
      <div class="pin" style="top: 57%; left: 55%;">
        <div class="pin-label">Visoka</div>
      </div>
      <div class="pin" style="top: 33%; left: 60%;">
        <div class="pin-label">Visoka</div>
      </div>
      <!-- Add more pins here -->
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        status: null
      };
    },
    mounted() {
      // Fetching status is removed for simplicity
    }
  };
  </script>
  
  <style>
  .map-container {
    position: relative;
  }
  
  .pin {
    position: absolute;
    width: 20px;
    height: 20px;
    background-color: red;
    border-radius: 50%;
    transform: translate(-50%, -50%);
  }
  
  .pin-label {
    position: absolute;
    top: 25px;
    left: -10px;
    font-size: 12px;
    color: black;
  }
  </style>
  