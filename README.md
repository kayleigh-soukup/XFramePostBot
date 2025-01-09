A friend asked me to create an automation for X (formerly Twitter) that would post every frame from the movie Tenet that featured Robert Pattinson.

Using her X Developer API credentials, I wrote a Python script to authenticate the credentials and utilized the Tweepy library (both v1.1 and v2) to upload the locally stored images and post them hourly in sequence.

She then suggested an idea inspired by Tenet: after posting the frames in chronological order, the automation should repost them in reverse order. I implemented this concept by using the post_images_in_range function to include both the forward and reverse posting sequences.

In order to use the automation code for your own purposes, I would recommend following the instructions in the separate text file. The post-images-in-range functions at the bottom of the code can be deleted in order to remove the automatic reverse-order posting sequence.