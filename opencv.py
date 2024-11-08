import cv2

cap = cv2.VideoCapture(0)  # Open webcam

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Preprocess frame (resize, normalize, etc.)
    input_frame = preprocess_for_model(frame)
    
    # Run model prediction
    prediction = model.predict(input_frame)
    
    # Display result
    if prediction > 0.5:
        cv2.putText(frame, "Movement Detected", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    cv2.imshow('Live Movement Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()