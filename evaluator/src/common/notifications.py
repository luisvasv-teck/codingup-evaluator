import smtplib
import imaplib
import email
from __meta__ import  __root_config__
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from src.common.utilities import Application, Struct
from src.common.cipher import AES


class Email:
    def __init__(self, app: Struct):
        self.__app = app
        self.__enc =  AES(self.__app.profile.hashx)
        self.__IMAP_SERVER = self.__app.profile.email["imap_server"]
        self.__IMAP_PORT = self.__app.profile.email["imap_port"]
        self.__SMPT_SERVER = self.__app.profile.email["smtp_server"]
        self.__SMPT_PORT = self.__app.profile.email["smtp_port"]
        self.__USERNAME = self.__app.profile.email["account"]
        self.__PASSWORD = self.__enc.decrypt_value(self.__app.profile.email["password"])
        self.__MESSAGE = MIMEMultipart()
        
    def __set_attachments(self, files: list[str]) -> None:
        for file_to_load in files:
            # Agregar imágenes como archivos adjuntos en línea
            with open(file_to_load, 'rb') as file:
                attachment = MIMEImage(file.read())
            attachment.add_header('Content-Disposition', 'inline', filename='definir nombre ...')
            self.__MESSAGE.attach(attachment)

    def send_email(self, email_info: dict):
        # set message init
        self.__MESSAGE['From'] = self.__USERNAME
        self.__MESSAGE['To'] = email_info["to"]
        self.__MESSAGE['Subject'] = email_info["subject"]

        # set message html template
        html_content: str = Application.read_file(email_info["html_template"])
        # TODO: replace variables html
        self.__MESSAGE.attach(MIMEText(html_content, 'html'))
        
        # set attachments
        self.__set_attachments(email_info["files"])
        
        # set up connection and send email
        with smtplib.SMTP(self.__SMPT_SERVER, self.__SMPT_PORT) as server:
            server.starttls()
            server.login(self.__USERNAME, self.__PASSWORD)
            server.send_message(self.__MESSAGE)
        print('mail sent successfully')
        
    def read_email(self):

        # set connection IMAP server
        mail = imaplib.IMAP4_SSL(self.__IMAP_SERVER, self.__IMAP_PORT)
        mail.login(self.__USERNAME, self.__PASSWORD)

        # set-up inbox folder
        mail.select('INBOX')

        # getting unseen emails
        status, data = mail.search(None, '(UNSEEN)')

        # Procesamiento de los correos electrónicos encontrados
        for num in data[0].split():
            status, data = mail.fetch(num, '(RFC822)')
            raw_email = data[0][1]
            email_message = email.message_from_bytes(raw_email)
            
            # Descarga de los adjuntos (si existen)
            for part in email_message.walk():
                if part.get_content_maintype() == 'multipart':
                    continue
                if part.get('Content-Disposition') is None:
                    continue

                filename = part.get_filename()
                if filename:
                    # Descargar el adjunto
                    with open(filename, 'wb') as attachment:
                        attachment.write(part.get_payload(decode=True))

        # close connection
        mail.logout()
            
    def test_connection(self):
        """
        
        import smtplib
from email.mime.text import MIMEText

def test_email_connection(smtp_server, smtp_port, sender_email, password, recipient_email):
    try:
        # Crear un objeto de conexión SMTP
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            # Establecer conexión segura (TLS)
            server.starttls()
            
            # Iniciar sesión en el servidor de correo
            server.login(sender_email, password)
            
            # Crear un mensaje de prueba
            message = MIMEText("This is a test email.")
            message["Subject"] = "Test Email"
            message["From"] = sender_email
            message["To"] = recipient_email
            
            # Enviar el mensaje de prueba
            server.sendmail(sender_email, recipient_email, message.as_string())
            
        print("La conexión y el envío de correo fueron exitosos.")
    except smtplib.SMTPAuthenticationError:
        print("Error de autenticación. Verifica las credenciales de correo electrónico.")
    except smtplib.SMTPException as e:
        print("Error al enviar el correo:", str(e))

# Ejemplo de uso
smtp_server = "smtp.gmail.com"  # Servidor SMTP
smtp_port = 587  # Puerto SMTP (generalmente 587 para TLS)
sender_email = "coding.up.my.future@gmail.com"  # Tu dirección de correo electrónico
password = "xdrxzhktxxaezdil"  # Tu contraseña de correo electrónico
recipient_email = "luisvasv@gmail.com"  # Dirección de correo electrónico del destinatario

test_email_connection(smtp_server, smtp_port, sender_email, password, recipient_email)
        
        """
            
# TODO read_email agregar loger ya que es sera una tarea programada
# TODO create dao para almacenar entrengas
# TODO definir filename location para archivos entregados
# TODO agregar mas segurtidad y logueo