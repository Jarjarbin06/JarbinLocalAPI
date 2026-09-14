async function updateBattery() {
    try {
        const response =
            await fetch("/api/system/sensors?meta=falsecategory=battery");

        if (!response.ok) {
            throw new Error(`HTTP ${response.status}`);
        }

        const data = await response.json();
        const battery = data.battery;

        if (!battery) {
            return;
        }

        // Percentage
        const percent =
            document.getElementById("battery-percent");

        if (percent) {
            percent.textContent =
                `${battery.percent}%`;
        }

        // Battery information
        for (const [name, value] of Object.entries(battery)) {
            const element =
                document.getElementById(`battery-${name}`);

            if (element) {
                element.textContent = value;
            }
        }

        // Power status
        const status =
            document.getElementById("battery-status");

        if (status) {
            status.textContent =
                battery.power_plugged
                    ? "Charging / Plugged"
                    : "On battery";
        }

    } catch (error) {
        console.error("Failed to update battery:", error);
    }
}


// Update immediately
updateBattery();

// Update every second
setInterval(updateBattery, 1000);
