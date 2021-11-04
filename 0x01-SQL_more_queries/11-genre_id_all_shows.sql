-- database dump of hbtn_od_tvshows to MYSQL server

SELECT tv_shows.title, tv_show_genres.genre_id
from tv_shows
LEFT JOIN tv_show_genres
on tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
