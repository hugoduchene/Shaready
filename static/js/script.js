import { get_button_edit, get_modal_class, get_box_make_message } from './module/popup_make_message.js';

get_button_edit().addEventListener("click", function onclick(e) {
  get_modal_class().classList.toggle("visible");
  get_modal_class().classList.toggle("invisible");
});

get_modal_class().onclick = function(e) {
  const target = e.target;
  
  if (target === get_modal_class()) {
    get_modal_class().classList.toggle("visible");
    get_modal_class().classList.toggle("invisible");
  }
}
