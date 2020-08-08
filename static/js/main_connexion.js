import {
    add_class_connexion,
    add_placeholder,
    get_your_id,
} from './module/add_class_connexion.js';

add_class_connexion(get_your_id("id_username"));
add_class_connexion(get_your_id("id_password"));

add_placeholder(get_your_id("id_username"), "Pseudo");
add_placeholder(get_your_id("id_password"), "Password");
