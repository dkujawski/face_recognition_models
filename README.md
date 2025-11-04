# Face Recognition Models

Pre-trained model binaries used by the [`face_recognition`](https://github.com/ageitgey/face_recognition) project, packaged for straightforward redistribution.

The model weights were created by [Davis King](https://github.com/davisking/dlib-models) and are licensed under CC0 1.0 or the public domain. Refer to the [LICENSE](./LICENSE) file for details.

## Installation

```bash
# Optionally ensure Python 3.12 is available
uv tool install python@3.12

# Install the package from PyPI
uv pip install face-recognition-models
```

## Usage

Each helper returns the absolute path to one of the bundled model files:

```python
import face_recognition_models as frm

pose68 = frm.pose_predictor_model_location()
pose5 = frm.pose_predictor_five_point_model_location()
face_encoder = frm.face_recognition_model_location()
cnn_detector = frm.cnn_face_detector_model_location()
```

The returned paths can be passed directly to libraries such as [dlib](http://dlib.net/).

## Development Workflow

This repository is managed with [uv](https://github.com/astral-sh/uv). The included `Makefile` wraps the common commands:

```bash
# Create/update the local virtual environment with dev dependencies
make install

# Run static analysis and the (empty) test suite
make lint
make test

# Produce source and wheel distributions
make build
```

To update dependencies, run `make lock` and commit the resulting `uv.lock`.

## Releasing

To publish a new release:

1. Update the version in `pyproject.toml`.
2. Build the distributions with `make build`.
3. Publish using `make publish` (requires the appropriate PyPI credentials in your environment).

## Credits

- Adam Geitgey for the original `face_recognition` project.
- Davis King for the dlib model weights.

## License

The packaged models are distributed under CC0 1.0 / public domain terms. See [LICENSE](./LICENSE) for the exact text.
