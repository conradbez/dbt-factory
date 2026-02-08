SELECT 
    *
FROM {{ref(##source_table##)}}
ORDER BY ##sort_columns##
