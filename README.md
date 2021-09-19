# Virtual-Painter

<img src="https://github.com/keerthan657/Virtual-Painter/blob/main/gif_large.gif" width="800" height="500" />

This is a virtual drawing application developed in Python using OpenCV.

<hr>

An object like a laser-pointer or any bright coloured thing is needed to track movement. Depending on the object, certain threshold needs to be set.
This threshold is defined in variables - lowerThresh and upperThresh in file:"final3.py"
The threshold values need to be calculated using another python script - "color_range.py"
We need to make an appropriate guess and do some bruteforce testing to get the right threshold, but it should work for most cases
(given that background is not that noisy and an appropriate light-level is maintained in the room)
IMP: test threshold values with the lighting conditions of the room, and not somewhere else
Keep adjusting sliders as shown in the below image, until we get only our pointer object as white, and remaining else as black
![image](https://user-images.githubusercontent.com/62998415/133929062-6ce090b4-fd52-4d16-b352-9880a5a29469.png)
Some spots might remain, we can fix them by adjusting the number of iterations done on dilating and eroding the image in "final3.py"

<hr>

Here are the keyboard inputs:
<div>
q - exit
</div>
<div>
a - clear entire canvas
</div>
<div>
r - red coloured line
</div>
<div>
g - green coloured line
</div>
<div>
b - blue coloured line
</div>
