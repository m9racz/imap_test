from __future__ import unicode_literals
from imapclient import IMAPClient
from email.mime.text import MIMEText
import imaplib
import smtplib
import random
import time
import datetime

class imap_test(object):
    '''test imap server: working with folders and messages + IDLE mod of server

    Attributes:
        host:
        username:
        password:
    '''
    def __init__(self, host, username, password):
        """create server object with credentials"""
        self.host = host
        self.username = username
        self.password = password
        self.server = self.login()

    def xatom(self, name, *args):
        """
        !!!override method without RFC compatibility
        Allow simple extension commands
                notified by server in CAPABILITY response.

        Assumes command is legal in current state.

        (typ, [data]) = <instance>.xatom(name, arg, ...)

        Returns response appropriate to extension command `name'.
        """
        name = name.lower()
        #if not name in self.capabilities:      # Let the server decide!
        #    raise self.error('unknown extension command: %s' % name)
        try:
                self.server._imap._simple_command(name, *args)
        except:
                pass

    def login(self, ssl = False):
        '''try to login over imap to server with credential in attributes
            return server object
        '''
        server = IMAPClient(self.host, use_uid=True, ssl=ssl)
        try:
            server.login(self.username, self.password)
            print('login successful')
            return server
        except imaplib.IMAP4.error as err:
            print("login failed:\nHost = ", self.host, "\nUser = ", self.username, "\nPW  = ", self.password)
            print(str(err))
            raise RuntimeError("can't login: ", err)

    def test_name_folder(self, name):
        '''return false if this folder already exists
        '''
        xlist = self.server.xlist_folders()
        for names in xlist:
            if str(names[2]) == name:
                return False
        return True

    def test_create_folder(self, test_folder = "TEST_folder"):
        '''try to create folder, if already exists it create another one and test it... return name of tested folder
        '''
        i = 0
        while not self.test_name_folder(test_folder):
            i += 1
            test_folder = test_folder + str(i)
        try:
            self.server.create_folder(test_folder)
        except imaplib.IMAP4.error as err:
            if str(err) == "create failed: CREATE Mailbox already exists":
                print("folder %s already exists..." %test_folder)
                raise RuntimeError("folder already exist: ", err)
            else:
                print("ERROR: ", err)
            #return err
            raise RuntimeError("unknow error: ", err)
        except:
            print("nejaka jina chyba:", err)
            #return err
            raise RuntimeError("unknow error: ", err)
        try:
            self.server.select_folder(test_folder)
        except imaplib.IMAP4.error as err:
            print("TEST - create folder - FAILED")
            print(str(err))
            return False
        else:
            print("TEST - create folder - OK")
            self.server.close_folder()
            return test_folder

    def test_folder_cs(self, test_folder = "TEST_folder"):
        '''Try to create swapcased folder if it's not possible => OK
        '''
        swap_folder = test_folder.swapcase()
        if self.test_name_folder(test_folder):
            i = 0
            while not self.test_name_folder(test_folder):
                i += 1
                test_folder = test_folder + str(i)
            self.server.create_folder(test_folder)
        try:
            self.server.create_folder(swap_folder)
        except imaplib.IMAP4.error as err:
            if str(err) == "create failed: CREATE Mailbox already exists":
                print("TEST - case sensitivity - OK")
                return True
        except:
            print("nejaka jina chyba:", err)
            raise RuntimeError("unknow error: ", err)
        else:
            print("TEST - case sensitivity - FAILED")
            print(str(err))
            return False

    def test_rename_folder(self, test_folder = "TEST_folder"):
        '''it rename folder to another one. returns name of new folder 
        '''
        xlist = self.server.xlist_folders()
        if not self.test_name_folder(test_folder):
            new_folder = test_folder + '-new'
            i = 0
            while not self.test_name_folder(new_folder):
                i += 1
                new_folder = new_folder + str(i)
            try:
                self.server.rename_folder(test_folder, new_folder)
                try:
                    self.server.select_folder(new_folder)
                except imaplib.IMAP4.error as err:
                    print("TEST - rename folder - FAILED")
                    print(str(err))
                    raise RuntimeError("can't open new folder: ", err)
                else:
                    print("TEST - rename folder - OK")
                    self.server.close_folder()
                    return new_folder
            except imaplib.IMAP4.error as err:
                print("TEST - rename folder - FAILED")
                print(str(err))
                raise RuntimeError("rename folder failed: ", err)
        else:
            print("Folder to rename doesn't exists...")
            return False                                                      #DOPSAT VLASTNI EXCEPTION!!!!

    def send_test_msg(self, to):
        '''send MSG with random subject to self
        return this message...
        '''
        test_msg = MIMEText('Testovaci zprava...')
        test_msg['Subject'] = 'TEST email c.: ' + str(random.randrange(10000,99999))
        test_msg['From'] = self.username
        test_msg['To'] = to
        try:
            s = smtplib.SMTP(self.host)
            try:
                s.send_message(test_msg)
                s.quit()
                return test_msg
            except smtplib.SMTPException as err:
                print(str(err))
                raise RuntimeError("unable to send MSG:", err)
        except smtplib.SMTPException as err:
            print(str(err))
            raise RuntimeError("can't setup connection to SMTP server:", err)

    def test_idle_mode(self):
        self.send_test_msg(to=self.username)
        self.server.select_folder('INBOX')
        try:
            self.server.idle()
        except imaplib.IMAP4.error as err:
            print("TEST - IDLE MODE - FAILED")
            print(str(err))
            raise RuntimeError("Can't start IDLE mode:", err)
        try:    
            check = self.server.idle_check(7)
            self.server.idle_done()
            self.server.close_folder()
            if check == []:
                print("TEST - IDLE MODE - FAILED")
                return False
            else:
                print("TEST - IDLE MODE - OK")
                return True
        except imaplib.IMAP4.error as err:
            print("TEST - IDLE MODE - FAILED")
            print(str(err))
            raise RuntimeError("Can't start waiting mode:", err)

    def find_msg_by_subject(self, folder = 'INBOX', subject = None):
        '''it try to find latest message in specific folder by msg's subject
        return ID of this msg or false if nothing is found
        '''
        try:
            self.server.select_folder(folder)
        except imaplib.IMAP4.error as err:
            raise RuntimeError("This folder doesn't exists....", err)

        msg = self.server.search([b'NOT', b'DELETED'])
        msg_ID = None
        if msg != []:
            for x in reversed(msg):
                try:
                    msg_details = (self.server.fetch([x], 'ENVELOPE'))
                    subject2 = msg_details[x][b'ENVELOPE'].subject
                    if str(subject2.decode("utf-8")) == str(subject):
                        msg_ID = x
                        break
                except imaplib.IMAP4.error as err:
                    print("TEST - received MSG - FAILED")
                    print(str(err))  
                    self.server.close_folder()
                    raise RuntimeError("Can't fetch msg from server:", err)
            self.server.close_folder()
        else:
            print("TEST - received MSG - FAILED (MSG not found...)")
            self.server.close_folder()
            return False
        if msg_ID == None:
            print("TEST - received MSG - FAILED")
            return False
        else:
            #print("TEST - received MSG - OK")
            return msg_ID

    def test_received_msg(self):
        '''It send MSG and than try to received it...
        return msg_ID
        '''
        test_msg = self.send_test_msg(to=self.username)
        #test_msg['Subject']
        time.sleep(2)
        return self.find_msg_by_subject(subject = test_msg['Subject'])

    def test_search_msg(self):
        '''try to find any today MSG...
        '''
        self.server.select_folder('INBOX')
        try:
            if self.server.search([u'SINCE', datetime.date.today()]):
                self.server.close_folder()
                print("TEST - SEARCHING MSG - OK")
                return True
            else:
                print("TEST - SEARCHING MSG - FAILED")
                return False
        except imaplib.IMAP4.error as err:
            print("TEST - SEARCHING MSG - FAILED")
            print(str(err))
            raise RuntimeError("Can't search in server:", err)

    def test_copy_msg(self, ID = None, folder_from = 'INBOX',folder_to = 'TEST_folder'):
        '''try copy MSG with specific ID and folder and than find this MSG in new folder...
        default folder_from is 'INBOX'
        with no ID it send MSG and this msg copy to: folder_to if this folder doesn't exist it will create another one
        return name of folder where MSG was sent
        '''
        if ID == None:
            ID = self.test_received_msg()

        try:
            self.server.select_folder(folder_to)
            self.server.close_folder()
        except imaplib.IMAP4.error as err:
            folder_to = self.test_create_folder(folder_to)

        try:
            self.server.select_folder(folder_from)
        except imaplib.IMAP4.error as err:
            raise RuntimeError("Unable to select this folder:", folder_from , err)

        msg_details = (self.server.fetch([ID],'ENVELOPE'))
        subject = (msg_details[ID].get(b'ENVELOPE')).subject

        try:
            self.server.copy(ID, folder_to)
        except imaplib.IMAP4.error as err:
            print("TEST - COPY MSG - FAILED")
            print(str(err))
            return False
        finally:
            print("TEST - COPY MSG - OK")
            return self.find_msg_by_subject(folder=folder_to,subject=subject.decode("utf-8"))
      
    def test_del_MSG(self, ID = None, folder = 'INBOX'):
        '''try to delete MSG
        return True if is this MSG deleted...
        '''
        try:
            self.server.select_folder(folder)
        except imaplib.IMAP4.error as err:
            raise RuntimeError("Unable to select this folder:", folder , err)

        try:
            self.server.delete_messages(ID)
        except imaplib.IMAP4.error as err:
            print("TEST - DELETE MSG - FAILED")
            print(str(err))
            return False
        IDs = self.server.search(['NOT', 'DELETED'])
        if ID in IDs:
            print("TEST - DELETE MSG - FAILED")
            return False
        else:
            print("TEST - DELETE MSG - OK")
            return True
        self.server.close_folder()

    def test_flag_msg(self, ID = None, folder = 'INBOX', flag = '\\Flagged'):
        '''to specific msg in folder add specific flagged
            '\\Flagged'
            ["\\Flagged","$Completed"]
            return all flags in MSG
        '''
        try:
            self.server.select_folder(folder)
        except imaplib.IMAP4.error as err:
            raise RuntimeError("Unable to select this folder:", folder , err)
        
        try:
            FlagResponse = self.server.add_flags(ID,flag)
        except imaplib.IMAP4.error as err:
            print("TEST - FLAGED MSG - FAILED (",flag," - add_flags)")
            print(str(err))

        if flag.encode() in FlagResponse[ID]:
                print("TEST - FLAGED MSG - OK",flag)
        else:
            print("TEST - FLAGED MSG - FAILED (",flag," -is not in flag list)")
        self.server.close_folder()
        return FlagResponse[ID]
        
    def test_delete_folder(self, folder = 'TEST_folder'):
        '''to specific msg in folder add specific flagged
            return all flags in MSG
        '''
        try:
            self.server.delete_folder(folder)
            try:
                self.server.select_folder(folder)
            except imaplib.IMAP4.error as err:
                print("TEST  - delete folder - OK")
                return True
            else:
                print("TEST  - delete folder - FAILED")
                print(str(err))
                return False
        except imaplib.IMAP4.error as err:
            print("TEST  - delete folder - FAILED")
            print(str(err))
            return False

    def create_folder_tree(self):
        '''create folders and subfolders in mailbox
        -INBOX  -sub_inbox1
                -SUB_inbox2
        -FOLDER1 -subfolder1-1
                 -SUBfolder1-2
        -folder2 -subfolder2-1
                 -SUBfolder2-2
        '''
        folder_tree = ["FOLDER1","folder2","FOLDER1/subfolder1-1","FOLDER1/SUBfolder1-2","folder2/subfolder2-1","folder2/SUBfolder2-2","INBOX/sub_inbox1","INBOX/SUB_inbox2"]
        for folder in folder_tree:
            try:
                self.server.create_folder(folder)
            except imaplib.IMAP4.error as err:
                if str(err) == "create failed: CREATE Mailbox already exists":
                    print("folder %s already exists..." %folder)
                    #raise RuntimeError("folder already exist: ", err)
                    continue
                else:
                    print("ERROR: ", err)
                return False
                raise RuntimeError("unknow error: ", err)
            except:
                print("nejaka jina chyba:", err)
                return False
                raise RuntimeError("unknow error: ", err)

    def test_xlist_pattern(self,folder = "INBOX", pattern = "*", expected = ["INBOX/SUB_INBOX2","INBOX/SUB_INBOX1"]):
        '''test if xlist return correct folders
        expected write with capitals 
        '''
        xlist = self.server.xlist_folders(folder,pattern)
        count = 0
        list_fail = []
        xlist_name = []
        
        for folder in xlist:
            xlist_name.append(folder[2].upper())
        
        for item in expected:
            if item in xlist_name:
                count += 1
            else:
                list_fail.append(item)
        if count == len(expected):
            print("TEST - Xlist pattern - OK")
            return True
        else:
            print("TEST - Xlist pattern - FAIL ",list_fail," folder: ",folder, "pattern: ",pattern)

    def test_subscribe(self,folder = 'FOLDER1/SUBfolder1-2'):
        '''subscribe folder (default = 'FOLDER1/SUBfolder1-2') return True if is this folder in LSUB list
        '''
        returncode = False
        try:
            self.server.subscribe_folder(folder)
        except imaplib.IMAP4.error as err:
            print("unknow ERROR", err)
            return False
            raise RuntimeError("unknow error: ", err)
        except:
            print("nejaka jina chyba:", err)
            return False
            raise RuntimeError("unknow error: ", err)
        lsub = self.server.list_sub_folders()
        for item in lsub:
            if folder == item[2]:
                print("TEST - subscribe folder - OK")
                returncode = True
        
        if returncode == False:
            print("TEST - subscribe folder - FAIL")
        return returncode

    def test_unsubscribe(self,folder = 'FOLDER1/SUBfolder1-2'):
        '''unsubscribe folder (default = 'FOLDER1/SUBfolder1-2') return True if is not present this folder in LSUB list
        '''
        returncode = True
        try:
            self.server.unsubscribe_folder(folder)
        except imaplib.IMAP4.error as err:
            print("unknow ERROR", err)
            return False
            raise RuntimeError("unknow error: ", err)
        except:
            print("nejaka jina chyba:", err)
            return False
            raise RuntimeError("unknow error: ", err)
        lsub = self.server.list_sub_folders()
        for item in lsub:
            if folder == item[2]:
                print("TEST - unsubscribe folder - FAIL")
                returncode = False
        
        if returncode == True:
            print("TEST - unsubscribe folder - OK")
        return returncode    

    def test_move_folder(self, from_folder = "FOLDER1/SUBfolder1-2", to_folder = "FOLDER2/SUBfolder1-2"):
        '''
        '''
        xlist = self.server.xlist_folders()
        if not self.test_name_folder(from_folder):
            
            try:
                self.server.rename_folder(from_folder, to_folder)
                try:
                    self.server.select_folder(to_folder)
                except imaplib.IMAP4.error as err:
                    print("TEST - MOVE folder - FAILED")
                    print(str(err))
                    raise RuntimeError("can't open new folder: ", err)
                else:
                    if not self.test_name_folder(to_folder):
                        print("TEST - MOVE folder - OK")
                        self.server.close_folder()
                        return True
                    else:
                        print("TEST - MOVE folder - FAILED  -new folder is not reachable")
            except imaplib.IMAP4.error as err:
                print("TEST - MOVE folder - FAILED")
                print(str(err))
                raise RuntimeError("MOVE folder failed: ", err)
        else:
            print("TEST - MOVE folder - FAILED  -Folder to rename doesn't exists...")
            return False         
'''

    server.close_folder


    server.logout()
 '''

#host = 'super-test.com'
#username = 'alpha@super-test.com'
#pw = 'a'

#connection = imap_test(host, username, pw)

#print(connection.test_name_folder("NAme"))

#print(connection.test_rename_folder("TEST_FOLDER"))
#connection.test_received_msg()
#print(connection.test_received_msg())

#print(test_search_msg())
'''
try:
    session = serv.login()
except RuntimeError as err:
    print(err)
'''
