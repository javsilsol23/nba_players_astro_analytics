import streamlit as st
import pandas as pd
import plotly.express as px


def plot_venus_data(df, title):
    grouped = df.groupby('venus_cycle').size().reset_index(name='count')

    interval_order = ['White_1', 'Blue_5', 'Black_4', 'Red_3', 'White_2', 'Blue_1', 'Black_5', 'Red_4', 'White_3', 'Blue_2',
                      'Black_1', 'Red_5', 'White_4', 'Blue_3', 'Black_2', 'Red_1', 'White_5', 'Blue_4', 'Black_3', 'Red_2']
    interval_colors = ['white', 'blue', 'black', 'red', 'white', 'blue', 'black', 'red', 'white',
                       'blue', 'black', 'red', 'white', 'blue', 'black', 'red', 'white', 'blue', 'black', 'red']

    fig = px.bar(grouped, x='venus_cycle', y='count', title=title,
                 color='venus_cycle', color_discrete_sequence=interval_colors,
                 category_orders={'venus_cycle': interval_order}
                 )

    fig.update_layout(
        plot_bgcolor='lightgreen',
        showlegend=False,
        width=1000,
        height=600
    )

    return fig


def plot_horoscope_data(df, title, planet):
    grouped = df.groupby(planet).size().reset_index(name='count')

    order = ['ARIES', 'TAURUS', 'GEMINI', 'CANCER', 'LEO', 'VIRGO',
             'LIBRA', 'SCORPIO', 'SAGITTARIUS', 'CAPRICORN', 'AQUARIUS', 'PISCES']
    colors = ['red', 'brown', 'green', 'blue', 'red', 'brown', 'green', 'blue',
              'red', 'brown', 'green', 'blue', 'red', 'brown', 'green', 'blue']

    fig = px.bar(grouped, x=planet, y='count', title=title,
                 color=planet, color_discrete_sequence=colors,
                 category_orders={planet: order}
                 )

    fig.update_layout(
        plot_bgcolor='lightgreen',
        showlegend=False,
        width=1000,
        height=600
    )

    return fig


@st.cache_data
def load_data():
    data = pd.read_csv('players_astro3.csv')
    data = data.drop(['lat', 'lon', 'sn'], axis=1)
    return data

#################################################################
#       MAIN        MAIN        MAIN        MAIN        MAIN    #
#################################################################


st.set_page_config(layout="wide")

tab1, tab2 = st.tabs(['Venus Cycle', 'Horoscope'])

with tab1:
    st.markdown('# Venus Cycle')

    col1, col2, col3 = st.columns([1, 3, 1])

    with col1:
        st.write('')

    with col2:

        st.markdown(
            '<h1 style="text-align: center">NBA Players by Venus Cycle</h1>', unsafe_allow_html=True)
        data = load_data()
        data = data.drop(['sun', 'moon', 'mercury', 'venus', 'mars', 'jupiter',
                         'saturn', 'uranus', 'neptune', 'pluto', 'nn', 'asc', 'mc'], axis=1)

        with st.expander('Display filters'):

            max_gp = int(data['gp'].max())
            gp = st.slider('Games Played', 0, max_gp, 0, key='gp_v')

            max_pts = int(data['pts'].max())
            pts = st.slider('Points per Game', 0, max_pts, 0, key='pts_v')

            max_rbs = int(data['rbs'].max())
            rbs = st.slider('Rebounds per Game', 0, max_rbs, 0, key='rbs_v')

            max_ast = int(data['ast'].max())
            ast = st.slider('Assists per game', 0, max_ast, 0, key='ast_v')

            max_fg = int(data['fg'].max())
            fg = st.slider('Field Goal Percentage', 0, max_fg, 0, key='fg_v')

            max_fg3 = int(data['fg3'].max())
            fg3 = st.slider('3 Pointers Percentage',
                            0, max_fg3, 0, key='fg3_v')

            max_ft = int(data['ft'].max())
            ft = st.slider('Free Throw Percentage', 0, max_ft, 0, key='ft_v')

            max_efg = int(data['efg'].max())
            efg = st.slider('Effective Field Goal Percentage',
                            0, max_efg, 0, key='efg_v')

            aux = data[data['gp'] > 10]
            max_per = int(aux['per'].max())
            per = st.slider('Player Efficiency Rating', 0, max_per, 0)

            max_ws = int(data['ws'].max())
            ws = st.slider('Win Shares', 0, max_ws, 0)

        filtered_data = data[(data['gp'] > gp) & (data['pts'] > pts) & (data['rbs'] > rbs) &
                             (data['ast'] > ast) & (data['fg'] > fg) & (data['fg3'] > fg3) &
                             (data['ft'] > ft) & (data['efg'] > efg) & (data['per'] > per) & (data['ws'] > ws)]

        if st.checkbox('Show table', key='show_v'):
            st.subheader('Players')
            st.write(filtered_data)

        fig = plot_venus_data(
            filtered_data, 'Total Player Count by Venus Interval')
        st.plotly_chart(fig)

    with col3:
        st.write('')


with tab2:
    st.markdown('# Horoscope')

    col1, col2, col3 = st.columns([1, 3, 1])

    with col1:
        st.write('')

    with col2:

        st.markdown(
            '<h1 style="text-align: center">NBA Players by Horoscopic Signs</h1>', unsafe_allow_html=True)
        data = load_data()
        data = data.drop(['venus_cycle'], axis=1)

        with st.expander('Display filters'):

            max_gp = int(data['gp'].max())
            gp = st.slider('Games Played', 0, max_gp, 0, key='gp_h')

            max_pts = int(data['pts'].max())
            pts = st.slider('Points per Game', 0, max_pts, 0, key='pts_h')

            max_rbs = int(data['rbs'].max())
            rbs = st.slider('Rebounds per Game', 0, max_rbs, 0, key='rbs_h')

            max_ast = int(data['ast'].max())
            ast = st.slider('Assists per game', 0, max_ast, 0, key='ast_h')

            max_fg = int(data['fg'].max())
            fg = st.slider('Field Goal Percentage', 0, max_fg, 0, key='fg_h')

            max_fg3 = int(data['fg3'].max())
            fg3 = st.slider('3 Pointers Percentage',
                            0, max_fg3, 0, key='fg3_h')

            max_ft = int(data['ft'].max())
            ft = st.slider('Free Throw Percentage', 0, max_ft, 0, key='ft_h')

            max_efg = int(data['efg'].max())
            efg = st.slider('Effective Field Goal Percentage',
                            0, max_efg, 0, key='efg_h')

            aux = data[data['gp'] > 10]
            max_per = int(aux['per'].max())
            per = st.slider('Player Efficiency Rating',
                            0, max_per, 0, key='per_h')

            max_ws = int(data['ws'].max())
            ws = st.slider('Win Shares', 0, max_ws, 0, key='ws_h')

        filtered_data = data[(data['gp'] > gp) & (data['pts'] > pts) & (data['rbs'] > rbs) &
                             (data['ast'] > ast) & (data['fg'] > fg) & (data['fg3'] > fg3) &
                             (data['ft'] > ft) & (data['efg'] > efg) & (data['per'] > per) & (data['ws'] > ws)]

        if st.checkbox('Show table', key='show_h'):
            st.subheader('Players')
            st.write(filtered_data)

        planet = st.selectbox(
            'Which Planet?',
            ('Sun', 'Moon', 'Mercury', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto', 'North Node', 'ASC', 'MC'))

        title = 'Total Player Count by ' + planet + ' Sign'
        if planet == 'North Node':
            planet = 'nn'

        fig = plot_horoscope_data(filtered_data, title, planet.lower())
        st.plotly_chart(fig)

    with col3:
        st.write('')
