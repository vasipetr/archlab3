import matplotlib.pyplot as plt
#specbzip
# Cache Line Size
x1 = [32,64,128]
y1 = [7.07233, 9.24063, 25.80104]
plt.plot(x1, y1, label = "Area")
 
x2 = [32,64,128]
y2 = [2.12765, 3.65447, 7.9813]
plt.plot(x2, y2, label = "Peak Power")
 
plt.xlabel('Cache Line Size (KB)')
plt.title('Area/Peak Power vs Cache Line Size')
plt.legend()
plt.show()
#L1 Associativity
x1 = [1, 2, 4, 8]
y1 = [9.24063, 9.31363, 8.94041, 10.08718]
plt.plot(x1, y1, label = "Area")
 
x2 = [1, 2, 4, 8]
y2 = [3.65447, 3.68941, 3.82721, 4.42659]
plt.plot(x2, y2, label = "Peak Power")
 
plt.xlabel('L1 Associativity')
plt.title('Area/Peak Power vs L1 Associativity')
plt.legend()
plt.show()
#L1 Dcache
x1 = [32, 64, 128]
y1 = [6.61289, 9.24063, 11.80212]
plt.plot(x1, y1, label = "Area")
 
x2 = [32, 64, 128]
y2 = [2.75792, 3.65447, 4.14478]
plt.plot(x2, y2, label = "Peak Power")
 
plt.xlabel('L1 Dcache (KB)')
plt.title('Area/Peak Power vs L1 Dcache')
plt.legend()
plt.show()
#L1 Icache
x1 = [32, 64, 128]
y1 = [9.24063, 11.62949, 13.9581]
plt.plot(x1, y1, label = "Area")
 
x2 = [32, 64, 128]
y2 = [3.65447, 4.67857, 5.2115]
plt.plot(x2, y2, label = "Peak Power")
 
plt.xlabel('L1 Icache (KB)')
plt.title('Area/Peak Power vs L1 Icache')
plt.legend()
plt.show()
#L2 Cache
x1 = [512, 2048, 4096]
y1 = [9.240632, 14.84274, 20.02923]
plt.plot(x1, y1, label = "Area")
 
x2 = [512, 2048, 4096]
y2 = [3.65447, 3.82998, 3.95297]
plt.plot(x2, y2, label = "Peak Power")
 
plt.xlabel('L2 cache (KB)')
plt.title('Area/Peak Power vs L2 cache')
plt.legend()
plt.show()
#L2 Associativity
x1 = [1, 2, 4, 8]
y1 = [9.24155, 9.24063, 9.23934, 9.27738]
plt.plot(x1, y1, label = "Area")
 
x2 = [1, 2, 4, 8]
y2 = [3.65443, 3.65447, 3.65474, 3.65612]
plt.plot(x2, y2, label = "Peak Power")
 
plt.xlabel('L2 Associativity')
plt.title('Area/Peak Power vs L2 Associativity')
plt.legend()
plt.show()



