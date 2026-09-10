async function updateCPU() {
    try {
        const response = await fetch("/api/system/cpu");

        if (!response.ok) {
            throw new Error(`HTTP ${response.status}`);
        }

        const cpu = await response.json();

        // Usage
        document.getElementById("cpu-percent").textContent =
            `${cpu.percent}%`;

        document.getElementById("cpu-usage-bar").style.width =
            `${cpu.percent}%`;


        // CPU count
        document.getElementById("cpu-count").textContent =
            cpu.count;


        // Frequency
        document.getElementById("cpu-frequency-current").textContent =
            `${cpu.frequency.current} MHz`;

        document.getElementById("cpu-frequency-min").textContent =
            `${cpu.frequency.min} MHz`;

        document.getElementById("cpu-frequency-max").textContent =
            `${cpu.frequency.max} MHz`;


        // Load average
        document.getElementById("cpu-load-1").textContent =
            cpu.load[0];

        document.getElementById("cpu-load-5").textContent =
            cpu.load[1];

        document.getElementById("cpu-load-15").textContent =
            cpu.load[2];


        // CPU times
        for (const [name, value] of Object.entries(cpu.times)) {
            const element = document.getElementById(`cpu-time-${name}`);

            if (element) {
                element.textContent = value;
            }
        }


        // CPU times percent
        for (const [name, value] of Object.entries(cpu.times_percent)) {
            const element = document.getElementById(`cpu-time-percent-${name}`);

            if (element) {
                element.textContent = `${value}%`;
            }
        }


        // CPU statistics
        for (const [name, value] of Object.entries(cpu.stats)) {
            const element = document.getElementById(`cpu-stat-${name}`);

            if (element) {
                element.textContent = value;
            }
        }

    } catch (error) {
        console.error("Failed to update CPU:", error);
    }
}


// Update immediately
updateCPU();

// Update every second
setInterval(updateCPU, 1000);
