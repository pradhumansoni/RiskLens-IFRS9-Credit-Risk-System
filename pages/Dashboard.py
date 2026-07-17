import streamlit as st

from src.utils import load_css

from src.components import (
    create_page_header,
    create_welcome_banner,
    create_system_overview,
    create_quick_actions,
    create_project_highlights,
    create_footer
)

load_css()

create_page_header(
    "🏦 IFRS 9 Compliant Risk Management And  Support Platform",
    ""
)

create_welcome_banner()

create_system_overview()

create_quick_actions()


create_project_highlights()

create_footer()