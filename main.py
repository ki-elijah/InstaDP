import instaloader

ig = instaloader.Instaloader()
profile = input("Enter Username: ")
ig.downloader_profile(profile, profile_pic_only = True)