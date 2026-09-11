async function updateTopProcesses() {
    try {
        const response =
            await fetch("/api/system/processes?category=processes");

        if (!response.ok) {
            throw new Error(`HTTP ${response.status}`);
        }

        const data = await response.json();

        const processes = [...data.processes]
            .sort((a, b) => b.cpu_percent - a.cpu_percent)
            .slice(0, 10);

        for (const [index, process] of processes.entries()) {

            const name =
                document.getElementById(
                    `top-process-${index}-name`
                );

            if (name) {
                name.textContent =
                    process.name;
            }

            const pid =
                document.getElementById(
                    `top-process-${index}-pid`
                );

            if (pid) {
                pid.textContent =
                    `PID ${process.pid}`;
            }

            const cpu =
                document.getElementById(
                    `top-process-${index}-cpu`
                );

            if (cpu) {
                cpu.textContent =
                    `${process.cpu_percent}% CPU`;
            }

            const memory =
                document.getElementById(
                    `top-process-${index}-memory`
                );

            if (memory) {
                memory.textContent =
                    `${process.memory_percent}%`;
            }

            const status =
                document.getElementById(
                    `top-process-${index}-status`
                );

            if (status) {
                status.textContent =
                    process.status;
            }
        }

    } catch (error) {
        console.error("Failed to update top processes:", error);
    }
}


// Update immediately
updateTopProcesses();

// Update every second
setInterval(updateTopProcesses, 1000);
