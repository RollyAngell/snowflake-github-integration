# Snowflake Project with GitHub Actions

This project demonstrates the integration between Snowflake and GitHub, using GitHub Actions for CI/CD.

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

## Configuration

1. Set up Snowflake credentials in GitHub Secrets:
   - `SNOWFLAKE_ACCOUNT`
   - `SNOWFLAKE_USER`
   - `SNOWFLAKE_PASSWORD`
   - `SNOWFLAKE_ROLE`
   - `SNOWFLAKE_WAREHOUSE`
   - `SNOWFLAKE_DATABASE`

2. Configure the settings file in `snowflake/config/config.yml`

## Usage

The GitHub Actions pipeline will run automatically when you push to the main branch. 