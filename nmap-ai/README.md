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
    cd ai_tools/nmap-ai
    ```

3. **Create a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

4. **Install the required Python libraries**:
    ```bash
    pip install python-nmap openai
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

### Nmap Scan Results (example - see scan_results_EXAMPLE.txt located above):
```json
Nmap Scan Results:
{
  "host": "192.168.1.200",
  "status": "up",
  "ports": [
    {
      "port": 22,
      "state": "open",
      "service": "ssh"
    },
    {
      "port": 53,
      "state": "open",
      "service": "domain"
    },
    {
      "port": 111,
      "state": "open",
      "service": "rpcbind"
    },
    {
      "port": 3128,
      "state": "open",
      "service": "squid-http"
    },
    {
      "port": 8006,
      "state": "open",
      "service": "wpl-analytics"
    },
    {
      "port": 34894,
      "state": "open",
      "service": ""
    },
    {
      "port": 35923,
      "state": "open",
      "service": ""
    }
  ]
}
Security Recommendations from ChatGPT:
Based on the nmap scan results for host 192.168.1.200, here are some security recommendations:

1. **Secure SSH (Port 22)**:
   - Ensure strong passwords or use key-based authentication for SSH access.
   - Disable root login and consider using tools like Fail2ban to prevent brute force attacks.

2. **Secure DNS (Port 53)**:
   - Keep your DNS server software up-to-date to patch any known vulnerabilities.
   - Review the configuration of your DNS server to prevent information leakage.

3. **Secure RPCbind (Port 111)**:
   - RPCbind is known to have security issues. Consider firewall rules to restrict access to the RPC services.

4. **Secure Squid-HTTP (Port 3128)**:
   - Keep Squid proxy server updated to patch any security vulnerabilities.
   - Implement access controls to restrict who can use the proxy server.

5. **Investigate Unknown Services** (Ports 34894 and 35923):
   - Investigate services running on ports 34894 and 35923 to ensure they are legitimate. These unidentified services could be potential security risks.

6. **Review Firewall Rules**:
   - Check firewall rules to ensure that only necessary ports are open to the internet.
   - Configure strict egress filtering to restrict outbound traffic to necessary destinations.

7. **Regularly Monitor and Update**:
   - Regularly monitor network traffic and logs for any suspicious activity on these open ports.
   - Keep all network services and applications updated with the latest security patches.

By implementing these security recommendations, you can help protect the host at 192.168.1.200 from potential security threats and unauthorized access.
```

### Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

### License
This project is licensed under the MIT License. See the LICENSE file for details.
