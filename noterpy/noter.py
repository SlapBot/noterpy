from collections.abc import Sequence
from simplenote import Simplenote


class Noter:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.token = None
        self.simple_note = Simplenote(email, password)

    def authenticate(self, email, password):
        token = self.simple_note.authenticate(email, password)
        return token

    def get_token(self):
        self.token = self.authenticate(self.email, self.password)
        return self.token

    def get_note_list(self, since=None, tags=None):
        if tags is None:
            tags = []
        data = self.simple_note.get_note_list(since=since, tags=tags)
        return NoteList(data[0], self.simple_note)

    def add_note(self, content, tags=None, note=None):
        if note:
            return self.simple_note.add_note(note)
        note = {}
        if tags:
            if isinstance(tags, list):
                note['tags'] = tags
            else:
                note['tags'] = [tags]
        note['content'] = content
        return NoteInfo(self.simple_note.add_note(note)[0], self.simple_note)


class NoteList(Sequence):
    def __getitem__(self, index):
        return self.notes[index]

    def __len__(self):
        return len(self.notes)

    def __init__(self, data, simple_note):
        self.data = data
        self.simple_note = simple_note
        self.notes = []
        self.process()

    def process(self):
        for note in self.data:
            self.notes.append(NoteInfo(note, self.simple_note))


class BaseNote:
    def __init__(self, note, simple_note):
        self.simple_note = simple_note
        self.tags = note['tags']
        self.version = note['version']
        self.modify_date = note['modifydate']
        self.sync_num = note['syncnum']
        self.system_tags = note['systemtags']
        self.key = note['key']
        self.create_date = note['createdate']
        self.deleted = note['deleted']

    def update(self, content, tags=None):
        note = {
            "key": self.key,
            "tags": self.tags,
        }
        if tags:
            if isinstance(tags, list):
                note['tags'] = tags
            else:
                note['tags'] = [tags]
        note['content'] = content
        return NoteInfo(self.simple_note.update_note(note)[0], self.simple_note)

    def trash(self):
        return NoteInfo(self.simple_note.trash_note(self.key)[0], self.simple_note)

    def delete(self):
        status = self.simple_note.delete_note(self.key)[1]
        return status


class NoteInfo(BaseNote):
    def __init__(self, note_info, simple_note):
        super(NoteInfo, self).__init__(note_info, simple_note)
        self.min_version = note_info['minversion']

    def get(self):
        note = self.simple_note.get_note(self.key)
        return Note(note[0], self.simple_note)

    def get_by_version(self, version):
        note = self.simple_note.get_note(self.key, version=version)
        return NoteVersion(note[0], self.simple_note)


class Note(BaseNote):
    def __init__(self, note, simple_note):
        super(Note, self).__init__(note, simple_note)
        self.content = note['content']


class NoteVersion:
    def __init__(self, note, simple_note):
        self.simple_note = simple_note
        self.version = note['version']
        self.content = note['content']
        self.version_date = note['versiondate']
