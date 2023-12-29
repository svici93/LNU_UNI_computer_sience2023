// Import the 'moment' library

async function populateSensorOptions() {
    const sensorList = document.getElementById('sensorList');

    // Fetch sensor IDs from the server
    try {
        const response = await fetch('/get_sensor_ids');
        const sensorIds = await response.json();

        sensorIds.forEach(sensorId => {
            const sensorOption = document.createElement('div');
            sensorOption.classList.add('sensor-option');
            sensorOption.textContent = `Sensor ${sensorId}`;
            sensorOption.addEventListener('click', () => showSensorDetails(sensorId));
            sensorList.appendChild(sensorOption);
        });
    } catch (error) {
        console.error('Error fetching sensor IDs:', error);
    }
}

async function showSensorDetails(sensorId) {
    const sensorDetails = document.getElementById('sensorDetails');
    const historicalCanvas = document.getElementById('historicalCanvas');

    try {
        // Fetch historical sensor data
        const historicalResponse = await fetch(`/get_sensor_history/${sensorId}`);
        const { history } = await historicalResponse.json();

        // Prepare data for the graph
        const formatted_history = history.map(entry => ({
            normal_light_state: entry.normal_light_state,
            timestamp: new Date(entry.timestamp),
        }));

        // Display current sensor details
        sensorDetails.innerHTML = `
            <h2>Sensor ${sensorId} Details</h2>
            <p>Normal Light State: ${formatted_history[formatted_history.length - 1].normal_light_state}</p>
            <p>Light Out Event: ${formatted_history[formatted_history.length - 1].light_out_event ? 'Yes' : 'No'}</p>
            <p>Last Update: ${formatted_history[formatted_history.length - 1].timestamp.toLocaleString()}</p>
        `;

        // Extract x and y values for Chart.js
        const xValues = formatted_history.map(entry => entry.timestamp);
        const yValues = formatted_history.map(entry => entry.normal_light_state);

        // Draw the graph using Chart.js
        const ctx = historicalCanvas.getContext('2d');
        ctx.clearRect(0, 0, historicalCanvas.width, historicalCanvas.height);

        new Chart(ctx, {
            type: 'line',
            data: {
                labels: xValues.map(time => time.toLocaleTimeString('en-US', { hour: 'numeric', minute: 'numeric', second: 'numeric' })),
                datasets: [{
                    label: 'Normal Light State (LX)',
                    borderColor: 'rgba(75, 192, 192, 1)',
                    borderWidth: 2,
                    data: yValues,
                }],
            },
            options: {
                scales: {
                    x: {
                        type: 'category',
                        position: 'bottom',
                        title: {
                            display: true,
                            text: 'Time of Day',
                        },
                    },
                    y: {
                        title: {
                            display: true,
                            text: 'Normal Light State (LX)',
                        },
                    },
                },
            },
        });
    } catch (error) {
        console.error('Error fetching sensor data:', error);
        sensorDetails.innerHTML = '<p>Error fetching sensor data</p>';
    }
}

// Function to format timestamp in 24-hour format
function formatTimestamp(timestamp) {
    const options = { year: 'numeric', month: '2-digit', day: '2-digit', hour: '2-digit', minute: '2-digit', second: '2-digit' };
    return new Date(timestamp).toLocaleString('en-US', options);
}

// Event listener for initializing sensor options on page load
document.addEventListener('DOMContentLoaded', populateSensorOptions);