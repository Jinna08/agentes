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

> **Nota:** El modo desarrollo incluye **hot reload** (recarga automática al detectar cambios en el código)

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

> **Nota:** El modo producción **NO** incluye hot reload y está optimizado para entornos de producción

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
---

## Estructura de Carpetas y Componentes

### Estructura del Proyecto

A continuación se presenta la estructura completa de archivos y directorios del proyecto:

```
/
├── app/                       # Código fuente de la aplicación
│   ├── agentes/               # Implementación de Agentes Inteligentes
│   │   ├── agente_aulas_virtuales/
│   │   ├── agente_horarios/
│   │   ├── agente_info_personal/
│   │   ├── agente_notas/
│   │   └── agente_presupuesto/
│   ├── core/                  # Configuración y lógica central
│   │   ├── config.py          # Configuración global
│   │   └── logging.py         # Configuración de logs
│   ├── db/                    # Capa de base de datos
│   │   ├── connection.py      # Conexión DB
│   │   ├── history.py         # Historial de chat
│   │   └── models.py          # Modelos
│   ├── helpers/               # Utilidades y helpers
│   │   └── agent_helpers.py   # Helpers para rutas de agentes
│   ├── routes/                # Endpoints de la API
│   │   ├── agents.py          # Rutas de agentes
│   │   ├── info.py            # Rutas de información
│   │   └── openai_api.py      # Rutas compatibles con OpenAI
│   ├── schemas/               # Esquemas Pydantic
│   │   ├── requests.py        # Modelos de solicitud
│   │   └── responses.py       # Modelos de respuesta
│   └── services/              # Servicios de negocio e integración
│       ├── ai/                # Modelos de IA (Gemini, OpenAI, etc.)
│       ├── agents_loader.py   # Servicio de carga de agentes
│       └── history.py         # Servicio de historial
└── docs/                      # Documentación completa
│   └── documentacion.md
├── .env                       # Variables de entorno (no incluido en repo)
├── .gitignore                 
├── .python-version            
├── docker-compose.yml         # Configuración de servicios Docker (DB)
├── main.py                    # Punto de entrada de la aplicación FastAPI
├── Makefile                   # Comandos de automatización
├── pyproject.toml             # Configuración de dependencias y UV
├── uv.lock                    # Archivo de bloqueo de dependencias
└── README.md                  # Documentación del proyecto
```

### Detalle de Carpetas y Componentes
#### `/app/agentes` - Implementación de Agentes

Esta carpeta contiene todos los agentes especializados del sistema. Cada subcarpeta representa un agente con responsabilidad específica:
```
app/agentes/
├── agente_aulas_virtuales/    # Agente de Moodle
├── agente_horarios/           # Agente de Horarios
├── agente_info_personal/      # Agente de Datos Personales
├── agente_notas/              # Agente de Notas
├── agente_presupuesto/        # Agente de Presupuesto
└── [nombre_agente]/
    ├── agent.py               # Construcción del Agente
    ├── prompts/               # Prompts del agente
    ├── services/              # Conexión a APIs externas
    └── tools/                 # Herramientas invocables
```
- `agente-horarios`: Consultar horarios
- `agente-info-personal`: Información del estudiante
- `agente-aulas-virtuales`: Contenido de Moodle
- `agente-notas`: Calificaciones y créditos
- `agente-presupuesto`: Consultas financieras

**Cada agente tiene su propia estructura modular:**

- **`agent.py`**: Punto de entrada que construye el agente, define sus herramientas y el prompt del sistema.
- **`/prompts`**: Contiene los prompts de texto que definen la personalidad y reglas del agente.
- **`/services`**: Módulos encargados de realizar las peticiones HTTP a las APIs externas.
- **`/tools`**: Funciones decoradas (`@tool`) que exponen las capacidades del agente al LLM.

#### `/app/services` - Servicios de Negocio e Integración

Esta carpeta contiene la lógica de negocio central y servicios de integración del sistema, incluyendo la carga de agentes y la gestión del historial.

```
app/services/
├── ai/                # Modelos de IA (Gemini, OpenAI, etc.)
├── agents_loader.py   # Servicio de carga de agentes
└── history.py         # Servicio de historial de chat
```

- **`agents_loader.py`**: Implementa el **Control de Acceso Basado en Roles**.
  - Define la matriz de permisos (qué roles pueden usar qué agentes).
  - Instancia los agentes solicitados bajo demanda o al inicio.

- **`history.py`**: Gestiona la persistencia del historial de conversaciones.
  - Implementa la clase `PostgresTurnBasedHistory` que hereda de `BaseChatMessageHistory` de LangChain.
  - Recupera y guarda mensajes (System, Human, AI) en PostgreSQL para mantener el contexto de las sesiones.
  - Se integra con la capa de base de datos (`app/db`).

#### `/app/services/ai` - Inicializadores de modelos de IA

Encapsula la lógica de inicialización de diferentes modelos de IA.

```
app/services/ai/
├── factory.py             # Fábrica de modelos
├── gemini_model.py        # Google Gemini
├── hf_model.py            # HuggingFace
└── openai_model.py        # OpenAI
```

- **`factory.py`**: Patrón Factory para instanciar el modelo correcto.
- **`gemini_model.py`**: Implementación para Gemini.
- **`openai_model.py`**: Implementación para OpenAI.

#### `/app/routes` - Rutas y endpoints de la API REST

Define todos los endpoints expuestos por la aplicación.

```
app/routes/
├── agents.py            # Endpoints principales de agentes
├── info.py              # Endpoints de informativos
└── openai_api.py        # Endpoints compatibles con OpenAI
```

- **`agents.py`**: Rutas `/api/agente-*` que reciben el prompt del usuario y devuelven la respuesta.
- **`info.py`**: Rutas como `/api/status` y `/api/accesos`.
- **`openai_api.py`**: Permite que este sistema sea usado como backend compatible con clientes de OpenAI.

#### `/app/helpers` - Helpers

- **`agent_helpers.py`**: Funciones auxiliares para validar sesiones, manejar errores, formatear respuestas y realizar warm-up de servicios.

#### `/app/core` - Configuración global de la aplicación

Centraliza la configuración global.

```
app/core/
├── config.py            # Variables globales y configuración
└── logging.py           # Configuración de logging
```
- **`config.py`**:
  - Carga variables de entorno (`.env`).
  - Define constantes (`SERVER_PORT`, `CORS_ORIGINS`).
  - Define la clase `Settings` usando Pydantic.
- **`logging.py`**: Configura el formato de logs para toda la aplicación.

#### `/app/db` - Persistencia

Maneja la conexión a base de datos y modelos.

```
app/db/
├── connection.py              # Engine y SessionLocal
├── history.py                 # Implementación de historial
└── models.py                  # Modelos ORM (ChatHistory)
```

- **`connection.py`**: Gestiona la conexión a la base de datos y la creación de sesiones.
- **`models.py`**: Define la estructura de las tablas (ej. `chat_history`).
- **`history.py`**: Implementación para guardar la conversación en Postgres.


#### `.env` - Configuración de Variables de Entorno

Archivo de configuración que almacena variables de entorno como:

- Credenciales de API (OpenAI, Google Gemini)
- Credenciales de autenticación
- URLs de servicios externos

#### `main.py` - Punto de entrada de la aplicación

- Configura el servidor FastAPI
- Inicializa la aplicación web
- Configura el middleware CORS
- Incluye las rutas de los endpoints desde `app/routes`
- Ejecuta el servidor Uvicorn

#### `Makefile` - Definición de Comandos Automatizados

Contiene comandos automatizados para tareas comunes del desarrollo:

```makefile
venv:          # Crear entorno virtual
install:       # Instalar dependencias
run-dev:       # Ejecutar en modo desarrollo
run-pro:       # Ejecutar en modo producción
format:        # Formatear código con Ruff
lint:          # Análisis estático
clean:         # Limpiar archivos generados
```

---

## Capas de la Arquitectura

### Capa 1: Presentación (API Layer)

La aplicación expone una API REST con FastAPI configurada con CORS para permitir solicitudes desde cualquier origen.

**Routers principales:**

- `agents.py`: Endpoints para invocar agentes específicos
- `info.py`: Rutas informativas y de estado
- `openai_api.py`: Endpoints compatibles con OpenAI API

### Capa 2: Lógica de Negocio 

#### a) Control de Acceso y Validaciones

El sistema implementa un control de acceso basado en roles que define qué usuarios pueden acceder a cada agente.

**Roles disponibles:** `estudiante`, `docente`, `administrativo`

#### b) Modelos de Datos

Se definen modelos Pydantic en `app/schemas` para validar las solicitudes entrantes. Cada solicitud debe incluir:

- `prompt`: La pregunta o consulta
- `id_usuario`: Identificación del usuario
- `role`: Rol del usuario
- `model` (opcional): Modelo de IA a usar

#### c) Funciones Helper

El módulo `app/helpers/agent_helpers.py` contiene funciones utilitarias para:

- Validar prompts y emails
- Verificar disponibilidad de agentes
- Registrar llamadas
- Construir respuestas
- Manejar errores

### Capa 3: Capa de Agentes

Cada agente sigue una estructura modular estandarizada.

#### Ejemplo: Agente de Horarios

**Inicialización y disponibilidad** en `__init__.py`

**Construcción del agente** con herramientas específicas y un prompt del sistema. La función recibe el modelo de IA a usar como parámetro.

**Herramientas (Tools)** - Funciones decoradas con `@tool` de LangChain:

- `obtener_datos_horario`: Obtiene el horario actual del estudiante
- `obtener_tiempo_actual`: Obtiene la fecha y hora actual
- `obtener_info_profesor`: Obtiene información de los profesores

**System Prompt**

Define el comportamiento, reglas y tono del agente. Incluye instrucciones específicas sobre:

- Cómo contar materias vs clases
- Cómo manejar fechas
- El estilo de respuesta

**Servicios**

Se encargan de consumir APIs externas para obtener datos. Ejemplo: `cargar_datos_horario` consulta una API REST y maneja errores de conexión.

### Capa 4: Capa de Modelos de IA

El sistema soporta múltiples modelos de IA mediante una función centralizadora (Factory) que instancia el agente correcto según el modelo especificado.

#### Inicializador de Gemini

Usa `GoogleGenerativeAI` con el modelo `gemini-2.5-flash-lite`

- Temperatura: 0
- Máximo de iteraciones: 15
- Timeout: 60 segundos

#### Inicializador de OpenAI

Usa `ChatOpenAI` con el modelo `gpt-4o-mini`

- Temperatura: 0
- Máximo de iteraciones: 5
- Timeout: 30 segundos

### Capa 5: Capa de Datos

Gestiona el almacenamiento y recuperación del historial de conversaciones.

- **Tecnología**: PostgreSQL (vía SQLAlchemy)
- **Responsabilidad**: Persistir mensajes de usuario y respuestas de la IA para mantener el contexto de la sesión (`session_id`).
- **Integración**: Se integra con LangChain mediante una implementación personalizada de `BaseChatMessageHistory` en `app/db/history.py`.


---

## Notas

> **Validación de claves API**: El sistema validará que la clave API del modelo seleccionado esté configurada, de lo contrario lanzará un error.
> 

> **Control de Acceso**: Cada solicitud es validada contra la matriz de control de acceso del usuario.
> 

> **Manejo de Errores**: El sistema maneja errores de conexión.
> 

> **Hot Reload**: En desarrollo, los cambios se reflejan automáticamente sin reiniciar el servidor.
> 

> **Modelos de IA**: La temperatura 0 se utiliza para respuestas deterministas y precisas.
>

> **Inicio del Agente Presupuestal**: Para probar o iniciar el agente de presupuesto, se debe verificar previamente que la API se encuentre en ejecución y que el usuario tenga rol administrativo, ya que el acceso a las funciones presupuestales está restringido a este perfil.
>
 
---

## Autores

>- **Juan David Casallas**
>- **Jinna Lorena Rojas** 
---
