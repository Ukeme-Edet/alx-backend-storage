-- A SQL script that lists all bands with `Glam rock` as their main style, ranked by their longevity
-- Requirements:
-- - Import table `metal_bands` from https: / / intranet.alxswe.com / rltoken / uPn947gnZLaa0FJrrAFTGQ
-- - Column names must be: `band_name` and `lifespan` (in years until 2022)
-- Attributes `formed` and `split` are used for computing `lifespan`
-- Script can be executed on any database
SELECT
	`band_name`,
	IF(
		`split` IS NULL,
		2022 - `formed`,
		`split` - `formed`
	) AS `lifespan`
FROM
	`metal_bands`
WHERE
	`style` LIKE '%Glam rock%'
ORDER BY
	`lifespan` DESC;
