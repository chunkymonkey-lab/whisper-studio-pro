from setuptools import setup, find_packages

setup(
    name="whisper-studio-pro",
    version="1.0.0",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=[
        "PyQt6>=6.4.0",
        "whisper>=1.0.0",
        "speechbrain>=0.5.12",
        "torch>=1.10.0",
        "torchaudio>=0.10.0",
        "psutil>=5.8.0",
        "pydub>=0.25.1",
        "requests>=2.26.0",
        "packaging>=21.0.0",
    ],
    entry_points={
        "console_scripts": [
            "whisper-studio=whisper_studio.gui.main:main",
        ],
    },
)