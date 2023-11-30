import subprocess


def processFile(path):
    try:
        subprocess.run(['pianoplayer', path])
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
