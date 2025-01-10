import tweepy
import os
import time

# X Dev API credentials
API_KEY = ""
API_SECRET_KEY = ""
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""

def auth_v1(consumer_key, consumer_secret, access_token, access_token_secret):
    """
    Authenticate using API v1.1 credentials.
    """
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return tweepy.API(auth)

def auth_v2(consumer_key, consumer_secret, access_token, access_token_secret):
    """
    Authenticate using API v2 credentials.
    """
    return tweepy.Client(
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        access_token=access_token,
        access_token_secret=access_token_secret
    )

def post_tweet_with_image_v2(api_v1, client, image_path, tweet_text=""):
    """
    Upload an image using v1.1 and post a tweet with v2.
    """
    try:
        # Step 1: Upload the image using v1.1
        media = api_v1.media_upload(image_path)
        print(f"Media uploaded: {media.media_id}")

        # Step 2: Post the tweet with the image using v2
        response = client.create_tweet(
            text=tweet_text,
            media_ids=[media.media_id_string]  # Use media_id from v1.1
        )
        print(f"Tweet posted successfully: {response.data}")
    except tweepy.errors.TweepyException as e:
        print(f"Error posting tweet with image: {e}")

# Initialize API clients
api_v1 = auth_v1(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
client = auth_v2(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Path to the folder containing the images
image_folder = "/image/path/here"

# Loop through the images and tweet them
for i in range(1, 818):  # Frame numbers: 1 to 817
    image_name = f"frame{i}.png"
    image_path = os.path.join(image_folder, image_name)

    if os.path.exists(image_path):
        tweet_text = f"Frame {i}/817"  # Modify tweet text
        post_tweet_with_image_v2(api_v1, client, image_path, tweet_text=tweet_text)
    else:
        print(f"Image not found: {image_name}")

    # Wait for 1 hour before the next tweet
    if i < 817:  # Avoid waiting after the last image
        print("Waiting 1 hour before the next tweet...")
        time.sleep(60 * 60)  # 1 hour in seconds

# Loop through the images and tweet them forward
post_images_in_range(1, 871, step=1, total_frames=871)

# Loop through the images and tweet them backward
post_images_in_range(871, 1, step=-1, total_frames=871)
