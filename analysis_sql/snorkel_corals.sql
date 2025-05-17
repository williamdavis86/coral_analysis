-- Question: What corals are commonly at a depth suitable for snorkeling?
-- Return the top 10 coral species with the most occurrences at a depth of 0-10m.

select s.scientific_name, count(*) as cnt_observations
from occurrences o
inner join species s on o.species_id = s.species_id
inner join locations l on o.location_id = l.location_id
where l.depth >= 0 and l.depth <= 10
group by s.scientific_name
order by cnt_observations desc
limit 10
