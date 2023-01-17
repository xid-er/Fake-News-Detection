$('input[type=radio][name=model_select]').change(function() {
    if (this.value == 'simple_model') {
        $('form').find("textarea[type=text]").each(function(){
            $(this).attr("placeholder", "Paste the text of the Tweet here!");
        });
    }
    else if (this.value == 'complex_model') {
        $('form').find("textarea[type=text]").each(function(){
            $(this).attr("placeholder", "Put the link of the Tweet here!");
        });
    }
});