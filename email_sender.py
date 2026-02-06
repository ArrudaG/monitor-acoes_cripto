import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def enviar_email(assunto, corpo, usuario, senha):
    try:
        msg = MIMEMultipart()
        msg['From'] = usuario
        msg['To'] = usuario
        msg['Subject'] = assunto

        msg.attach(MIMEText(corpo, 'plain'))

        # Conexão com SMTP do Gmail
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(usuario, senha)
        server.sendmail(usuario, usuario, msg.as_string())
        server.quit()

        print(f"E-mail enviado: {assunto}")

    except Exception as e:
        print(f"Erro ao enviar email: {e}")
