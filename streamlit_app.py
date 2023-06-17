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
        plot_bgcolor='#ccffe6',
        showlegend=False,
        width=1000,
        height=600
    )

    return fig


def plot_venus_colors(df, title):
    fig = px.pie(df,
                 names='color', title='Venus Cycle Distribution',
                 color='color', color_discrete_map={
                     'Red': 'red',
                     'Blue': 'blue',
                     'Black': 'black',
                     'White': "white"
                 }
                 )
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='#ccffe6'  # Set the desired background color
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
        plot_bgcolor='#ccffe6',
        showlegend=False,
        width=1000,
        height=600
    )

    return fig


def plot_pie_chart(df, title, names, color_map):

    fig = px.pie(df,
                 names=names, title=title,
                 color=names, color_discrete_map=color_map
                 )
    fig.update_layout(
        # Set to 'rgba(0,0,0,0)' for transparent background
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='#ccffe6'  # Set the desired background color
    )

    return fig


def classify_sign(s):

    if s == 'ARIES':
        return 'fire', 'cardinal'
    elif s == 'TAURUS':
        return 'earth', 'fix'
    elif s == 'GEMINI':
        return 'air', 'mutable'
    elif s == 'CANCER':
        return 'water', 'cardinal'
    elif s == 'LEO':
        return 'fire', 'fix'
    elif s == 'VIRGO':
        return 'earth', 'mutable'
    elif s == 'LIBRA':
        return 'air', 'cardinal'
    elif s == 'SCORPIO':
        return 'water', 'fix'
    elif s == 'SAGITTARIUS':
        return 'fire', 'mutable'
    elif s == 'CAPRICORN':
        return 'earth', 'cardinal'
    elif s == 'AQUARIUS':
        return 'air', 'fix'
    elif s == 'PISCES':
        return 'water', 'mutable'


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

        data['color'] = data['venus_cycle'].str[:-2]

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

        fig2 = plot_venus_colors(filtered_data, 'By Color')
        st.plotly_chart(fig2)

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

        filtered_data[['element', 'modality']] = filtered_data['sun'].apply(
            classify_sign).apply(pd.Series)

        col2_a, col2_b = st.columns(2)

        with col2_a:
            color_map = {
                'fire': 'red',
                'earth': 'brown',
                'air': 'yellow',
                'water': 'blue'
            }
            fig1 = plot_pie_chart(
                filtered_data, 'Players by element', 'element', color_map)
            st.plotly_chart(fig1, use_container_width=True)

        with col2_b:
            color_map = {
                'cardinal': 'red',
                'fix': 'blue',
                'mutable': 'white'
            }
            fig2 = plot_pie_chart(
                filtered_data, 'Players by modality', 'modality', color_map)
            st.plotly_chart(fig2, use_container_width=True)

    with col3:
        st.write('')
