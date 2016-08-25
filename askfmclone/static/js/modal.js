(function() {
    $('#answer-form').on('show.bs.modal', function(e) {
        var button = $(e.relatedTarget),
            questionText = button.data('questiontext'),
            questionId = button.data('questionid'),
            modal = $(this);
        modal.find('#question-text')
            .text(questionText);
        modal.find('#question-id').val(questionId);
    })
})();
