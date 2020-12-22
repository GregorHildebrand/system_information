# developed in November 2020 Gregor Hildebrand

import psutil
import platform
import os

try:
	# for using python 3.x
	import tkinter as tk
except ImportError:
	# for using python 2.x
	import Tkinter as tk


class NewWindow(tk.Toplevel):
	def __init__(self, master=None):
		super().__init__(master=master)
		self.title("New Window")
		self.geometry("300x200")

class Print_SysInfo(tk.Toplevel):
	def __init__(self, master=None):
		super().__init__(master=master)
		self.title("System Information")
		self.geometry("400x200")
		comp_name = tk.Label(self, text="Name of computer: " + os.environ["COMPUTERNAME"]).pack()
		comp_username = tk.Label(self, text="Username: " + os.environ["USERNAME"]).pack()
		o_s = tk.Label(self, text="Operating System: " + platform.uname()[0]).pack()
		o_s_release = tk.Label(self, text="Operating System Release: "+ platform.uname()[2]).pack()
		o_s_version = tk.Label(self, text="Operating System Version: " + platform.uname()[3]).pack()
		bit_arch = tk.Label(self, text="Bit Architecture: " + str(platform.architecture()[0])).pack() # class tuple
		linkage_format = tk.Label(self, text="Linkage format used for executable: " + str(platform.architecture()[1])).pack()
		# print(os.environ["COMSPEC"]) -> returns path to cmd.exe
		# print(os.environ["USERPROFILE"]) returns path to c:\users\$user$

class Print_ProcInfo(tk.Toplevel):
	def __init__(self, master=None):
		super().__init__(master=master)
		self.title("Processor Information")
		self.geometry("400x200")
		proc_identifier = tk.Label(self, text="Identifier of processor: " + os.environ["PROCESSOR_IDENTIFIER"]).pack()
		machine_type = tk.Label(self, text="Machine Type: " + os.environ["PROCESSOR_ARCHITECTURE"]).pack()
		physical_cpu_cores = tk.Label(self, text="Number of physical CPU cores: "+ str(psutil.cpu_count(logical=False))).pack()
		logical_cpu_cores = tk.Label(self, text="Number of logical CPU cores: " + str(psutil.cpu_count(logical=True))).pack()
		min_proc_freq = tk.Label(self, text="Minimum CPU frequency: " + str(psutil.cpu_freq().min)).pack()
		max_proc_freq = tk.Label(self, text="Maximum CPU frequency: " + str(psutil.cpu_freq().max)).pack()
		curr_cpu_freq = tk.Label(self, text="Current CPU frequency: " + str(psutil.cpu_freq().current)).pack()

class Print_RAMInfo(tk.Toplevel):
	def __init__(self, master=None):
		super().__init__(master=master)
		self.title("Processor Information")
		self.geometry("400x200")
		ram_total = tk.Label(self, text="RAM total (exclusive swap): {:.4}".format(psutil.virtual_memory().total / (1024 * 1024 * 1024)) + " GB").pack()
		ram_available = tk.Label(self, text="RAM available for processes (without swap): {:.4}".format(psutil.virtual_memory().available / (1024 * 1024 * 1024)) + " GB").pack()
		ram_curr_used = tk.Label(self, text="RAM currently used: {:.4}".format(psutil.virtual_memory().used / (1024 * 1024 * 1024)) + " GB").pack()
		ram_remaining = tk.Label(self, text="RAM remaining: {:.4}".format(psutil.virtual_memory().free / (1024 * 1024 * 1024)) + " GB").pack()
		swap_total = tk.Label(self, text="Swap total: {:.4}".format(psutil.swap_memory().total / (1024 * 1024 * 1024)) + " GB").pack()
		swap_free = tk.Label(self, text="Swap free: {:.4}".format(psutil.swap_memory().free / (1024 * 1024 * 1024)) + " GB").pack()
		swap_curr_used = tk.Label(self, text="Swap currently used: {:.4}".format(psutil.swap_memory().used / (1024 * 1024 * 1024)) + " GB").pack()

def print_DiskInfo():
	for i in range(len(psutil.disk_partitions())):
		print(f"Disk partition {i}: Device: {psutil.disk_partitions()[i].device}, Mountpoint: {psutil.disk_partitions()[i].mountpoint}, Filesystem: {psutil.disk_partitions()[i].fstype}, Options: {psutil.disk_partitions()[i].opts}")
		print(f"Disk partition {i} Total Usage: {psutil.disk_usage(psutil.disk_partitions()[i].device).total/(1024*1024*1024):.6} GB")
		print(f"Disk partition {i} Current Usage: {psutil.disk_usage(psutil.disk_partitions()[i].device).used/(1024*1024*1024):.6} GB")
		print(f"Disk partition {i} Remaining Usage: {psutil.disk_usage(psutil.disk_partitions()[i].device).free/(1024*1024* 1024):.6} GB")
		print(f"Disk partition {i} Usage in percentage: {psutil.disk_usage(psutil.disk_partitions()[i].device).percent}")
		print("*"*15)

def print_NWInfo():
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

def main():
	parent_widget = tk.Tk(className="Tkinter Tutorial")
	parent_widget.geometry("400x200")
	btn_printSysInfo = tk.Button(master=parent_widget, text="Display System Info")
	btn_printSysInfo.bind("<Button>", lambda e: Print_SysInfo(master=parent_widget))
	# bind() - for binding click event; on any click on the button of mouse a new window appears
	btn_printSysInfo.pack()
	btn_printProcInfo = tk.Button(master=parent_widget, text="Display Processor Info")
	btn_printProcInfo.bind("<Button>", lambda e: Print_ProcInfo(master=parent_widget))
	btn_printProcInfo.pack()
	btn_printRAMInfo = tk.Button(master=parent_widget, text="Display RAM Info")
	btn_printRAMInfo.bind("<Button>", lambda e: Print_RAMInfo(master=parent_widget))
	btn_printRAMInfo.pack()
	tk.mainloop()
	exit()

	print("*"*15+" Disk Information "+"*"*15)
	print_DiskInfo()
	print("*"*15+" Network Information "+"*"*15)
	print_NWInfo()

if __name__ == '__main__':
	main()
