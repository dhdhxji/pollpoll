function documentReady()
{
    $(".hidden").hide()

    function add_choise_element(){
        let prev_el = $(this).parent().find(".new_poll_choises").find(".new_poll_choise").last()
        
        let prev_num = prev_el.find("input").attr("id").match(/\d+$/).toString()
        let prev_name_attr_val_t = prev_el.find("input").attr("name").match(/^\D+/).toString()
        
        let old_text = prev_el.find("label").text().match(/^\D+/).toString()
        let input_id_val_t = prev_el.find("input").attr("id").match(/^\D+/).toString()
        let new_num = Number(prev_num) + 1

        let new_element = prev_el.clone()

        new_element.find("input").attr("id", input_id_val_t + new_num)
        new_element.find("input").attr("name", prev_name_attr_val_t + new_num)
        new_element.find("label").text(old_text + new_num + " : ")

        new_element.appendTo($(this).parent().find(".new_poll_choises"))
    }


    $("#add_choise").click(add_choise_element);
}

$(document).ready(documentReady)