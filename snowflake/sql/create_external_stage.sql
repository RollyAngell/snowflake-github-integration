-- Create storage integration (run only once per account)
-- TODO: Replace 'arn:aws:iam::123456789012:role/snowflake_role' with your actual AWS Role ARN obtained from AWS IAM
-- TODO: Replace 's3://s3-demo-snowflake0/data/' with your actual S3 bucket path
CREATE OR REPLACE STORAGE INTEGRATION S3_INT
    TYPE = EXTERNAL_STAGE
    STORAGE_PROVIDER = S3
    ENABLED = TRUE
    STORAGE_AWS_ROLE_ARN = 'arn:aws:iam::333742357667:role/snowflake-s3-access-role'
    STORAGE_ALLOWED_LOCATIONS = ('s3://s3-demo-snowflake0/data/');

-- Create external stage (run once per environment)
-- TODO: Replace 's3://s3-demo-snowflake0/data/' with the same S3 bucket path as above
CREATE OR REPLACE STAGE s3_demo_stage
  URL='s3://s3-demo-snowflake0/data/'
  STORAGE_INTEGRATION = S3_INT;
