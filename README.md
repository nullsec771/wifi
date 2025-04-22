# WiFiKeyExtractor

**WiFiKeyExtractor** is a Windows-based Python script that exports and reads stored WiFi profiles on your system, revealing saved SSIDs and their corresponding passwords.

> ⚠️ **Requires Administrator Privileges**

## 🚀 Features

- Automatically exports WiFi profiles using `netsh`
- Parses the exported XML to reveal:
  - SSID (WiFi Name)
  - Password
- Works on any Windows machine with admin access
- No third-party dependencies required

## 🛠 Requirements

- Windows OS
- Python 3.x
- Administrator privileges

## 📦 Installation

1. Clone or download this repository.
2. Open a command prompt as administrator.
3. Run the script using Python:

```bash
python WiFiKeyExtractor.py
