SELECT name
FROM people 
JOIN stars ON people.id = stars.person_id 
JOIN movies ON movies.id = stars.movie_id
WHERE year = 2004
GROUP By name, person_id
ORDER BY birth ASC;