import imap

host = 'super-test.com'
username = 'alpha@super-test.com'
pw = 'a'

connection = imap.imap_test(host, username, pw)

#===========test scenario=====================
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

#find MSG
connection.test_search_msg()
connection.server.select_folder('INBOX')
connection.server.delete_messages(msg_ID)

#Copy MSG

connection.test_copy_msg(ID=msg_ID, folder_to=active_folder)
connection.test_delete_folder(active_folder)

#delete MSG
#connection.test_del_MSG(ID=msg_ID)







#print(connection.test_name_folder("NAme"))

#print(connection.test_rename_folder("TEST_FOLDER"))
#connection.test_received_msg()
#print(connection.test_search_msg())