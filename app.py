import subprocess
from flask import Flask, render_template, request

app = Flask(__name__)

# Function to list VMs
def list_vms():
    result = subprocess.run(["VBoxManage", "list", "vms"], capture_output=True, text=True)
    vm_names = [line.split('"')[1] for line in result.stdout.splitlines()]
    return vm_names

# Function to start a VM
def start_vm(vm_name):
    subprocess.run(["VBoxManage", "startvm", vm_name])

# Function to stop a VM
def stop_vm(vm_name):
    subprocess.run(["VBoxManage", "controlvm", vm_name, "poweroff"])

# Define the root route to list VMs
@app.route('/')
def vm_list():
    vm_names = list_vms()
    return render_template('index.html', vm_names=vm_names)

# Define a route to start a VM
@app.route('/start_vm', methods=['POST'])
def start_vm_route():
    vm_name = request.form.get('vm_name')
    start_vm(vm_name)
    return "VM started successfully"

# Define a route to stop a VM
@app.route('/stop_vm', methods=['POST'])
def stop_vm_route():
    vm_name = request.form.get('vm_name')
    stop_vm(vm_name)
    return "VM stopped successfully"

if __name__ == '__main__':
    app.run(debug=True)
