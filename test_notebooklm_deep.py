import sys
import json
import subprocess
import time
import os

def run_mcp_test():
    mcp_path = r"C:\Users\PC\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\Scripts\notebooklm-mcp.exe"
    
    # Start the process
    process = subprocess.Popen(
        [mcp_path],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        bufsize=0  # Unbuffered
    )

    # 1. Initialize
    init_req = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "initialize",
        "params": {
            "protocolVersion": "2024-11-05",
            "capabilities": {},
            "clientInfo": {"name": "test-client", "version": "1.0"}
        }
    }
    
    print(f"Sending Initialize...", file=sys.stderr)
    process.stdin.write(json.dumps(init_req) + "\n")
    process.stdin.flush()
    
    # Read Initialize Response
    response = process.stdout.readline()
    print(f"Received: {response}", file=sys.stderr)

    # 2. Send Initialized Notification
    notify_req = {
        "jsonrpc": "2.0",
        "method": "notifications/initialized"
    }
    process.stdin.write(json.dumps(notify_req) + "\n")
    process.stdin.flush()

    # 3. List Resources
    list_req = {
        "jsonrpc": "2.0",
        "id": 2,
        "method": "resources/list"
    }
    print(f"Sending List Resources...", file=sys.stderr)
    process.stdin.write(json.dumps(list_req) + "\n")
    process.stdin.flush()

    # Read List Response
    response = process.stdout.readline()
    print(f"Received Resources: {response}", file=sys.stderr)
    
    process.terminate()

if __name__ == "__main__":
    try:
        run_mcp_test()
        print("MCP Test Completed Successfully")
    except Exception as e:
        print(f"Error: {e}")
