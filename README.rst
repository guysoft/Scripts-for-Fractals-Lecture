Scripts for a Lecture On Fractals
=================================
Guy Sheffer guy.sheffer at mail.huji.ac.il

These scripts were written for a lecture i gave on fractals during a seminar in Chaos and Dynamical systems given by Prof. Baruch Meerson.

It took me a while to figure out how to calculate the correlation dimension of the logistic map, and since all other work I found online was not as accurate (or in many cases completely wrong) I thought I might publish this.

Scripts in the project:

 #. ``logistic_map_dim.py`` - Calculates the correlation dimension of the logistic map Based on `Measuring the strangeness of strange attractors <http://www.sciencedirect.com/science/article/pii/0167278983902981>`_ and "Chaos in Dynamical Systems: Edward Ott" page 90-91.
 #. ``sierpinski_gasket_animation/sierpinski_gasket_animation.py`` - Generated the Sierpinski gasket fractal, with a cute cat as the base (image can be changed).
 #. ``not_shown_in_lecture/logistic_map_plot.py`` - plots the logistic map.
 #. ``not_shown_in_lecture/feigenbaum_function_zoom.py`` - Generates images of the Feigenbaum Function, images can be assembled to create a zoom in map.