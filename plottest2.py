import matplotlib.pyplot as plt
import numpy as np

#labels=['Fingers straight', 'Fist','Wrist straight','Wrist bend','Pinch grip','Hook grip','"I love you"','Thumb up','Wrist adduction','"Telephone"','Wrist abduction','Middle$ring straight, thumb,index&pinky bend']
labels = ['1','2','3','4','5','6','7','8','9','10','11','12']
markers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
str_markers = ["10", "20", "30", "40", "50", "60"]

def make_radar_chart(name, stats, attribute_labels = labels, plot_markers = markers, plot_str_markers = str_markers):

    labels = np.array(attribute_labels)

    angles = np.linspace(0, 2*np.pi, len(labels), endpoint=False)
    stats = np.concatenate((stats,[stats[0]]))
    angles = np.concatenate((angles,[angles[0]]))

    fig= plt.figure()
    ax = fig.add_subplot(111, polar=True)
    ax.plot(angles, stats, 'o-', linewidth=2)
    ax.fill(angles, stats, alpha=0.1)
    ax.set_thetagrids(angles * 180/np.pi, labels)
    plt.yticks(markers)
    ax.set_title(name)
    ax.grid(True)

    fig.savefig("%s.png" % name)

    return plt.show()

make_radar_chart("Classification_result", [0,0,0,0,0,0,0,0,0,0,10,90]) # example

