from __future__ import annotations

from importlib.resources import files
from typing import Final

__all__ = [
    "cnn_face_detector_model_location",
    "face_recognition_model_location",
    "pose_predictor_five_point_model_location",
    "pose_predictor_model_location",
    "__version__",
]

# Keep the version in sync with pyproject.toml.
__version__: Final[str] = "0.4.0"

_MODELS_DIR: Final = files(__name__) / "models"


def _model_path(filename: str) -> str:
    """Return the fully-qualified path to a packaged model file."""
    return str(_MODELS_DIR / filename)


def pose_predictor_model_location() -> str:
    """Return the filesystem path to the 68-point facial landmark predictor."""
    return _model_path("shape_predictor_68_face_landmarks.dat")


def pose_predictor_five_point_model_location() -> str:
    """Return the filesystem path to the 5-point facial landmark predictor."""
    return _model_path("shape_predictor_5_face_landmarks.dat")


def face_recognition_model_location() -> str:
    """Return the filesystem path to the dlib face recognition ResNet model."""
    return _model_path("dlib_face_recognition_resnet_model_v1.dat")


def cnn_face_detector_model_location() -> str:
    """Return the filesystem path to the CNN face detector model."""
    return _model_path("mmod_human_face_detector.dat")
