with open('sources/retweets') as f:
    lines = f.readlines()
accounts_to_track = [x.strip() for x in lines]
print(accounts_to_track)