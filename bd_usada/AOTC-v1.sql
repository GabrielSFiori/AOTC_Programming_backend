-- primera ejecucion
CREATE DATABASE App_Coding;
-- segunda ejecucion
USE app_coding;

-- 1ra ejecucion tabla users 
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    users VARCHAR(255),
    email VARCHAR(255),
    passwords VARCHAR(255),
    birthday_date DATE,
    route_img VARCHAR(255)
);

-- 2da ejecucion tabla servers
CREATE TABLE servers (
    server_id INT AUTO_INCREMENT PRIMARY KEY,
    name_server VARCHAR(255),
    description_server TEXT,
    property_id INT,
    FOREIGN KEY (property_id) REFERENCES users(user_id)
);

-- 3ra ejecucion tabla chats
CREATE TABLE chats (
    id_msg INT AUTO_INCREMENT PRIMARY KEY,
    id_user INT,
    content TEXT,
    date_day DATE,
    date_time TIME,
    id_channel INT,
    FOREIGN KEY (id_user) REFERENCES users(user_id),  -- Clave externa para el usuario
    FOREIGN KEY (id_channel) REFERENCES channels(channel_id) -- Clave externa para el canal
);

-- 4ta ejecucion tabla channels
CREATE TABLE channels (
    channel_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(255),
    description_ TEXT,
    property_id INT,
    server_id INT, -- Nueva columna para la relaciÃ³n con servidores
    FOREIGN KEY (property_id) REFERENCES users(user_id),
    FOREIGN KEY (server_id) REFERENCES servers(server_id) -- Clave externa para el servidor
);

-- 5ta ejecucion
CREATE TABLE servermembers (
    user_id INT,
    id_server INT,
    msg_id INT,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (id_server) REFERENCES servers(server_id),
    FOREIGN KEY (msg_id) REFERENCES chats(id_msg)
);