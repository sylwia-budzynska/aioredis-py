# flake8: noqa
try:
    from typing import Literal, Protocol, TypedDict  # lgtm [py/unused-import]
except ImportError:
    from typing_extensions import Literal, Protocol, TypedDict  # lgtm [py/unused-import]
