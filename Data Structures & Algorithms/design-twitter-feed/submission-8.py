class Twitter:

    def __init__(self):
        self.users_tweets = defaultdict(list)
        self.users_followees = defaultdict(set)
        self.time = 0 
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time -= 1
        self.users_tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        # using heap 

        from heapq import heapify, heappush, heappop
        all_tweets = []
        for followee_id in self.users_followees[userId]:
            all_tweets += self.users_tweets[followee_id]
        if userId not in self.users_followees[userId]:
            all_tweets += self.users_tweets[userId]
        heapify(all_tweets)
        result = []
        while all_tweets and len(result) < 10:
            result.append(heappop(all_tweets))
        return [y for x,y in result]
    def follow(self, followerId: int, followeeId: int) -> None:
        self.users_followees[followerId].add(followeeId)
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.users_followees[followerId]:
            self.users_followees[followerId].remove(followeeId)