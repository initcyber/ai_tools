# Nmap AI Security Scanner

This Python script automates the process of checking for outdated packages in your Python environment and queries OpenAI's GPT model for potential security vulnerabilities associated with these outdated packages.

## Features

- Identifies outdated Python packages in your environment
- Queries OpenAI's GPT model for vulnerability information
- Provides upgrade recommendations
- Saves vulnerability reports to a text file

## Requirements

Before you begin, ensure you have met the following requirements:

- Python 3.6 or higher
- pip (Python package installer)
- An OpenAI API key

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
    pip install -r requirements.txt
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

4. The script will:
- List all outdated packages in your Python environment.
- Query OpenAI's GPT model for vulnerability information for each outdated package.
- Display the results in the console.
- Save the results to a file named `package_vulnerabilities.txt` in the same directory.


## Customization

- You can modify the `max_tokens` parameter in the `get_package_vulnerabilities` function to adjust the length of the GPT model's response.
- To change the output file name or location, modify the `filename` parameter in the `append_to_file` function.

## Important Notes

- This script uses the OpenAI API, which may incur costs depending on your usage and plan.
- The vulnerability information provided by the GPT model is based on its training data and may not always be up-to-date or comprehensive. Always verify critical security information from official sources.


## Example Output

Please note this is a work in progress. Still tweaking it a bit. But you can check out the example output in package_vulnerabilities_EXAMPLE.txt

### Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

### License
This project is licensed under the MIT License. See the LICENSE file for details.
