#!/usr/bin/env python

import sys, paramiko, os

hostname = ""
username = ""
password = ""
privateKey = ""
port = 22

class SFTPHost():
    def __init__(self):
        self.private_key = 0
        self.transporter = 0
        self.sftp = 0

    def getFiles(self, source, destination):
        sftp_handler.sftp.chdir(source)
        files = self.sftp.listdir();
        for name in files:
            fileSystem =  destination+name
            sftp_handler.sftp.get(name, fileSystem)

    def putFiles(self, source, destination):
        for root, dirs, files in os.walk(source, topdown=False):
           for name in files:
               sourceFileToSend = source+name
               destinationFileSystem =  destination+name
               sftp_handler.sftp.put(sourceFileToSend, destinationFileSystem)
               

def main():
    try:
        sftp_handler.private_key = paramiko.RSAKey.from_private_key_file(privateKey)
        sftp_handler.transporter = paramiko.Transport((hostname, port))
        sftp_handler.transporter.connect(username=username, password=password, pkey=sftp_handler.private_key)
        sftp_handler.sftp = paramiko.SFTPClient.from_transport(sftp_handler.transporter)

        print("connected")
        
    finally:
        sftp_handler.transporter.close()


if __name__ == "__main__":
    sftp_handler = SFTPHost()
    main()
