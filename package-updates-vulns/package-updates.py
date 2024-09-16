import subprocess
import requests
import re
import os

def get_package_updates():
    # Update package list
    subprocess.run(["sudo", "apt", "update"], check=True)
    
    # Get upgradable packages
    result = subprocess.run(["apt", "list", "--upgradable"], capture_output=True, text=True)
    upgradable_packages = result.stdout.strip().split("\n")[1:]  # Skip the first line
    
    return len(upgradable_packages), upgradable_packages

def extract_usn_descriptions(usn_page_content):
    pattern = r'### (USN-\d+-\d+: [\w ]+)[^#]*'
    usn_entries = re.findall(pattern, usn_page_content, re.DOTALL)
    return usn_entries

def get_usn_detail(usn_number, page_content):
    lines = page_content.split('\n')
    usn_detail = ''
    capture_detail = False

    for line in lines:
        if usn_number in line:
            capture_detail = True
            usn_detail += line.strip() + '\n'
        elif capture_detail:
            if line.strip() == '' or 'USN-' in line:
                break
            usn_detail += line.strip() + '\n'
    return usn_detail

def get_security_vulnerabilities(packages):
    vulnerabilities = []
    
    # Fetch the main USN page
    usn_url = "https://ubuntu.com/security/notices"
    usn_response = requests.get(usn_url)
    
    if usn_response.status_code == 200:
        usn_page_content = usn_response.text
        usn_entries = extract_usn_descriptions(usn_page_content)
        
        for package in packages:
            package_name = package.split('/')[0]
            
            for usn_entry in usn_entries:
                if package_name.lower() in usn_entry.lower():
                    usn_number = usn_entry.split(':')[0].strip()
                    usn_detail = get_usn_detail(usn_number, usn_page_content)
                    
                    vulnerabilities.append({
                        "package": package_name,
                        "usn": usn_number,
                        "description": usn_detail
                    })
                    break  # Stop after finding the first relevant USN for this package
    
    return format_vulnerability_report(vulnerabilities)

def format_vulnerability_report(vulnerabilities):
    if not vulnerabilities:
        return "No specific vulnerability information found for the upgradable packages."
    
    report = "Potential security vulnerabilities and fixes:\n\n"
    
    for vuln in vulnerabilities:
        report += f"Package: {vuln['package']}\n"
        report += f"USN: {vuln['usn']}\n"
        report += f"Description: {vuln['description']}\n\n"
    
    return report

def main():
    try:
        num_updates, upgradable_packages = get_package_updates()
        print(f"Number of packages available to update: {num_updates}")
        
        if num_updates > 0:
            vulnerabilities = get_security_vulnerabilities(upgradable_packages)
            print("\nPotential security vulnerabilities and fixes:")
            print(vulnerabilities)
        else:
            print("No packages need updating. Your system is up to date.")
    
    except subprocess.CalledProcessError as e:
        print(f"Error running system commands: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()