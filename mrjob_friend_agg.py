'''
Read sample FB graph data and aggregate all user's friends.

Also flippsed the grouping so all friend's users are grouped.

'''

from mrjob.job import MRJob
import re

class MRCountFriend(MRJob):

    def mapper(self, _, line):
        val = line.split(' ')
        yield val[0], val[1]
        yield val[1], val[0]

    def reducer(self, user_id, friend_id):
        yield user_id, list(friend_id)

if __name__ == '__main__':
    MRCountFriend.run()