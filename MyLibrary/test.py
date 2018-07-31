import imap
#import imaplib

host = 'lenka.test.com'
username = 'alpha@lenka.test.com'
pw = 'a'
'''
host = 'super-test.com'
username = 'alpha@super-test.com'
pw = 'a'
'''
#CONN = imaplib.IMAP4(host)
#CONN.login(username, pw)

#CONN.send(bytes('a X-ICEWARP-SERVER iwconnector', 'ascii') + b'\r\n')

#CONN.list()
#CONN.xatom('X-ICEWARP-SERVER iwconnector')
#print(CONN.select())
#print(CONN.search(None, 'SUBJECT', 'fdsfsd'))



connection = imap.imap_test(host, username, pw)
connection.xatom('X-ICEWARP-SERVER iwconnector')
#connection.server.send_IWconnector()

#connection.create_folder_tree()

#xlist = connection.server.xlist_folders('','inbox/%')
#print(xlist)
#folders = ["INBOX/SUB_INBOX2","INBOX/SUB_INBOX1"]
#connection.test_xlist_pattern(expected=["INBOX/SUB_INBOX2","INBOX/SUB_INBOX1"])
#connection.test_xlist_pattern(folder="",pattern="INBOX/%",expected=["INBOX/SUB_INBOX2","INBOX/SUB_INBOX1"])
#connection.test_xlist_pattern(folder="FOLDER1",pattern="*",expected=["FOLDER1/SUBFOLDER1-1","FOLDER1/SUBFOLDER1-2"])
#xlist = connection.server.xlist_folders('','Inbox/%')
#connection.test_xlist_pattern(expected=["INBOX/SUB_INBOX2","INBOX/SUB_INBOX1"])
connection.test_xlist_pattern(folder="",pattern="inbox/%",expected=["INBOX/SUB_INBOX2","INBOX/SUB_INBOX1"])
connection.test_xlist_pattern(folder="",pattern="INBOX/%",expected=["INBOX/SUB_INBOX2","INBOX/SUB_INBOX1"])
#connection.test_xlist_pattern(folder="FOLDER1",pattern="*",expected=["FOLDER1/SUBFOLDER1-1","FOLDER1/SUBFOLDER1-2"])
#connection.test_xlist_pattern(folder="",pattern="*",expected=["FOLDER1/SUBFOLDER1-1","FOLDER1/SUBFOLDER1-2","INBOX/SUB_INBOX2","INBOX/SUB_INBOX1","FOLDER1","FOLDER2","INBOX","FOLDER2/SUBFOLDER2-1","FOLDER2/SUBFOLDER2-2"])

#type(xlist)

#for names in xlist:
#    print(names)

#print(connection.server.capabilities())
#connection.server.send_IWconnector()
#connection.server.select_folder('INBOX')

#connection.test_create_folder('TEST')
#print(connection.server._raw_command(b'X-ICEWARP-SERVER',b'iwconnector',uid=False))

#print(connection.server._command_and_check('x-icewarp-server iwconnector "12.1.2.0.31125 (2018-06-13)"', unpack=True))