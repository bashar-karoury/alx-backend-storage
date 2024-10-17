--  script that ranks country origins of bands
--  ordered by the number of (non-unique) fans
SELECT origin, fans AS origin, nb_fans FROM metal_bands ORDER BY nb_fans DESC;
