'''
Read FB graph data and aggregate all users friends
'''

from mrjob.job import MRJob
import re

class MRCountFriend(MRJob):

    def mapper(self, _, line):
        yield line[0], line[1]

    def reducer(self, user_id, friend_id):
        yield user_id, list(friend_id)

if __name__ == '__main__':
    MRCountFriend.run()