import streamlit as st
from streamlit_calendar import calendar

mode = st.selectbox(
        "Calendar Mode:",
        (
            "Month",
            "Week",
            "Schedule",
            "Year",
        ),
    )
events = [
        {
            "title": "Singapore Perspectives conference",
            "color": "#FF6C6C",
            "start": "2024-01-22",
            "end": "2024-01-22",
            "resourceId": "a",
        },
        {
            "title": "Singapore Perspectives conference",
            "color": "#FF6C6C",
            "start": "2024-01-29",
            "end": "2023-01-29",
            "resourceId": "a",
        },
        {
            "title": "Conversations with YOUths",
            "color": "#FF4B4B",
            "start": "2024-05-31",
            "end": "2024-05-31",
            "resourceId": "b",
        },
        {
            "title": "Conversations with YOUths",
            "color": "#FF4B4B",
            "start": "2024-06-07",
            "end": "2024-06-07",
            "resourceId": "",
        },
        {
            "title": "Conversations with YOUths",
            "color": "#FF4B4B",
            "start": "2024-06-14",
            "end": "2024-06-14",
            "resourceId": "b",
        },
        {
            "title": "Conversations with YOUths",
            "color": "#FF4B4B",
            "start": "2024-06-21",
            "end": "2024-06-21",
            "resourceId": "b",
        },
        {
            "title": "Singapore Model Cabinet",
            "color": "#FFBD45",
            "start": "2024-03-13",
            "end": "2024-03-16",
            "resourceId": "c",
        },
        {
            "title": "Pre-University Seminar",
            "color": "#3D9DF3",
            "start": "2024-05-27",
            "end": "2024-05-30",
            "resourceId": "d",
        }
    ]
calendar_resources = [
        {"id": "a", "building": "Building A", "title": "Room A"},
        {"id": "b", "building": "Building A", "title": "Room B"},
        {"id": "c", "building": "Building B", "title": "Room C"},
        {"id": "d", "building": "Building B", "title": "Room D"},
        {"id": "e", "building": "Building C", "title": "Room E"},
        {"id": "f", "building": "Building C", "title": "Room F"},
    ]
calendar_options = {
        "editable": "true",
        "navLinks": "true",
        "resources": calendar_resources,
        "selectable": "true",
    }

if mode == "Month":
            calendar_options = {
                **calendar_options,
                "headerToolbar": {
                    "left": "today prev,next",
                    "center": "title",
                    "right": "dayGridDay,dayGridWeek,dayGridMonth",
                },
                "initialDate": "2024-05-01",
                "initialView": "dayGridMonth",
            }
elif mode == "Week":
    calendar_options = {
        **calendar_options,
        "initialView": "timeGridWeek",
    }

elif mode == "Schedule":
    calendar_options = {
        **calendar_options,
        "initialDate": "2024-05-01",
        "initialView": "listMonth",
    }
elif mode == "Year":
    calendar_options = {
        **calendar_options,
        "initialView": "multiMonthYear",
    }

state = calendar(
        events=st.session_state.get("events", events),
        options=calendar_options,
        custom_css="""
        .fc-event-past {
            opacity: 0.8;
        }
        .fc-event-time {
            font-style: italic;
        }
        .fc-event-title {
            font-weight: 700;
        }
        .fc-toolbar-title {
            font-size: 2rem;
        }
        """,
        key=mode,
    )

if state.get("eventsSet") is not None:
        st.session_state["events"] = state["eventsSet"]

