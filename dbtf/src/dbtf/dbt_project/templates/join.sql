SELECT 
    l.*, 
    r.* 
FROM {{ref(##left_table##)}} l
##join_type## JOIN {{ref(##right_table##)}} r 
    ON l.##left_key## = r.##right_key##
