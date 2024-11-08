import instaloader
import os

# Creating an instance of Instaloader
L = instaloader.Instaloader()

# Post URL
post_url = input("Enter the post link : ")

# Getting code from URL (last second part in url)
post_url_code = post_url.split('/')[-2]

# Getting the post from the URL Code
post = instaloader.Post.from_shortcode(L.context, post_url_code)

# Downloading the post
L.download_post(post, target="posts")

# After downloading, filtering out non-image files (like .json.xz, .txt)
for filename in os.listdir("posts"):
    if filename.endswith(".json.xz") or filename.endswith(".txt"):
        os.remove(os.path.join("posts", filename))