-- A SQL script that creates an index `idx_name_first_score` on the table `names` and the the first letter of `name` and the score
-- Requirements:
-- - Only the first letter of `name` and the score must be indexed
CREATE INDEX idx_name_first_score ON names(name(1), score);