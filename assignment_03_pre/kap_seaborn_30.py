import subprocess as sb
from time import time
sb.run("cls", shell=True)
#
# Theme & convention
#
'''
import seaborn as sns
import matplotlib.pyplot as plt
#
sns.set_theme(style="whitegrid", palette="mako")
plt.figure(figsize=(5, 0.5))
plt.title("Theme set ✓")
plt.axis("off")
plt.show()
'''
#
# Distribution — histplot & kdeplot
#
'''
import seaborn as sns, numpy as np, matplotlib.pyplot as plt
sns.set_theme(style="whitegrid")
#
x = np.random.default_rng(0).normal(75, 12, 500)
plt.figure(figsize=(6, 3.5))
sns.histplot(x, bins=20, kde=True, color="#0f766e")
plt.title("Score distribution with KDE")
plt.tight_layout()
plt.show()
'''
#
# Categorical — boxplot
#
'''
import seaborn as sns, pandas as pd, matplotlib.pyplot as plt
sns.set_theme(style="whitegrid")
#
df = pd.read_csv("sales.csv", sep="\t")
plt.figure(figsize=(6, 3.5))
sns.boxplot(data=df, x="City", y="Revenue", hue="City", palette="mako", legend=False)
plt.title("Revenue spread by city")
plt.tight_layout()
plt.show()
'''
# 
# Categorical — barplot with hue
#
'''
import seaborn as sns, pandas as pd, matplotlib.pyplot as plt
sns.set_theme(style="whitegrid")

df = pd.read_csv("sales.csv", sep="\t")
plt.figure(figsize=(6, 3.5))
sns.barplot(data=df, x="City", y="Revenue", hue="Product", palette="mako")
plt.title("Revenue by City and Product")
plt.tight_layout()
plt.show()
'''
#
# Relationship — scatter + regression
#
'''
import seaborn as sns, pandas as pd, matplotlib.pyplot as plt
sns.set_theme(style="whitegrid")

df = pd.read_csv("sales.csv", sep="\t")
plt.figure(figsize=(6, 3.5))
sns.regplot(data=df, x="Units_Sold", y="Revenue", color="#0f766e",
            scatter_kws={"alpha": 0.7})
plt.title("Units vs Revenue (with regression line)")
plt.tight_layout()
plt.show()
'''
#
# Heatmap — correlation matrix
#
'''
import seaborn as sns, pandas as pd, matplotlib.pyplot as plt
sns.set_theme()

df = pd.read_csv("sales.csv", sep="\t")
corr = df[["Units_Sold", "Revenue"]].corr()

plt.figure(figsize=(4, 3))
sns.heatmap(corr, annot=True, cmap="mako", fmt=".2f")
plt.title("Correlation")
plt.tight_layout()
plt.show()
'''
#
# Pairplot — multi-variable overview
#
'''
import seaborn as sns, pandas as pd, matplotlib.pyplot as plt
sns.set_theme(style="whitegrid")

df = pd.read_csv("sales.csv", sep="\t")
g = sns.pairplot(df, vars=["Units_Sold", "Revenue"], hue="City",
                 palette="mako", height=2.2)
g.fig.suptitle("Pairwise relationships", y=1.02)
plt.tight_layout()
plt.show()
'''

# Next: assignment_03_pre/kap_seaborn_40.py
# https://colab.research.google.com/drive/16z8l7CYJIUwcAw01BtxpRqlq19jkPgF7
#'''
#import numpy as np
