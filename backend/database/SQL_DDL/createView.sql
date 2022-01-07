create view tag_access_count as (select tname, count(*) from tag_log group by tname);
