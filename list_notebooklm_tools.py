import sys
import json
import subprocess
import os

def run_mcp_test():
    mcp_path = r"C:\Users\PC\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\Scripts\notebooklm-mcp.exe"
    
    process = subprocess.Popen(
        [mcp_path],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        bufsize=0
    )

    # Initialize
    process.stdin.write(json.dumps({
        "jsonrpc": "2.0",
        "id": 1,
        "method": "initialize",
        "params": {
            "protocolVersion": "2024-11-05",
            "capabilities": {},
            "clientInfo": {"name": "test-client", "version": "1.0"}
        }
    }) + "\n")
    process.stdin.flush()
    process.stdout.readline()

    # Initialized
    process.stdin.write(json.dumps({
        "jsonrpc": "2.0",
        "method": "notifications/initialized"
    }) + "\n")
    process.stdin.flush()

    # List Tools
    process.stdin.write(json.dumps({
        "jsonrpc": "2.0",
        "id": 2,
        "method": "tools/list"
    }) + "\n")
    process.stdin.flush()
    
    tools_response = process.stdout.readline()
    with open('full_tools_output.json', 'w') as f:
        f.write(tools_response)

    process.terminate()

if __name__ == "__main__":
    run_mcp_test()
