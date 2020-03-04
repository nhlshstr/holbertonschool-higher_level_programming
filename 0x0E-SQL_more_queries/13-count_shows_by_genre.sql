-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked t
--o each.
SELECT name AS genre, COUNT(show_id) AS number_of_shows FROM tv_shows
INNER JOIN tv_show_genres ON tv_show_genre.genre_id = tv_show.id
GROUP BY genre ORDER BY number_of_shows DESC;
