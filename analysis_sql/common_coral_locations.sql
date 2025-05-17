-- question: where are corals most often seen?
-- return the top 10 countries with the most coral observations.
select l.country, count(*) as cnt_observations
from occurrences o
inner join locations l on o.location_id = l.location_id
where l.country is not null
group by l.country
order by cnt_observations desc
LIMIT 10;
