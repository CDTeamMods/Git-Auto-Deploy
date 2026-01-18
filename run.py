import sys
import os
import subprocess

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))

def add_to_startup():
    """Adds current script to crontab to start on boot"""
    if os.name == 'nt':
        print("⚠️  Error: This feature is designed for Linux systems (crontab).")
        return

    python_path = sys.executable
    script_path = os.path.realpath(__file__)
    # Command to be executed on boot
    command = f"{python_path} {script_path}"
    # Crontab line
    cron_job = f"@reboot {command}"
    
    print(f"🔄 Attempting to add to crontab: {cron_job}")

    try:
        # Read current crontab
        try:
            current_cron = subprocess.check_output(["crontab", "-l"], stderr=subprocess.PIPE).decode()
        except subprocess.CalledProcessError:
            current_cron = "" # User has no crontab yet or error reading
        
        # Check if command already exists in crontab (simple check)
        if command in current_cron:
            print("✅ The script is already configured to start on boot.")
            return

        # Add new job
        new_cron = current_cron.rstrip() + "\n" + cron_job + "\n"
        
        # Write new crontab
        process = subprocess.Popen(["crontab", "-"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate(input=new_cron.encode())
        
        if process.returncode == 0:
            print("🚀 Success! Added to crontab.")
            print("📋 Use 'crontab -l' to verify.")
        else:
            print(f"❌ Error updating crontab: {stderr.decode()}")

    except Exception as e:
        print(f"❌ Unexpected error configuring startup: {e}")

try:
    from gitautodeploy import main
except ImportError as e:
    print(f"Error importing gitautodeploy: {e}")
    print("Check if dependencies are installed: pip install -r requirements.txt")
    sys.exit(1)

if __name__ == '__main__':
    # Check startup argument
    if len(sys.argv) > 1 and sys.argv[1] in ['startup', '--startup']:
        add_to_startup()
        sys.exit(0)

    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupted by user.")
        sys.exit(0)
    except Exception as e:
        print(f"Fatal error: {e}")
        sys.exit(1)
