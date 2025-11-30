from picamera2 import Picamera2
import cv2
import time

# Initialize Picamera2
picam2 = Picamera2(1)

# Define preview and full-resolution settings
preview_resolution = (1280, 960)  # 4:3 aspect ratio

sensor_resolution = picam2.sensor_resolution  # Full res: 4056x3040 on HQ Cam

# Configure preview with correct aspect ratio
preview_config = picam2.create_preview_configuration(
    main={"size": preview_resolution, "format": "RGB888"},
    display="main"
)
picam2.configure(preview_config)
picam2.start()

# Start time
start_time = time.time()

print(f"Starting preview at {preview_resolution} resolution.")
print("Capturing full-resolution image after 10 seconds...")

# Preview loop
try:
    while True:
        # Show live preview
        frame = picam2.capture_array()
        cv2.imshow("Preview", frame)

        # Break after 10 seconds
        if time.time() - start_time >= 4000:
            break

        # Allow manual exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            raise KeyboardInterrupt

except KeyboardInterrupt:
    print("Interrupted by user.")

# Stop preview window
cv2.destroyAllWindows()
picam2.stop()


# Configure for full-resolution still capture
still_config = picam2.create_still_configuration(
    main={"size": sensor_resolution, "format": "RGB888"}
)
picam2.switch_mode_and_capture_request(still_config)
#cam2.configure(still_config)
picam2.start()
time.sleep(1)  # Allow camera to stabilize

# Capture full-res image
image = picam2.capture_array()

# Save as PNG (viewable and lossless)
cv2.imwrite("hq_capture.png", cv2.cvtColor(image, cv2.COLOR_RGB2BGR))
print(f"Saved full-resolution image as hq_capture.png ({sensor_resolution})")

picam2.stop()
