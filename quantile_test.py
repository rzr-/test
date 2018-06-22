import matplotlib.pyplot as plt
import numpy as np
from   sklearn.preprocessing import QuantileTransformer

def plot_data (X, X_quantile, X_quantile_ref):
	fig = plt.figure(figsize=(10,6.5))
	fig.subplots_adjust(wspace=0.6, hspace=0.35)

	ax1 = fig.add_subplot(321, title="Signal", ).plot(X)
	ax2 = fig.add_subplot(322, title="Signal's after QT").plot(X_quantile)
	ax3 = fig.add_subplot(323, title="Signal's histogram").hist(X)
	ax4 = fig.add_subplot(324, title="Signal's histogram after QT").hist(X_quantile)

	#histogram of sample when bulk-transformed with other samples
	ax6 = fig.add_subplot(326, title="Signal's histogram in reference file").hist(X_quantile_ref)
	
	fig.savefig('before_after.png', transparent=False)
	plt.show()


# 138 samples, raw signal
signals = np.genfromtxt('data/signals.csv', delimiter=',')
# 138 samples, Quantile-transformed using QT.fit_transform(signals)
signals_QT = np.genfromtxt('data/signals_quantile.csv', delimiter=',')

#transform single random sample
QT        = QuantileTransformer()
rand      = np.random.randint(low=0, high=len(signals)-1)
X_rand_QT = QT.fit_transform(signals[rand][:, np.newaxis])

plot_data (signals[rand], X_rand_QT, signals_QT[rand])