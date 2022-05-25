// Used from GymFit Website
$('.profile-buttons').click(function(){
    section = this.id.slice(0, -7);
    $('#' + section).show();
    $(".profile-section").not($('#' + section)).hide();
    $("#visible-section-name").html(section.replace(/-/g, " ").toUpperCase());
});

$(document).ready(function(){
    $('#my-info').show();
});
