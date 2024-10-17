-- No table for a meeting
-- creates a view need_meeting that lists all students that have a score under 80 (strict) and no last_meeting or more than 1 month.
CREATE VIEW need_meeting
AS SELECT name
FROM studnets
WHERE score < 80 AND
(last_meeting = NULL OR
(DATEDIFF(last_meeting, CURDATE()) > 30));
~                                                
