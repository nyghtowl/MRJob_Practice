'''
Read sample FB graph data and aggregate all user's friends.

Also flippsed the grouping so all friend's users are grouped.

'''

from mrjob.job import MRJob
import re

class MRCountFriend(MRJob):

    def map_friends(self, _, line):
        val = line.split(' ')
        yield val[0], val[1]
        yield val[1], val[0]

    def create_friend_list(self, user_id, friend_id):
        yield user_id, list(friend_id)

    def steps(self):
        return [self.mr(mapper=self.map_friends,
            reducer=self.create_friend_list)
        ]

if __name__ == '__main__':
    MRCountFriend.run()