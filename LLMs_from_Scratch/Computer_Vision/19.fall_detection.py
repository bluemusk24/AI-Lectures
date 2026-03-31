import cv2
import requests

# -------------------------------
# CONFIGURATION
# -------------------------------

API_KEY = "XhvqTtf1sLawkQQRgrAE"
PROJECT_ID = "fall-detection-qyulz"
MODEL_VERSION = "2"

# Roboflow REST API endpoint for inference
INFERENCE_URL = f"https://detect.roboflow.com/{PROJECT_ID}/{MODEL_VERSION}?api_key={API_KEY}"

# Input and output videos
INPUT_VIDEO = "Computer_Vision/fall_video.mp4"
OUTPUT_VIDEO = "fall_output_annotatedv1.mp4"

# Confidence threshold
CONF_THRESHOLD = 0.2


# -------------------------------
# FUNCTION TO RUN INFERENCE
# -------------------------------

def infer_frame(frame):
    _, img_encoded = cv2.imencode(".jpg", frame)

    response = requests.post(
        INFERENCE_URL,
        files={"file": img_encoded.tobytes()},
        data={"name": "video_frame"}
    )

    if response.status_code == 200:
        return response.json()
    else:
        return None


# -------------------------------
# MAIN PROCESS
# -------------------------------

def main():
    cap = cv2.VideoCapture(INPUT_VIDEO)

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    out = cv2.VideoWriter(OUTPUT_VIDEO, fourcc, fps, (width, height))

    frame_count = 0

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        frame_count += 1
        print(f"Processing frame {frame_count}")

        result = infer_frame(frame)

        if result and "predictions" in result:
            for pred in result["predictions"]:
                confidence = pred.get("confidence", 0)

                # Skip low-confidence detections
                if confidence < CONF_THRESHOLD:
                    continue

                # Extract bounding box
                x, y = int(pred["x"]), int(pred["y"])
                w, h = int(pred["width"]), int(pred["height"])
                class_name = pred["class"].lower()

                # Flip labels
                if class_name == "fall":
                    display_label = "stand"
                    color = (0, 255, 0)
                elif class_name == "stand":
                    display_label = "fall"
                    color = (0, 0, 255)
                else:
                    display_label = class_name
                    color = (255, 255, 0)

                # Draw bounding box
                cv2.rectangle(
                    frame,
                    (x - w // 2, y - h // 2),
                    (x + w // 2, y + h // 2),
                    color,
                    5
                )

                # Draw label
                label = f"{display_label}, ({confidence:.2f})"
                cv2.putText(
                    frame,
                    label,
                    (x - w // 2, y - h // 2 - 15),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1.8,
                    color,
                    5
                )

        # Write frame
        out.write(frame)

        # Show frame
        cv2.imshow('Fall detection', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print('Stopped by User')
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()

    print('Processing Complete. Annotated Video saved as:', OUTPUT_VIDEO)


if __name__ == "__main__":
    main()