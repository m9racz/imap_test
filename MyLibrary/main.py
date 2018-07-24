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
    #msg_flag = connection.test_flag_msg(ID=msg_ID,flag=["\\Flagged","$Completed"])

#delete MSG
connection.test_del_MSG(ID=msg_ID)

#send & received msg
msg_ID = connection.test_received_msg()
connection.test_search_msg()
#connection.server.delete_messages(msg_ID)


#active_folder = connection.test_copy_msg(ID=msg_ID, folder_to=active_folder)
#print(active_folder)

connection.test_delete_folder(active_folder)









#print(connection.test_name_folder("NAme"))

#print(connection.test_rename_folder("TEST_FOLDER"))
#connection.test_received_msg()
#print(connection.test_search_msg())