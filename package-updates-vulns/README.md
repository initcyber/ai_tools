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

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/initcyber/ai_tools.git
    cd ai_tools/package-updates-vulns
    ```

3. **Create a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

4. **Install the required Python libraries**:
    ```bash
    pip install openai==0.28
    ```

## Usage

1. **Set your OpenAI API key**:
    Replace `'YOUR_OPENAI_API_KEY'` in the script with your actual OpenAI API key.

2. **Run the script**:
    ```bash
    python package-updates.py
    ```

3. **Check the output**:
    The scan results and security recommendations will be saved to `scan_results.txt`.

## Example Output

Please note this is a work in progress. Still tweaking it a bit.

### Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

### License
This project is licensed under the MIT License. See the LICENSE file for details.
