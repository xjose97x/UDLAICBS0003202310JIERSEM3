import csv

class Channel:
    def __init__(self, channel_id, channel_desc, channel_class, channel_class_id):
        self.channel_id = channel_id
        self.channel_desc = channel_desc
        self.channel_class = channel_class
        self.channel_class_id = channel_class_id

def compute():
    channels = []
    with open('csv/channels.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            channels.append(Channel(row['CHANNEL_ID'], row['CHANNEL_DESC'], row['CHANNEL_CLASS'], row['CHANNEL_CLASS_ID']))
    return channels