import praw

reddit = praw.Reddit(
    client_id='O0WZueTOzHS7NCLcdax7mA',
    client_secret='GVXWhTrPNt6uvk2dVMZ9Gdz7bXjn3w',
    user_agent='myredditpostscraper',
)

def scrape_subreddit(subreddit_name, post_limit=100, comment_limit=5):
    subreddit = reddit.subreddit(subreddit_name)

    output_file = f"{subreddit_name}_scraped_data.txt"

    with open(output_file, 'w', encoding='utf-8') as file:
        for submission in subreddit.new(limit=post_limit):
            file.write(f"\nTitle: {submission.title}\n")
            file.write(f"Author: {submission.author}\n")
            file.write(f"Score: {submission.score}\n")
            file.write(f"URL: {submission.url}\n")

            # Check if the post has zero comments
            if submission.num_comments == 0:
                file.write("  This post has 0 comments.\n")
                file.write("\n" + "-"*50 + "\n")
                continue

            # Fetch comments for this post
            file.write(f"\nFetching {comment_limit} comments for this post:\n")
            submission.comments.replace_more(limit=None)  # Replaces all comments
            comment_count = 0

            for comment in submission.comments.list():
                # Check if the comment is not removed
                if comment.banned_by is None:
                    file.write(f"  Comment by {comment.author}: {comment.body}\n")
                    comment_count += 1

                # Check if the desired comment limit is reached
                if comment_count >= comment_limit:
                    break

            file.write("\n" + "-"*50 + "\n")

if __name__ == "__main__":
    subreddit_name = "explainlikeimfive"
    scrape_subreddit(subreddit_name)

#O0WZueTOzHS7NCLcdax7mA
#GVXWhTrPNt6uvk2dVMZ9Gdz7bXjn3w
#myredditpostscraper