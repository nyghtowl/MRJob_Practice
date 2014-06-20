'''
Read sample FB graph data and aggregate all user's friends.

Also flipped the grouping so all friend's users are grouped.

Expanded for multi step

Add creating keys out of friend pairs and count the number of pairs in common

'''

from mrjob.job import MRJob
import re
import itertools

class MRCountFriend(MRJob):

    def map_friends(self, _, line):
        val = line.split(' ')
        yield val[0], val[1]
        yield val[1], val[0]

    def create_friend_list(self, user_id, friend_id):
        yield user_id, list(friend_id)

    def pair_associations(self, user, friends):
        for pair in (itertools.combinations(friends, 2)):
            yield pair, user

    def count_users(self, pair, user):
        yield pair, len(list(user))

    def steps(self):
        return [self.mr(mapper=self.map_friends,
            reducer=self.create_friend_list), 
            self.mr(mapper=self.pair_associations, reducer=self.count_users)
        ]

if __name__ == '__main__':
    MRCountFriend.run()