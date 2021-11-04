-- import database dump from hbtn_0d_tvshows to MYSQL server

SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_show_genres
LEFT JOIN tv_genres
ON tv_genres.id = genre_id
GROUP BY genre_id
ORDER BY number_of_shows DESC;
