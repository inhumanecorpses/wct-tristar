def generate_ip_addresses():
    for a in range(256):
        for b in range(256):
            for c in range(256):
                for d in range(256):
                    yield f"{a}.{b}.{c}.{d}"

# File path to save the IP addresses
file_path = "ip_addresses.txt"

# Open the file in write mode
with open(file_path, "w") as file:
    # Iterate over generated IP addresses and write each one to the file
    for ip in generate_ip_addresses():
        file.write(ip + "\n")

print(f"IP addresses saved to {file_path}")
