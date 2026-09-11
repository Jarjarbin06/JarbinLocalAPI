async function updateProcesses() {
    try {
        const response = await fetch("/api/system/processes");

        if (!response.ok) {
            throw new Error(`HTTP ${response.status}`);
        }

        const processes = await response.json();


        // Process count
        document.getElementById("process-count").textContent =
            processes.count;


        // Process information
        for (const process of processes.processes) {
            const cpu =
                document.getElementById(
                    `process-${process.pid}-cpu`
                );

            if (cpu) {
                cpu.textContent =
                    `${process.cpu_percent}% CPU`;
            }


            const status =
                document.getElementById(
                    `process-${process.pid}-status`
                );

            if (status) {
                status.textContent =
                    process.status;
            }


            const memory =
                document.getElementById(
                    `process-${process.pid}-memory`
                );

            if (memory) {
                memory.textContent =
                    `${process.memory_percent}%`;
            }
        }

    } catch (error) {
        console.error("Failed to update processes:", error);
    }
}


// Update immediately
updateProcesses();

// Update every second
setInterval(updateProcesses, 1000);
