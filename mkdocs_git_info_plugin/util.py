from git import Git
from datetime import datetime


class Util:

    def __init__(self):
        self.g = Git()

    def get_timestamps_for_file(self, path: str):
        
        # unix timestamp is UTC
        unix_timestamp = int(self.g.log(path, n=1, format='%at'))
        dt = datetime.utcfromtimestamp(unix_timestamp)

        timestamps = {
            'unix': unix_timestamp,
            'short': dt.strftime('%Y-%m-%d'),
            'long': dt.strftime('%Y-%m-%d %H:%M:%S'),
            'iso': dt.isoformat()
        }

        return timestamps

    def get_number_of_commits_for_file(self, path: str):

        return int(self.g.rev_list('--all', '--count', path))

    def get_number_of_authors_for_file(self, path: str):
        
        auhtor_string = self.g.log(path, format='%aN')
        auhtor_list = auhtor_string.split('\n')
        author_count = len(set(auhtor_list))
        return author_count