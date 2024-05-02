import json
import csv


message_path = "/messages.json" # <-- update path to messages file (should be "[whatever the chat is called]/message.json")
people_path = "/people.json" # <-- update path to people file (should be "[whatever the chat is called]/people.json")

csv_file_path = "analysis.csv"


with open(csv_file_path, mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)


    headers = ["Author ", "Number of Messages ", "Number of Words ", "Number of likes ", "Average likes ", "Self Likes ", "Total Likes Given "]
    csv_writer.writerow(headers)


    with open(people_path, "r") as json_file1:
        people = json.load(json_file1)
        with open(message_path, "r") as json_file2:
            messages = json.load(json_file2)

            for person in people:
                
                print(people[person]["name"])
                
                num_messages = 0
                total_words = 0
                total_likes = 0
                self_likes = 0
                total_likes_given = 0

                for message in messages:

                    if person in message["favorited_by"]:
                        total_likes_given += 1

                    if message["author"] == person:
                        num_messages += 1
                        if message["text"] != None:
                            total_words += len(message["text"])
                        if message["favorited_by"] != None:
                            total_likes += len(message["favorited_by"])

                            for like in message ["favorited_by"]:
                                if like == person:
                                    self_likes +=1
                
                if num_messages != 0:
                    avg_likes = total_likes/num_messages

                data = [people[person]["name"], num_messages, total_words, total_likes,avg_likes, self_likes, total_likes_given]

                csv_writer.writerow(data)

            csv_file.close