import instaloader

# Get instance
L = instaloader.Instaloader()

# Optionally, login or load session
L.login("faraztest456", "43456")        # (login)
L.interactive_login("faraztest456")      # (ask password on terminal)
L.load_session_from_file("faraztest456") # (load session created w/

for post in instaloader.Hashtag.from_name(L.context, 'cat').get_posts():
    # post is an instance of instaloader.Post
    L.download_post(post, target='#cat')
    # post = Post.from_shortcode(L.context, SHORTCODE)
    # profile = Profile.from_username(L.context, USERNAME)
    # Profile.from_id(L.context, USERID).username