<template>
    <div class="map-container">
        <img
            src="../assets/slovenia-hd-map-3744772488.jpg"
            alt="Slovenia Map"
            style="max-width: 100%; height: auto;"
        />
        <div class="pin" style="top: 35%; left: 20%;" :style="{ backgroundColor: getPinColor(0).color }">
            <div class="pin-label">{{ getPinColor(0).label }}</div>
        </div>
        <div class="pin" style="top: 38%; left: 15%;" :style="{ backgroundColor: getPinColor(0).color }">
            <div class="pin-label">{{ getPinColor(0).label }}</div>
        </div>
        <div class="pin" style="top: 85%; left: 15%;" :style="{ backgroundColor: getPinColor(1).color }">
            <div class="pin-label">{{ getPinColor(1).label }}</div>
        </div>
        <div class="pin" style="top: 40%; left: 35%;" :style="{ backgroundColor: getPinColor(2).color }">
            <div class="pin-label">{{ getPinColor(2).label }}</div>
        </div>
        <div class="pin" style="top: 57%; left: 55%;" :style="{ backgroundColor: getPinColor(3).color }">
            <div class="pin-label">{{ getPinColor(3).label }}</div>
        </div>
        <div class="pin" style="top: 33%; left: 60%;" :style="{ backgroundColor: getPinColor(2).color }">
            <div class="pin-label">{{ getPinColor(2).label }}</div>
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
    },
    methods: {
        getPinColor(value) {
            switch (value) {
                case 0:
                    return { color: 'green', label: 'Nizka' };
                case 1:
                    return { color: 'orange', label: 'Srednja' };
                case 2:
                    return { color: 'red', label: 'Visoka' };
                case 3:
                    return { color: 'gray', label: 'N/A' };
                default:
                    return { color: 'red', label: 'Visoka' };
            }
        }
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
