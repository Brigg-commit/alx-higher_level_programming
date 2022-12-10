-- Lists all genres from hbtn_0d_tvshows
-- Record should display: <TV Show genre> - <Number of shows linked to this genre>
-- Results must be sorted in descending order by order of show linked.
-- You can use only one SELECT statement
SELECT tv_genres.name AS genre, COUNT(*) AS number_shows
FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_show_genres.genre_id
ORDER BY number_shows DESC;

