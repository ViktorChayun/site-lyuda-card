select count(*) from app_main_visitlog


select 
	count(distinct ip_address) 
from app_main_visitlog

select 
	 country
	 ,city
	 , count(*) cnt
from app_main_visitlog
group by
	country
	 ,city
order by
	cnt desc
	
	
select 
	path
	 , count(*) cnt
from app_main_visitlog
group by
	path
order by
	cnt desc
	
	
SELECT
  CASE
    WHEN user_agent LIKE '%Windows%' THEN 'Windows'
    WHEN user_agent LIKE '%Android%' THEN 'Android'
    WHEN user_agent LIKE '%iPhone%' THEN 'iPhone'
    WHEN user_agent LIKE '%iPad%' THEN 'iPad'
    WHEN user_agent LIKE '%Macintosh%' THEN 'Mac'
    ELSE 'Інше'
  END AS os_type,
  COUNT(*) AS count
FROM app_main_visitlog
GROUP BY os_type
ORDER BY count DESC;