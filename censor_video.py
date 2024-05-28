import cv2

from utils import detected_and_draw_faces


def process_video(input_path, output_path):
    cap = cv2.VideoCapture(input_path)

    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    nof_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for .mp4
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    # Process each frame
    idx = 0
    while True:
        print(f'{idx}/{nof_frames}')
        ret, frame = cap.read()
        if not ret:
            break
        frame_with_circle = detected_and_draw_faces(frame)
        out.write(frame_with_circle)
        idx += 1
        # if idx > 10:
            # break

    cap.release()
    out.release()
    cv2.destroyAllWindows()
    print("Video processing complete and saved to", output_path)


input_video_path = 'data/persa_stable.mp4'
output_video_path = 'save/out.mp4'
process_video(input_video_path, output_video_path)
