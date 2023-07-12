from time import sleep
import Scenario1
import Scenario2
from io import TextIOWrapper
import gpustat
import psutil

def GetCpuStatus() -> str:
    percs = psutil.cpu_percent(percpu=True)
    res = "CPU Util : "
    for (i,p) in enumerate(percs):
        res += "[CORE({}) {}%]\t".format(i,p)
    try:
        temps = psutil.sensors_temperatures()["coretemp"]
        for (i,t) in enumerate(temps):
            res += "[UNIT({}) {}C]\t".format(i,t)
    except:
        temps = "N/A"
    res += "\nCPU Temps : "
    return res

def GetGpuStatus() -> str:
    info = gpustat.GPUStatCollection[0].new_query().jsonify()["gpus"]
    res = ""
    for gpu in info:
        res += "{} : {}Mb - {}% - {}C".format(gpu["name"],gpu["memory.used"],gpu["utilization.gpu"],gpu["temperature.gpu"])
    return res

def CreateLogFile()->TextIOWrapper:
    fileTmp = open("./result.txt",mode="w")
    fileTmp.write("Run,Scenario,Unit,Unit Load,Response Time (ms),Average\n")
    return fileTmp

csvFile = CreateLogFile()

scenCpuList = []
scenGpuList = []

def ExecuteScen15TimesWithResult(round):
    cpuLoad = psutil.cpu_percent(percpu=False)
    gpuLoad = gpustat.GPUStatCollection[0].new_query().jsonify()["gpus"][0]["utilization.gpu"]

    cpuTime = Scenario1.ExecuteCpuWithResult() * 100
    gpuTime = Scenario1.ExecuteGpuWithResult() * 100

    scenCpuList.append(cpuTime)
    scenGpuList.append(gpuTime)

    cpuText = "{0},{1},{2},{3},{4}\n".format(round,"No.1","CPU",cpuLoad,cpuTime,"-")
    gpuText = "{0},{1},{2},{3},{4}\n".format(round,"No.1","GPU",gpuLoad,gpuTime,"-")
    
    csvFile.write(cpuText)
    csvFile.write(gpuText)

    print("{0} of scenario 1...".format(round))

def ExecuteScen25TimesWithResult(round):
    cpuLoad = psutil.cpu_percent(percpu=False)
    gpuLoad = gpustat.GPUStatCollection[0].new_query().jsonify()["gpus"][0]["utilization.gpu"]

    cpuTime = Scenario2.ExecuteCpuWithResult() * 100
    gpuTime = Scenario2.ExecuteGpuWithResult() * 100

    scenCpuList.append(cpuTime)
    scenGpuList.append(gpuTime)

    cpuText = "{0},{1},{2},{3},{4}\n".format(round,"No.2","CPU",cpuLoad,cpuTime,"-")
    gpuText = "{0},{1},{2},{3},{4}\n".format(round,"No.2","GPU",gpuLoad,gpuTime,"-")
    
    csvFile.write(cpuText)
    csvFile.write(gpuText)

    print("{0} of scenario 2...".format(round))

print(GetCpuStatus())
print(GetGpuStatus())

print("Evaluating Scenario1...")
for i in range(5):
    ExecuteScen15TimesWithResult(i)
    sleep(2)

csvFile.write("AVG,No.1,CPU,-,-,{0}\n".format(sum(scenCpuList)/len(scenCpuList)))
csvFile.write("AVG,No.1,GPU,-,-,{0}\n".format(sum(scenGpuList)/len(scenGpuList)))

print("Scenario 1 has been completed")

print("Evaluating Scenario2...")
scenCpuList = []
scenGpuList = []
for i in range(5):
    ExecuteScen25TimesWithResult(i)
    sleep(2)

csvFile.write("AVG,No.2,CPU,-,-,{0}\n".format(sum(scenCpuList)/len(scenCpuList)))
csvFile.write("AVG,No.2,GPU,-,-,{0}\n".format(sum(scenGpuList)/len(scenGpuList)))

print("Scenario 2 has been completed.")