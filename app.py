import subprocess


def keep_system_awake():
    try:
        subprocess.run(["caffeinate", "-d"])
    except KeyboardInterrupt:
        print("Sleep app is oof!")


if __name__ == "__main__":
    keep_system_awake() 
