import subprocess

def get_wifi_passwords():
    # Run command to get all Wi-Fi profiles
    profiles_data = subprocess.check_output(
        ["netsh", "wlan", "show", "profiles"], encoding="utf-8", errors="ignore"
    )
    
    wifi_profiles = []
    
    # Extract profile names (SSIDs)
    for line in profiles_data.splitlines():
        if "All User Profile" in line:
            profile = line.split(":")[1].strip()
            wifi_profiles.append(profile)
    
    results = {}
    
    # For each profile, try to get the password
    for profile in wifi_profiles:
        profile_info = subprocess.check_output(
            ["netsh", "wlan", "show", "profile", profile, "key=clear"],
            encoding="utf-8", errors="ignore"
        )
        
        password = None
        for line in profile_info.splitlines():
            if "Key Content" in line:
                password = line.split(":")[1].strip()
                break
        
        results[profile] = password if password else "(No password stored)"
    
    return results


if __name__ == "__main__":
    wifi_data = get_wifi_passwords()
    for ssid, password in wifi_data.items():
        print(f"SSID: {ssid} | Password: {password}")






# OUTPUT

# SSID: Home_WiFi | Password: mypassword123
# SSID: Office_Network | Password: securepass
# SSID: Guest_WiFi | Password: (No password stored)
