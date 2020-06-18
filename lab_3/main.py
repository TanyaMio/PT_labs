from scipy.optimize import fsolve
import math, random

global ri
global rj
global yfinish
global ydown
global xroot
global gxi

def fx(xi):
    xi = float(xi)
    if xi >= -1 and xi <= 1:
        res = (2*xi*math.sqrt(1-pow(xi,2))+pow(xi,3)*math.log((1-math.sqrt(1-pow(xi,2)))/(1+math.sqrt(1-pow(xi,2))))/2+math.asin(xi))/math.pi+0.5-float(ri)
    else: res = 2
    return res

def fy(yi):
    yi = float(yi)
    if yi >= -xroot and yi <= xroot:
        xyroot = math.sqrt(pow(gxi,2)+pow(yi,2))
        res = (xroot-yi*(xyroot-2)+pow(gxi,2)*math.log((1-xroot)/(yi+xyroot)))/ydown-float(rj)
    else: res = 2
    return res

tmx = 0.0
tmy = 0.0
tdx = 0.15
tdy = 0.15
tsx = math.sqrt(tdx)
tsy = math.sqrt(tdy)
tcov = 0
tro = 0

print("Theory:\n\nmx = ", tmx, "\nmy = ", tmy, "\n\ndx = ", tdx, "\tsigmaX = ", tsx, "\ndy = ", tdy, "\tsigmaY = ", tsy, "\n\ncov = ", tcov, "\nro = ", tro)
print("\n\nCalculating experimental values...")

x = []
y = []
random.seed()
n = 1000

mx = 0
my = 0
for i in range(n):
    ri = random.uniform(0.0, 1.0)
    gxi = fsolve(fx, -1)[0]
    x.append(gxi)
    mx += gxi
    xroot = math.sqrt(1-pow(gxi,2))
    ydown = 2*xroot+pow(gxi,2)*math.log((1-xroot)/(1+xroot))
    rj = random.uniform(0.0, 1.0)
    gyi = fsolve(fy, 0)[0]
    y.append(gyi)
    my += gyi

print("\nExperiment:")

mx /= n
my /= n
print("\nmx = ", mx, "\nmy = ", my)

dx = 0
for elx in x:
    dx += pow((elx-mx), 2)

dx /= n
sx = math.sqrt(dx)
print("\ndx = ", dx, "\tsigmaX = ", sx)

dy = 0
for ely in y:
    dy += pow((ely-my), 2)

dy /= n
sy = math.sqrt(dy)
print("dy = ", dy, "\tsigmaY = ", sy)

cov = 0
for i in range(1000):
    cov += (x[i]-mx)*(y[i]-my)

cov /= n
print("\ncov = ", cov)

ro = cov/(sx*sy)
print("ro = ", ro)
