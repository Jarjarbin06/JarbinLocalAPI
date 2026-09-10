import psutil


def get_users(
    ) -> list[psutil._ntuples.suser]:
    return psutil.users()
