import cv2
import requests
import streamlit as st
import tempfile
import numpy as np

# -------------------------------
# CONFIGURATION
# -------------------------------

API_KEY = "XhvqTtf1sLawkQQRgrAE"
PROJECT_ID = "fall-detection-qyulz"
MODEL_VERSION = "2"

INFERENCE_URL = f"https://detect.roboflow.com/{PROJECT_ID}/{MODEL_VERSION}?api_key={API_KEY}"

CONF_THRESHOLD = 0.2


# -------------------------------
# INFERENCE FUNCTION
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
    return None


# -------------------------------
# ANNOTATION FUNCTION (MISSING FIX)
# -------------------------------

def annotate_frame(frame, result, conf_threshold):
    if result and "predictions" in result:
        for pred in result["predictions"]:
            confidence = pred.get("confidence", 0)

            if confidence < conf_threshold:
                continue

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

            # Draw box
            cv2.rectangle(
                frame,
                (x - w // 2, y - h // 2),
                (x + w // 2, y + h // 2),
                color,
                3
            )

            label = f"{display_label} ({confidence:.2f})"
            cv2.putText(
                frame,
                label,
                (x - w // 2, y - h // 2 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                color,
                2
            )

    return frame


# -------------------------------
# STREAMLIT APP
# -------------------------------

st.title("Fall Detection Demo: Roboflow + Streamlit")

conf_threshold = st.slider("Confidence Threshold", 0.0, 1.0, 0.2, 0.05)

option = st.radio("Choose Input Source:", ["Upload Video", "Webcam"])


# -------------------------------
# VIDEO UPLOAD
# -------------------------------

if option == "Upload Video":
    uploaded_file = st.file_uploader("Upload a Video", type=["mp4", "mov", "avi"])

    if uploaded_file is not None:
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(uploaded_file.read())

        cap = cv2.VideoCapture(tfile.name)
        stframe = st.empty()

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            result = infer_frame(frame)
            annotated_frame = annotate_frame(frame, result, conf_threshold)

            stframe.image(
                cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB),
                channels="RGB"
            )

        cap.release()


# -------------------------------
# WEBCAM
# -------------------------------

elif option == "Webcam":
    st.write("Capture from webcam")

    camera_input = st.camera_input("Take a picture or record a short video")

    if camera_input is not None:
        file_bytes = np.asarray(bytearray(camera_input.read()), dtype=np.uint8)
        frame = cv2.imdecode(file_bytes, 1)

        result = infer_frame(frame)
        annotated_frame = annotate_frame(frame, result, conf_threshold)

        st.image(
            cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB),
            channels="RGB"
        )