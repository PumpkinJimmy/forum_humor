create materialized view post_content_of_user as
(
    select uid, content
    from ForumUser join Post on Post.poster_uid = ForumUser.uid
);

create or replace function tri_post_content_of_user_func() returns trigger as $$ 
declare
begin
  refresh materialized view  post_content_of_user with data; 
  return null;
end; 
$$ language plpgsql;

create trigger tri_ForumUser_change
after insert or update or delete on ForumUser
for each statement 
  execute procedure tri_post_content_of_user_func();

create trigger tri_Post_change
after insert or update or delete on Post
for each statement 
  execute procedure tri_post_content_of_user_func();