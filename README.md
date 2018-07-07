# Flash-no-Flash
The code enhances the appearance of photographs shot in dark environments by combining a picture taken with the available light and one taken with the flash. It preserve the ambiance of the original lighting and insert the sharpness and along with decreasing noise.


## Getting Started
The function takes 2 images of the same scene as the input one using flash and other without flash and outputs a new image 'result.jpg' with denoised and a more sharp scene.


## Prerequisites
- Numpy
- OpenCV


## Arguments
- img1 - location/name of the flash image
- img2 - location/name of the non-flash image
- d - size of neighbourhood for gaussian filtering. (use -1 for default value)
- sig_col - Filter sigma in the color space. A larger value of the parameter means that farther colors within the pixel neighborhood will be mixed together. (use -1 for default value)
- sigma - Filter sigma in the coordinate space. A larger value of the parameter means that farther pixels will influence each other as long as their colors are close enough. (use -1 for default value)


## References
- Elmar Eisemann , Frédo Durand, Flash photography enhancement via intrinsic relighting, ACM Transactions on Graphics (TOG), v.23 n.3, August 2004
- Georg Petschnigg, Richard Szeliski, Maneesh Agrawala, Michael Cohen, Hugues Hoppe, and Kentaro Toyama. 2004. Digital photography with flash and no-flash image pairs. ACM Trans. Graph. 23, 3 (August 2004), 664-672. DOI: https://doi.org/10.1145/1015706.1015777
- Sylvain Paris , Pierre Kornprobst , Jack Tumblin , Frédo Durand, A gentle introduction to bilateral filtering and its applications, ACM SIGGRAPH 2007 courses, August 05-09, 2007, San Diego, California  [doi>10.1145/1281500.1281602]
