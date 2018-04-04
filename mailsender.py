# coding:utf-8
# python3 soucecode
# author : rogerclark



import os
import time
import imaplib, smtplib, email
import pprint
import chardet
import getpass

# set basic parameters of ustc mail box

POP_USTC, IMAP_USTC, SMTP_USTC = 110, 143, 25
ENC_POP_USTC, ENC_IMAP_USTC, ENC_SMTP_USTC = 995, 993, 465
HOST_USTC = 'mail.ustc.edu.cn'
# login process

def mkdir(path):
    """
    make a folder at specific path
    """
    pathexists = os.path.exists(path)
    if pathexists:
        print('path {} has existed'.format(path))
    else:
        os.makedirs(path)
        print('path {} has created successful'.format(path))
    return not pathexists


def login_imap(host, port, username, passwd, ssl = True):
    """
    login email server and return the client subject
    """
    if ssl:
        client = imaplib.IMAP4_SSL(host = host, port = port)
    else:
        client = imaplib.IMAP4(host = host, port = port)
    client.login(getpass.username_ustc, getpass.passwd_ustc)
    return client
def get_attachment(msg, header, path):
    """
    fetch the content and attachment of email
    """
    for part in msg.walk():
        filename = part.get_filename()
        content = part.get_content_type()
        if filename:
            filename_decode = email.header.decode_header(filename)[0]
            if type(filename_decode[0]) is bytes:
                try:
                    filename = filename_decode[0].decode(filename_decode[1],
                    errors='ignore')
                except UnicodeError:
                    filename = 'error_unicode_' + 'filename_decode[1]'
            else:
                filename = filename_decode[0]
            data = part.get_payload(decode=True)
            with open(path + filename, 'wb+') as f:
                f.write(data)
                print('write complete!:{}'.format(filename))
        elif content == 'text/plain':
            data = part.get_payload(decode=True)
            charset = chardet.detect(data)['encoding']
            try:
                data = data.decode(charset, errors='ignore')+'\n'+str(header)
            except UnicodeError:
                pass
            with open(path + header['subject'], 'w+') as f:
                f.write(data)

def fetch_imap(client, savepath=True, mailbox = 'INBOX',
search_key = '(LARGER 10485760)', delete=False):
    """
    screen the mailbox, select and fetch the header of mails
    """
    # FIXME: there are some problem with encoding, cannot find right charset
    client.select(mailbox = mailbox)
    typ, data = client.search(None, search_key)
    titlelist=[]
    if typ == 'OK':
        mail_index = data[0].split()
        print('search complete, there are %d mails fit the search condition'
         %(len(mail_index)))
        for index, mail in enumerate(mail_index):
            print('Fetching the {}st mail from {}...\n'
            .format(index+1, client.host))
            try:
                code, raw = client.fetch(mail, '(RFC822)')
            except imaplib.IMAP4.error:
                print('Fetching faluire!, mail index:{}\n'
                .format(mail.decode('utf-8')))
            print('Download complete!')
            #charinfo = chardet.detect(raw[0][1])
            #print('encoding:{}  confidence:{}'.format(charinfo['encoding'],
            #charinfo['confidence']))
            msg = email.message_from_bytes(raw[0][1])
            # get attachment and header from ms
            msg_header = {'from':'None', 'date':'None', 'subject':'None'}
            for key in msg_header:
                data = msg.get(key)
                if data:
                    decode_data = email.header.decode_header(data)[0]
                    if decode_data[1]:
                        try:
                            decode_str = decode_data[0].decode(decode_data[1], 'ignore')
                        except Exception:
                            print('decode error, encoding:{}'.
                            format(decode_data[1]))
                            decode_str = 'WRONG_ENCODE'+str(index+1)
                    else:
                        decode_str = decode_data[0]
                    msg_header[key] = decode_str
            print(msg_header)
            titlelist.append(msg_header['subject'])
            #get_attachment(msg, msg_header)
            path = savepath + '/'+msg_header['subject'] + '/'
            trymk = mkdir(path)
            if trymk:
                get_attachment(msg, msg_header, path)
            else:
                path = savepath + '/' + msg_header['subject']+'2'+'/'
                get_attachment(msg, msg_header, path)
    else:
        raise RuntimeError('search failue reason:{}'.format(typ))
    if delete:
        print('Are you sure you want to delete these mails?\n')
        pprint.pprint(titlelist)
        user_choose = input('Press Y/N ?\n')
        if user_choose == 'Y':
            for mail in zip(mail_index, titlelist):
                res = client.store(mail[0], '+FLAGS', '\\Deleted')
                time.sleep(5)
                print(res)
                print('mail:{} has been deleted'.format(mail[1]))
            resp = client.expunge()
            print(resp)
        else:
            print('Delete process is cancelled by user')
            client.logout()
    else:
        client.logout()

    def delmail(mailindex):
        pass

if __name__ == '__main__':
    client = login_imap(host = HOST_USTC, port = ENC_IMAP_USTC,
    username = getpass.username_ustc, passwd = getpass.passwd_ustc)
    searchkey = '(FROM "rogerclark")'
    fetch_imap(client, savepath='/home/roger/Documents', delete=True,
    search_key=searchkey)
