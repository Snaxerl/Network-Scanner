import subprocess
import re
import tkinter as tk
from tkinter import ttk

class NetworkScannerGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Network Scanner")
        self.geometry("400x400")

        
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("TButton", padding=6, relief="flat", background="#007bff", foreground="white")
        self.style.map("TButton", foreground=[("pressed", "white"), ("active", "white")], background=[("pressed", "!disabled", "#0062cc"), ("active", "#0062cc")])
        self.style.configure("TLabel", padding=6, background="#f5f5f5", foreground="#333")
        self.style.configure("TFrame", padding=10, background="#f5f5f5")
        self.style.configure("TListbox", padding=6, background="white", foreground="#333")
        self.style.map("TListbox", background=[("selected", "#007bff"), ("active", "#f5f5f5")])

        
        self.instructions_label = ttk.Label(
            self, text="Click the button to scan for network devices:")
        self.instructions_label.pack(pady=10)

        
        self.scan_button = ttk.Button(
            self, text="Scan", command=self.scan_network_devices)
        self.scan_button.pack()

        
        self.devices_frame = ttk.Frame(self)
        self.devices_frame.pack(pady=10)

      
        self.devices_label = ttk.Label(self.devices_frame, text="Devices:")
        self.devices_label.pack()

       
        self.devices_listbox = tk.Listbox(
            self.devices_frame, width=50, height=10)
        self.devices_listbox.pack()

        
        self.ips_label = ttk.Label(self.devices_frame, text="IP Addresses:")
        self.ips_label.pack()

       
        self.ips_listbox = tk.Listbox(
            self.devices_frame, width=50, height=10)
        self.ips_listbox.pack()

    def scan_network_devices(self):
        
        self.devices_listbox.delete(0, tk.END)
        self.ips_listbox.delete(0, tk.END)

       
        arp_output = subprocess.check_output(["arp", "-a"]).decode()

        
        lines = arp_output.strip().split("\n")
        devices = []
        ips = []
        for line in lines:
            parts = re.split(r'\s+', line)
            if len(parts) >= 2:
                ip_address = parts[1]
                devices.append(parts[0])
                ips.append(ip_address)

       
        for device in devices:
            self.devices_listbox.insert(tk.END, device)
        for ip in ips:
            self.ips_listbox.insert(tk.END, ip)

if __name__ == "__main__":
    app = NetworkScannerGUI()
    app.mainloop()
