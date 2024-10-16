# About Code
## These are my solutions to problems that were in the [ Human Benchmark](https://humanbenchmark.com/).


## About Human Benchmark
![Preview](preview/preview.png)

### Human Benchmark is a website offering a series of tests designed to assess cognitive functions such as reaction time and memory. The platform provides eight tests, most of which focus on memory, including the ability to remember words, phrases, and sequences of shapes.

# Installation
## Creating virtual environment

```py
# Virtual environments are created by executing the venv module:
python -m venv /path/to/new/virtual/environment
```
## Activation of the virtual environment
### A virtual environment may be “activated” using a script in its binary directory.

### For Windows
* bash/zsh - source <venv>/bin/activate

### For Linux
* cmd.exe - C:\> <venv>\Scripts\activate.bat
* PowerShell - PS C:\> <venv>\Scripts\Activate.ps1

## Installion packages
```py
pip install -r requirements.txt
```

## Steps to Download and Configure Tesseract-OCR
## 1. Download and Install Tesseract-OCR

Tesseract is a free and open-source OCR (Optical Character Recognition) engine.
For Windows:
* Go to the official Tesseract GitHub release page: https://github.com/UB-Mannheim/tesseract/wiki
* Download the Windows installer (tesseract-ocr-setup.exe) from the releases section.
* Run the installer and complete the installation process.

For macOS:
```
brew install tesseract
```

For Linux (Ubuntu/Debian):
```
sudo apt update
sudo apt install tesseract-ocr
```

## 2. Add Tesseract to the Environment Variables
For Windows:
* Open the Start Menu, search for Environment Variables, and select Edit the system environment variables.
* In the System Properties window, click the Environment Variables button.
* Under System variables, find and select the Path variable, then click Edit.
* Click New and add the path to the tesseract.exe file (usually located in C:\Program Files\Tesseract-OCR\).
* Click OK to save changes.

For macOS and Linux:
* Open a terminal and add the Tesseract path to the shell configuration file (.bashrc, .zshrc, or .bash_profile):
    ```
    export PATH="/usr/local/bin/tesseract:$PATH"
    ```
* Save the file and run the following command to apply changes:
    ```
    source ~/.bashrc  # or source ~/.zshrc
    ```

## 3. Verify Tesseract Installation

After adding Tesseract to our environment variables, open a terminal (or Command Prompt on Windows) and type:
```
tesseract --version
```

# Using
* Open Terminal and Run command:

    ```
    python task-name.py
    ```
* Open Browser page 