select distinct
  s0.city_a, s1.city_a
, s2.city_a
, s3.city_a
, s4.city_a

from
  connection s0
, connection s1
, connection s2
, connection s3
, connection s4
where s1.city_a = s0.city_b 
and s2.city_a = s1.city_b 
and s3.city_a = s2.city_b
and s4.city_a = s3.city_b
