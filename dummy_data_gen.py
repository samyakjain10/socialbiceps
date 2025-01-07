import random
import uuid
import json

# Constants
INSTAGRAM_IDS = ["ranveerallahbadia", "beerbiceps"]
POST_TYPES = ["photo", "reel", "carousel", "video"]

# Engagement patterns based on post types
ENGAGEMENT_PATTERNS = {
    "ranveerallahbadia": {"photo": (8000, 1500), "reel": (3000, 800), "carousel": (9000, 1700), "video": (6000, 1200)},
    "beerbiceps": {"photo": (4000, 1000), "reel": (12000, 3000), "carousel": (5000, 1200), "video": (7000, 1500)}
}

# Function to generate random post data
def generate_post_data(user_id, post_type):
    like_count, comment_count = ENGAGEMENT_PATTERNS[user_id][post_type]
    share_count = random.randint(100, 500)  # Random share count
    post_id = str(uuid.uuid4())
    return {
        "postId": post_id,
        "likeCount": random.randint(int(like_count * 0.8), int(like_count * 1.2)),
        "commentCount": random.randint(int(comment_count * 0.8), int(comment_count * 1.2)),
        "shareCount": share_count,
        "userId": user_id,
        "postType": post_type
    }

# Generate dataset
def generate_dataset(num_posts):
    dataset = []
    for _ in range(num_posts):
        user_id = random.choice(INSTAGRAM_IDS)
        post_type = random.choice(POST_TYPES)
        post_data = generate_post_data(user_id, post_type)
        dataset.append(post_data)
    return dataset

# Generate 50 random posts
dataset = generate_dataset(1700)

# Save to a JSON file
with open("instagram_posts.json", "w") as f:
    json.dump(dataset, f, indent=4)

print("Dataset generated and saved to instagram_posts.json")
