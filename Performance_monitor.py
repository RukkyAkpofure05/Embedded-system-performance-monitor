import psutil
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


def get_network_speed():
    try:
        net_io = psutil.net_io_counters()
        return (net_io.bytes_sent + net_io.bytes_recv) / 1_000_000  # Mbps
    except:
        return "Error"

def update_stats():
    try:
        cpu = psutil.cpu_percent()
        ram = psutil.virtual_memory().percent
        disk = psutil.disk_usage('/').percent
        net = get_network_speed()

        print(f"Raw data - CPU: {cpu}, RAM: {ram}, Disk: {disk}, Net: {net}")

        cpu_label.config(text=f"CPU: {cpu:.1f}%")
        ram_label.config(text=f"RAM: {ram:.1f}%")
        disk_label.config(text=f"Disk Usage: {disk:.1f}%")
        network_label.config(text=f"Network: {net:.2f} Mbps")
    except Exception as e:
        print(f"Error updating stats: {e}")

    root.after(1000, update_stats)

root = tk.Tk()
root.title("PC Performance Monitor")
root.geometry("200x150")

root.configure(bg='#000000')

# Custom style for labels
style = ttk.Style()
style.configure("Custom.TLabel", foreground="white", background="#000000", font=("Oswald", 12, "bold"))

cpu_label = ttk.Label(root, text="CPU: 0%", style="Custom.TLabel")
cpu_label.pack(pady=5)
ram_label = ttk.Label(root, text="RAM: 0%", style="Custom.TLabel")
ram_label.pack(pady=5)
disk_label = ttk.Label(root, text="Disk Usage: 0%", style="Custom.TLabel")
disk_label.pack(pady=5)
network_label = ttk.Label(root, text="Network: 0 Mbps", style="Custom.TLabel")
network_label.pack(pady=5)

update_stats()
root.mainloop()
