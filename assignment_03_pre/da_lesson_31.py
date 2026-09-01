import subprocess
# Clear screen on Windows
subprocess.run("cls", shell=True)

import numpy as np

# A class is a blueprint — you define it once, use it many times
class DataPipeline:

    def __init__(self, label):
        # __init__ runs automatically when you create a new object
        self.label = label   # the name you give this pipeline run
        self.data  = None    # will hold the DataFrame after loading
        self.steps = ['DataPipeline Created']      # keeps a log of what has been done

    def __repr__(self):
        # __repr__ controls what prints when you type the object's name
        n = len(self.data) if self.data is not None else 0
        self.steps.append('repr called')
        return f"DataPipeline('{self.label}', rows={n}, steps={self.steps})"
    def __len__(self):
        return len(self.data) if self.data is not None else 0
    def load(self, dataframe):
        self.data = dataframe.copy()   # work on a copy — never touch the original
        self.steps.append("load")
        return self   
    def clean_names(self):
        self.data["name"] = [n.strip().title() for n in self.data["name"]]
        self.steps.append("clean_names")
        return self
    def add_avg_score(self):
        cols = ["maths", "science", "english", "history", "pe"]
        self.data["avg_score"] = self.data[cols].mean(axis=1).round(1)
        self.steps.append("avg_score")
        return self
    def add_grade(self):
        self.data["grade"] = pd.cut(
            self.data["avg_score"],
            bins=[0, 40, 55, 70, 85, 100],
            labels=["Fail", "D", "C", "B", "A"]
        )
        self.steps.append("grade")
        return self

    def flag_at_risk(self):
        # At-risk: attendance below 75% OR average score below 40
        self.data["at_risk"] = (
            (self.data["attendance"] < 75) | (self.data["avg_score"] < 40)
        )
        self.steps.append("flag_at_risk")
        return self
    @property
    def pass_rate(self):
        return round((self.data["avg_score"] >= 40).mean(), 3)

    @property
    def at_risk_count(self):
        return int(self.data["at_risk"].sum())
'''
# Create an object from the blueprint — calls __init__ automatically
p = DataPipeline("Term 1")
print(p)   # calls __repr__ automatically

# Term 1
pipe = DataPipeline("Term 1").load(term1_data).clean().enrich()

# Term 2 — same code, new data
pipe = DataPipeline("Term 2").load(term2_data).clean().enrich()
'''
# Create the school dataset — 300 students, 5 subjects
np.random.seed(42)   # seed makes random numbers reproducible
N = 300

raw_df = pd.DataFrame({
    "student_id":  [f"S{i:04d}" for i in range(N)],
    "name":        [f"  student_{i}  " for i in range(N)],   # messy names (spaces)
    "class":       np.random.choice(["10A","10B","10C","11A","11B"], N),
    "gender":      np.random.choice(["Male","Female"], N),
    "maths":       np.random.randint(20, 100, N),
    "science":     np.random.randint(20, 100, N),
    "english":     np.random.randint(20, 100, N),
    "history":     np.random.randint(20, 100, N),
    "pe":          np.random.randint(40, 100, N),
    "attendance":  np.random.randint(55, 100, N),
    "term":        np.random.choice(["T1","T2","T3"], N),
})

# Run the entire pipeline in ONE chained expression
# Each method returns self, so you can keep chaining
pipe = (DataPipeline("2024 Annual")
        .load(raw_df)
        .clean_names()
        .add_avg_score()
        .add_grade()
        .flag_at_risk())

print(pipe)
print(f"Pass rate:     {pipe.pass_rate:.1%}")
print(f"At-risk count: {pipe.at_risk_count}")

# Look at what the pipeline produced
pipe.data[["name","class","avg_score","grade","at_risk"]].head(5)
