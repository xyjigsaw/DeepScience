# DeepScience

In this repo, we choose the domain of **COVID-19** and **deep learning** to predict the trends of the science of science. 
It is worth noting that we have also collected papers from the whole academia consisting of 19 subjects (Mathematics, History, Psychology, Economics, Sociology, Art, Geography, Business, Physics, Political science, Philosophy, Biology, Computer science, Materials science, Environmental science, Medicine, Chemistry, Engineering, and Geology) and 292 sub-fields (sub-subjects). 

To predict the academic trends, we construct a field graph based on citations among papers. Specifically, the papers we crawled have been labeled with fields. Each paper may belong to several fields. We use citation information to link these fields. For example, paper $P_1$ belongs to field $F_1$ and $F_2$, paper $P_2$ belongs to field $F_2$ and $F_3$, also, $P_1$ cites $P_2$. Then, we add edges $(F_1, F_2)$, $(F_1, F_3)$, $(F_2, F_2)$ and $(F_2, F_3)$, and the weight of each edge is the total number of citations in terms of fields. 

We generate the dynamic field graph day by day ranging from January 1, 2020, to March 31, 2021 (456 days) for COVID-19. As to deep learning, the time range is from October 1, 2017 to  March 31, 2021. Finally, the dynamic field graph is constructed, and we called it the COVID-19 (Deep Learning) academic graph.

You can download these two datasets from [Google Drive](https://drive.google.com/drive/folders/11GArAGnx655sOrDBPm5BwKH-eDsUJvQX?usp=sharing).
