import instaloader

# Define your login credentials
USERNAME = "faraztest456"  # Replace with your Instagram username
PASSWORD = "43456fr"  # Replace with your Instagram password
TARGET_PROFILE = "farazzabihian"  # Replace with the target profile's username

# Initialize Instaloader
L = instaloader.Instaloader()

# Login to Instagram
try:
    L.login(USERNAME, PASSWORD)
    print("Login successful!")
except instaloader.exceptions.BadCredentialsException:
    print("Invalid credentials! Please check your username and password.")
    exit()
except instaloader.exceptions.TwoFactorAuthRequiredException:
    print("Two-factor authentication is enabled. Please log in manually first.")
    exit()

# Download pictures from the target profile
print(f"Downloading pictures from {TARGET_PROFILE}...")
try:
    profile = instaloader.Profile.from_username(L.context, TARGET_PROFILE)
    for post in profile.get_posts():
        L.download_post(post, TARGET_PROFILE)
    print("Download completed!")
except instaloader.exceptions.ProfileNotExistsException:
    print("The target profile does not exist. Please check the username.")
except instaloader.exceptions.PrivateProfileNotFollowedException:
    print("The profile is private. Follow the account first to download content.")
except Exception as e:
    print(f"An error occurred: {e}")