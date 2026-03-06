# 🤖 Sistema de Agentes Inteligentes

---

## Descripción del Sistema

Este es un sistema de API de Agentes Inteligentes construido con FastAPI que proporciona microservicios especializados para consultas académicas. El sistema utiliza LangChain para orquestar agentes de IA que pueden usar diferentes modelos Gemini y OpenAI para responder preguntas sobre horarios, información personal, aulas virtuales y notas.

---

## Tecnologías Utilizadas

- **Python**: Lenguaje de programación
- **FastAPI**: Framework web
- **LangChain**: Orquestación de agentes y herramientas
- **OpenAI & Gemini**: Modelos de lenguaje
- **UV**: Gestor de paquetes

---

## Instalación, Configuración y Ejecución del Proyecto

### Requisitos

1. **Versión de Python**: El proyecto requiere Python 3.13 o superior
2. **Gestor de Paquetes UV**: Primero se debe instalar el gestor de paquetes uv

### Pasos de Instalación

#### **Instalar gestor de paquetes UV**

```python
pip install uv
```

#### Crear entorno virtual e instalar dependencias

```bash
uv sync
```

#### Activar el Entorno Virtual

**En Windows:**

```bash
.venv\Scripts\activate
```

**En Linux/Mac:**

```bash
source .venv/bin/activate
```

### Ejecución del Proyecto

#### Ejecutar servidor en modo desarrollo

**Con Makefile:**

```bash
make run-dev
```

**O con comandos directos:**

```bash
uv run fastapi dev
```

```python
uv run uvicorn main:app --host 0.0.0.0 --port 3000 --reload
```

> El modo desarrollo incluye **hot reload** (recarga automática al detectar cambios en el código)
> 

#### Ejecutar servidor en modo produccion

**Con Makefile:**

```bash
make run-pro
```

**O con comandos directos:**

```bash
uv run fastapi run
```

```bash
uv run uvicorn main:app --host 0.0.0.0 --port 3000
```

> El modo producción **NO** incluye hot reload y está optimizado para entornos de producción
> 

### Variables de Entorno Requeridas

Se debe crear un archivo `.env` en la raíz del proyecto con las siguientes variables.

(Tener en cuenta que las siguientes urls se encuentran completas, pero en el .env solo van hasta cierta parte, observar el ejemplo que encontrara mas adelante)

#### 🧠 Modelos de IA

Credenciales para los modelos de lenguaje. Se requiere al menos una según el modelo que se vaya a utilizar.

| Variable | Descripción |
|----------|-------------|
| `GOOGLE_API_KEY` | API Key para Gemini (Google AI Studio) |
| `OPENAI_API_KEY` | API Key para OpenAI (GPT-4o, etc.) |

#### 🎓 Servicios Académicos (Uniminuto)

Endpoints para consultar información del estudiante.

| Variable | Descripción | Variable | apiKey |
|----------|-------------| ---------- |---------- |
| `API_INFORMACION_PERSONAL` | Base URL para datos personales | `https://registros.uniminuto.edu/api_egresado_act/service/banner.php?fn=datosPersonales&id=id_estudiante` |N/A|
| `API_HORARIO_ACTUAL` | Base URL para horario | `https://registros.uniminuto.edu/api_horario/select/?cn=id_estudiante` |N/A|
| `API_HISTORIAL` | Consultar el historial de notas |`https://webapi.uniminuto.edu/API/NotasBanner/ConsultaNotasBannerV_ID=id_estudiante`|N/A|
| `API_CURSOS` |Consultar los cursos actuales |`https://uniminuto.api.digibee.io/pipeline/uniminuto/v1/servicios-banner/consultaCursos`|`ITnjVcrLWfYpY2B246EcrWO6Hln3LD7a`|
| `API_CUMPLIMIENTO` |Consultar el cumplimiento de créditos|`https://uniminuto.api.digibee.io/pipeline/uniminuto/v1/servicios-banner-dos/cumplimientoCursos`|`ITnjVcrLWfYpY2B246EcrWO6Hln3LD7a`|
| `API_CALIFICACIONES` | Notas actuales del estudiante |`https://uniminuto.api.digibee.io/pipeline/uniminuto/v1/servicios-banner/calificacionActual`|`ITnjVcrLWfYpY2B246EcrWO6Hln3LD7a`|

#### 📚 Aulas Virtuales (Moodle)

| Variable | Descripción | Variable | apiKey |
|----------|-------------| ---------- |---------- |
| `MOODLE_API_URL` | Base URL para consultar cursos |`https://uniminuto.api.digibee.io/pipeline/uniminuto/v1/moodle-lms-umd/getUserCourses?correoInstitucional=email_estudiante`|`ITnjVcrLWfYpY2B246EcrWO6Hln3LD7a`|
| `MOODLE_API_URL` | Base URL para consultar eventos |`https://uniminuto.api.digibee.io/pipeline/uniminuto/v1/moodle-lms-umd/getEventsByCourse?idCurso=id_curso&instancia=instancia`|`ITnjVcrLWfYpY2B246EcrWO6Hln3LD7a`|

### 🏗️ Servicio Gestión Presupuestal (Administrativo)

| Variable | Descripción | Variable | apiKey |
|----------|-------------| ---------- |---------- |
| `API_PRESUPUESTO` | Gestión de presupuesto (CRUD) |`http://localhost:9000/api`|N/A|


#### 🗄️ Base de Datos (Opcional)

| Variable | Descripción | Variable |
|----------|-------------|---------|
| `POSTGRES_CONNECTION_STRING` | URI de conexión a PostgreSQL | `postgresql://postgres:admin@localhost:5433/agentes_db`|
| `AUTO_INIT_DB` | Ejecuta `init_db()` al iniciar para crear tablas faltantes | `true`|

#### 📝 Ejemplo de archivo .env

```bash
# Modelos IA
GOOGLE_API_KEY=AIzaSyPodns7GSvpa...
OPENAI_API_KEY=skudjYgnIje7gHjme...

# Servicios Académicos
API_INFORMACION_PERSONAL=https://registros.uniminuto.edu/api_egresado_act/service/
API_HORARIO_ACTUAL=https://registros.uniminuto.edu/api_horario/select/
API_NOTAS=https:https://uniminuto.api.digibee.io/pipeline/uniminuto/v1

# Servicios Gestión Presupuestal
API_PRESUPUESTO=http://localhost:9000/api

# Aulas Virtuales
MOODLE_API_URL=https://uniminuto.api.digibee.io/pipeline/uniminuto/v1/moodle-lms-umd/

# Autenticación Servicios
apikey=ITnjVcrLWfYpY2B246EcrWO6Hln3LD7a

# Base de Datos
POSTGRES_CONNECTION_STRING=postgresql://postgres:admin@localhost:5433/agentes_db
AUTO_INIT_DB=true
```

---

## Base de Datos y Persistencia

El sistema utiliza **PostgreSQL** (opcional) para almacenar el historial de conversaciones de los agentes. Esto permite mantener el contexto de las charlas a lo largo del tiempo.

### Configuración

Para habilitar la persistencia, se debe configurar la variable de entorno `POSTGRES_CONNECTION_STRING` en el archivo `.env`.

```bash
POSTGRES_CONNECTION_STRING=postgresql://postgres:admin@localhost:5433/agentes_db
```

### Ejecución con Docker

Existe un archivo `docker-compose.yml` para desplegar la base de datos rápidamente.

**Comando para iniciar la base de datos:**

```bash
docker-compose up -d postgres
```

**Detalles del contenedor:**
- **Imagen**: postgres:15-alpine
- **Puerto Host**: 5433 (para evitar conflictos con instalaciones locales)
- **Puerto Contenedor**: 5432
- **Usuario**: postgres
- **Contraseña**: admin
- **Base de Datos**: agentes_db
- **Volumen**: `postgres_data` (persistencia de datos)

### Modelo de Datos

La persistencia se maneja a través de la tabla `chat_history`, definida mediante SQLAlchemy. Al iniciar la aplicación, si la conexión es exitosa, se crean automáticamente las tablas necesarias.

> **Nota**: Si no se configura la cadena de conexión, el sistema funcionará correctamente pero sin guardar el historial de las conversaciones (modo sin memoria persistente).

---

## Acceso a la Aplicación

Una vez ejecutado el servidor, se puede acceder a:

- **Web**: [http://localhost:3000](http://localhost:3000)
- **Documentación API (Swagger)**: [`http://localhost:3000/docs`](http://localhost:3000/docs)

### Configuración del Servidor

El servidor está configurado para escuchar en:

- **Host**: `0.0.0.0` (todas las interfaces de red)
- **Puerto**: `3000`

---

## Endpoints

### Agentes

| **Endpoint** | **Método** | **Descripción** |
| --- | --- | --- |
| `/api/agente-horarios` | POST | 🕒 Gestión de horarios |
| `/api/agente-info-personal` | POST | 👤 Información personal |
| `/api/agente-aulas-virtuales` | POST | 📚 Información aulas virtuales |
| `/api/agente-notas` | POST | 📚 Información notas, creditos y cursos |

### Sistema

| **Endpoint** | **Método** | **Descripción** |
| --- | --- | --- |
| `/api/status` | GET | ℹ️ Estado del sistema |
| `/api/accesos` | GET | 🔐 Control de accesos |
| `/api/modelos_ai` | GET | 📚 Modelos IA disponibles |

---

## Uso

Todos los agentes cuentan con una estructura base de body request como la siguiente:

```python
{
  "uuid": "string",
  "prompt": "string",
  "id_usuario": "string",
  "email_usuario": "string",
  "rol": "string",
  "modelo_ia": "string",
  "programa": "string"
}
```

**Ejemplo de request a agente-horarios:**

```python
{
    "uuid": "1165b682-45fb-4bb9-875c-c65f3d46c14f",
    "prompt": "Cual es mi horario de clases?",
    "id_usuario": "000999999",
    "email_usuario": "",
    "rol": "estudiante",
    "modelo_ia": "gemini",
    "programa": "ingenieria"
}
```

## 📚 Documentación completa

Para una descripción detallada de la arquitectura, modelos y endpoints, consulta la documentación completa en:

- [docs/documentacion.md](docs/documentacion.md)

## Autores

>- **Juan David Casallas**
>- **Jinna Lorena Rojas** 
---
