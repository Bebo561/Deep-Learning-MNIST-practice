The purpose of this project is to retrieve data from the MNIST datset, a dataset which contains tens of thousands of hand drawn images of integers between 0-9.
After first outputting the integers 0-9 into a neatly formatted subplot utilizing matplotlib, I then retrieved every value from the dataset that contained
the integers 0 and 8, and then outputted the first 10 images into subplots. I then created a function that would retrieve the average amount of values 
in the center 4x4 matrix of pixels in each image using Numpy functions, and then created two separate lists that held each corresponding digit and their
average center pixel count. I then used these lists to create a final graph that would format this information nicely for the developer to see, and 
then added a function that would take in a threshold for differentiating between the two digits. If the average pixel count was higher or equal to the threshold,
it would be counted as an 8, otherwise it would be counted as a 0. I then compared the thresholds accuracy with classifying the digits with multiple testing
sets, and then outputted the accuracy percentage to the screen, and asked the user if they would like to input another threshold to test.
