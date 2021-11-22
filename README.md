# Gun Related Incidents & Federal/State Policy
# <font size="3"> An Analysis By: James Gamarra <ul><em> Data Set: U.S. Gun Violence Records 2014-2021: Archive of Gun Violence incidents in United States</em></ul></font> 
<h2>Introduction:</h2>
    <ul><p>Gun violence in the United States is a well documented problem that has no clear resolution. My aim through the course of this analysis is to examine an aggregated data set in an attempt to examine correlations, outliers, and any key contributing factors that may cause an influx or deflux in gun related incidents.
    </p> 
    </ul>

<h3>Data Set: <em>U.S. Gun Violence Records 2014-2021: Archive of Gun Violence incidents in United States</em></h3>
<ul>
    <li>
    Columns(7): incident_id, incident_date, state, city_or_county, address, killed, injured.
    </li>
    <li>
    4 Numerical, 3 Categorical
    </li>
    <li>
    3230 Entries
    </li>
    <li>
    31Dec13 - 28Sep21
    </li>
    <li>
    Data Set is cleaned so there are no Nan’s.
    </li>
    <li>
     Gun violence  and crime incidents are collected/validated from 7,500 sources daily – Incident Reports and their source data are found at the gunviolencearchive.org website. However, this does not ensure a complete data set. 
    </li>
    <img src="data/images/DataFrame.png" alt="Data Frame PNG" title="Title" />
</ul>
<h3>Data Set Constraints:</h3>
<li>Aggregated Data
    <ul>
        <li>Data is condensed to 3,230 from over 300,000 entries for purposes of analysis.</li>
    </ul>
</li>
<li>
    States are not required to report all incidents.
</li>
<h2> Part 1:<em> Federal Analysis</em>
</h2>
<p>
In terms of the scope of the data, 3230 entries representing 8 years of gun related incidents, it is best to begin analysis on a broader scope and narrow through calculated research.
</p>
<p>
In the past decade federal policy has been forced to address the impeding crisis that is gun violence in the United States. This talking point, widely debated, has seemingly no remedy in sight. Our data set contains data from the Obama Administration as well as the Trump administration. Two presdencies with vastly diffrent views on gun-policy and gun control in the United States.
</p>
<p>
<img src="data/images/InjuredByYear.png" alt="Data Frame PNG" title="InjuredByYear" />
</p>
<p>
At face value, you can deduce two things:
<ul>
1. There is a clear and obvious increase between every year with 17'-18' & 20'-21'as an exception.
</ul>
<ul>
&
</ul>
<ul>
2. The Obama Administration yeilded less Gun Related Injuries than the Trump Administration
</ul>
And the same can be deduced from the "Killed by Gun Related Incident" graph below.
</p>
<p>
<img src="data/images/KilledByYear.png" alt="Data Frame PNG" title="KilledByYear" />
</p>
<p>
But why? Maybe a more in depth analysis will reveal a correlation.
</p>
<p>
The consistent outlier between the "Injured" and "Killed" by year graphic is the apparent drop in incidents in 2018.
</p>
<p>
Looking only at Federal level actions, there were no federal gun laws passed in 2017 that could have spurred a fluctuation. How can we explain this?
</p>
<p>
October 1st, 2017 the largest mass shooting in modern history left 58 people dead and injured close to 700. Following this incident, while there were no federal gun laws implemented... 
</p>
<h4><em>
"... More than 30 laws preventing gun violence passed in state legislatures..." - Newsweek
</h4></em>
<p>
<img src="data/images/LasVegasShooting.jpeg" alt="Data Frame PNG" title="KilledByYear" />
</p>
<p>
This influx of new policies can be attributed as a possible explanation to the decrease in gun related incidences. Besides, this outlier the only correlation that can be derived on a federal level is the 101.4% increase between 2014 and 2021 per the data set. 
</p>
<img src="data/images/KilledByYearData.png" alt="Data Frame PNG" title="KilledByYearData" />
</p>
