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

## Workflow Summary

This project uses a professional CI/CD workflow for Snowflake with GitHub Actions:

- **Branching:**  
  - `dev` branch deploys to the development environment (`MYPROJECT_DEV`).
  - `master` branch deploys to the production environment (`MYPROJECT_PROD`).

- **Key files:**
  - `snowflake/sql/init.sql`: Contains all SQL DDL for schema, tables, and views.
  - `deploy_snowflake.py`: Python script that connects to Snowflake, removes comments from the SQL, and executes each statement, printing results and errors.
  - `.github/workflows/snowflake-deploy.yml`: GitHub Actions workflow that installs dependencies and runs the deployment script, using secrets for environment separation.
  - `snowflake/config/config.yml`: Example configuration file for Snowflake connection and deployment settings.

- **How it works:**
  1. Developers push or open PRs to `dev` for development/testing. The pipeline deploys to the dev environment.
  2. Once validated, changes are merged to `master` for production deployment.
  3. The pipeline uses the correct secrets and parameters for each environment.

- **Best practices:**
  - All SQL is idempotent and versioned.
  - All deployments are automated and logged.
  - Secrets are managed securely in GitHub.

## External Data Load (Azure Blob Storage)

This project also demonstrates how to load external data from Azure Blob Storage into Snowflake tables:

- **Stage setup:**
  - The file `snowflake/sql/create_external_stage.sql` contains the SQL to create a storage integration and an external stage in Snowflake pointing to your Azure Blob Storage container.
  - This script should be run manually by an admin when setting up the environment for the first time.

- **Data load:**
  - The file `snowflake/sql/load_customers_data.sql` contains a `COPY INTO` command to load data from the CSV file in Azure Blob Storage into the `DEMO.CUSTOMERS` table.
  - The pipeline executes this file after the DDL scripts, so your tables are automatically populated with external data during deployment.

- **How it works:**
  1. Upload your CSV file (e.g., `customers.csv`) to your Azure Blob Storage container (e.g., `demo-data`).
  2. Run the SQL in `create_external_stage.sql` in Snowflake to create the storage integration and stage.
  3. The pipeline will execute `load_customers_data.sql` to load the data into the target table.

- **Benefits:**
  - Automates the ingestion of external data as part of your CI/CD process.
  - Keeps infrastructure (stage creation) and data load scripts versioned and documented. 