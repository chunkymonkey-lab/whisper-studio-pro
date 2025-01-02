# Installation Guide

This guide provides detailed instructions for installing WhisperStudio Pro on your system. The process has been designed to be straightforward while ensuring all components are properly configured.

## System Requirements

Before beginning the installation, please ensure your system meets these minimum requirements:

Python 3.8 or higher must be installed on your system. The application requires at least 4GB of RAM and 2GB of free disk space. For optimal performance, we recommend 8GB of RAM and a CUDA-compatible GPU.

## Basic Installation

The basic installation process consists of a few simple steps:

First, clone the repository to your local machine using Git:

```bash
git clone https://github.com/chunkymonkey-lab/whisper-studio-pro.git
cd whisper-studio-pro
```

Next, create a virtual environment to isolate the application dependencies:

```bash
python -m venv venv
```

Activate the virtual environment:

For Windows:
```bash
venv\Scripts\activate
```

For macOS and Linux:
```bash
source venv/bin/activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## GPU Support Installation

If you have a CUDA-compatible GPU and wish to enable GPU acceleration, install the GPU-specific dependencies:

```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

## Verifying the Installation

To verify your installation, run the application:

```bash
python -m whisper_studio
```

The application should launch with a graphical interface. If you encounter any issues, please check the troubleshooting section below.

## Troubleshooting Common Issues

If you encounter the error "No module named 'whisper_studio'", ensure you have:
1. Activated the virtual environment
2. Run the installation from the project's root directory
3. Installed all requirements successfully

For GPU-related issues, verify that:
1. Your GPU drivers are up to date
2. CUDA is properly installed
3. The correct torch version is installed for your CUDA version

## Additional Components

Some features require additional components:

For video support:
```bash
pip install python-vlc
```

For enhanced audio processing:
```bash
pip install pydub
```

## Updating the Application

To update to the latest version:

```bash
git pull origin main
pip install -r requirements.txt
```

## Getting Help

If you encounter any issues during installation:

1. Check our FAQ in the docs/FAQ.md file
2. Review existing GitHub issues
3. Create a new issue with details about your problem
4. Contact our support team

Please include your system information and any error messages when seeking help.