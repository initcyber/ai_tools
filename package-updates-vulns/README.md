# Nmap AI Security Scanner

This Python script automates the process of checking for outdated packages in your Python environment and queries OpenAI's GPT model for potential security vulnerabilities associated with these outdated packages. It assumes you are running Ubuntu and it checks it against the Ubuntu Security Notices database. It does not provide any results if its not posted to the USN.

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


5. **Export your OpenAPI key to your environment variables**:
    ```bash
    export OPENAI_API_KEY='<your API key>'
    ```


## Usage

1. **Run the script**:
    ```bash
    python package-updates.py
    ```

3. **Check the output**:
    The scan results and security recommendations will be shown in the terminal

4. The script will:
- Query OpenAI's GPT model for vulnerability information for each outdated package.
- Display the results in the console.


## Customization

- You can modify the `max_tokens` parameter in the `get_package_vulnerabilities` function to adjust the length of the GPT model's response.
- To change the output file name or location, modify the `filename` parameter in the `append_to_file` function.

## Important Notes

- This script uses the OpenAI API, which may incur costs depending on your usage and plan.
- The vulnerability information provided by the GPT model is based on its training data and may not always be up-to-date or comprehensive. Always verify critical security information from official sources.


## Example Output
```bash
(venv) justin@Justin-Laptop:~/github/ai_tools/package-updates-vulns$ python package-updates.py 
Hit:1 https://dl.google.com/linux/chrome/deb stable InRelease
Hit:2 https://download.docker.com/linux/ubuntu jammy InRelease                                 
Hit:3 http://archive.ubuntu.com/ubuntu jammy InRelease                                         
Hit:4 http://archive.ubuntu.com/ubuntu jammy-updates InRelease               
Hit:5 http://archive.ubuntu.com/ubuntu jammy-backports InRelease             
Hit:6 http://security.ubuntu.com/ubuntu jammy-security InRelease             
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
25 packages can be upgraded. Run 'apt list --upgradable' to see them.
Number of packages available to update: 25

Potential security vulnerabilities and fixes:
No specific vulnerability information found for the upgradable packages.
```


### Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

### License
This project is licensed under the MIT License. See the LICENSE file for details.
