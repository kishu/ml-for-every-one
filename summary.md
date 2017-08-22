# Linear Regression

![](http://latex.codecogs.com/gif.latex?%5Cdpi%7B150%7D%20%5CLARGE%20H%28x%29%20%3D%20Wx%20&plus;%20b)

![](http://latex.codecogs.com/gif.latex?%5Cdpi%7B150%7D%20%5CLARGE%20cost%28W%2C%20b%29%20%3D%20%5Cfrac%7B1%7D%7Bm%7D%28H%28x%5E%7B%28i%29%7D%29%20-%20y%5E%7B%28i%29%7D%29%5E2)

![](http://latex.codecogs.com/gif.latex?%5Cdpi%7B120%7D%20%5Chuge%20W%20%3A%3D%20W%20-%20a%5Cfrac%7B%5Cpartial%7D%7B%5Cpartial%20W%7Dcost%28W%29)

---

# Multi Variable Linear Regression

![](http://latex.codecogs.com/gif.latex?%5Cinline%20%5Cdpi%7B150%7D%20%5CLARGE%20H%28x_1%2C%20x_2%2C%20...%2C%20x_n%29%20%3D%20W_1x_1%20&plus;%20W_2x_2%20&plus;%20...%20&plus;%20W_nx_n%20&plus;%20b)

![](http://latex.codecogs.com/gif.latex?%5Cdpi%7B150%7D%20%5Clarge%20cost%28W%2C%20b%29%20%3D%20%5Cfrac%7B1%7D%7Bm%7D%5Csum_%7Bm%7D%5E%7Bi%3D1%7D%28H%28x_1%5E%7B%28i%29%7D%2C%20x_2%5E%7B%28i%29%7D%2C%20...%2C%20x_n%5E%7B%28i%29%7D%29%20-%20y%5E%7B%28i%29%7D%29%5E2)

![](http://latex.codecogs.com/gif.latex?%5Cdpi%7B150%7D%20%5Clarge%20%5Cbegin%7Bpmatrix%7D%20x_1%5C%5C%20x_2%5C%5C%20...%5C%5C%20x_n%20%5Cend%7Bpmatrix%7D%20%5Cbegin%7Bpmatrix%7D%20w_1%26w_2%26...%26w_n%20%5Cend%7Bpmatrix%7D%20&plus;%20b)

![](http://latex.codecogs.com/gif.latex?%5Cdpi%7B150%7D%20%5Chuge%20H%28X%29%20%3D%20XW%20&plus;%20b)

![](http://latex.codecogs.com/gif.latex?%5Cdpi%7B120%7D%20%5Chuge%20W%20%3A%3D%20W%20-%20a%5Cfrac%7B%5Cpartial%7D%7B%5Cpartial%20W%7Dcost%28W%29)

---

# Logistic Regression

![](http://latex.codecogs.com/gif.latex?%5Cdpi%7B120%7D%20%5Chuge%20z%20%3D%20Wx%20&plus;%20b)

![](http://latex.codecogs.com/gif.latex?%5Cdpi%7B120%7D%20%5Chuge%20g%28z%29%20%3D%20%5Cfrac%7B1%7D%7B%281&plus;e%5E%7B-z%7D%29%7D)

![](http://latex.codecogs.com/gif.latex?%5Cdpi%7B120%7D%20%5Chuge%20H%28X%29%20%3D%20%5Cfrac%7B1%7D%7B1%20&plus;%20e%5E%7BW%5EtX%7D%7D)

![](http://latex.codecogs.com/gif.latex?%5Cdpi%7B120%7D%20%5Chuge%20cost%28W%29%20%3D%20%5Cfrac%7B1%7D%7Bm%7D%5Csum_%7Bi%3D1%7D%5E%7Bm%7Dc%28H%28x%29%2C%20y%29)

![](http://latex.codecogs.com/gif.latex?%5Cdpi%7B120%7D%20%5Chuge%20c%28H%28x%29%2C%20y%29%20%3D%20%5Cleft%5C%7B%5Cbegin%7Bmatrix%7D%20-log%28H%28x%29%29%26%26%3Ay%20%3D%201%5C%5C%20-log%281-H%28x%29%29%26%26%3Ay%20%3D%200%20%5Cend%7Bmatrix%7D%5Cright.)

![](http://latex.codecogs.com/gif.latex?%5Cdpi%7B150%7D%20%5Clarge%20C%28H%28x%29%2C%20y%29%20%3D%20ylog%28H%28x%29%29%20-%20%281%20-%20y%29log%281%20-%20H%28x%29%29)
