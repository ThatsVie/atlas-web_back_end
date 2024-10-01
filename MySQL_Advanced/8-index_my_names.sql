-- In the vast sea of names, searching through every single one can feel like navigating without a map.
-- This index acts as our compass, pointing directly to names starting with the same letter.
-- By indexing only the first letter of the name column, we can swiftly narrow down the search,
-- making sure that queries no longer have to traverse the entire ocean of names.
-- It's like charting a course through the stars, efficient, quick, and focused on the first sign.
CREATE INDEX idx_name_first ON names (name(1));
