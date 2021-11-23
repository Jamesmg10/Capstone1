import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("../data/US-Gun-Violence.csv")
df['year'] = pd.DatetimeIndex(df['incident_date']).year

def plot_IncidentsByYear(df, title = 'Incidents By Year'):
    '''
        Prints a barchart of Incidents per year
        
        ARGS:
            df - pandas df
    '''
    IncidentsByYear = df.groupby("year")["injured"].count()
    IncidentsByYear.plot.bar(x='year', y='incidents')
    plt.show()
    return IncidentsByYear
    

def plot_InjuredByYear(df, title = 'Injured By Year'):
    '''
        Prints a barchart of Injured per year
        
        ARGS:
            df - pandas df
    '''
    InjuredByYear = df.groupby("year")["injured"].sum()
    ax = InjuredByYear.plot.bar(x='year', y='injured', color = 'black', figsize = (10,8))
    ax.set_title('Injured in Gun Related Incident', fontdict={'fontsize':14})
    ax.set_xlabel('Year', fontdict={'fontsize':12})
    ax.set_ylabel('Injured', fontdict={'fontsize':12})
    ax.get_xticklabels()[0].set_color("blue")
    ax.get_xticklabels()[1].set_color("blue")
    ax.get_xticklabels()[2].set_color("blue")
    ax.get_xticklabels()[3].set_color("red")
    ax.get_xticklabels()[4].set_color("red")
    ax.get_xticklabels()[5].set_color("red")
    ax.get_xticklabels()[6].set_color("red")
    ax.get_xticklabels()[7].set_color("blue")
    plt.show()
    return InjuredByYear
    

def plot_KilledByYear(df, title = 'Killed By Year'):
    '''
        Prints a barchart of Killed By Year
        
        ARGS:
            df - pandas df
    '''
    KilledByYear = df.groupby("year")["killed"].sum()
    ax = KilledByYear.plot.bar(x='year', y='killed', figsize = (10,8), color = 'red')
    ax.set_title('Killed in Gun Related Incident', fontdict={'fontsize':14})
    ax.set_xlabel('Year', fontdict={'fontsize':12})
    ax.set_ylabel('Killed', fontdict={'fontsize':12})
    ax.get_xticklabels()[0].set_color("blue")
    ax.get_xticklabels()[1].set_color("blue")
    ax.get_xticklabels()[2].set_color("blue")
    ax.get_xticklabels()[3].set_color("red")
    ax.get_xticklabels()[4].set_color("red")
    ax.get_xticklabels()[5].set_color("red")
    ax.get_xticklabels()[6].set_color("red")
    ax.get_xticklabels()[7].set_color("blue")
    plt.show()
    return KilledByYear
    

def plot_IncidentsByState(df, title = 'Incidents By State'):
    '''
        Prints a barchart of Incidents By State
        
        ARGS:
            df - pandas df
    '''
    stateSortdf = df[['state','injured','killed']]
    stateSortdf.groupby(by = "state").sum().sort_values(by = 'injured', ascending = False).head(10)
    IncidentsByState = stateSortdf.groupby(by="state").sum().sort_values(by="injured", ascending=False)
    ax = IncidentsByState.plot(kind="bar", figsize = (18,12), color = {"killed": "red", "injured": "black"})
    ax.set_title('Gun Related Incidents per State 2014-2021', fontdict={'fontsize':18})
    ax.set_xlabel('State', fontdict={'fontsize':14})
    ax.set_ylabel('Killed/Injured', fontdict={'fontsize':14})
    ax.get_xticklabels()[0].set_color("blue")
    ax.get_xticklabels()[1].set_color("blue")
    ax.get_xticklabels()[2].set_color("purple")
    ax.get_xticklabels()[3].set_color("red")
    ax.get_xticklabels()[4].set_color("blue")
    ax.get_xticklabels()[5].set_color("red")
    ax.get_xticklabels()[6].set_color("blue")
    ax.get_xticklabels()[7].set_color("purple")
    ax.get_xticklabels()[8].set_color("blue")
    ax.get_xticklabels()[9].set_color("red")
    ax.get_xticklabels()[10].set_color("red")
    ax.get_xticklabels()[11].set_color("red")
    ax.get_xticklabels()[12].set_color("blue")
    ax.get_xticklabels()[13].set_color("blue")
    ax.get_xticklabels()[14].set_color("blue")
    ax.get_xticklabels()[15].set_color("red")
    ax.get_xticklabels()[16].set_color("red")
    ax.get_xticklabels()[17].set_color("red")
    ax.get_xticklabels()[18].set_color("blue")
    ax.get_xticklabels()[19].set_color("red")
    ax.get_xticklabels()[20].set_color("blue")
    ax.get_xticklabels()[21].set_color("red")
    ax.get_xticklabels()[22].set_color("red")
    ax.get_xticklabels()[23].set_color("red")
    ax.get_xticklabels()[24].set_color("blue")
    ax.get_xticklabels()[25].set_color("blue")
    ax.get_xticklabels()[26].set_color("blue")
    ax.get_xticklabels()[27].set_color("red")
    ax.get_xticklabels()[28].set_color("blue")
    ax.get_xticklabels()[29].set_color("blue")
    ax.get_xticklabels()[30].set_color("blue")
    ax.get_xticklabels()[31].set_color("red")
    ax.get_xticklabels()[32].set_color("red")
    ax.get_xticklabels()[33].set_color("blue")
    ax.get_xticklabels()[34].set_color("blue")
    ax.get_xticklabels()[35].set_color("red")
    ax.get_xticklabels()[36].set_color("purple")
    ax.get_xticklabels()[37].set_color("red")
    ax.get_xticklabels()[38].set_color("blue")
    ax.get_xticklabels()[39].set_color("red")
    ax.get_xticklabels()[40].set_color("red")
    ax.get_xticklabels()[41].set_color("red")
    ax.get_xticklabels()[42].set_color("red")
    ax.get_xticklabels()[43].set_color("blue")
    ax.get_xticklabels()[44].set_color("red")
    ax.get_xticklabels()[45].set_color("red")
    ax.get_xticklabels()[46].set_color("blue")
    ax.get_xticklabels()[47].set_color("red")
    ax.get_xticklabels()[48].set_color("blue")
    plt.show()
    return IncidentsByState
    





