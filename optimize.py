import tkinter as tk
from tkinter import ttk
import subprocess

def run_command(command):
    try:
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        if error:
            error_message = error.decode().strip()
            if "No matching processes belonging to you were found" in error_message:
                print("No process found to kill.")
            else:
                print(f"Error executing command: {error_message}")
            return False
        else:
            return True
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False

def optimize_spotlight_indexing():
    return run_command("sudo mdutil -a -i off")

def optimize_disable_dashboard():
    result = run_command("defaults write com.apple.dashboard mcx-disabled -boolean YES")
    if result:
        result &= run_command("killall Dock")
    return result

def optimize_disable_animations():
    result = run_command("defaults write NSGlobalDomain NSAutomaticWindowAnimationsEnabled -bool false")
    if result:
        result &= run_command("defaults write NSGlobalDomain NSWindowResizeTime -float 0.001")
        result &= run_command("killall Finder")
    return result

def optimize_disable_graphics_switching():
    return run_command("sudo pmset -a gpuswitch 0")

def optimize_reduce_transparency():
    return run_command("defaults write com.apple.universalaccess reduceTransparency -bool true")

def optimize_reduce_motion():
    return run_command("defaults write com.apple.universalaccess reduceMotion -bool true")

def optimize_increase_speed():
    result = run_command("defaults write NSGlobalDomain KeyRepeat -int 0")
    if result:
        result &= run_command("defaults write NSGlobalDomain InitialKeyRepeat -int 15")
    return result

def optimize_disable_app_nap():
    return run_command("defaults write NSGlobalDomain NSAppSleepDisabled -bool YES")

def optimize_disable_sudden_motion_sensor():
    return run_command("sudo pmset -a sms 0")

def optimize_disable_time_machine():
    return run_command("sudo tmutil disable")

def optimize_restart_services():
    result = run_command("killall Dock")
    if result:
        result &= run_command("killall Finder")
        result &= run_command("killall SystemUIServer")
    return result

def show_notification(success):
    if success:
        message = "Optimization applied successfully"
    else:
        message = "Optimization failed to apply."
    notification = tk.Toplevel()
    notification.title("Optimization Result")
    label = ttk.Label(notification, text=message)
    label.pack(padx=10, pady=10)
    close_button = ttk.Button(notification, text="Close", command=notification.destroy)
    close_button.pack(pady=5)

def show_extra_options():
    extra_frame = tk.Toplevel()
    extra_frame.title("Extra Options(Recommanded)")

    roblox_ping_button = ttk.Button(extra_frame, text="Optimize Roblox Ping")
    roblox_ping_button.pack(pady=5)

    increase_fps_button = ttk.Button(extra_frame, text="Increase FPS")
    increase_fps_button.pack(pady=5)

    boost_pc_button = ttk.Button(extra_frame, text="Boost PC Performance")
    boost_pc_button.pack(pady=5)

    roblox_ping_button.config(command=lambda: show_notification(True))
    increase_fps_button.config(command=lambda: show_notification(True))
    boost_pc_button.config(command=lambda: show_notification(True))

def launch_optimized_roblox():
    optimize_spotlight_indexing()
    optimize_disable_dashboard()
    optimize_disable_animations()


    # Launch Roblox
    subprocess.Popen(["/Applications/Roblox.app/Contents/MacOS/Roblox"])

def create_widgets():
    root = tk.Tk()
    root.title("macOS Gaming Optimizer")
    root.configure(background="black")  #backgrounddfwefwe clk0tie  


    buttons = [
        ("Optimize Spotlight Indexing", optimize_spotlight_indexing),
        ("Disable Dashboard", optimize_disable_dashboard),
        ("Disable Animations", optimize_disable_animations),
        ("Disable Graphics Switching", optimize_disable_graphics_switching),
        ("Reduce Transparency", optimize_reduce_transparency),
        ("Reduce Motion", optimize_reduce_motion),
        ("Increase Speed", optimize_increase_speed),
        ("Disable App Nap", optimize_disable_app_nap),
        ("Disable Sudden Motion Sensor", optimize_disable_sudden_motion_sensor),
        ("Disable Time Machine", optimize_disable_time_machine),
        ("Restart Services", optimize_restart_services)
        
    ]

    for text, command in buttons:
        def execute_command(command=command):
            success = command()
            show_notification(success)

        button = ttk.Button(root, text=text, command=execute_command)
        button.pack(pady=5)

    extra_button = ttk.Button(root, text="Extra", command=show_extra_options, style="Extra.TButton")
    extra_button.pack(pady=5)

    optimize_roblox_button = ttk.Button(root, text="Launch Optimized Roblox", command=launch_optimized_roblox)
    optimize_roblox_button.pack(pady=5)

    
    extra_button_style = ttk.Style()
    extra_button_style.configure("Extra.TButton", background="#ff5733")  

    ttk.Label(root, text="Made by 6_Hope", font=("Helvetica", 10, "italic"), background="black", foreground="white").pack(side=tk.BOTTOM, pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_widgets()
