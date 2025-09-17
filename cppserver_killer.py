import wmi
import psutil

# Target description from Task Manager
TARGET_DESCRIPTION = "vcpkgsrv.exe"

def kill_processes_by_description(description):
    c = wmi.WMI()
    killed = []

    for process in c.Win32_Process():
        if process.Name and process.Name.lower() == description.lower():
            try:
                psutil.Process(process.ProcessId).kill()
                killed.append(process.ProcessId)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
    return killed

if __name__ == "__main__":
    killed_pids = kill_processes_by_description(TARGET_DESCRIPTION)
    if killed_pids:
        print(f"Killed processes with PIDs: {killed_pids}")
    else:
        print("No matching processes found.")
