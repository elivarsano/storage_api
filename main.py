from fastapi import FastAPI
import os
import json

app = FastAPI()

# Get data about the storage using df command
mount_points = {}

storage_data = os.popen('df -h').read()
for line in storage_data.split('\n')[1:]:
    if line:
        device, size, used, available, percent, mountpoint = line.split()
        mount_points[mountpoint] = {
            'device': device,
            'size': size,
            'used': used,
            'available': available,
            'percent': percent
        }

@app.get("/storage")
def get_storage():
    return json.dumps(mount_points, indent=4)

if __name__ == "__main__":
    get_storage()

# Run the FastAPI application
# uvicorn storage_api.main:app --reload

    

