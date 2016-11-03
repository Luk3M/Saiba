﻿function sendComment(formId, formType, formSlug, formContent, sendCommentApiEndpoint, getCommentApiEndpoint) {
    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                var csrftoken = getCookie("csrftoken");
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    $.ajax({
        type: "POST",
        url: sendCommentApiEndpoint,
        data: { type: formType, slug: formSlug, content: formContent, id: formId },
        success: function (data) {
            updateCommentSection("#comment-section", getCommentApiEndpoint);
        }
    })
}

function sendReply(commentId, formContent, sendReplyApiEndpoint, getCommentApiEndpoint) {
    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                var csrftoken = getCookie("csrftoken");
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    $.ajax({
        type: "POST",
        url: sendReplyApiEndpoint,
        data: { comment: commentId, content: formContent },
        success: function (data) {
            updateCommentSection("#comment-section", getCommentApiEndpoint);
        }
    })
}

function updateCommentSection(commentSectionId, getCommentApiEndpoint) {
    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                var csrftoken = getCookie("csrftoken");
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    $.ajax({
        type: "GET",
        url: getCommentApiEndpoint,
        data: $(this).serialize(),
        success: function (data) {
            createCommentSection(commentSectionId, data);
        }
    })
}

function createCommentSection(commentSectionId, json_comments) {
    $(commentSectionId).empty();
    for (i = 0; i < json_comments.results.length; i++) {
        var comment = createComment(json_comments.results[i].id, json_comments.results[i].author,
                                    json_comments.results[i].update_date, json_comments.results[i].content);


        $(commentSectionId).append(comment);

        for (j = 0; j < json_comments.results[i].replies.length; j++) {
            var reply = createReply(json_comments.results[i].replies[j].id,
                                    json_comments.results[i].replies[j].author,
                                    json_comments.results[i].replies[j].update_date,
                                    json_comments.results[i].replies[j].content);

            $('#comment-' + (i + 1) + ' #replies').append(reply);
        };
    }
}

function createComment(id, author, date, content) {
    var div_comment = $('<div />').addClass('col-md-12').attr('id', 'comment-' + id).attr("data-id", id);
    var span_author = $('<span />').addClass('col-md-12').html(author);
    var span_date = $('<span />').addClass('col-md-12').html(date);
    var span_content = $('<span />').addClass('col-md-12').html(content);

    var button_upvote = $('<button />').addClass('btn btn-default btn-xs').html("Cimavoto");
    var button_downvote = $('<button />').addClass('btn btn-default btn-xs').html("Baixovoto");
    var button_reply = $('<button />').addClass('btn btn-default btn-xs').html("Responder");
    var button_send = $('<button />').addClass('btn btn-default btn-xs').css('display', 'none').html("Enviar");

    var textarea_reply = $('<textarea />').addClass('').css('display', 'none');

    var div_replies = $('<div />').addClass('col-md-12').attr('id', 'replies');

    button_reply.click(function () {
        textarea_reply.css('display', '');
        button_send.css('display', '');
        button_reply.css('display', 'none');
    });

    button_send.click(function () {
        sendReply(id, textarea_reply.val(), sendReplyApiEndpoint, getCommentApiEndpoint);
    });

    div_comment.append(span_author).append(span_date).append(span_content).append(button_upvote).append(button_downvote)
                .append(button_reply).append(button_send).append(textarea_reply).append(div_replies);
    return div_comment;
}

function createReply(id, author, date, content) {
    var div_reply = $('<div />').addClass('col-md-12').attr('id', 'reply-' + id).attr("data-id", id);
    var span_author = $('<span />').addClass('col-md-12').html(author);
    var span_date = $('<span />').addClass('col-md-12').html(date);
    var span_content = $('<span />').addClass('col-md-12').html(content);

    div_reply.append(span_author).append(span_date).append(span_content);
    return div_reply;
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}