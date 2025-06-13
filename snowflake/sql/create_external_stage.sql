-- Create storage integration (run only once per account)
CREATE OR REPLACE STORAGE INTEGRATION azure_int
  TYPE = EXTERNAL_STAGE
  STORAGE_PROVIDER = AZURE
  ENABLED = TRUE
  STORAGE_ALLOWED_LOCATIONS = ('azure://snowflakedemo0.blob.core.windows.net/demo-data');

-- Create external stage (run once per environment)
CREATE OR REPLACE STAGE azure_demo_stage
  URL='azure://snowflakedemo0.blob.core.windows.net/demo-data'
  STORAGE_INTEGRATION = azure_int;
