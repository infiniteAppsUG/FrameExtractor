import cv2

def extract_frames(video_path, output_folder):
    # Load the video
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print("Error opening video file")
        return

    # Get video frame rate
    fps = cap.get(cv2.CAP_PROP_FPS)
    
    current_frame = 0
    second = 0
    
    while True:
        # Read the next frame
        ret, frame = cap.read()
        if not ret:
            break  # Break the loop if there are no more frames
        
        # Calculate the current second in the video
        current_second = int(current_frame / fps)
        
        # If the current second is greater than the tracked second, save the frame
        if current_second > second:
            second = current_second
            frame_name = f"{output_folder}/frame_{second}.jpg"
            cv2.imwrite(frame_name, frame)
            print(f"Extracted frame at second {second}")
        
        current_frame += 1
    
    cap.release()

# Example usage
video_path = "video.mp4"
output_folder = "output_folder"
extract_frames(video_path, output_folder)