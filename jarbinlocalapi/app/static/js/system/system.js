async function updateSystem() {
    try {
        const response = await fetch("/api/system/system");

        if (!response.ok) {
            throw new Error(`HTTP ${response.status}`);
        }

        const system = await response.json();


        // Boot time
        document.getElementById("system-boot-time").textContent =
            system.boot_time;


        // Users
        const users = document.getElementById("system-user-count");

        if (users) {
            users.textContent =
                system.users.length;
        }


        // User information
        for (const [index, user] of system.users.entries()) {
            for (const [name, value] of Object.entries(user)) {
                const element =
                    document.getElementById(
                        `system-user-${index}-${name}`
                    );

                if (element) {
                    element.textContent = value;
                }
            }
        }

    } catch (error) {
        console.error("Failed to update system:", error);
    }
}


// Update immediately
updateSystem();

// Update every second
setInterval(updateSystem, 1000);
