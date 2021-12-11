import numpy as np
import matplotlib.pyplot as plt

def main():
    x = np.array(np.arange(0,4*np.pi,.02))
    y = np.array([np.sin(t1) for t1 in x])

    y1 = np.array([1.8*np.sin(t1*2 + np.pi/3) for t1 in x])
    y2 = np.array([3.4*np.sin(t1/1.4 + np.pi/2) for t1 in x])

    y3 = y + y1 + y2
    # y3 = np.array([y3[i] * np.sin(x[i]*5) for i in range(len(x))])

    ycar = np.array([10*np.sin(t1*20) for t1 in x])
    y3max = max(y3)

    yampmod = []
    for i in range(len(x)):
        yampmod.append((y3[i] + 10) * np.sin(x[i]*20))

    yampmod = np.array(yampmod)


    ydemod = []
    for i in range(len(x)):
        ydemod.append(yampmod[i] / np.sin(x[i]*20) - 10 + 10)

    ydemod = np.array(ydemod)

    ydemod1 = (ydemod - 10)
    
    fig, axes = plt.subplots(nrows=2, ncols=2)

    # plot signal
    axes[0,0].plot(x,y3,c="blue")
    axes[0,0].set_title("Signal Wave")

    # plot carrier wave
    axes[0,1].plot(x,ycar,c="red")
    axes[0,1].set_title("Carrier Wave")

    # plot modulated signal
    axes[1,0].plot(x,yampmod,c="purple")
    axes[1,0].plot(x,ydemod)
    axes[1,0].plot(x,-1*ydemod)
    axes[1,0].set_title("Modulated Signal")

    # plot demodulated signal
    axes[1,1].plot(x,ydemod1,c="green")
    axes[1,1].set_title("Demodulated Signal")

    for row in axes:
        for ax in row:
            ax.grid()
            ax.set_yticks(range(-15,16,5))
            ax.set_ybound(lower=-17,upper=17)

    # fig.savefig("test.png")
    plt.show()

    # print("hello world")
    

if __name__ == "__main__":
    main()