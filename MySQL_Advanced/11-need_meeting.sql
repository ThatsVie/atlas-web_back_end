-- Create the view need_meeting to identify students who need a follow-up.
-- The view selects students with scores under 80 and either have no recorded last meeting,
-- or their last meeting was more than one month ago.
-- This helps ensure timely interventions for students who may be falling behind.

CREATE VIEW need_meeting AS
SELECT name
FROM students
WHERE score < 80
AND (last_meeting IS NULL OR last_meeting < ADDDATE(CURDATE(), INTERVAL -1 MONTH));

-- Just like in any support group, regular check-ins are essential to prevent things from spiraling.
-- Whether it’s a student or someone in recovery, missing meetings can signal trouble.
-- This view is an alert system for those who might be slipping through the cracks, 
-- ensuring no one is left without the support they need at the crucial moment.
