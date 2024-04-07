<template>
    <div class="map-container">
        <img
            src="../assets/slovenia-hd-map-3744772488.jpg"
            alt="Slovenia Map"
            style="max-width: 100%; height: auto;"
        />
        <!-- Pins will be dynamically rendered here -->
    </div>
</template>

<script>
export default {
    data() {
        return {
            predictions: []
        };
    },
    mounted() {
        // Fetch predictions when the component is mounted
        this.fetchPredictions();
    },
    methods: {
        async fetchPredictions() {
            try {
                const response = await fetch('http://127.0.0.1:8000/predict/2023-06-14');
                const data = await response.json();
                this.predictions = data.predictions;
                this.renderPins();
                // show in log
                console.log(this.predictions);
            } catch (error) {
                console.error('Error fetching predictions:', error);
            }
        },
        renderPins() {
            // Remove any existing pins
            const pins = document.querySelectorAll('.pin');
            pins.forEach(pin => pin.remove());

            // Render new pins based on predictions
            this.predictions.forEach((value, index) => {
                const pin = document.createElement('div');
                pin.className = 'pin';
                pin.style.backgroundColor = this.getPinColor(value).color;

                const pinLabel = document.createElement('div');
                pinLabel.className = 'pin-label';
                pinLabel.textContent = this.getPinColor(value).label;

                pin.appendChild(pinLabel);

                // Set position of the pin dynamically
                let top, left;
                switch (index) {
                    case 4:
                        top = '35%';
                        left = '20%';
                        break;
                    case 5:
                        top = '38%';
                        left = '15%';
                        break;
                    case 2:
                        top = '85%';
                        left = '15%';
                        break;
                    case 3:
                        top = '40%';
                        left = '35%';
                        break;
                    case 0:
                        top = '57%';
                        left = '55%';
                        break;
                    case 1:
                        top = '33%';
                        left = '60%';
                        break;
                    // Add more cases here if needed
                    default:
                        break;
                }
                pin.style.top = top;
                pin.style.left = left;

                document.querySelector('.map-container').appendChild(pin);
            });
        },
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
