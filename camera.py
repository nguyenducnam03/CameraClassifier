import cv2 as cv
# pip install 
import time
from time import sleep

class Camera:
    def __init__(self):
        self.camera = cv.VideoCapture(0)
        if not self.camera.isOpened():
            raise ValueError("Unable to open camera!")

        self.width = self.camera.get(cv.CAP_PROP_FRAME_WIDTH)
        self.height = self.camera.get(cv.CAP_PROP_FRAME_HEIGHT)

    def __del__(self):
        if self.camera.isOpened():
            self.camera.release()

    def get_frame(self):
        if self.camera.isOpened():
            ret, frame = self.camera.read()

            if ret:
                # Change to RGB becaues default is BGR
                return (ret, cv.cvtColor(frame, cv.COLOR_BGR2RGB))
            else:
                return (ret, None)
        else:
            return None
        
# Test
def test_camera():
    cam = Camera()
    
    try:
        while True:
            ret, frame = cam.get_frame()
            
            if ret:
                cv.imshow("Camera Test", cv.cvtColor(frame, cv.COLOR_RGB2BGR))  # Convert back to BGR for OpenCV display

            if cv.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
                break
            
            sleep(0.03)  # Prevent high CPU usage

    except Exception as e:
        print(f"Error: {e}")

    finally:
        del cam  # Ensure camera resource is released
        cv.destroyAllWindows()

# if __name__ == "__main__":
#     test_camera()