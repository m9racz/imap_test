import imap

host = 'super-test.com'
username = 'alpha@super-test.com'
pw = 'a'

connection = imap.imap_test(host, username, pw)

#test scenario
active_folder = connection.test_create_folder('TEST')
connection.test_folder_cs()
active_folder = connection.test_rename_folder(active_folder)
connection.test_idle_mode()


msg_ID = connection.test_received_msg()
connection.test_search_msg()

active_folder = connection.test_copy_msg(ID=msg_ID, folder_to=active_folder)

connection.test_del_MSG(ID=msg_ID, folder=active_folder)



#print(connection.test_name_folder("NAme"))

#print(connection.test_rename_folder("TEST_FOLDER"))
#connection.test_received_msg()
#print(connection.test_search_msg())