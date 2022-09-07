create table products(
    int product_id,
    varchar(255) p_name,
    int price,
    date creation_date
);
create table products_categories(
    int pk
    int product_id
    int category_id
);
create table categories(
    int category_id,
    varchar(255) c_name,
    int flag
);

select product_id from products_categories where category_id in
    (select category_id from categories where flag = 1)
    group by product_id having count(*)>5

--Flag = 1 si public