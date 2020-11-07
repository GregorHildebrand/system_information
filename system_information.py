# Copyright (c) 2020 Gregor Hildebrand

import psutil
import platform

print("*"*15+" System Information "+"*"*15)
print("Operating System: "+platform.uname()[0])
print("Computer Network Name: "+platform.uname()[1])
print("Operating System Release: "+platform.uname()[2])
print("Operating System Version: "+platform.uname()[3])
print("Machine Type: "+platform.uname()[4])
print("Processor: "+platform.uname()[5])
print("Architecture: "+str(platform.architecture()))
print("*"*15+" CPU Information "+"*"*15)
print(f"Number of physical cpu-cores: {psutil.cpu_count(logical=False)}")
print(f"Number of logical cpu-cores: {psutil.cpu_count(logical=True)}")
print(f"Minimum cpu frequency: {psutil.cpu_freq().min}")
print(f"Maximum cpu frequency: {psutil.cpu_freq().max}")
print(f"Current cpu frequency: {psutil.cpu_freq().current}")

print("*"*15+" RAM Information "+"*"*15)
print(f"RAM total (exclusive swap): {psutil.virtual_memory().total/(1024*1024*1024):.4} GB")
print(f"RAM available for processes (without swap): {psutil.virtual_memory().available/(1024*1024*1024):.4} GB")
print(f"RAM currently used: {psutil.virtual_memory().used/(1024*1024*1024):.4} GB")
print(f"RAM remaining: {psutil.virtual_memory().free/(1024*1024*1024):.4} GB")
print(f"Swap total: {psutil.swap_memory().total/(1024*1024*1024):.4} GB")
print(f"Swap free: {psutil.swap_memory().free/(1024*1024*1024):.4} GB")
print(f"Swap currently used: {psutil.swap_memory().used/(1024*1024*1024):.4} GB")

print("*"*15+" Disk Information "+"*"*15)
for i in range(len(psutil.disk_partitions())):
	print(f"Disk partition {i}: Device: {psutil.disk_partitions()[i].device}, Mountpoint: {psutil.disk_partitions()[i].mountpoint},"
		  f" Filesystem: {psutil.disk_partitions()[i].fstype}, Options: {psutil.disk_partitions()[i].opts}")
	print(f"Disk partition {i} Total Usage: {psutil.disk_usage(psutil.disk_partitions()[i].device).total/(1024*1024*1024):.6} GB")
	print(f"Disk partition {i} Current Usage: {psutil.disk_usage(psutil.disk_partitions()[i].device).used/(1024*1024*1024):.6} GB")
	print(f"Disk partition {i} Remaining Usage: {psutil.disk_usage(psutil.disk_partitions()[i].device).free/(1024*1024* 1024):.6} GB")
	print(f"Disk partition {i} Usage in percentage: {psutil.disk_usage(psutil.disk_partitions()[i].device).percent}")
	print("*"*15)

print("*"*15+" Network Information "+"*"*15)
for i in range(len(psutil.net_connections())):
	print(f"Net-Adapter {i} family: {psutil.net_connections('all')[i].family._name_}, value: {psutil.net_connections('all')[i].family._value_}")
	print(f"Net-Adapter {i} type: {psutil.net_connections('all')[i].type._name_}, value: {psutil.net_connections('all')[i].type._value_}")
	# print(f"{psutil.net_connections('all')[i].family._member_map_}")
	# print(f"{psutil.net_connections('all')[i].family._member_names_}")
	print(f"Net-Adapter {i} local address: {psutil.net_connections('all')[i].laddr}")
	print(f"Net-Adapter {i} remote address: {psutil.net_connections('all')[i].raddr}")
	print(f"Net-Adapter {i} status (of TCP connection): {psutil.net_connections('all')[i].status}")
	print(f"Net-Adapter {i} Process ID (PID): {psutil.net_connections('all')[i].pid}")
	print("*"*15)