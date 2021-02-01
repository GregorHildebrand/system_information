# developed in November 2020 Gregor Hildebrand

import psutil
import platform
import os

try:
	# for using python 3.x
	import tkinter as tk
	import tkinter.scrolledtext
except ImportError:
	# for using python 2.x
	import Tkinter as tk
	import Tkinter.scrolledtext


class NewWindow(tk.Toplevel):
	def __init__(self, master=None):
		super().__init__(master=master)
		self.title("New Window")
		self.geometry("200x200")

class Print_SysInfo(tk.Toplevel):
	def __init__(self, master=None):
		super().__init__(master=master)
		self.title("System Information")
		self.geometry("400x200")
		comp_name = tk.Label(self, text="Name of computer: " + platform.node()).pack()
		comp_username = tk.Label(self, text="Username: " + os.getlogin()).pack()
		op_sys_and_release = tk.Label(self, text="Operating System: " + platform.uname().system + " " + platform.uname().release).pack()
		os_release_version = tk.Label(self, text="Operating System Version: " + platform.uname().version).pack()
		bit_arch = tk.Label(self, text="Bit Architecture: " + str(platform.architecture()[0])).pack()
		linkage_format = tk.Label(self, text="Linkage format used for executable: " + str(platform.architecture()[1])).pack()
		# print(os.environ["COMSPEC"]) -> returns path to cmd.exe under Windows
		# print(os.environ["USERPROFILE"]) returns path to c:\users\$user$ under Windows

class Print_ProcInfo(tk.Toplevel):
	def __init__(self, master=None):
		super().__init__(master=master)
		self.title("Processor Information")
		self.geometry("400x200")
		proc_identifier = tk.Label(self, text="Identifier of processor: " + platform.uname().processor).pack()
		machine_type = tk.Label(self, text="Machine Type: " + platform.machine()).pack()
		physical_cpu_cores = tk.Label(self, text="Number of physical CPU cores: "+ str(psutil.cpu_count(logical=False))).pack()
		logical_cpu_cores = tk.Label(self, text="Number of logical CPU cores: " + str(psutil.cpu_count(logical=True))).pack()
		min_proc_freq = tk.Label(self, text="Minimum CPU frequency: " + str(psutil.cpu_freq().min)).pack()
		max_proc_freq = tk.Label(self, text="Maximum CPU frequency: " + str(psutil.cpu_freq().max)).pack()
		curr_cpu_freq = tk.Label(self, text="Current CPU frequency: " + str(psutil.cpu_freq().current)).pack()

class Print_RAMInfo(tk.Toplevel):
	def __init__(self, master=None):
		super().__init__(master=master)
		self.title("RAM Information")
		self.geometry("400x200")
		tk.Label(self, text="RAM total (exclusive swap): {:.4}".format(psutil.virtual_memory().total / (1024 * 1024 * 1024)) + " GB").pack()
		tk.Label(self, text="RAM available for processes (without swap): {:.4}".format(psutil.virtual_memory().available / (1024 * 1024 * 1024)) + " GB").pack()
		tk.Label(self, text="RAM currently used: {:.4}".format(psutil.virtual_memory().used / (1024 * 1024 * 1024)) + " GB").pack()
		tk.Label(self, text="RAM remaining: {:.4}".format(psutil.virtual_memory().free / (1024 * 1024 * 1024)) + " GB").pack()
		tk.Label(self, text="Swap total: {:.4}".format(psutil.swap_memory().total / (1024 * 1024 * 1024)) + " GB").pack()
		tk.Label(self, text="Swap free: {:.4}".format(psutil.swap_memory().free / (1024 * 1024 * 1024)) + " GB").pack()
		tk.Label(self, text="Swap currently used: {:.4}".format(psutil.swap_memory().used / (1024 * 1024 * 1024)) + " GB").pack()

class Print_DiskInfo(tk.Toplevel):
	def __init__(self, master=None):
		super().__init__(master=master)
		self.title("DISK Information")
		self.geometry("500x300")
		for i in range(len(psutil.disk_partitions())):
			tk.Label(self, text=f"Disk partition {i}: Device: {psutil.disk_partitions()[i].device}, Mountpoint: {psutil.disk_partitions()[i].mountpoint}, Filesystem: {psutil.disk_partitions()[i].fstype}, Options: {psutil.disk_partitions()[i].opts}").pack()
			tk.Label(self, text=f"Disk partition {i} Total Usage: {psutil.disk_usage(psutil.disk_partitions()[i].device).total / (1024 * 1024 * 1024):.6} GB").pack()
			tk.Label(self, text=f"Disk partition {i} Current Usage: {psutil.disk_usage(psutil.disk_partitions()[i].device).used / (1024 * 1024 * 1024):.6} GB").pack()
			tk.Label(self, text=f"Disk partition {i} Remaining Usage: {psutil.disk_usage(psutil.disk_partitions()[i].device).free / (1024 * 1024 * 1024):.6} GB").pack()
			tk.Label(self, text=f"Disk partition {i} Current Usage in percentage: {psutil.disk_usage(psutil.disk_partitions()[i].device).percent} {chr(ord('%'))}").pack()
			tk.Label(self, text=f"Disk partition {i} Remaining Usage in percentage: {100.00 - (psutil.disk_usage(psutil.disk_partitions()[i].device).percent)} {chr(ord('%'))}").pack()

def main():
	parent_widget = tk.Tk(className="Tool printing System Information")
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
	btn_printDiskInfo = tk.Button(master=parent_widget, text="Display Disk Info")
	btn_printDiskInfo.bind("<Button>", lambda e: Print_DiskInfo(master=parent_widget))
	btn_printDiskInfo.pack()
	btn_quitProgram = tk.Button(master=parent_widget, text="Quit Program")
	btn_quitProgram.bind("<Button>", lambda e: parent_widget.destroy())
	btn_quitProgram.pack()
	tk.mainloop()

if __name__ == '__main__':
	main()
