SELECT DISTINCT name
FROM stars
JOIN people ON stars.person_id = people.id

WHERE movie_id IN (
SELECT movie_id 
FROM people 
JOIN stars ON stars.person_id = people.id
Where name = "Kevin Bacon" AND birth = 1958
) 
AND name != "Kevin Bacon"
ORDER BY name asc
