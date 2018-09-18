'''
Created on Sep 16, 2018

@author: hp
'''

#Step 1: Biodiversity Project
from matplotlib import pyplot as plt
import pandas as pd
species = pd.read_csv('species_info.csv')
print(species.head())
#Step 8
from scipy.stats import chi2_contingency

#Step 2: Inspected the DataFrame
species_count = species.scientific_name.nunique()
species_type = species.category.unique()
conservation_status = species.conservation_status.unique()

#Step 3: Analyze Species Conservation Status
conservation_counts = species.groupby('conservation_status').scientific_name.nunique().reset_index()
print(conservation_counts)

#Step 4: Analyze Conservation Status II
species.fillna('No Intervention', inplace = True)
conservation_counts_fixed = species.groupby('conservation_status').scientific_name.nunique().reset_index()
cons_status = species.groupby('conservation_status').scientific_name.nunique()

#Step 5: Plotting Conservation Status by Species
protection_counts = species.groupby('conservation_status').scientific_name.nunique().reset_index().sort_values(by='scientific_name')
plt.figure(figsize=(10, 4))
ax = plt.subplot()
plt.bar(range(len(protection_counts)),protection_counts.scientific_name.values)
ax.set_xticks([0, 1, 2, 3, 4])
ax.set_xticklabels(protection_counts.conservation_status.values)
plt.ylabel('Number of Species')
plt.title('Conservation Status by Species')
plt.show()
plt.close('all')

#Step 6: Investigating Endangered Species
species['is_protected'] = species.conservation_status != 'No Intervention'
category_counts = species.groupby(['category', 'is_protected']).scientific_name.nunique().reset_index()
print (category_counts.head())
category_pivot = category_counts.pivot(columns='is_protected', index='category', values='scientific_name').reset_index()

#Step 7: Investigating Endangered Species II
category_pivot.columns = ['category', 'not_protected', 'protected']
category_pivot['percent_protected'] = category_pivot.protected / (category_pivot.protected + category_pivot.not_protected)
print (category_pivot)

#Step 8: Chi-Squared Test for Significance
contingency = [[30, 146], [75, 413]]
chi2, pval, dof, expected = chi2_contingency(contingency)
print(pval)
contingency_rp = [[5, 73], [30, 146]]
chi2_rp, pval_reptile_mammal, dof_rp, expected_rp = chi2_contingency(contingency_rp)
print(pval_reptile_mammal)

#Step 9: Final Thoughts on Protected Species
#===============================================================================

#Step 10: Observations DataFrame
observations = pd.read_csv('observations.csv')
print(observations.head())

#Step 11: In Search of Sheep
species['is_sheep'] = species.common_names.apply(lambda x: True if 'Sheep' in x else False)
species_is_sheep = species[species.is_sheep == True]
print(species_is_sheep)
sheep_species = species_is_sheep[species_is_sheep.category == 'Mammal']
print(sheep_species)

#Step 12: Merging Sheep and Observation DataFrames
sheep_observations = pd.merge(sheep_species, observations)
print(sheep_observations.head())
obs_by_park = sheep_observations.groupby('park_name').observations.sum().reset_index()
print(obs_by_park)

#Step 13: Plotting Sheep Sightings
plt.figure(figsize=(16, 4))
ax = plt.subplot()
plt.bar(range(len(obs_by_park)),obs_by_park.observations.values)
ax.set_xticks(range(len(obs_by_park)))
ax.set_xticklabels(obs_by_park.park_name.values)
plt.ylabel('Number of Observations')
plt.title('Observations of Sheep per Week')
plt.show()

#Step 14: Foot and Mouth Reduction Effort - Sample Size Determination
baseline = 15
minimum_detectable_effect = 100*5./15
sample_size_per_variant = 870
yellowstone_weeks_observing = sample_size_per_variant/507.
bryce_weeks_observing = sample_size_per_variant/250.

#Step 15: Foot and Mouth Reduction Effort - Final Thoughts 