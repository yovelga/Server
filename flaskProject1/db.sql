create table users
(
    id           int auto_increment
        primary key,
    name         varchar(255) null,
    email        text         not null,
    password     varchar(120) null,
    phone_number varchar(10)  null
);

INSERT INTO myflaskappdb.users (name, email, password, phone_number) VALUES ('yovelg', 'yovelgani@gmail.com', '213213321', '132321123');
INSERT INTO myflaskappdb.users (name, email, password, phone_number) VALUES ('orr', 'or@gmal.com', '12345678', '1234567890');
INSERT INTO myflaskappdb.users (name, email, password, phone_number) VALUES ('yossi', 'yossi@gmail.com', '123111111111', '0522222222');
INSERT INTO myflaskappdb.users (name, email, password, phone_number) VALUES ('moshe', 'moshe@gmail.com', '123111111', '0533333333');
INSERT INTO myflaskappdb.users (name, email, password, phone_number) VALUES ('tamir', 'tamir@gmail.com', '1111111111', '0544444444');
INSERT INTO myflaskappdb.users (name, email, password, phone_number) VALUES ('lior', 'lior@gmail.com', '123111111', '0541111111');
