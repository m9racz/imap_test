import imap

host = 'super-test.com'
username = 'alpha@super-test.com'
pw = 'a'

connection = imap.imap_test(host, username, pw)
connection.server.send_IWconnector()

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
msg = connection.send_test_msg()
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
connection.test_delete_folder(active_folder)

#delete MSG
#connection.test_del_MSG(ID=msg_ID)

#=========== test scenario BASICS =====================



connection.server.logout()


