SELECT 
    *
FROM {{ref(##source_table##)}}
WHERE ##condition##
