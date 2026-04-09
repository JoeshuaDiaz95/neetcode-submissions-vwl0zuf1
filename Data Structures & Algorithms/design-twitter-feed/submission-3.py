from collections import defaultdict
import heapq
class Twitter:

    def __init__(self):
        self.tweet = defaultdict(list)
        self.following = defaultdict(set)
        self.time = 0 

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweet[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        maxheap = []
        users = set(self.following[userId])
        users.add(userId)

        for u in users:
            if self.tweet[u]:
                time, tid = self.tweet[u][-1]
                idx = len(self.tweet[u]) - 1
                heapq.heappush(maxheap,(-time,u,idx))

        result = []

        while maxheap and len(result) < 10:
            negtime, u, idx = heapq.heappop(maxheap)
            time, tid = self.tweet[u][idx]
            result.append(tid)

            if idx > 0:
                next_time, next_tid = self.tweet[u][idx-1]
                heapq.heappush(maxheap, (-next_time,u,idx - 1))
        return result

            


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
        
