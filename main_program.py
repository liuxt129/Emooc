from face_detect import analyze_image
from camera_capture import capture_image
import matplotlib.pyplot as plt
total_time = int(input("total time in seconds: "))

assert total_time > 9

capture_image(total_time, 2)


x, y = analyze_image()
print(x)
print(y)



# plotting the points
plt.plot(x, y)

# naming the x axis
plt.xlabel('Time Elapsed (/10s)')
# naming the y axis
plt.ylabel('Difficulty Level')

# giving a title to my graph
plt.title('The Difficult Level of the Course')

# function to show the plot

plt.savefig('result.png')
plt.show()