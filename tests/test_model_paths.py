from pathlib import Path

import face_recognition_models as frm


def test_packaged_model_files_exist():
    paths = [
        frm.pose_predictor_model_location(),
        frm.pose_predictor_five_point_model_location(),
        frm.face_recognition_model_location(),
        frm.cnn_face_detector_model_location(),
    ]

    for path in paths:
        file_path = Path(path)
        assert file_path.is_file(), f"missing packaged model: {file_path.name}"
