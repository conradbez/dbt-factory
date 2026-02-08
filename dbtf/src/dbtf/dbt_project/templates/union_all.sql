SELECT * FROM {{ref(##table_1##)}}
UNION ALL
SELECT * FROM {{ref(##table_2##)}}
