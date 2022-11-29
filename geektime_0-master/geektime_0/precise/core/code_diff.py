from dataclasses import dataclass

import git

from geektime_0.precise.core.code_line import CodeLine


@dataclass
class CodeDiff:
    def __init__(self):
        self.data: list[CodeLine]=[]

    def load(self, project, old, new):
        repo = git.Repo(project)
        commit_dev = repo.commit(new)
        commit_origin_dev = repo.commit(old)
        diff_index = commit_origin_dev.diff(commit_dev)

        for diff_item in diff_index.iter_change_type('M'):
            print("A blob:\n{}".format(diff_item.a_blob.data_stream.read().decode('utf-8')))
            print("B blob:\n{}".format(diff_item.b_blob.data_stream.read().decode('utf-8')))

