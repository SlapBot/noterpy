import unittest
from noterpy.noter import Noter

""" MAKE SURE TO TEST EACH TEST FUNCTION ALONE SINCE LOTS OF REQUEST BEING MADE TO SIMPLENOTE
LEADS TO INTERNAL SERVER ERROR 500 IF YOUR ACCOUNT IS OF FREE SUBSCIPTION"""


class TestNoter(unittest.TestCase):
    @staticmethod
    def do_init():
        noter = Noter("mafowohet@katztube.com", "Slapbot")
        return noter

    def test_noter_init(self):
        n = self.do_init()
        if n:
            self.assertEqual(True, True)
        else:
            self.assertEqual(False, True)

    def test_authenticate(self):
        n = self.do_init()
        token = n.authenticate("mafowohet@katztube.com", "Slapbot")
        self.assertEqual(token, b'36EA18B26481A6D83D0225FF7F1BBEEF15ADC633760A965E39D7E9E160291819')

    def test_get_note_list_length(self):
        n = self.do_init()
        noteslist = n.get_note_list()
        length = len(noteslist.notes)
        self.assertEqual(length, 13)

    def test_get_note_list(self):
        n = self.do_init()
        noteslist = n.get_note_list()
        for note in noteslist.notes:
            status = isinstance(note.key, str)
            self.assertEqual(status, True)

    def test_note(self):
        n = self.do_init()
        noteinfo = n.add_note("new note")
        status = isinstance(noteinfo.key, str)
        self.assertEqual(status, True)
        noteinfo = noteinfo.update("new content")
        note = noteinfo.get()
        self.assertEqual(note.content, "new content")
        noteinfo = note.trash()
        self.assertEqual(noteinfo.deleted, 1)
        status = noteinfo.delete()
        self.assertEqual(status, -1)


if __name__ == "__main__":
    unittest.main()
