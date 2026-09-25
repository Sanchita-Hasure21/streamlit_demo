# import streamlit as st 

# st.title('Hello world ,This is My First Web Page Application')
# st.markdown('---')
# name = st.text_input('Enter your Name : ')
# st.number_input('Enter your Age : ',min_value=5,max_value=100)
# st.selectbox('Gender : ',options= ['Male','Female','Others'])
# st.radio('Maritial Status : ',options= ['Married','unmaried','separted'])
# st.multiselect('Meal',options=['vadapav','misalpav','pulav','pavbhaji'],
#                max_selections = 2)
# st.segmented_control('Coach',options=['3Tier','2Tier','Firstclass','General'])
# st.date_input('Departure Date :')
# st.time_input('Departure Time: ')

# st.date_input('Arrival Date : ')
# st.time_input('Arrival Time : ')

# st.feedback(options='stars')
# st.button('Click Me')
# st.success(f'My name is {name}')


# import streamlit as st

# # Page settings
# st.set_page_config(
#     page_title="Railway Ticket Booking",
#     page_icon="🚆",
#     layout="wide"
# )

# # Main title
# st.title("🚆 Railway Ticket Booking")
# st.markdown("---")

# # Passenger Details
# with st.container():

#     st.subheader("👤 Passenger Details")

#     col1, col2 = st.columns(2)

#     with col1:
#         name = st.text_input("Passenger Name")

#         age = st.number_input(
#             "Age",
#             min_value=5,
#             max_value=100,
#             value=18
#         )

#         gender = st.selectbox(
#             "Gender",
#             options=["Male", "Female", "Others"]
#         )

#     with col2:
#         marital_status = st.radio(
#             "Marital Status",
#             options=["Married", "Unmarried", "Separated"]
#         )

#         meal = st.multiselect(
#             "Meal Preference",
#             options=["Vada Pav", "Misal Pav", "Pulav", "Pav Bhaji"],
#             max_selections=2
#         )

#         coach = st.segmented_control(
#             "Coach Type",
#             options=["3 Tier", "2 Tier", "First Class", "General"]
#         )

# st.markdown("---")

# # Journey Details
# with st.container():

#     st.subheader("🚉 Journey Details")

#     col1, col2 = st.columns(2)

#     with col1:
#         st.write("### Departure")

#         departure_date = st.date_input(
#             "Departure Date",
#             key="departure_date"
#         )

#         departure_time = st.time_input(
#             "Departure Time",
#             key="departure_time"
#         )

#     with col2:
#         st.write("### Arrival")

#         arrival_date = st.date_input(
#             "Arrival Date",
#             key="arrival_date"
#         )

#         arrival_time = st.time_input(
#             "Arrival Time",
#             key="arrival_time"
#         )

# st.markdown("---")

# # Feedback and Booking
# with st.container():

#     st.subheader("⭐ Feedback")

#     feedback = st.feedback(
#         options="stars",
#         key="passenger_feedback"
#     )

#     submit = st.button(
#         "🎫 Book Ticket",
#         type="primary",
#         use_container_width=True
#     )

# # Booking message
# if submit:

#     if name.strip() == "":
#         st.warning("Please enter passenger name.")

#     else:
#         st.success(
#             f"🎉 Ticket booking request submitted successfully for {name}!"
#         )


import streamlit as st
import sqlite3
from datetime import date


# --------------------------------------------------
# DATABASE CONNECTION
# --------------------------------------------------

conn = sqlite3.connect("railway.db")
cursor = conn.cursor()


# --------------------------------------------------
# CREATE TABLE
# --------------------------------------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS bookings (
    booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
    passenger_name TEXT NOT NULL,
    phone TEXT NOT NULL,
    email TEXT,
    train_name TEXT NOT NULL,
    source TEXT NOT NULL,
    destination TEXT NOT NULL,
    journey_date TEXT NOT NULL,
    seat_class TEXT NOT NULL,
    seats INTEGER NOT NULL,
    fare_per_seat REAL NOT NULL,
    total_fare REAL NOT NULL,
    booking_status TEXT DEFAULT 'Confirmed'
)
""")

conn.commit()


# --------------------------------------------------
# STREAMLIT PAGE
# --------------------------------------------------

st.set_page_config(
    page_title="Railway Reservation System",
    page_icon="🚆",
    layout="wide"
)

st.title("🚆 Railway Reservation System")
st.write("Book your railway ticket and manage your bookings.")


# --------------------------------------------------
# SIDEBAR MENU
# --------------------------------------------------

menu = st.sidebar.selectbox(
    "Select Option",
    [
        "Book Ticket",
        "Search Booking",
        "View All Bookings",
        "Cancel Booking"
    ]
)


# ==================================================
# 1. BOOK TICKET
# ==================================================

if menu == "Book Ticket":

    st.header("🎫 Book Your Ticket")

    col1, col2 = st.columns(2)

    with col1:

        passenger_name = st.text_input(
            "Passenger Name"
        )

        phone = st.text_input(
            "Phone Number"
        )

        email = st.text_input(
            "Email"
        )

        train_name = st.selectbox(
            "Select Train",
            [
                "Mumbai Express",
                "Deccan Express",
                "Rajdhani Express",
                "Shatabdi Express",
                "Duronto Express"
            ]
        )

        source = st.selectbox(
            "From",
            [
                "Mumbai",
                "Pune",
                "Delhi",
                "Bengaluru",
                "Hyderabad"
            ]
        )

    with col2:

        destination = st.selectbox(
            "To",
            [
                "Pune",
                "Mumbai",
                "Delhi",
                "Bengaluru",
                "Hyderabad"
            ]
        )

        journey_date = st.date_input(
            "Journey Date",
            min_value=date.today()
        )

        seat_class = st.selectbox(
            "Select Class",
            [
                "Sleeper",
                "AC 3 Tier",
                "AC 2 Tier",
                "AC First Class"
            ]
        )

        seats = st.number_input(
            "Number of Seats",
            min_value=1,
            max_value=10,
            value=1,
            step=1
        )


    # ----------------------------------------------
    # FARE
    # ----------------------------------------------

    fare = {
        "Sleeper": 500,
        "AC 3 Tier": 1000,
        "AC 2 Tier": 1500,
        "AC First Class": 2500
    }

    fare_per_seat = fare[seat_class]

    total_fare = seats * fare_per_seat


    st.subheader("💰 Fare Details")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Fare / Seat",
            f"₹{fare_per_seat}"
        )

    with col2:
        st.metric(
            "Number of Seats",
            seats
        )

    with col3:
        st.metric(
            "Total Fare",
            f"₹{total_fare}"
        )


    # ----------------------------------------------
    # BOOK BUTTON
    # ----------------------------------------------

    if st.button(
        "🎫 Book Ticket",
        use_container_width=True
    ):

        if passenger_name == "":
            st.error("Please enter passenger name.")

        elif phone == "":
            st.error("Please enter phone number.")

        elif source == destination:
            st.error(
                "Source and destination cannot be same."
            )

        else:

            cursor.execute("""
            INSERT INTO bookings
            (
                passenger_name,
                phone,
                email,
                train_name,
                source,
                destination,
                journey_date,
                seat_class,
                seats,
                fare_per_seat,
                total_fare,
                booking_status
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                passenger_name,
                phone,
                email,
                train_name,
                source,
                destination,
                str(journey_date),
                seat_class,
                seats,
                fare_per_seat,
                total_fare,
                "Confirmed"
            ))

            conn.commit()


            # Get generated booking ID
            booking_id = cursor.lastrowid


            st.success(
                "🎉 Ticket booked successfully!"
            )

            st.info(
                f"Your Booking ID is: {booking_id}"
            )

            st.write(
                f"**Passenger:** {passenger_name}"
            )

            st.write(
                f"**Train:** {train_name}"
            )

            st.write(
                f"**Journey:** {source} → {destination}"
            )

            st.write(
                f"**Date:** {journey_date}"
            )

            st.write(
                f"**Seats:** {seats}"
            )

            st.write(
                f"**Total Fare:** ₹{total_fare}"
            )


# ==================================================
# 2. SEARCH BOOKING
# ==================================================

elif menu == "Search Booking":

    st.header("🔎 Search Booking")

    booking_id = st.number_input(
        "Enter Booking ID",
        min_value=1,
        step=1
    )


    if st.button(
        "Search Booking",
        use_container_width=True
    ):

        cursor.execute("""
        SELECT *
        FROM bookings
        WHERE booking_id = ?
        """, (booking_id,))

        booking = cursor.fetchone()


        if booking:

            st.success("Booking found!")


            st.subheader(
                f"Booking ID: {booking[0]}"
            )

            col1, col2 = st.columns(2)


            with col1:

                st.write(
                    f"**Passenger Name:** {booking[1]}"
                )

                st.write(
                    f"**Phone:** {booking[2]}"
                )

                st.write(
                    f"**Email:** {booking[3]}"
                )

                st.write(
                    f"**Train:** {booking[4]}"
                )

                st.write(
                    f"**From:** {booking[5]}"
                )

                st.write(
                    f"**To:** {booking[6]}"
                )


            with col2:

                st.write(
                    f"**Journey Date:** {booking[7]}"
                )

                st.write(
                    f"**Class:** {booking[8]}"
                )

                st.write(
                    f"**Seats:** {booking[9]}"
                )

                st.write(
                    f"**Fare / Seat:** ₹{booking[10]}"
                )

                st.write(
                    f"**Total Fare:** ₹{booking[11]}"
                )

                st.write(
                    f"**Status:** {booking[12]}"
                )


        else:

            st.error(
                "No booking found with this Booking ID."
            )


# ==================================================
# 3. VIEW ALL BOOKINGS
# ==================================================

elif menu == "View All Bookings":

    st.header("📋 All Bookings")


    cursor.execute("""
    SELECT
        booking_id,
        passenger_name,
        train_name,
        source,
        destination,
        journey_date,
        seat_class,
        seats,
        total_fare,
        booking_status
    FROM bookings
    ORDER BY booking_id DESC
    """)


    bookings = cursor.fetchall()


    if bookings:

        st.dataframe(
            bookings,
            use_container_width=True
        )

    else:

        st.info(
            "No bookings available."
        )


# ==================================================
# 4. CANCEL BOOKING
# ==================================================

elif menu == "Cancel Booking":

    st.header("❌ Cancel Booking")


    booking_id = st.number_input(
        "Enter Booking ID",
        min_value=1,
        step=1
    )


    if st.button(
        "Cancel Ticket",
        use_container_width=True
    ):

        cursor.execute("""
        SELECT booking_status
        FROM bookings
        WHERE booking_id = ?
        """, (booking_id,))

        booking = cursor.fetchone()


        if booking is None:

            st.error(
                "Booking ID not found."
            )

        elif booking[0] == "Cancelled":

            st.warning(
                "This booking is already cancelled."
            )

        else:

            cursor.execute("""
            UPDATE bookings
            SET booking_status = 'Cancelled'
            WHERE booking_id = ?
            """, (booking_id,))

            conn.commit()


            st.success(
                "Ticket cancelled successfully."
            )