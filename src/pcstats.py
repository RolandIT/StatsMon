import psutil
import math

def getStats():
    #dictionary to hold all the current resource stats
    stats = {}

    stats["cpu_count_logical"] = psutil.cpu_count()
    stats["cpu_count_physical"] = psutil.cpu_count(logical=False)
    stats["cpu_freq_current"] = psutil.cpu_freq().current
    stats["cpu_load_1sec"] = psutil.cpu_percent(interval=1)

    ramStats = psutil.virtual_memory()
    stats["ram_total"] = math.floor(((ramStats.total)/ 1024**3) * 100)/100
    stats["ram_load"] = ramStats.percent
    stats["ram_free"] = math.floor(((ramStats.free)/ 1024**3) * 100)/100
    stats["ram_used"] = math.floor(((ramStats.used)/ 1024**3) * 100)/100

    diskStats = psutil.disk_usage('/')
    stats["disk_total"] = math.floor(((diskStats.total)/ 1024**3) * 100)/100
    stats["disk_free"] = math.floor(((diskStats.free)/ 1024**3) * 100)/100
    stats["disk_load"] = diskStats.percent
    stats["disk_used"] = math.floor(((diskStats.used)/ 1024**3) * 100)/100
    print(psutil.virtual_memory())
    return stats
