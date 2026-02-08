SELECT 
    ##group_by_columns##,
    ##aggregations##
FROM {{ref(##source_table##)}}
GROUP BY ##group_by_columns##
