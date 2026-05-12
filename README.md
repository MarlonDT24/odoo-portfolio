# Odoo Portfolio — Marlon Torres

Colección de módulos personalizados para Odoo 17 desarrollados como
portfolio profesional. Cada módulo demuestra técnicas reales usadas
en proyectos de consultoría Odoo.

## Módulos

### 📁 Project Billing Manager
Extiende la gestión de proyectos añadiendo un ciclo completo de
facturación automática basada en partes de horas.

| Técnica | Implementación |
|---|---|
| Herencia de modelos | `_inherit = 'project.project'` |
| Campos computados | `@api.depends('timesheet_ids', 'hourly_rate')` |
| Validaciones | `ValidationError` con lógica de negocio |
| Creación via ORM | `env['account.move'].create()` |
| Herencia de vistas XML | `xpath` sobre vistas estándar de Odoo |
| QWeb (reportes PDF) | Template de resumen de facturación |
| SQL directo | `env.cr.execute()` para estadísticas agregadas |
| Seguridad | `ir.model.access.csv` con roles diferenciados |

**Flujo de uso:**
1. Abre un proyecto en Odoo
2. Ve a la pestaña **Facturación**
3. Asigna un cliente y configura la tarifa por hora
4. Registra horas en los partes de horas del proyecto
5. Pulsa **Generar Factura** — se crea automáticamente

---

### 📁 Account Invoice Customizer
Extiende las facturas de cliente añadiendo campos personalizados,
validaciones de negocio al confirmar y reporte PDF personalizado.

| Técnica | Implementación |
|---|---|
| Herencia de `account.move` | `_inherit = 'account.move'` |
| Lógica en confirmación | Herencia de `action_post()` |
| Validaciones | `@api.constrains` con reglas de negocio |
| Campos computados | Días de retraso, total formateado |
| Herencia de vistas XML | Nueva pestaña en formulario de factura |
| Herencia de reporte QWeb | Extensión del PDF estándar de factura |

**Flujo de uso:**
1. Abre una factura de cliente en Odoo
2. Rellena el número de expediente en la cabecera
3. Ve a la pestaña **Información Interna**
4. Confirma la factura — valida automáticamente las reglas de negocio
5. El PDF incluye el expediente y el aviso de facturas vencidas

---

## Entorno de desarrollo

### Requisitos
- Docker Desktop
- Odoo 17 Community

### Instalación

```bash
git clone https://github.com/MarlonDT24/odoo-portfolio.git
cd odoo-portfolio
docker-compose up -d
```

Accede a `http://localhost:8069` e instala los módulos desde
Aplicaciones.

## Autor

**Marlon Torres** — Desarrollador Odoo & FullStack
[LinkedIn](https://www.linkedin.com/in/marlon-torres-982a17305) ·
[GitHub](https://github.com/MarlonDT24) ·
[Portfolio](https://marlondev-portfolio.vercel.app)
