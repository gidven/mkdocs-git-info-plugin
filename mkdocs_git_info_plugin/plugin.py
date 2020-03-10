from mkdocs.plugins import BasePlugin
from .util import Util


class GitInfoPlugin(BasePlugin):
    '''
    Simple plugin to return Git data as object in the context of 
    '''

    def __init__(self):
        self.util = Util()

    def on_page_context(self, context, page, config, nav, **kwargs):

        _path = page.file.abs_src_path

        _timestamps = self.util.get_timestamps_for_file(_path)
        
        context['git_info'] = {
            'last_updated_unix': _timestamps['unix'],
            'last_updated_short': _timestamps['short'],
            'last_updated_long': _timestamps['long'],
            'last_updated_iso': _timestamps['iso'],
            'number_commits': self.util.get_number_of_commits_for_file(_path),
            'number_authors': self.util.get_number_of_authors_for_file(_path)
        }

        return context