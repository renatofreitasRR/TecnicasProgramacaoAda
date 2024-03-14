import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches


def plot_income_group(wdi_country_Slice, incomegroups):
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

    # Specify the countries you want to color differently
    fig, ax = plt.subplots(1, 1)
    world.plot(ax=ax, color='lightgrey')
    legends = []
    for incomegroup in incomegroups:
        countries_to_color = wdi_country_Slice[wdi_country_Slice["Income Group"] == incomegroup]["Country Code"].tolist()

        # Plot the world map
        

        # Color the specified countries
        r = np.round(np.random.rand(),1)
        g = np.round(np.random.rand(),1)
        b = np.round(np.random.rand(),1)
        for country in countries_to_color:
            
            try:
                world[world.iso_a3 == country].plot(ax=ax, color=[r,g,b])
            except:
                pass
        red_patch = mpatches.Patch(color=[r,g,b], label=incomegroup)
        legends.append(red_patch)
    ax.legend(handles=legends, bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0. )
    ax.set_title("Income groups")