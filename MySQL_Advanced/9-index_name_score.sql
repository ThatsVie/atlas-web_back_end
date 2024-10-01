-- In a world full of names and numbers, searching through millions can be daunting.
-- This composite index is like a dual-filter: first, we narrow down by the initial letter,
-- and then, like a second lens, we refine the search by score.
-- By indexing both the first letter of the name and the score, we optimize our query,
-- allowing us to glide swiftly through the data and arrive at the desired results faster.
-- It's like zooming in with a high-powered telescope: focused and precise, no time wasted!
CREATE INDEX idx_name_first_score ON names (name(1), score);
