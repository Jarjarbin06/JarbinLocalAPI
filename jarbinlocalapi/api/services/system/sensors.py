import psutil


def get_temperatures(
    ) -> dict:
    return psutil.sensors_temperatures()


def get_fans(
    ) -> dict:
    return psutil.sensors_fans()


def get_battery(
    ) -> psutil._ntuples.sbattery | None:
    return psutil.sensors_battery()
