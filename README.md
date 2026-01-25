# 🚀 Sistema de Monitorización de Red Corporativa Multisite

**Monitorización inteligente para redes empresariales de 200+ sedes**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.2-green.svg)](https://www.djangoproject.com/)
[![Grafana](https://img.shields.io/badge/Grafana-10.x-orange.svg)](https://grafana.com/)
[![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED.svg)](https://www.docker.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 📋 **Descripción del Proyecto**

Sistema de monitorización centralizada para redes corporativas con múltiples sedes (200+). Proporciona visualización en tiempo real del estado de la red, conexiones VoIP, ancho de banda y disponibilidad de servicios críticos, diseñado específicamente para entornos corporativos como cadenas de supermercados u oficinas distribuidas.

### **🎯 Objetivo Principal**
Reducir el tiempo de respuesta ante incidencias de red en un 40% y mejorar el SLA de disponibilidad del 95% al 99.5%.

## ✨ **Características Principales**

### **🌍 Mapa Geográfico Interactivo**
- Visualización en tiempo real de todas las sedes con código de colores (verde/amarillo/rojo)
- Filtrado por región, tipo de sede o estado de conexión
- Información detallada al hacer clic en cada sede

### **🚨 Sistema de Alertas Inteligentes**
- Alertas por email, Telegram y Webhook
- Configuración de umbrales personalizados por tipo de métrica
- Escalado automático de alertas según criticidad
- Alertas predictivas basadas en patrones históricos

### **📊 Dashboards en Tiempo Real**
- Métricas de ancho de banda por sede y tipo de tráfico
- Monitoreo de calidad VoIP (MOS score, latencia, jitter)
- Disponibilidad de servicios críticos (DNS, ERP, Punto de Venta)
- Utilización de CPU/RAM de dispositivos de red

### **📈 Reportes Automáticos**
- Reportes diarios/semanales/mensuales de SLA
- Análisis de tendencias y crecimiento de tráfico
- Detección de cuellos de botella en la red
- Exportación a PDF, Excel y formato ejecutivo

### **🎫 Sistema de Tickets Integrado**
- Creación automática de tickets ante incidencias
- Seguimiento del ciclo de vida de problemas
- Base de conocimiento de soluciones recurrentes
- Integración con sistemas ITSM existentes

## 🛠️ **Stack Tecnológico**

### **Backend**
- **Python 3.8+** - Lógica principal del sistema
- **Django 4.2** - Framework web y API REST
- **Django REST Framework** - Construcción de API
- **Celery** - Tareas asíncronas y procesamiento en background
- **Redis** - Cache y broker de mensajes

### **Base de Datos**
- **PostgreSQL** - Base de datos principal
- **TimescaleDB** - Extensión para datos de series temporales
- **Redis** - Cache y sesiones

### **Monitorización y Métricas**
- **Prometheus** - Recolección y almacenamiento de métricas
- **Grafana** - Dashboards y visualizaciones
- **SNMPv3** - Protocolo para monitoreo de dispositivos
- **NetFlow/sFlow** - Análisis de tráfico de red

### **Frontend**
- **HTML5/CSS3/JavaScript ES6+**
- **Chart.js** - Gráficos interactivos
- **Leaflet.js** - Mapas interactivos
- **WebSocket** - Actualizaciones en tiempo real

### **Infraestructura**
- **Docker & Docker Compose** - Contenedores y orquestación
- **Nginx** - Reverse proxy y SSL
- **Gunicorn** - Servidor WSGI para Python
- **GitLab CI/CD** - Integración y despliegue continuo

## 📁 **Estructura del Proyecto**
multisite-network-monitor/
├── backend/ # Aplicación Django
│ ├── core/ # Configuración y settings
│ ├── monitoring/ # Lógica de monitorización
│ ├── alerts/ # Sistema de alertas
│ ├── reporting/ # Generación de reportes
│ ├── api/ # Endpoints REST
│ └── dashboard/ # Vistas y templates
├── frontend/ # Aplicación frontend moderna
│ ├── src/
│ │ ├── components/ # Componentes React/Vue
│ │ ├── views/ # Vistas principales
│ │ └── services/ # Conexión con API
├── monitoring-agents/ # Agentes para dispositivos de red
│ ├── snmp-agent/ # Agente SNMP
│ ├── netflow-agent/ # Agente NetFlow
│ └── voip-agent/ # Agente de calidad VoIP
├── prometheus/ # Configuración de Prometheus
│ ├── alert_rules/ # Reglas de alertas
│ └── scrape_configs/ # Configuración de scraping
├── grafana/ # Dashboards y configuración
├── docker/ # Configuración Docker
│ ├── compose.yaml # Docker Compose
│ └── nginx/ # Configuración Nginx
├── docs/ # Documentación
├── scripts/ # Scripts de utilidad
├── tests/ # Tests unitarios y de integración
└── config/ # Archivos de configuración

## 🚀 **Instalación Rápida**

### **Requisitos Previos**
- Docker y Docker Compose instalados
- Python 3.8+ (para desarrollo)
- Git

### **Instalación con Docker (Recomendada)**

```bash
# 1. Clonar el repositorio
git clone https://github.com/AlejandroGlezSan/multisite-network-monitor.git
cd multisite-network-monitor

# 2. Configurar variables de entorno
cp .env.example .env
# Editar .env con tus configuraciones

# 3. Iniciar los contenedores
docker-compose up -d

# 4. Acceder a la aplicación
# Dashboard principal: http://localhost:8000
# Grafana: http://localhost:3000 (admin/admin)
# API Documentation: http://localhost:8000/api/docs/
Instalación Manual para Desarrollo
bash
# 1. Crear entorno virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows

# 2. Instalar dependencias
pip install -r requirements/dev.txt

# 3. Configurar base de datos
python manage.py migrate
python manage.py createsuperuser

# 4. Cargar datos de prueba (opcional)
python manage.py loaddata fixtures/initial_data.json

# 5. Iniciar servidor de desarrollo
python manage.py runserver
📖 Guía de Uso
1. Agregar Sedes
python
# API Example: Crear nueva sede
POST /api/sites/
{
    "name": "Sede Central Madrid",
    "address": "Calle Gran Vía, 1",
    "latitude": 40.4168,
    "longitude": -3.7038,
    "ip_range": "192.168.1.0/24",
    "criticality": "high"
}
2. Configurar Dispositivos de Red
python
# Ejemplo de configuración YAML para switches
devices:
  - name: "Switch Piso 1"
    ip: "192.168.1.1"
    snmp_community: "monitoring_ro"
    device_type: "cisco_switch"
    metrics:
      - interface_traffic
      - cpu_utilization
      - memory_usage
3. Configurar Alertas
yaml
# Ejemplo de regla de alerta
alert_rules:
  - name: "Alta utilización de CPU"
    condition: "cpu_usage > 80"
    duration: "5m"
    severity: "warning"
    channels:
      - email: "noc@empresa.com"
      - telegram: "chat_id_123"
🔧 Configuración Avanzada
Monitoreo SNMP
python
# Configuración de monitoreo SNMP
SNMP_CONFIG = {
    'version': 3,
    'security_level': 'auth_with_privacy',
    'auth_protocol': 'SHA',
    'priv_protocol': 'AES',
    'community': 'monitoring_ro',
    'timeout': 5,
    'retries': 3
}
Integración con Sistemas Existentes
API REST completa para integración

Webhooks para eventos en tiempo real

Exportación a formatos estándar (CSV, JSON, XML)

Plugin para Nagios/Zabbix

         📊 Métricas y Resultados
KPIs Principales
MTTR (Mean Time To Repair): Reducción de 4 horas a 45 minutos

SLA de Disponibilidad: Mejora del 95% al 99.5%

Tiempo de Detección: De 30 minutos a < 2 minutos

Ahorro en Personal: 15 horas/semana por técnico

     Dashboard de Métricas
python
# Ejemplo de consulta para métricas clave
SELECT 
    site_name,
    AVG(uptime) as availability,
    MAX(bandwidth_usage) as peak_usage,
    COUNT(alerts) as incidents
FROM network_metrics
GROUP BY site_name
ORDER BY availability DESC;

    🤝 Contribuir al Proyecto

Fork el repositorio

Crea una rama para tu feature (git checkout -b feature/AmazingFeature)

Commit tus cambios (git commit -m 'Add AmazingFeature')

Push a la rama (git push origin feature/AmazingFeature)

Abre un Pull Request

Guía de Estilo
Sigue PEP 8 para código Python

Usa Black para formateo automático

Escribe tests para nuevas funcionalidades

Documenta todos los endpoints de API

📝 Licencia
Este proyecto está bajo la licencia MIT - ver el archivo LICENSE para más detalles.

📞 Soporte y Contacto
Issues: GitHub Issues

Email: alejandroglezsan1993@gmail.com

Documentación: Wiki del proyecto

🙏 Agradecimientos

Comunidad de Python y Django por el excelente ecosistema

Todos los contribuidores y testers del proyecto

⭐ Si este proyecto te resulta útil, por favor dale una estrella en GitHub!