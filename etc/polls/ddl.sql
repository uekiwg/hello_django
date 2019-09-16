create table ma_user (
    id bigserial not null
  , user_id VARCHAR(10) not null
  , lang VARCHAR(2) default('en')
--  , delete_flg boolean default(false)
  , delete_flg boolean
  , create_id bigint
  , create_ts timestamp
  , update_id bigint
  , update_ts timestamp
  , primary key (id)
)
;

create table mb_product (
    id bigserial not null
  , product_no VARCHAR(10) not null
  , product_nm VARCHAR(50) not null
--  , delete_flg boolean default(false)
  , delete_flg boolean
  , create_id bigint
  , create_ts timestamp
  , update_id bigint
  , update_ts timestamp
  , primary key (id)
)
;
