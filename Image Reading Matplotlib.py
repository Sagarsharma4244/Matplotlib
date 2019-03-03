import matplotlib.image as mp_image
filename = "keras.jpg"
input_image = mp_image.imread(filename)

print(input_image)
import matplotlib.pyplot as plt
plt.imshow(input_image)
plt.show()