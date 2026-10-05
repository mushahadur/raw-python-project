# routes/logout.py

from middleware.auth import (
    get_session_id_from_cookie,
    destroy_session
)


def logout(handler):

    session_id = get_session_id_from_cookie(handler)

    if session_id:
        destroy_session(session_id)

    handler.send_response(303)

    handler.send_header(
        "Set-Cookie",
        "session_id=; Path=/; Max-Age=0; HttpOnly"
    )

    handler.send_header(
        "Location",
        "/login"
    )

    handler.end_headers()