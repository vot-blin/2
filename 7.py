import sys
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv(r'C:\Users\User\Downloads\Telegram Desktop\test-2.csv')
s = ["The dead", "Survivors "]
explode = (0.05, 0.05)
df.groupby(['Sex']).sum().plot(kind='pie', y="Survived", autopct='%1.0f%%' , explode=explode, shadow= True)
plt.pie(explode, labels = s)
plt.show()
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()

import sys
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv(r'C:\Users\User\Downloads\Telegram Desktop\test-2.csv')
color=['hotpink' if value == 0 else 'purple'for value in df['Survived']]
plt.scatter(df.Age, df.Fare, color=color)
plt.xlabel('Age')
plt.ylabel('Fare')
plt.show()
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
