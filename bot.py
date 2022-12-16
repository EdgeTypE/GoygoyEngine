import tweepy
import instagram_private_api
import time

# Twitter API anahtarlarını kullanarak tweepy nesnesini oluşturun
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
twitter_api = tweepy.API(auth)

# Instagram API anahtarlarını kullanarak instagram_private_api nesnesini oluşturun
instagram_api = instagram_private_api.Client(access_token=instagram_access_token)

user_name = "goygoyengineen2"
start_date = "2022-01-01"
end_date = "2022-12-31"

while True:
    # Tweetleri çekin
    tweets = twitter_api.user_timeline(screen_name=user_name, since=start_date, until=end_date)

    # Tweetleri döngüyle gezin ve içeriklerini yazdırın
    for tweet in tweets:
        print(tweet.text)

        # Tweet metnini ve resimleri çekin
        text = tweet.text
        images = tweet.entities['media']

        # Her resim için ayrı bir gönderi yayınlayın
        for image in images:
            # Resim URL'sini kullanarak gönderiyi yayınlayın
            instagram_api.media.upload(image_url=image['media_url'])
            # Gönderi açıklaması olarak tweet metnini kullanın
            instagram_api.media.configure(caption=text)

    # Belirli bir süre bekleyin ve döngüyü tekrar başlatın
    time.sleep(3600)  # 1 saat bekle
