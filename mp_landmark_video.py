import cv2
import mediapipe as mp
import numpy as np


def lm_video_fn(video, normalize=True,
                save_lm = False, lm_filename = 'lm_save.npy',
                save_vid = False, vid_filename = 'video_marked.mp4',
                thickness=-1, circle_radius=1, color=(128, 255, 255),
                min_detection_confidence=0.8,
                min_tracking_confidence=0.8
                ):

    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles
    mp_face_mesh = mp.solutions.face_mesh
    drawing_spec = mp_drawing.DrawingSpec(thickness=thickness,
                                          circle_radius=circle_radius,
                                          color=color)

    cap = cv2.VideoCapture(video)
    # get geometry of the video
    w = int(cap.get(3))
    h = int(cap.get(4))
    fps = int(cap.get(5))
    print(f'Video {video}: \nWidth: {w} \nHeight: {h} \nFrame rate: {fps}')

    if save_vid:
        # Initialize video writer object
        output = cv2.VideoWriter(vid_filename,
                                 cv2.VideoWriter_fourcc(*'mp4v'), fps, (w, h))
    with mp_face_mesh.FaceMesh(
        static_image_mode= False,
        max_num_faces=1,
        refine_landmarks=True,
        min_detection_confidence=min_detection_confidence,
        min_tracking_confidence=min_tracking_confidence) as face_mesh:
        while cap.isOpened():
            success, image = cap.read()
            if not success:
              print("Ignoring empty camera frame.")
              break

            # To improve performance, optionally mark the image as not writeable to
            # pass by reference.
            image.flags.writeable = False
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = face_mesh.process(image)
            
            if save_vid:
                # Draw the face mesh annotations on the image.
                annotated_image = image.copy()
                annotated_image.flags.writeable = True
                annotated_image = cv2.cvtColor(annotated_image, cv2.COLOR_RGB2BGR)
                if results.multi_face_landmarks:
                    for face_landmarks in results.multi_face_landmarks:
                        mp_drawing.draw_landmarks(
                            image=annotated_image,
                            landmark_list=face_landmarks,
                            connections=mp_face_mesh.FACEMESH_TESSELATION,
                                                   landmark_drawing_spec = drawing_spec,
                            connection_drawing_spec=mp_drawing_styles
                                                                           .get_default_face_mesh_tesselation_style())
                        output.write(annotated_image)

                # Flip the image horizontally for a selfie-view display.
                cv2.imshow('MediaPipe Face Mesh', cv2.flip(annotated_image, 1))
                if cv2.waitKey(5) & 0xFF == 27:
                    break
    cap.release()
    if save_vid:
        output.release()
        cv2.destroyAllWindows()
    
    if results.multi_face_landmarks[0]:
        xyz = [[lm.x, lm.y, lm.z] for lm in results.multi_face_landmarks[0].landmark] # landmarks coords
        if normalize:
            xyz_norm = np.multiply(xyz, [w, h, w]).astype(int)
            if save_lm:
                np.save(lm_filename, xyz_norm)
            return xyz_norm
        else:
            if save_lm:
                np.save(lm_filename, xyz)
            return xyz

########################################## MAIN #######################
if __name__ == "__main__":
    lm = lm_video_fn('feel.mp4', normalize=True, save_vid=True, save_lm=True)