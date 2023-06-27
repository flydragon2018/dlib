import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

import numpy as np 

'''
model_path = 'face_landmarker_v2_with_blendshapes.task'



BaseOptions = mp.tasks.BaseOptions
FaceLandmarker = mp.tasks.vision.FaceLandmarker
FaceLandmarkerOptions = mp.tasks.vision.FaceLandmarkerOptions
FaceLandmarkerResult = mp.tasks.vision.FaceLandmarkerResult
VisionRunningMode = mp.tasks.vision.RunningMode

# Create a face landmarker instance with the live stream mode:
def print_result(result: FaceLandmarkerResult, output_image: mp.Image, timestamp_ms: int):
    print('face landmarker result: {}'.format(result))

options = FaceLandmarkerOptions(
    base_options=BaseOptions(model_asset_path=model_path),
    running_mode=VisionRunningMode.LIVE_STREAM,
    result_callback=print_result)
'''



#with FaceLandmarker.create_from_options(options) as landmarker:
    # The landmarker is initialized. Use it here.
    # ...

'''
This task has the following configuration options for Python applications:

Option Name	Description	Value Range	Default Value
running_mode	Sets the running mode for the task. The landmarker has the following modes:
IMAGE: The mode for recognizing face landmarks on single image inputs.
VIDEO: The mode for recognizing face landmarks on the decoded frames of a video.
LIVE_STREAM: The mode for recognizing face landmarks on a live stream of input data, such as from camera. In this mode, result_callback must be called to set up a listener to receive the recognition results asynchronously.
{IMAGE, VIDEO, LIVE_STREAM}	IMAGE
num_faces	The maximum number of faces that can be detected by the the FaceLandmarker. Smoothing is only applied when num_faces is set to 1.	Integer > 0	1
min_face_detection_confidence	The minimum confidence score for the face detection to be considered successful.	Float [0.0,1.0]	0.5
min_face_presence_confidence	The minimum confidence score of face presence score in the face landmark detection.	Float [0.0,1.0]	0.5
min_tracking_confidence	The minimum confidence score for the face tracking to be considered successful.	Float [0.0,1.0]	0.5
output_face_blendshapes	Whether Face Landmarker outputs face blendshapes. Face blendshapes are used for rendering the 3D face model.	Boolean	False
output_facial_transformation_matrixes	Whether FaceLandmarker outputs the facial transformation matrix. FaceLandmarker uses the matrix to transform the face landmarks from a canonical face model to the detected face, so users can apply effects on the detected landmarks.	Boolean	False
result_callback	Sets the result listener to receive the landmarker results asynchronously when FaceLandmarker is in the live stream mode. Can only be used when running mode is set to LIVE_STREAM	ResultListener	N/A

'''

# Use OpenCV’s VideoCapture to start capturing from the webcam.

# Create a loop to read the latest frame from the camera using VideoCapture#read()

# Convert the frame received from OpenCV to a MediaPipe’s Image object.

##mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=numpy_frame_from_opencv)

# Send live image data to perform face landmarking.
# The results are accessible via the `result_callback` provided in
# the `FaceLandmarkerOptions` object.
# The face landmarker must be created with the live stream mode.


##landmarker.detect_async(mp_image, frame_timestamp_ms)



# STEP 1: Import the necessary modules.
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

from mediapipe import solutions
from mediapipe.framework.formats import landmark_pb2
import numpy as np
import matplotlib.pyplot as plt

import cv2


# import numpy as np
def get_facemesh_coords(landmark_list, img):
    """Extract FaceMesh landmark coordinates into 468x3 / 478x3 NumPy array.
    """
    h, w = img.shape[:2]  # grab width and height from image
    print("image width {0},height {1}".format(w,h))
    #xyz = [(lm.x, lm.y, lm.z) for lm in landmark_list.landmark]
    xyz = [[lm.x,lm.y, lm.z] for lm in landmark_list]

    #return np.multiply(xyz, [w, h, w]).astype(int)
    return np.multiply(xyz, [w, h, w]).astype(int)


def draw_landmarks_on_image(rgb_image, detection_result):
  face_landmarks_list = detection_result.face_landmarks
  annotated_image = np.copy(rgb_image)

  # Loop through the detected faces to visualize.
  for idx in range(len(face_landmarks_list)):
    face_landmarks = face_landmarks_list[idx]

    # Draw the face landmarks.
    face_landmarks_proto = landmark_pb2.NormalizedLandmarkList()
    face_landmarks_proto.landmark.extend([
      landmark_pb2.NormalizedLandmark(x=landmark.x, y=landmark.y, z=landmark.z) for landmark in face_landmarks
    ])

    solutions.drawing_utils.draw_landmarks(
        image=annotated_image,
        landmark_list=face_landmarks_proto,
        connections=mp.solutions.face_mesh.FACEMESH_TESSELATION,
        landmark_drawing_spec=None,
        connection_drawing_spec=mp.solutions.drawing_styles
        .get_default_face_mesh_tesselation_style())
    solutions.drawing_utils.draw_landmarks(
        image=annotated_image,
        landmark_list=face_landmarks_proto,
        connections=mp.solutions.face_mesh.FACEMESH_CONTOURS,
        landmark_drawing_spec=None,
        connection_drawing_spec=mp.solutions.drawing_styles
        .get_default_face_mesh_contours_style())
    solutions.drawing_utils.draw_landmarks(
        image=annotated_image,
        landmark_list=face_landmarks_proto,
        connections=mp.solutions.face_mesh.FACEMESH_IRISES,
          landmark_drawing_spec=None,
          connection_drawing_spec=mp.solutions.drawing_styles
          .get_default_face_mesh_iris_connections_style())

  return annotated_image, face_landmarks_proto.landmark


# STEP 2: Create an FaceLandmarker object.
base_options = python.BaseOptions(model_asset_path='face_landmarker_v2_with_blendshapes.task')
options = vision.FaceLandmarkerOptions(base_options=base_options,
                                       output_face_blendshapes=True,
                                       output_facial_transformation_matrixes=True,
                                       num_faces=1)
detector = vision.FaceLandmarker.create_from_options(options)

# STEP 3: Load the input image.
image = mp.Image.create_from_file("test.jpg")

# STEP 4: Detect face landmarks from the input image.
detection_result = detector.detect(image)

# STEP 5: Process the detection result. In this case, visualize it.
annotated_image, facelm_list = draw_landmarks_on_image(image.numpy_view(), detection_result)

#print(facelm_list)
print(type(facelm_list))

print("\n\n\n")
for k in facelm_list:
    print('\n\n\n')
    print(type(k))
    print(k)

#img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
img=cv2.imread("test.jpg")

fkp_coord=get_facemesh_coords(facelm_list, img)

print(fkp_coord)

#save to txt file

facelmks = "mediapipe_facelmks.txt"
 
with open(facelmks, 'w') as outfile:
    for idx in range(0, len(fkp_coord)):
        print(fkp_coord[idx], file=outfile)




#cv2.namedWindow("demo_face", cv2.WINDOW_AUTOSIZE)
#cv2.imshow('demo_face', cv2.cvtColor(annotated_image, cv2.COLOR_RGB2BGR))

# Naming a window
cv2.namedWindow("Resized_Window", cv2.WINDOW_NORMAL)
  
# Using resizeWindow()
cv2.resizeWindow("Resized_Window", 800, 800)

cvt_img= cv2.cvtColor(annotated_image, cv2.COLOR_RGB2BGR)
cv2.imshow('Resized_Window', cvt_img)

cv2.waitKey(0)
  
# closing all open windows
cv2.destroyAllWindows()
 