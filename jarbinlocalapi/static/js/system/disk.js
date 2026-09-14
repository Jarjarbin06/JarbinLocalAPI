async function updateDisk() {
    try {
        const response = await fetch("/api/system/disk?meta=false");

        if (!response.ok) {
            throw new Error(`HTTP ${response.status}`);
        }

        const disk = await response.json();


        // Disk usage
        for (const [name, value] of Object.entries(disk.usage)) {
            const element = document.getElementById(`disk-usage-${name}`);

            if (element) {
                element.textContent = value;
            }
        }


        // Disk usage percentage
        const usageBar = document.getElementById("disk-usage-bar");

        if (usageBar) {
            usageBar.style.width =
                `${disk.usage.percent}%`;
        }


        // Partitions
        for (const partition of disk.partitions) {
            const mountpoint =
                document.getElementById(
                    `disk-partition-${partition.mountpoint}`
                );

            if (mountpoint) {
                mountpoint.textContent =
                    partition.percent;
            }
        }


        // Disk I/O
        for (const [name, counter] of Object.entries(disk.io)) {
            for (const [field, value] of Object.entries(counter)) {
                const element =
                    document.getElementById(
                        `disk-io-${name}-${field}`
                    );

                if (element) {
                    element.textContent = value;
                }
            }
        }

    } catch (error) {
        console.error("Failed to update disk:", error);
    }
}


// Update immediately
updateDisk();

// Update every second
setInterval(updateDisk, 1000);
