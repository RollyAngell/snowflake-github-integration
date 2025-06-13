# Proyecto Snowflake con GitHub Actions

Este proyecto demuestra la integración entre Snowflake y GitHub, utilizando GitHub Actions para CI/CD.

## Estructura del Proyecto

```
.
├── .github/
│   └── workflows/
│       └── snowflake-deploy.yml
├── snowflake/
│   ├── sql/
│   │   └── init.sql
│   └── config/
│       └── config.yml
└── README.md
```

## Configuración

1. Configurar las credenciales de Snowflake en GitHub Secrets:
   - `SNOWFLAKE_ACCOUNT`
   - `SNOWFLAKE_USER`
   - `SNOWFLAKE_PASSWORD`
   - `SNOWFLAKE_ROLE`
   - `SNOWFLAKE_WAREHOUSE`
   - `SNOWFLAKE_DATABASE`

2. Configurar el archivo de configuración en `snowflake/config/config.yml`

## Uso

El pipeline de GitHub Actions se ejecutará automáticamente cuando se haga push a la rama main. 