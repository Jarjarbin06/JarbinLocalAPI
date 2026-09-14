async function updateTemperatures() {
    try {
        const response =
            await fetch("/api/system/sensors?meta=falsecategory=temperatures");

        if (!response.ok) {
            throw new Error(`HTTP ${response.status}`);
        }

        const data = await response.json();
        const temperatures = data.temperatures;

        for (const [sensor, entries] of Object.entries(temperatures)) {
            for (const [index, temperature] of entries.entries()) {
                const element =
                    document.getElementById(
                        `temperature-${sensor}-${index}`
                    );

                if (element) {
                    element.textContent =
                        `${temperature.current}°C`;
                }
            }
        }

    } catch (error) {
        console.error("Failed to update temperatures:", error);
    }
}


// Update immediately
updateTemperatures();

// Update every second
setInterval(updateTemperatures, 1000);
