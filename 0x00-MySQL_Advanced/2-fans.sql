-- A SQL script that ranks country origins of bands, ordered by the number of (non-unique) fans
-- Requirements:
-- - Import table `metal_bands` from https: / / intranet.alxswe.com / rltoken / uPn947gnZLaa0FJrrAFTGQ
-- - Column names must be: `origin` and `nb_fans`
-- Script can be executed on any database
SELECT
	`origin`,
	COUNT(`fans`) AS `nb_fans`
FROM
	`metal_bands`
GROUP BY
	`origin`
ORDER BY
	`nb_fans` DESC;
