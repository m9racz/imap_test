import imap
#import imaplib
'''
host = 'lenka.test.com'
username = 'beta@lenka.test.com'
pw = 'a'
'''
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
connection.server.send_IWconnector()
connection.send_test_msg(to='public-folders@super-test.com')
connection.test_subscribe(folder="Public/INBOX")
#msg_ID = connection.find_msg_by_subject(subject ='Guida: Firma di dominio')
#print(msg_ID)

#connection.server.select_folder('INBOX')
#connection.server.rename_folder('inbox/aaa','inbox/podadresář2')



#xlist = connection.server.xlist_folders('','*')
#print(xlist)
#connection.server.subscribe_folder('FOLDER2')

#folder = 'FOLDER1/SUBfolder1-2'
#connection.server.create_folder(folder)
#print(connection.server.subscribe_folder(folder))
#lsub = connection.server.list_sub_folders()
#connection.test_unsubscribe()

#print(connection.server.unsubscribe_folder(folder))
#print(connection.server.list_sub_folders())
#connection.server.delete_folder(folder)


#print(connection.server.getacl('group_all@lenka.test.com/INBOX'))



#connection.create_folder_tree()
#connection.test_subscribe(folder='group_all@lenka.test.com/INBOX')
#xlist = connection.server.xlist_folders('','*')
#print(xlist)

#connection.test_xlist_pattern(expected=["INBOX/SUB_INBOX2","INBOX/SUB_INBOX1"])
#connection.test_xlist_pattern(folder="",pattern="inbox/%",expected=["INBOX/SUB_INBOX2","INBOX/SUB_INBOX1"])
#connection.test_xlist_pattern(folder="",pattern="INBOX/%",expected=["INBOX/SUB_INBOX2","INBOX/SUB_INBOX1"])
#connection.test_xlist_pattern(folder="FOLDER1",pattern="*",expected=["FOLDER1/SUBFOLDER1-1","FOLDER1/SUBFOLDER1-2"])
#connection.test_xlist_pattern(folder="",pattern="*",expected=["FOLDER1/SUBFOLDER1-1","FOLDER1/SUBFOLDER1-2","INBOX/SUB_INBOX2","INBOX/SUB_INBOX1","FOLDER1","FOLDER2","INBOX","FOLDER2/SUBFOLDER2-1","FOLDER2/SUBFOLDER2-2"])

#print(connection.server.append('INBOX', "nejaky text XXX"))



#xlist = connection.server.xlist_folders('','*')
#print(xlist)

#print(connection.server.capabilities())
#connection.server.send_IWconnector()
#connection.server.select_folder('INBOX')

#connection.test_create_folder('TEST')
#print(connection.server._raw_command(b'X-ICEWARP-SERVER',b'iwconnector',uid=False))

#print(connection.server._command_and_check('x-icewarp-server iwconnector "12.1.2.0.31125 (2018-06-13)"', unpack=True))