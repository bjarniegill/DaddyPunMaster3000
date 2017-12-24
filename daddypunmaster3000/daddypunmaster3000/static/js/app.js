$(document).ready(function() {

    var clearJokeTemplate = function () {
        $("#question").text("");
        $("#answer").text("");
        $("#question-heading").text("");
        $("#answer-heading").text("");
    };

    var setupJokeTemplate = function () {
        $("#question-heading").text("Question");
        $("#answer-heading").text("Answer");
        $("#joke-error").text("");
    };

    var commitButton = $("button").get(1);
    $(commitButton).attr("disabled", "disabled")
    $(commitButton).button("refresh");

    var groupId = $('#group-id').val();
    clearJokeTemplate();

    $("#get-new-joke").click(function() {
        $.get( "/api/joke/" + groupId, function(result, status, jqXHR) {
            if (jqXHR.status === 204) {
                $("#joke-error").text("Sorry no more jokes.");
                clearJokeTemplate();
                $(commitButton).attr("disabled", "disabled")
                $(commitButton).button("refresh");
                return;
            }
            setupJokeTemplate();
            console.log(result);
            $("#question").text(result.question);
            $("#answer").text(result.answer);
            $("#joke-id").val(result.id);

            $(commitButton).removeAttr("disabled");
            $(commitButton).button("refresh");
        });
    });

    $("#commit-to-joke").click(function() {
        var jokeId = $('#joke-id').val();
        $.post("/api/commit/", { joke_id: jokeId }, function(data) {
            setupJokeTemplate();
            $(commitButton).attr("disabled", "disabled")
            $(commitButton).button("refresh");

        }).fail(function(e) {
            $("#joke-error").text("Joke has already been taken by another user");
            clearJokeTemplate();
        });
    });
});
