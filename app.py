from flask import Flask, request
import subprocess

app = Flask(__name__)
port = 3000

@app.route('/new', methods=['POST'])
def create_folder():
    # take folder name from query string
    folder_name = request.args.get('foldername')
    cmd = f"mkdir {folder_name}"

    print(f"Executing command: {cmd}")

    if not cmd:
        return "No command provided", 400

    try:
        # Use subprocess to execute the command
        result = subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(f"Command output: {result.stdout}")
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
        return "Error executing command", 500

if __name__ == '__main__':
    app.run(port=port)

