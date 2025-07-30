import requests
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
import smtplib
import time

def enviar_correo_relay(smtp_host, smtp_port, remitente, destinatario, asunto, cuerpo):
    try:
        msg = MIMEText(cuerpo)
        msg['Subject'] = asunto
        msg['From'] = remitente
        msg['To'] = destinatario

        servidor = smtplib.SMTP(smtp_host, smtp_port, timeout=10)
        servidor.ehlo()
        # No starttls ni login, relay autorizado por IP
        servidor.sendmail(remitente, [destinatario], msg.as_string())
        servidor.quit()
        print("Correo enviado correctamente vía SMTP Relay.")
    except Exception as e:
        print(f"Error enviando correo: {e}")

def check_domain_niccl_search(domain):
    # domain sin .cl (ejemplo: "TuDominio")
    url = "https://www.nic.cl/registry/BuscarDominio.do"
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }
    data = {
        'patron': domain,
        'filtro': 'exacta',
        'buscar': ' Buscar Dominio '
    }

    try:
        response = requests.post(url, data=data, headers=headers)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error en la consulta: {e}")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')
    texto = soup.get_text(separator="\n").lower()

    boton = soup.find('button', class_='submitButton showListBtn')
    if boton and domain.lower() in boton.get_text().lower() and "inscribir" in boton.get_text().lower():
        return True
    if "no existen resultados para su búsqueda" in texto:
        return True
    if domain.lower() in texto:
        return False

    print("No se pudo determinar el estado del dominio, posible cambio en la página.")
    return None

if __name__ == "__main__":
    smtp_host = "CAMBIAR" #Utilice SMTP-Relay
    smtp_port = 25
    remitente = "Remitente" #Cambiar 
    destinatario = "Destino" #Cambiar
     

    dominio = "Tudominio"  # Solo el nombre sin .cl

    while True:
        disponible = check_domain_niccl_search(dominio)
        if disponible is True:
            asunto = f"Dominio disponible: {dominio}.cl"
            cuerpo = f"¡El dominio {dominio}.cl ESTÁ disponible para inscripción!"
            print(cuerpo)
            enviar_correo_relay(smtp_host, smtp_port, remitente, destinatario, asunto, cuerpo)
            # Opcional: para no enviar correos repetidos, puedes hacer un break aquí
            # break
        elif disponible is False:
            asunto = f"Dominio NOOOO DISPONIBLE: {dominio}.cl"
            cuerpo = f"¡El dominio {dominio}.cl NO ESTA DISPONIBLE!"
            print(f"El dominio {dominio}.cl NO está disponible.")
            enviar_correo_relay(smtp_host, smtp_port, remitente, destinatario, asunto, cuerpo)
        else:
            print("No se pudo determinar la disponibilidad del dominio.")

        time.sleep(3600)  # Espera 1 hora antes de volver a consultar
