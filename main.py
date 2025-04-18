import os
import subprocess
from datetime import datetime

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Check if we should use the combined script or the separate ones
    combined_script = os.path.join(script_dir, "extract_number.py")
    
    if os.path.exists(combined_script):
        print("Running combined detection and extraction script...")
        subprocess.run(["python", combined_script])
    else:
        # Fallback to running separate scripts if combined version doesn't exist
        print("Combined script not found, running separate scripts...")
        detect_script = os.path.join(script_dir, "detect.py")
        extract_script = os.path.join(script_dir, "extract_number.py")
        
        if os.path.exists(detect_script):
            print("Running detect.py...")
            subprocess.run(["python", detect_script])
        else:
            print("Error: detect.py not found!")
            return
        
        if os.path.exists(extract_script):
            print("Running extract_number.py...")
            subprocess.run(["python", extract_script])
        else:
            print("Error: extract_number.py not found!")
            return
    
    print(f"Processing completed at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    main()