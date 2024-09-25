import cv2
import os

def images_to_video(image_folder, output_video, fps=30):
    # Get all image files in the folder
    images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
    images.sort()  # Sort files (by name) to ensure correct order
    
    # Check if there are images in the folder
    if len(images) == 0:
        raise ValueError("No .jpg files found in the folder.")
    
    # Get the path to the first image to determine the size
    first_image_path = os.path.join(image_folder, images[0])
    
    # Load the first image to get the dimensions
    first_image = cv2.imread(first_image_path)
    height, width, layers = first_image.shape
    
    # Define the codec and create a VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for mp4
    video = cv2.VideoWriter(output_video, fourcc, fps, (width, height))
    
    # Read and write each image to the video
    for image in images:
        image_path = os.path.join(image_folder, image)
        frame = cv2.imread(image_path)
        
        if frame is None:
            print(f"Warning: Unable to read image {image_path}. Skipping it.")
            continue
        
        video.write(frame)
    
    # Release the video writer
    video.release()
    print(f"Video saved as {output_video}")

# Example usage
image_folder = '이미지들이 들어있는 폴더'
output_video = '영상 저장 경로 및 영상 이름'
fps = 30  # Frames per second
images_to_video(image_folder, output_video, fps)