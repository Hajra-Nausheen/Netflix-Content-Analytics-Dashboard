--SQL TABLE CREATION
create table netflix_titles(
	show_id VARCHAR(10),
	type VARCHAR(20),
	title TEXT,  
	director TEXT,
	cast_members TEXT,
	country TEXT,
	date_added DATE,
	release_year INT,
	rating  TEXT,
	duration TEXT,
	listed_in TEXT,
	description TEXT,
    duration_value INT,
	duration_unit TEXT,
	primary_genre TEXT ,
	year_added INT,
    month_added TEXT
);

SELECT COUNT(*) FROM netflix_titles;

select * from netflix_titles
limit 10;

select * from netflix_titles 
where duration_value is null;

select count(*) from netflix_titles
where director = 'Unknown';

-- Top Movies vs Shows

select type,
	count(*) as total_titles
from netflix_titles
group by type;


select count (*) title from netflix_titles;

-- Top 10 Countries by Number of titles
select country ,
	count(*) as total_titles
	from netflix_titles
	group by country
	order by  total_titles desc
	limit 10 ;


select distinct country from netflix_titles;

-- Most Common rating
select rating,
	COUNT (*) as total_titles
	from netflix_titles
	group by rating
	order by total_titles desc;

-- Content added each year
select year_added,
	count (*) as total_titles
	from netflix_titles
	group by year_added
	order by year_added;

select year_added,
	count (*) as total_titles
	from netflix_titles
	group by year_added
	order by total_titles;	

-- Top 10 grnres
select primary_genre,
	count(*) as top_genre
	from netflix_titles
	group by primary_genre
	order by top_genre desc;

--
select duration,
	count(*) as longest_movies
	from netflix_titles
	group by duration
	order by longest_movies desc;

-- longest Movies
select title,
	duration_value
	from netflix_titles
	where type ='Movie'
	order by duration_value desc
	limit 10;

-- TV shows with Most Seasons
select title,
	duration_value as seasons
	from netflix_titles
	where type = 'Tv Show'
	order by duration_value desc
	limit 10;
	
	