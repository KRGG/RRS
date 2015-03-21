$(function(){
    $('#datepicker').datepicker({
        showOtherMonths: true,
        selectOtherMonths: true,
        inline: true,
        altField: '#datepicker-input'
    });

    $('#datepicker-input').change(function(){
        $('#datepicker').datepicker('setDate', $(this).val());
        console.log($('#datepicker').datepicker('getDate'));
    });

    $('#today').click(function(){
        var today= getToday();
        $('#datepicker-input').val(today);
        $('#datepicker').datepicker('setDate', today);
    });
    
    function getToday(){
        var today =new Date();
        var dd = today.getDate();
        var mm = today.getMonth() + 1; //January is 0!
        var yyyy = today.getFullYear();
        if(dd<10){
            dd='0'+dd
        } 
        if(mm<10){
            mm='0'+mm
        } 
        return mm+'/'+dd+'/'+yyyy;
    }
});