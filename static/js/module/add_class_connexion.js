function get_your_id(id_you_want){
    let get_your_id = document.getElementById(id_you_want);
    return get_your_id;
}

function add_class_connexion(element){
    element.classList.add("input_connexion");
}

function add_placeholder(element, text_placeholder){
    element.placeholder = text_placeholder;
}

export { 
    add_class_connexion,
    add_placeholder,
    get_your_id,
};
