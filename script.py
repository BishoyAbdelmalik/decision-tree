import pandas as pd
from math import log2
from IPython.display import display
def entropy(df):
    last=df.columns[-1]
    all=float(len(df))
    y=float(len(df[df[last]==yes]))
    n=float(len(df[df[last]==no]))
    # print(f"{y} {n} {all}")
    positive=y/all
    negative=n/all
    entropy=-(positive)*log2((positive,1.0)[positive==0.0])-(negative)*log2((negative,1.0)[negative==0.0])
    entropy=(entropy,0.0)[entropy==0]
    return entropy
def information_gain(df,col):
    values=df[col].unique()
    entropyS=entropy(df)
    entropies={}
    for v in values:
        entropies[v]=entropy(df[df[col]==v])
        # print(f"entropy of {v} {entropies[v]}")
    gain=entropyS
    count=float(len(df))
    for v in values:
        sv=float(len(df[df[col]==v]))
        gain -=(sv/count)*entropies[v]
    return gain

if __name__ == "__main__":
    fname="data.csv"

    data= pd.read_csv(fname)
    col= list(data.columns[1:-1])
    yes="Y"
    no="N"

    m=-1
    root=""
    for c in col:
        g=information_gain(data,c)
        m=max(m,g)
        if m==g:
            root=c
        print(f"gain of {c} is {g}")
    print(f"root is {root}")
    subTrees=data[root].unique()
    print()
    print()
    for t in subTrees:
        sub=data[data[root]==t]
        print(t)
        display(sub)

        print()
        print()
        pure=""
        if len(sub[sub.columns[-1]].unique())==1:
            pure="-is pure"

        sub.drop([root], axis=1).to_csv(f"subtree-{t}{pure}.csv",index=False)
