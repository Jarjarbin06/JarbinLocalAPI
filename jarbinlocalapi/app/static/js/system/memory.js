async function updateMemory() {
    try {
        const response = await fetch("/api/system/memory");

        if (!response.ok) {
            throw new Error(`HTTP ${response.status}`);
        }

        const memory = await response.json();


        // Virtual memory
        document.getElementById("memory-percent").textContent =
            `${memory.virtual.percent}%`;

        document.getElementById("memory-usage-bar").style.width =
            `${memory.virtual.percent}%`;

        for (const [name, value] of Object.entries(memory.virtual)) {
            if (name === "percent") {
                continue;
            }

            const element =
                document.getElementById(`memory-virtual-${name}`);

            if (element) {
                element.textContent = value;
            }
        }


        // Swap memory
        document.getElementById("swap-percent").textContent =
            `${memory.swap.percent}%`;

        document.getElementById("swap-usage-bar").style.width =
            `${memory.swap.percent}%`;

        for (const [name, value] of Object.entries(memory.swap)) {
            if (name === "percent") {
                continue;
            }

            const element =
                document.getElementById(`memory-swap-${name}`);

            if (element) {
                element.textContent = value;
            }
        }

    } catch (error) {
        console.error("Failed to update Memory:", error);
    }
}


// Update immediately
updateMemory();

// Update every second
setInterval(updateMemory, 1000);
