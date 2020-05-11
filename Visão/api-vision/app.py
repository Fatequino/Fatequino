from flask import Flask
from flask_restful import Api, Resource, reqparse
from ftplib import FTP
import sys
import io
import ftplib 
import os

app = Flask(__name__)
api = Api(app)

account = [
	{
		"host": "fatequino.com.br",
		"user": "equipeweb",
		"pwd": "fatequino123"
	}
]

source = "/wp-content/uploads/rtMedia/users/"
destination = ""
interval = 0.05

def downloadFiles(path, destination, ftp):
    try:
        ftp.cwd(path)       
        os.chdir(destination)
        mkdir_p(destination[0:len(destination)-1] + path)
        print "Created: " + destination[0:len(destination)-1] + path
    except OSError:     
        pass
    except ftplib.error_perm:       
        print "Error: could not change to " + path
        sys.exit("Ending Application")
    
    filelist=ftp.nlst()

    for file in filelist:
        time.sleep(interval)
        try:            
            ftp.cwd(path + file + "/")          
            downloadFiles(path + file + "/", destination, ftp)
        except ftplib.error_perm:
            os.chdir(destination[0:len(destination)-1] + path)
            
            try:
                ftp.retrbinary("RETR " + file, open(os.path.join(destination + path, file),"wb").write)
                print "Downloaded: " + file
            except:
                print "Error: File could not be downloaded " + file
    return
    
def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise
	
class ftpConn(Resource):
	def get(self):
		for acc in account:
			ftp = FTP(acc["host"], acc["user"], acc["pwd"])	
			downloadFiles(source, destination, ftp)

			return ftp.getwelcome(), 200


api.add_resource(ftpConn, "/ftp")

app.run(debug=True)