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