SELECT 
    *,
    ##expression## AS ##new_column##
FROM {{ref(##source_table##)}}
