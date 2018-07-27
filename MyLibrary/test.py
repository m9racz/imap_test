import imap
#import imaplib

host = 'super-test.com'
username = 'alpha@super-test.com'
pw = 'a'

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

xlist = connection.server.xlist_folders('','Inbox/%')

folders = ["INBOX/SUB_inbox2","INBOX/SUB_inbox1"]

for folder in xlist:
    if folder[2] in folders:
        print(folder[2])


#xlist = connection.server.xlist_folders('','Inbox/%')

#type(xlist)

#for names in xlist:
#    print(names)

#print(connection.server.capabilities())
#connection.server.send_IWconnector()
#connection.server.select_folder('INBOX')

#connection.test_create_folder('TEST')
#print(connection.server._raw_command(b'X-ICEWARP-SERVER',b'iwconnector',uid=False))

#print(connection.server._command_and_check('x-icewarp-server iwconnector "12.1.2.0.31125 (2018-06-13)"', unpack=True))