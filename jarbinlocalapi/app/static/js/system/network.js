async function updateNetwork() {
    try {
        const response = await fetch("/api/system/network");

        if (!response.ok) {
            throw new Error(`HTTP ${response.status}`);
        }

        const network = await response.json();


        // Interfaces
        for (const [name, addresses] of Object.entries(network.interfaces)) {
            for (const [index, address] of addresses.entries()) {
                const element =
                    document.getElementById(
                        `network-interface-${name}-${index}`
                    );

                if (element) {
                    element.textContent =
                        address.address;
                }
            }
        }


        // Interface status
        for (const [name, status] of Object.entries(
            network.interface_status
        )) {
            const statusElement =
                document.getElementById(
                    `network-status-${name}`
                );

            if (statusElement) {
                statusElement.textContent =
                    status.isup ? "UP" : "DOWN";
            }


            const speedElement =
                document.getElementById(
                    `network-speed-${name}`
                );

            if (speedElement) {
                speedElement.textContent =
                    `${status.speed} Mbps`;
            }


            const mtuElement =
                document.getElementById(
                    `network-mtu-${name}`
                );

            if (mtuElement) {
                mtuElement.textContent =
                    status.mtu;
            }
        }


        // Network I/O
        for (const [name, counter] of Object.entries(network.io)) {
            for (const [field, value] of Object.entries(counter)) {
                const element =
                    document.getElementById(
                        `network-io-${name}-${field}`
                    );

                if (element) {
                    element.textContent = value;
                }
            }
        }


        // Connections
        for (const [index, connection] of network.connections.entries()) {
            for (const [name, value] of Object.entries(connection)) {
                const element =
                    document.getElementById(
                        `network-connection-${index}-${name}`
                    );

                if (element) {
                    element.textContent = value;
                }
            }
        }

    } catch (error) {
        console.error("Failed to update network:", error);
    }
}


// Update immediately
updateNetwork();

// Update every second
setInterval(updateNetwork, 1000);
