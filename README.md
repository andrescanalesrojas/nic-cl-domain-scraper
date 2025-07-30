# nic-cl-domain-scraper
La función principal de este script es monitorear un dominio .cl que se encuentre en proceso de eliminación en NIC Chile, para detectar en el momento exacto en que el dominio se vuelva disponible nuevamente, de modo que puedas registrarlo o comprarlo lo antes posible.

<img width="595" height="61" alt="image" src="https://github.com/user-attachments/assets/da8149eb-c64d-4c01-8e91-35719041f850" />

# nic-cl-domain-scraper

Script para monitorizar dominios .cl en proceso de eliminación en NIC Chile, realizando scraping automatizado para detectar cuándo un dominio está disponible y enviando reportes cada 1 hora por correo electrónico.

## Descripción

Esta herramienta permite hacer scraping del estado de un dominio .cl en NIC Chile para saber si está en proceso de eliminación y enviar automáticamente un correo diario con el estado del dominio monitoreado.

## Pasos para usar

1. **Descargar el script**  
   Descarga el archivo `script.py` de este repositorio.

2. **Instalar librerías necesarias**  
   Las librerías que necesitas instalar son:

   - `beautifulsoup4` (para parsing HTML)  
   - `requests` (para hacer solicitudes HTTP)  
   - `time` (librería estándar de Python, no necesita instalación)  
   - `smtplib` (librería estándar de Python para enviar correos)  
   - `email.mime.text` (parte de la librería estándar `email` para crear el contenido del correo)

   Puedes instalar las librerías necesarias con pip:

  
   pip install beautifulsoup4 requests
   

3. **Configurar el script**
   Dentro de `script.py` tienes que ajustar los siguientes parámetros:  

   - `host` (servidor SMTP del correo que usarás para enviar el email)  
   - `remitente` (dirección de correo desde la que se envía el email)  
   - `destinatario` (dirección de correo que recibirá el reporte)  
   - `dominio` (el dominio .cl que quieres monitorear)

4. **Ejecutar el script**  
   Ejecuta el script y dejarlo correr para que cada cierto tiempo (por ejemplo, cada 24 horas) envíe el reporte del estado del dominio. Puedes usar un programador de tareas como `cron` en Linux o el programador de tareas en Windows para ejecutar el script automáticamente.

## Ejemplo sencillo de uso


python script.py

    
