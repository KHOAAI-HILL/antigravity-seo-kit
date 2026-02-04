import sys
import json
import subprocess
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
        bufsize=0
    )

    # 1. Initialize
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

    # 2. Initialized
    process.stdin.write(json.dumps({
        "jsonrpc": "2.0",
        "method": "notifications/initialized"
    }) + "\n")
    process.stdin.flush()

    # 3. List Tools
    process.stdin.write(json.dumps({
        "jsonrpc": "2.0",
        "id": 2,
        "method": "tools/list"
    }) + "\n")
    process.stdin.flush()
    
    tools_response = process.stdout.readline()
    print("Tools Response:")
    print(tools_response)

    # 4. List Resources
    process.stdin.write(json.dumps({
        "jsonrpc": "2.0",
        "id": 3,
        "method": "resources/list"
    }) + "\n")
    process.stdin.flush()
    
    resources_response = process.stdout.readline()
    print("\nResources Response:")
    print(resources_response)
    
    process.terminate()

if __name__ == "__main__":
    run_mcp_test()
