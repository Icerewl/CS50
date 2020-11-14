SELECT title FROM movies
JOIN stars ON movies.id = stars.movie_id
JOIN people ON stars.person_id = people.id
WHERE name = "Kevin Bacon"
INTERSECT
SELECT title FROM movies
JOIN stars ON movies.id = stars.movie_id
JOIN people ON stars.person_id = people.id
WHERE name = "%"