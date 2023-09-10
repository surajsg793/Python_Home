from instabot import Bot
bot = Bot()
bot.login(username = "jone_python08",password = "")

bot.follow('surajgupta8777')

bot.upload_photo("PROJECT/my_qr_code.png", caption ="I love coding")

bot.unfollow("surajgupta8777")

bot.send_message("I love India"[india123,india1])

followers = bot.get_user_followers("surajgupta8777")
for follower in followers :
    print(bot.get_user_info(follower))

following = bot.get_user_following("surajgupta8777")
for Following in following :
    print(bot.get_user_info(Following))


