import re

from Exscript.protocols.drivers import Driver

_user_re = [re.compile(r'login:')]
_password_re = [re.compile(r'Password:')]
_prompt_re = [re.compile(r'.*>\s'),
              re.compile(r'#\s')]

_apresia_re = re.compile(r"Apresia")

class AEOSDriver(Driver):

    def __init__(self):
        Driver.__init__(self, 'aeos')
        self.user_re = _user_re
        self.password_re = _password_re
        self.prompt_re = _prompt_re

    def check_head_for_os(self, string):
        if _apresia_re.search(string):
            return 100
        return 0

    def init_terminal(self, conn):
        conn.execute('enable\r')
        conn.execute('conf t\r')
        conn.execute('term len 0\r')

    def auto_authorize(self, conn, account, flush, bailout):
        pass
