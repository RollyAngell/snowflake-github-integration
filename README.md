# Snowflake Project with GitHub Actions

This project demonstrates the integration between Snowflake and GitHub, using GitHub Actions for CI/CD with support for multiple environments (development and production).

## Project Structure

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

## Branching and Environments

- `dev` branch: Used for development. All feature branches and initial testing should be merged here. Deploys to the development environment in Snowflake.
- `master` branch: Used for production. Only stable, tested code is merged here. Deploys to the production environment in Snowflake.

## Configuration

1. Set up Snowflake credentials in GitHub Secrets for both environments:
   - Development:
     - `SNOWFLAKE_DATABASE_DEV`
     - `SNOWFLAKE_WAREHOUSE_DEV`
   - Production:
     - `SNOWFLAKE_DATABASE_PROD`
     - `SNOWFLAKE_WAREHOUSE_PROD`
   - Shared:
     - `SNOWFLAKE_ACCOUNT`
     - `SNOWFLAKE_USER`
     - `SNOWFLAKE_PASSWORD`
     - `SNOWFLAKE_ROLE`

2. Configure the settings file in `snowflake/config/config.yml`

## Usage

- The GitHub Actions pipeline will run automatically when you push or open a pull request to the `dev` or `master` branches.
- Changes in `dev` are deployed to the development environment.
- Changes in `master` are deployed to the production environment. 