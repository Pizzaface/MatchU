    $(document).on("click", ".workingDayBG", function() {
        $(this).toggleClass('selected');
        day = $(this).attr("id");
        $('#'+day+'Hours').collapse('toggle');
    })

