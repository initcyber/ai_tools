import nmap
import openai
import json
import ipaddress

# Initialize the nmap scanner
nm = nmap.PortScanner()

# Function to scan a single IP for open ports
def scan_ip(ip):
    nm.scan(hosts=str(ip), arguments='-p 1-65535')  # Scans all ports
    if str(ip) in nm.all_hosts():
        host_info = {
            'host': str(ip),
            'status': nm[str(ip)].state(),
            'ports': []
        }
        for proto in nm[str(ip)].all_protocols():
            lport = nm[str(ip)][proto].keys()
            for port in lport:
                port_info = {
                    'port': port,
                    'state': nm[str(ip)][proto][port]['state'],
                    'service': nm[str(ip)][proto][port]['name']
                }
                host_info['ports'].append(port_info)
        return host_info
    else:
        return None

# Function to get security recommendations from OpenAI
def get_security_recommendations(scan_results):
    openai.api_key = 'YOUR_OPENAI_API_KEY'
    
    # Prepare the prompt for ChatGPT
    prompt = f"Here are the results of an nmap scan:\n{json.dumps(scan_results, indent=2)}\nPlease provide security recommendations based on these results. These are open ports found on the subnet and I need an explanation of current critical vulnerabilities associated with these open ports"
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500  # Increase this value as needed
    )
    
    return response.choices[0].message['content'].strip()

# Function to append results to a text file
def append_to_file(scan_results, recommendations, filename='scan_results.txt'):
    with open(filename, 'a') as file:
        file.write("Nmap Scan Results:\n")
        file.write(json.dumps(scan_results, indent=2))
        file.write("\n\nSecurity Recommendations from ChatGPT:\n")
        file.write(recommendations)
        file.write("\n\n")

# Main function
def main():
    subnet = '172.16.10.0/24'  # Change this to your subnet
    for ip in ipaddress.IPv4Network(subnet):
        scan_results = scan_ip(ip)
        if scan_results:
            recommendations = get_security_recommendations(scan_results)
            
            print(f"Nmap Scan Results for {ip}:")
            print(json.dumps(scan_results, indent=2))
            print(f"\nSecurity Recommendations from ChatGPT for {ip}:")
            print(recommendations)
            
            # Append results to a text file
            append_to_file(scan_results, recommendations)

if __name__ == "__main__":
    main()
