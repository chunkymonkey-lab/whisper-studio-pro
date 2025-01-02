# WhisperStudio Pro

WhisperStudio Pro is a professional-grade audio transcription application that combines OpenAI's Whisper technology with advanced speaker diarization capabilities. This tool provides accurate transcription, translation, and audio processing features in an efficient desktop application.

## Features

WhisperStudio Pro delivers powerful audio processing capabilities through its intuitive interface. The application provides real-time transcription with speaker detection, supporting over 100 languages. Users can process audio files locally, ensuring complete privacy and data security.

### Core Capabilities

Our application stands out by offering professional-grade features including speaker diarization, batch processing, and extensive format support. The local processing approach ensures your sensitive audio data never leaves your machine, making it ideal for confidential interviews and sensitive content.

### Language Support

WhisperStudio Pro handles transcription in over 100 languages, including English, Chinese, German, Spanish, Russian, Korean, French, Japanese, and many more. The application can automatically detect the source language and provide accurate transcriptions with timestamp alignment.

## Installation

### Prerequisites

The following components are required before installation:

    Python 3.8 or higher
    PyQt6
    CUDA-compatible GPU (optional, for enhanced performance)
    4GB RAM minimum (8GB recommended)
    2GB free disk space

### Installation Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/chunkymonkey-lab/whisper-studio-pro.git
   cd whisper-studio-pro
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\\Scripts\\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Install additional components:
   ```bash
   # For GPU support (optional)
   pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
   ```

## Usage

Launch the application using:
```bash
python -m whisper_studio
```

The application will guide you through the transcription process:

1. Select your audio or video files
2. Choose transcription options
3. Select output format preferences
4. Begin transcription

## Development Setup

For developers interested in contributing to WhisperStudio Pro, follow these additional steps:

1. Install development dependencies:
   ```bash
   pip install -r requirements-dev.txt
   ```

2. Set up pre-commit hooks:
   ```bash
   pre-commit install
   ```

3. Run tests:
   ```bash
   pytest
   ```

## Contributing

We welcome contributions to WhisperStudio Pro. Please review our [Contributing Guidelines](CONTRIBUTING.md) before submitting pull requests.

### Development Guidelines

When contributing, please:

1. Follow the established code style
2. Add unit tests for new features
3. Update documentation as needed
4. Create clear, focused pull requests

## Configuration

WhisperStudio Pro can be configured through the GUI or via a configuration file. Common settings include:

- Default language selection
- Output format preferences
- GPU/CPU processing selection
- Interface customization
- Hotkey configuration

## Troubleshooting

Common issues and their solutions are documented in our [FAQ](docs/FAQ.md). For additional support:

1. Check the application logs
2. Review our [Known Issues](docs/KNOWN_ISSUES.md)
3. Search existing GitHub issues
4. Create a new issue with detailed information

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

WhisperStudio Pro builds upon several excellent open-source projects:

- OpenAI's Whisper for core transcription
- SpeechBrain for speaker diarization
- PyQt6 for the user interface
- Various audio processing libraries

## Support

For support inquiries:

- Review our [Documentation](docs/)
- Join our [Discord Community]()
- Create a GitHub issue
- Contact our support team

## Roadmap

See our [Project Roadmap](docs/ROADMAP.md) for planned features and enhancements.

---

**Note**: This project is under active development. Please check for updates regularly.