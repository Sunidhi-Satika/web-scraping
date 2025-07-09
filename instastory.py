import instaloader
import os

L = instaloader.Instaloader()

session_id = input("Enter session id : ")
L.context._session.cookies.set("sessionid", session_id)

profile_name = input("Enter profile name : ")
profile = instaloader.Profile.from_username(L.context, profile_name)

L.download_stories(userids=[profile.userid])

for filename in os.listdir("：stories"):
    if filename.endswith(".json.xz"):
        os.remove(os.path.join("：stories", filename))
