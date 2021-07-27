from miscSupports import chunk_list, flatten, load_yaml
from stataLogObject import StataExtractor
from pyBlendFigures import BlendFigure
from csvObject import write_csv
from pathlib import Path

# Set the working directory and convert the log into an object
env = load_yaml(Path(Path(__file__).parent.parent, "env.yaml"))

LOG_DIR = env["LOG_DIR"]
FIGURE_DIR = env["BLEND_FIGURE_DIR"]

# Setup spacing parameters for forest plots
spacer = 3
spacing = [["#Delete", 0, 0, 0] for _ in range(spacer)]
front = [["#Delete", 0, 0, 0] for _ in range(4)]

# Extract the stata logs
tables_cont = StataExtractor(Path(LOG_DIR, "Averages.log"))
tables_cont.censure_log()
summary = StataExtractor(Path(LOG_DIR, "Summary.log"))
summary.censure_log()
tab = StataExtractor(Path(LOG_DIR, "Tab.log"))
tab.censure_log()

# Write out the summary tables
summary.sum_tables[0].write_csv(FIGURE_DIR, "SummaryStats")

# We have three value sets, average by age 1, 5 and 10. So chunk the list into those groups
outcome_models = chunk_list(tables_cont.hdfe_tables, 3)
phenotype_list = ["Rheumatic disease", "Vascular", "AMI", "IHD", "Stroke", "CVD", "Education Years",
                  "Fluid Intelligence"]

diseases = []
stand = []
for i in range(3):
    tables = []
    for pheno, table in zip(phenotype_list, outcome_models):
        tables.append([pheno] + table[i].format_for_forest(as_csv=False)[0][1:])

    # Rebase decimal percentage to RD
    diseases.append([[t[0]] + [v * 100 for v in t[1:]] for t in tables[:-2]])
    if i < spacer - 1:
        diseases.append(spacing)

    stand.append(front)
    stand.append(tables[-2:])
    if i < spacer - 1:
        stand.append(spacing)

write_csv(FIGURE_DIR, "DiseasesRD", ["Phenotype", "Coefficient", "Lower_Bound", "Upper_Bound"], flatten(diseases))
write_csv(FIGURE_DIR, "Standard", ["Phenotype", "Coefficient", "Lower_Bound", "Upper_Bound"], flatten(stand))

# Setup blendFigure
figure = BlendFigure(env["BLEND_PATH"], FIGURE_DIR)

# Plot the figures
figure.forest_plot(Path(FIGURE_DIR,  "DiseasesRD.csv"), "DiseasesRD", 0.05, 0.005, "RD per 100(95%CI)",
                   axis_label="Risk Difference", rounder=2)
figure.forest_plot(Path(FIGURE_DIR, "Standard.csv"), "Standard", 0.05, 0.005, "RD per 100(95%CI)",
                   axis_label="Standard Deviation Change", rounder=2)

# Plot the Prisma plot
figure.prisma_plot("Prisma", Path(FIGURE_DIR, "Prisma.yaml"), x_resolution=1080*2, y_resolution=1920*2)
