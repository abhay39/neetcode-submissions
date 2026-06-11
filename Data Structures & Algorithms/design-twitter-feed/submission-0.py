from collections import defaultdict
import heapq
from typing import List


class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)      # userId -> [(time, tweetId)]
        self.following = defaultdict(set)    # userId -> {followeeIds}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []

        self.following[userId].add(userId)

        for followee in self.following[userId]:
            tweets = self.tweets[followee]

            if tweets:
                idx = len(tweets) - 1
                time, tweetId = tweets[idx]

                heapq.heappush(
                    heap,
                    (-time, tweetId, followee, idx - 1)
                )

        result = []

        while heap and len(result) < 10:
            negTime, tweetId, followee, idx = heapq.heappop(heap)

            result.append(tweetId)

            if idx >= 0:
                time, nextTweetId = self.tweets[followee][idx]

                heapq.heappush(
                    heap,
                    (-time, nextTweetId, followee, idx - 1)
                )

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].discard(followeeId)