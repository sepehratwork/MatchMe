from instagrapi import Client

ACCOUNT_USERNAME = "faraztest456"
ACCOUNT_PASSWORD = "43456fr"
TARGET_PROFILE = "iranintltv"

cl = Client()
cl.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)

user_id = cl.user_id_from_username(TARGET_PROFILE)
medias = cl.user_medias(user_id, 20)
print(dict(medias[0])["caption_text"])