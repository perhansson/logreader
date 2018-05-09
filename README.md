# logreader

# Requirements:
- python3
- numpy
- matplotlib
- pandas

Recommend to install anaconda.

Tested with:
- Python 3.5.5 
- IPython 6.3.1
- numpy 1.14.2

# Run example script.
Navigate to directory holding the example script in terminal. 
```
python example.py path_to_log_file
```


# Interactive use from iPython terminal
```
import matplotlib.pyplot as plt
import Reader
logfile = Reader.LogFileType1("/Users/phansson/work/climeon/logging/data/Datalog_2018_05_03_01_00_02.csv")
logfile.df.between_time('10:00','13:00')["T33 [deg C]"].plot() # plot T33 temperature between specific times
plt.show()
```
