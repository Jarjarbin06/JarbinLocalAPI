async function updateOverview() {
    try {
        const response = await fetch("/api/system");

        if (!response.ok) {
            throw new Error(`HTTP ${response.status}`);
        }

        const system = await response.json();


        // ============================================================
        // CPU
        // ============================================================

        document.getElementById("overview-cpu-percent").textContent =
            `${system.cpu.percent}%`;

        document.getElementById("overview-cpu-usage-bar").style.width =
            `${system.cpu.percent}%`;

        document.getElementById("overview-cpu-count").textContent =
            system.cpu.count;

        document.getElementById("overview-cpu-frequency").textContent =
            `${system.cpu.frequency.current} MHz`;

        document.getElementById("overview-cpu-load").textContent =
            system.cpu.load[0];


        // ============================================================
        // MEMORY
        // ============================================================

        document.getElementById("overview-memory-percent").textContent =
            `${system.memory.virtual.percent}%`;

        document.getElementById("overview-memory-usage-bar").style.width =
            `${system.memory.virtual.percent}%`;

        document.getElementById("overview-memory-used").textContent =
            system.memory.virtual.used;

        document.getElementById("overview-memory-available").textContent =
            system.memory.virtual.available;

        document.getElementById("overview-memory-total").textContent =
            system.memory.virtual.total;

        document.getElementById("overview-swap-percent").textContent =
            `${system.memory.swap.percent}%`;


        // ============================================================
        // STORAGE
        // ============================================================

        const diskContainer =
            document.getElementById("overview-disk");

        diskContainer.innerHTML = "";

        for (const disk of system.disk.usage) {
            const row = document.createElement("div");
            row.className = "row";

            row.innerHTML = `
                <span>
                    <strong>${disk.mountpoint}</strong>
                </span>

                <strong>
                    ${disk.percent}%
                </strong>
            `;

            const bar = document.createElement("div");
            bar.className = "bar";

            const fill = document.createElement("div");
            fill.className = "bar-fill";
            fill.style.width = `${disk.percent}%`;

            bar.appendChild(fill);

            diskContainer.appendChild(row);
            diskContainer.appendChild(bar);
        }


        // ============================================================
        // NETWORK
        // ============================================================

        const networkContainer =
            document.getElementById("overview-network");

        networkContainer.innerHTML = "";

        for (
            const [interfaceName, status]
            of Object.entries(system.network.interface_status)
        ) {
            const row = document.createElement("div");
            row.className = "row";

            row.innerHTML = `
                <span>
                    ${interfaceName}
                </span>

                <strong>
                    ${status.isup ? "UP" : "DOWN"}
                </strong>
            `;

            networkContainer.appendChild(row);
        }


        // ============================================================
        // PROCESSES
        // ============================================================

        document.getElementById("overview-process-count").textContent =
            system.processes.count;


        // ============================================================
        // SYSTEM
        // ============================================================

        document.getElementById("overview-system-boot-time").textContent =
            system.system.boot_time;

        document.getElementById("overview-system-users").textContent =
            system.system.users.length;


        // ============================================================
        // BATTERY
        // ============================================================

        const batteryPercent =
            document.getElementById("overview-battery-percent");

        if (batteryPercent && system.sensors.battery) {
            batteryPercent.textContent =
                `${system.sensors.battery.percent}%`;

            document.getElementById("overview-battery-bar").style.width =
                `${system.sensors.battery.percent}%`;

            document.getElementById("overview-battery-status").textContent =
                system.sensors.battery.power_plugged
                    ? "Charging / Plugged"
                    : "On battery";

            document.getElementById("overview-battery-time").textContent =
                system.sensors.battery.secsleft;
        }


        // ============================================================
        // TEMPERATURES
        // ============================================================

        const temperaturesContainer =
            document.getElementById("overview-temperatures");

        temperaturesContainer.innerHTML = "";

        const temperatures =
            system.sensors.temperatures;

        if (Object.keys(temperatures).length === 0) {
            temperaturesContainer.innerHTML = `
                <span class="muted">
                    No temperature sensors available.
                </span>
            `;
        } else {
            for (
                const [sensor, entries]
                of Object.entries(temperatures)
            ) {
                const heading = document.createElement("h3");
                heading.textContent = sensor;

                temperaturesContainer.appendChild(heading);

                for (const temperature of entries) {
                    const row = document.createElement("div");
                    row.className = "row";

                    const label =
                        temperature.label || "Temperature";

                    row.innerHTML = `
                        <span>
                            ${label}
                        </span>

                        <strong>
                            ${temperature.current}°C
                        </strong>
                    `;

                    temperaturesContainer.appendChild(row);
                }
            }
        }


        // ============================================================
        // TOP PROCESSES
        // ============================================================

        const processesContainer =
            document.getElementById("overview-processes");

        processesContainer.innerHTML = "";

        for (const process of system.processes.processes) {
            const item = document.createElement("li");

            item.innerHTML = `
                <div class="row">
                    <span>
                        <strong>${process.name}</strong>

                        <span class="muted">
                            (PID ${process.pid})
                        </span>
                    </span>

                    <strong>
                        ${process.cpu_percent}% CPU
                    </strong>
                </div>

                <div class="label">
                    Memory: ${process.memory_percent}%
                    · Status: ${process.status}
                </div>
            `;

            processesContainer.appendChild(item);
        }

    } catch (error) {
        console.error("Failed to update System Overview:", error);
    }
}


// Update immediately
updateOverview();

// Update every second
setInterval(updateOverview, 1000);
