# Nmap AI Security Scanner

This Python script uses `nmap` to scan a local subnet for open ports and then sends the results to OpenAI's ChatGPT to get security recommendations. The results and recommendations are saved to a text file.

## Features

- Scans a specified subnet for open ports.
- Sends scan results to OpenAI's ChatGPT for security recommendations.
- Saves the scan results and recommendations to a text file.
- Processes each IP address individually and appends the results to the file.

## Requirements

- Python 3.6+
- `nmap` installed on your system
- `python-nmap` library
- `openai` library
- OpenAI API key

## Installation

1. **Install nmap**:
    ```bash
    sudo apt-get install nmap
    ```

2. **Clone the repository**:
    ```bash
    git clone https://github.com/initcyber/ai_tools.git
    cd ai_tools/nmap-ai-security-scanner
    ```

3. **Create a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

4. **Install the required Python libraries**:
    ```bash
    pip install python-nmap openai
    pip install openai
    ```

## Usage

1. **Set your OpenAI API key**:
    Replace `'YOUR_OPENAI_API_KEY'` in the script with your actual OpenAI API key.

2. **Run the script**:
    ```bash
    python nmapai.py
    ```

3. **Check the output**:
    The scan results and security recommendations will be saved to `scan_results.txt`.

## Example Output

### Nmap Scan Results:
```json
[
  {
    "host": "192.168.1.1",
    "status": "up",
    "ports": [
      {"port": 22, "state": "open", "service": "ssh"},
      {"port": 80, "state": "open", "service": "http"}
    ]
  },
  {
    "host": "192.168.1.2",
    "status": "up",
    "ports": [
      {"port": 22, "state": "open", "service": "ssh"},
      {"port": 443, "state": "open", "service": "https"}
    ]
  }
]

Based on the results of the nmap scan provided, here are some security recommendations:

1. **Close Unused Ports**: Identify and close any unnecessary open ports that are not required for the functioning of the server. Ports with services that are not needed should be closed to reduce the attack surface.

2. **Update Services**: Ensure that all the services running on the open ports are up to date with the latest security patches. Keeping services updated helps protect against known vulnerabilities and exploits.

3. **Implement Firewalls**: Set up firewalls to restrict access to the server and only allow traffic on necessary ports. This can help prevent unauthorized access and protect against malicious attacks.

4. **Use Strong Authentication**: Ensure that strong authentication mechanisms are in place for all services, such as using key-based authentication for SSH and strong passwords for other services.

### Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

### License
This project is licensed under the MIT License. See the LICENSE file for details.
