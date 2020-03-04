-- Problem 13
SELECT name AS genre, COUNT(show_id) AS number_of_shows FROM tv_genres
INNER JOIN tv_show_genres ON genre_id = id
GROUP BY genre ORDER BY number_of_shows DESC;
