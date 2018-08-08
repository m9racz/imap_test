import imap

host = 'lenka.test.com'
#host = 'super-test.com'
#host = 'win2k8x32.test.com'

username = 'beta@' + host
pw = 'a'

connection = imap.imap_test(host, username, pw)
connection.server.send_IWconnector()
#connection.xatom('X-ICEWARP-SERVER iwconnector')


#=========== test scenario BASICS =====================
#create folder
active_folder = connection.test_create_folder('TEST')

#check case sensitivity in folders
connection.test_folder_cs()
connection.server.delete_folder('TEST_folder')

#rename folder
active_folder = connection.test_rename_folder(active_folder)

#IDLE mode of server
connection.test_idle_mode()

#FLAG - flagged and Completed
msg = connection.send_test_msg(to=username)
imap.time.sleep(2)
msg_ID = connection.find_msg_by_subject(subject = msg['Subject'])
connection.test_flag_msg(ID=msg_ID,flag="\\Flagged")
msg_flag = connection.test_flag_msg(ID=msg_ID,flag="$Completed")
connection.server.select_folder('INBOX')
connection.server.delete_messages(msg_ID)
    #msg_flag = connection.test_flag_msg(ID=msg_ID,flag=["\\Flagged","$Completed"])

#send & received msg
msg_ID = connection.test_received_msg()
msg_ID_inbox = msg_ID
#find MSG
connection.test_search_msg()
connection.server.select_folder('INBOX')
#connection.server.delete_messages(msg_ID)

#Copy MSG
msg_ID = connection.test_copy_msg(ID=msg_ID, folder_to=active_folder)



#===== uklid =====
#connection.server.select_folder('INBOX')
#connection.server.delete_messages(msg_ID_inbox)
#connection.test_delete_folder(active_folder)

#delete MSG
#connection.test_del_MSG(ID=msg_ID)

#=========== test scenario ADVANCED =====================
#create folder structure
connection.create_folder_tree()

#test XLIST returns
connection.test_xlist_pattern(expected=["INBOX/SUB_INBOX2","INBOX/SUB_INBOX1"])
connection.test_xlist_pattern(folder="",pattern="INBOX/%",expected=["INBOX/SUB_INBOX2","INBOX/SUB_INBOX1"])
connection.test_xlist_pattern(folder="",pattern="inbox/%",expected=["INBOX/SUB_INBOX2","INBOX/SUB_INBOX1"])
connection.test_xlist_pattern(folder="",pattern="Inbox/%",expected=["INBOX/SUB_INBOX2","INBOX/SUB_INBOX1"])
#connection.test_xlist_pattern(folder="INBOX/",pattern="*",expected=["INBOX/SUB_INBOX2","INBOX/SUB_INBOX1"])
#connection.test_xlist_pattern(folder="inbox/",pattern="*",expected=["INBOX/SUB_INBOX2","INBOX/SUB_INBOX1"])
#connection.test_xlist_pattern(folder="Inbox/",pattern="*",expected=["INBOX/SUB_INBOX2","INBOX/SUB_INBOX1"])
connection.test_xlist_pattern(folder="FOLDER1",pattern="*",expected=["FOLDER1/SUBFOLDER1-1","FOLDER1/SUBFOLDER1-2"])
connection.test_xlist_pattern(folder="",pattern="*",expected=["FOLDER1/SUBFOLDER1-1","FOLDER1/SUBFOLDER1-2","INBOX/SUB_INBOX2","INBOX/SUB_INBOX1","FOLDER1","FOLDER2","INBOX","FOLDER2/SUBFOLDER2-1","FOLDER2/SUBFOLDER2-2"])

#test subscribe and unsubscribe folder
connection.test_subscribe()
connection.test_unsubscribe()
connection.send_test_msg(to='public-folders@super-test.com')
connection.test_subscribe(folder="Public/INBOX")
connection.test_unsubscribe(folder="Public/INBOX")
connection.test_subscribe(folder="Public/inbox")
connection.test_unsubscribe(folder="Public/inbox")
connection.test_subscribe(folder="Public/Inbox")
connection.test_unsubscribe(folder="Public/Inbox")

#test Move subfolder to another subfolder
connection.test_move_folder()
connection.test_move_folder(from_folder = "folder2/SUBfolder2-2", to_folder = "FOLDER1/podadresář2-2")



connection.server.logout()


