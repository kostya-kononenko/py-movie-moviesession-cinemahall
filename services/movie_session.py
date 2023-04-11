from datetime import datetime
from typing import Optional

from django.db.models import QuerySet

from db.models import MovieSession


def create_movie_session(movie_show_time: datetime,
                         movie_id: int,
                         cinema_hall_id: int) -> None:
    return MovieSession.objects.get_or_create(show_time=movie_show_time,
                                              movie_id=movie_id,
                                              cinema_hall_id=cinema_hall_id)


def get_movies_sessions(session_date: datetime
                        = None) -> QuerySet[MovieSession]:
    queryset = MovieSession.objects.all()
    if session_date is not None:
        queryset = queryset.filter(show_time__date=session_date)
    return queryset


def get_movie_session_by_id(movie_session_id: int) -> Optional[MovieSession]:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(session_id: int = None,
                         show_time: str = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None) -> None:
    movie_session = MovieSession.objects.filter(id=session_id)
    if show_time is not None:
        movie_session.update(show_time=show_time)
    if movie_id is not None:
        movie_session.update(movie_id=movie_id)
    if cinema_hall_id is not None:
        movie_session.update(cinema_hall_id=cinema_hall_id)


def delete_movie_session_by_id(session_id: int) -> None:
    get_movie_session_by_id(movie_session_id=session_id).delete()