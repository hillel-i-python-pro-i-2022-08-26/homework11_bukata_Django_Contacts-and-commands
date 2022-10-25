from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

KEY__COUNT_OF_VISITS = "count_of_visits"


def session_example_view(request: HttpRequest) -> HttpResponse:
    # SessionStorage its added inotation
    session = request.session
    # we add counter of coming in, for each session it will
    # be its own counter and will be more for one
    count_of_visits = session.get(KEY__COUNT_OF_VISITS, 0)
    # increment for one
    count_of_visits += 1
    # to save new "znachenie" by our key
    session[KEY__COUNT_OF_VISITS] = count_of_visits
    return render(
        request,
        "session_example.html",
        {
            # contacts in general will be refering
            # to generator fuc , but here to contacts in this fun upper (with objects)
            "session_id": session.session_key,
            # add one more "znachenie" to be showen on web page
            "count_of_visits": count_of_visits,
            "title": "Session example",
        },
    )
