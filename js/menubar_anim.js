

function documentReady()
{
    $(".hidden").hide()

    function menu_entr_show(){
        $(this).children(".hidden").fadeIn()
    }

    function menu_entr_hide(){
        $(this).children(".hidden").fadeOut()
    }

    $(".menubar div").hover(menu_entr_show, menu_entr_hide)
}

$(document).ready(documentReady)