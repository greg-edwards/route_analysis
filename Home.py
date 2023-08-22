import streamlit as st

st.set_page_config(layout="wide")

st.sidebar.image('https://becagroup.sharepoint.com/sites/ClientsandMarkets/Images1/Market%20Profile%20&%20Brand/Beca%20Brand%20&%20Standards/Beca%20Logo%20Black%20PNG.png?csf=1&web=1&e=p6QEq9&cid=d89ac465-29af-4979-83d9-a76c21e84693', width=150, output_format="auto")

st.sidebar.title("About")
st.sidebar.info(
    """
    The Western Bay of Plenty PT Services and Infrastructure Business Case is investigating options to anble signficant mode shift to PT in the Western Bay. The business case will identify both service and infrastructure modifications/interventions.
    """
)

st.sidebar.title("Questions / Contact")
st.sidebar.info(
    """
    If you have any questions or general feedback on this app or notice any errors, please contact Greg Edwards (greg.edwards@beca.com)
    """
)


st.title("Western Bay of Plenty PT Services and Infrastructure Business Case")
st.header("Route Modification Analysis and Options")


st.markdown(
    """
    This multi-page web app shows indicative options and corresponding analysis for service modifications for the Western Bay of Plenty PT Services and Infrastructure Business Case.
    This includes:
- Service modifications (routes and frequencies by day of week, operating times including start/finish times).
- Confirm interchange and layover requirements, issues and constraints (based on Reference Case assumptions).
- Park and Ride options to be tested for all options.
   
    """
)

st.info("Click on the left sidebar menu to navigate to the various service modification options.")

