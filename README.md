# Voice-Activated ChatGPT Automation

This project is designed to provide a voice-activated interface to ChatGPT using Python. The system listens for a wake word ("hey chatgpt"), opens Firefox, logs into ChatGPT (if necessary), and inputs a question automatically.

## Features

- **Wake Word Detection**: Uses Porcupine for efficient, offline wake word detection.
- **Browser Automation**: Automates login and interaction with ChatGPT using Selenium and Firefox.
- **Automatic Question Submission**: Inputs a predefined question and sends it to ChatGPT.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [How It Works](#how-it-works)
- [Running the System](#running-the-system)
- [Backend Deployment](#backend-deployment)
- [Customization](#customization)
- [Troubleshooting](#troubleshooting)
- [License](#license)

## Prerequisites

Before you begin, make sure you have the following installed on your system:

- Python 3.x
- Firefox browser
- [Geckodriver](https://github.com/mozilla/geckodriver/releases) for Selenium (add it to your system's PATH)
  
## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/voice-chatgpt-automation.git
   cd voice-chatgpt-automation
   ```

2. **Install dependencies** using `pip`:
   ```bash
   pip install -r requirements.txt
   ```

3. **Porcupine Setup**:
   - Download Porcupine wake word detection models from [Picovoice](https://github.com/Picovoice/porcupine) and place the model in your working directory.

4. **Geckodriver**:
   - Download [Geckodriver](https://github.com/mozilla/geckodriver/releases) and ensure it's in your system PATH, or specify its path in the script.

## How It Works

The system is divided into two parts:

1. **Wake Word Listener (`listener.py`)**: Continuously listens for the wake word ("hey chatgpt") using Porcupine. When the wake word is detected, it triggers the second script.
   
2. **ChatGPT Interaction (`chatgpt_interaction.py`)**: Opens Firefox using Selenium, checks if you're logged into ChatGPT, and logs in if not. It then sends a predefined question to ChatGPT and waits for the response.

### Running the System

1. **Configure Credentials**: Edit `chatgpt_interaction.py` and replace `your-email@example.com` and `your-password` with your ChatGPT login credentials.

2. **Run the Listener**:
   ```bash
   python listener.py
   ```

   This will start the system and begin listening for the wake word. Once detected, it will launch the ChatGPT interaction process automatically.

### Backend Deployment

If you want the system to run as a backend service and continue listening for the wake word without requiring manual execution, you can deploy the system as a background process or service.

#### Windows (Task Scheduler)

1. Open **Task Scheduler**.
2. Create a new task that runs `python listener.py` on system startup.
3. Set the task to run in the background with high privileges.
4. Ensure the task is configured to start even if the user is not logged in.

#### Linux/macOS (Systemd or Cron Job)

1. Create a systemd service file `/etc/systemd/system/voice_chatgpt.service`:
   ```ini
   [Unit]
   Description=Voice ChatGPT Automation Listener

   [Service]
   ExecStart=/usr/bin/python3 /path/to/your/listener.py
   Restart=always

   [Install]
   WantedBy=multi-user.target
   ```

2. Start and enable the service:
   ```bash
   sudo systemctl enable voice_chatgpt.service
   sudo systemctl start voice_chatgpt.service
   ```

3. Alternatively, use a **cron job**:
   ```bash
   @reboot /usr/bin/python3 /path/to/your/listener.py
   ```

This will ensure that the listener runs in the background whenever the system is booted.

## Customization

1. **Wake Word**: To change the wake word, edit `listener.py` and modify this line:
   ```python
   porcupine.create(keywords=["hey chatgpt"])
   ```
   You can change "hey chatgpt" to any other supported keyword or custom wake word using Picovoice’s platform.

2. **Predefined Question**: In `chatgpt_interaction.py`, modify this section to send a different question:
   ```python
   chat_input.send_keys("What is the capital of France?")
   ```

3. **Selenium Customization**:
   - You can modify the `chatgpt_interaction.py` script to handle different interactions with the ChatGPT page, including submitting multiple queries or interacting with other elements.

## Troubleshooting

1. **Porcupine Not Detecting Wake Word**: Ensure that the microphone is correctly set up and working. You can use system utilities to test if the microphone is receiving input.
   
2. **Selenium Not Opening Firefox**:
   - Check that the correct version of `geckodriver` is installed and it matches the version of Firefox you have.
   - Ensure `geckodriver` is added to your system’s PATH.

3. **ChatGPT Login Issues**:
   - Ensure that you’re using the correct email and password in `chatgpt_interaction.py`.
   - If there are additional login steps (such as CAPTCHA or multi-factor authentication), manual intervention may be required the first time.

## License

This project is licensed under the MIT License. See the LICENSE file for details.