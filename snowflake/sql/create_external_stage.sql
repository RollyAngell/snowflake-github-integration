-- Create storage integration (run only once per account)
CREATE OR REPLACE STORAGE INTEGRATION AZURE_INT
    TYPE = EXTERNAL_STAGE
    STORAGE_PROVIDER = AZURE
    ENABLED = TRUE
    STORAGE_ALLOWED_LOCATIONS = ('azure://snowflakedemo0.blob.core.windows.net/demo-data')
    AZURE_TENANT_ID = 'd3be2218-4171-4dfa-83b5-5386f93a9c2f';


-- Create external stage (run once per environment)
CREATE OR REPLACE STAGE azure_demo_stage
  URL='azure://snowflakedemo0.blob.core.windows.net/demo-data'
  STORAGE_INTEGRATION = AZURE_INT;