import subprocess
import openai
import json

# Set up your OpenAI API key
openai.api_key = 'YOUR_OPENAI_API_KEY'


# Function to get security vulnerabilities from OpenAI
def get_package_vulnerabilities(package_name, current_version, latest_version):
    # Prepare the prompt for ChatGPT
    prompt = (f"The following Python package is outdated:\n"
              f"Package: {package_name}\n"
              f"Current Version: {current_version}\n"
              f"Latest Version: {latest_version}\n"
              "Please provide information about any critical vulnerabilities "
              "associated with this package and version, and if upgrading to the "
              "latest version would mitigate these vulnerabilities.")

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or "gpt-4" if you have access
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500  # Adjust as needed
    )
    
    return response['choices'][0]['message']['content'].strip()

# Function to get the list of outdated packages
def get_outdated_packages():
    try:
        # Run the pip command to list outdated packages
        result = subprocess.run(["pip", "list", "--outdated"], capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout.splitlines()[2:]  # Skip the header lines
        else:
            return ["Error running pip list command."]
    except FileNotFoundError:
        return ["pip is not installed or not in your system PATH."]

# Function to process the outdated packages and query for vulnerabilities
def process_outdated_packages():
    outdated_packages = get_outdated_packages()
    for package_info in outdated_packages:
        # Assuming package_info format: 'package_name current_version latest_version'
        package_details = package_info.split()
        package_name = package_details[0]
        current_version = package_details[1]
        latest_version = package_details[2]

        print(f"Checking {package_name} for vulnerabilities...")
        vulnerabilities = get_package_vulnerabilities(package_name, current_version, latest_version)
        print(f"Vulnerabilities for {package_name}:\n{vulnerabilities}\n")

        # Optionally append results to a file
        append_to_file(package_name, vulnerabilities)

# Function to append results to a text file
def append_to_file(package_name, vulnerabilities, filename='package_vulnerabilities.txt'):
    with open(filename, 'a') as file:
        file.write(f"Package: {package_name}\n")
        file.write(f"Vulnerabilities:\n{vulnerabilities}\n\n")

# Run the script
if __name__ == "__main__":
    process_outdated_packages()