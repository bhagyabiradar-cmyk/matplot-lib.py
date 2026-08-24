import pandas as pd

joint = pd.DataFrame(
    [[0.2, 0.3],
     [0.1, 0.4]],
    index=["X=0", "X=1"],
    columns=["Y=0", "Y=1"]
)

print(joint)