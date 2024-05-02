import json
import csv

# Update these paths to reflect the correct locations or pass them as arguments.
message_path = "RIP Gamma Zeta/messages.json"
people_path = "RIP Gamma Zeta/people.json"
csv_file_path = "analysis.csv"

# Prepare to write to CSV
with open(csv_file_path, mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    headers = [
        "Author", "Number of Messages", "Number of Words", "Number of Likes",
        "Average Likes per Message", "Self Likes", "Total Likes Given"
    ]
    csv_writer.writerow(headers)

    # Load data from JSON files
    with open(people_path, "r") as json_file1, open(message_path, "r") as json_file2:
        people = json.load(json_file1)
        messages = json.load(json_file2)

        for person_id, person_info in people.items():
            print(person_info["name"])

            num_messages = 0
            total_words = 0
            total_likes = 0
            self_likes = 0
            total_likes_given = 0

            # Processing each message
            for message in messages:
                if message["author"] == person_id:
                    num_messages += 1
                    if message.get("text"):
                        total_words += len(message["text"].split())  # Split text to count words
                    message_likes = message.get("favorited_by", [])
                    total_likes += len(message_likes)
                    if person_id in message_likes:
                        self_likes += 1

                if person_id in message.get("favorited_by", []):
                    total_likes_given += 1

            # Calculate averages and other derived metrics
            avg_likes = total_likes / num_messages if num_messages > 0 else 0

            # Write data to CSV
            data = [
                person_info["name"], num_messages, total_words, total_likes,
                avg_likes, self_likes, total_likes_given
            ]
            csv_writer.writerow(data)
