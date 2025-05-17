-- question: what are the most commonly observed corals?
-- top 10 most commonly observed corals
select s.scientific_name, COUNT(*) AS cnt_observations
FROM occurrences o
inner join species s ON o.species_id = s.species_id
group by s.scientific_name
ORDER BY cnt_observations DESC
LIMIT 10;
