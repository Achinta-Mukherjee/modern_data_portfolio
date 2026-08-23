{{ config(materialized='table') }}

WITH staging_users AS (
    -- THE MAGIC: We never hardcode 'project.dataset.table' again.
    -- We tell dbt to reference the staging model, and it figures out the rest!
    SELECT * FROM {{ ref('stg_api_users') }}
),

rostered_users AS (
    SELECT 
        user_id,
        full_name,
        email,
        city,
        -- Advanced SQL: Assign a roster number that resets for every city
        ROW_NUMBER() OVER(PARTITION BY city ORDER BY full_name) as city_roster_number,
        
        -- Advanced SQL: Get the total count of users in that specific city
        COUNT(user_id) OVER(PARTITION BY city) as total_city_users
    FROM staging_users
)

SELECT * FROM rostered_users
ORDER BY city, city_roster_number