# challenger-woowup

## Description

This is an API that handles sending emails, with two email providers (Mailgun, Sendgrid).

## Clean Architecture
Elegi esta arquitectura ya que es mantenible y escalable, actualmente el proyecto acepta un email simple
pero puede escalar a todas las funcionalidades del envio de un email, 
como enviar adjuntos, copias, copias coultas, etc. Se separa la logica del negocio con las 
implementaciones, se puede cambiar la base de datos sin afectar nada del core del negocio. 
Al ser separado por capas es más fácil de entender y de testear. Si se desea agregar otro 
proveedor de correo, solo es crear otro adapter con la configuración del proveedor yu la lógica 
de negocio no se ve afectada. Este código está también orientado a controlar fallos, tiene 
implementado un middleware que controla cualquier excepción que no haya sido tenido en cuenta 
en la app. En cuanto a seguridad, seria ideal encriptar las variables de entornos con algun servicio 
como Ssm de AWS, más que todo variables sensibles como API KEYS o contraseñas. También es factible elegir 
una arquitectura MVC de acuerdo a lo que puede escalar el proyecto pero digamos que me siento 
más comodo con la implementada.

### Technologies
- Python 3.11
- FastApi (Framework)
- MongoDB (Database NoSQL)
- Sentry (Monitoring and exceptions)
- Pydantic (Validation)
- Uvicorn (ASGI web server)

### Installation local

1. Install Virtualenv and activate it
```sh
$ python3 -m venv venv
```
```sh
$ source venv/bin/activate
```
2. Install requirements.txt
```sh
$ pip install -r requirements.txt
```
3. Env vars
```sh
$ cp .env.example .env
```

### Fast Api Server
```sh
$ uvicorn app.config.http.app:app --reload --host=0.0.0.0 --port=8000
```

### Run Docker
```sh
$ docker-compose up
```

### Test
```sh
$ pytest -v
```

### Documentation
```sh
$ {host}/redoc
```

### Swagger
```sh
$ {host}/swagger
```

### FrontEnd
Se agrega un unico archivo index.html, como comentaba tiene una funcionalidad básica de enviar 
un email a un solo destinatario, llamemos la entrega como un MVP que luego va a ir teniendo 
nuevos features, esta funcionalidad tiene un select de remitente, son 2, un remitente que es 
el de mailgun (mailgun@sandbox066420485fa7479b9b9c15968b61dccf.mailgun.org) 
y un remitente que es el de sendgrid, mailgun tiene una limitación que solo puede enviar emails 
a correos registrados en el dominio, los cuales solo tengo agregados (juaco.1826@gmail.com y 
jforeroola@gmail.com), con sendgrid si puedo enviar a cualquier correo, para probar la funcionalidad 
que se envie el correo si llega a fallar mailgun que es el predeterminado, puede enviar un email como 
destinatario un correo diferente a los registrados y al fallar se enviara por sendgrid