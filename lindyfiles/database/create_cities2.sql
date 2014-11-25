create table cities2 as 
	select ct.country, ct.city, ct.region, ct.latitude, ct.longitude 
	from (
		select city, region, min(postalCode) as minZip
		from cities 
		where country = 'US'
		group by city, region
		)
	as c inner join cities as ct on ct.city=c.city 
	and ct.region=c.region 
	and ct.postalCode=c.minZip;
