{{ config(materialized='table') }}

WITH source_data AS (
    -- We just write a simple SELECT statement
    SELECT * 
    FROM `project-f8aca53c-7f41-4c40-968.raw_data.api_users`
),

clean_users AS (
    SELECT 
        id as user_id,
        name as full_name,
        email,
        city
    FROM source_data
    -- A simple cleaning rule: Only keep users who have an email address
    WHERE email IS NOT NULL
)

SELECT * FROM clean_users