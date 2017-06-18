# -*- coding: utf-8 -*-

#Database of specific energy of some fuels etc.:
#Simple compounds:
e_Carbon_CO2 = 32.8
e_Carbon_CO = 22.7
e_Methane = 55.5
e_Methanol = 22.7
e_Nitromethane = 11.6
e_Ethanol = 29.7
e_Propane = 50.3
e_Octane = 47.9
e_Hydrogen = 142
e_Sulfur = 9.16
#Fossil fuels:
e_Anthracite = 32.6
e_Bituminous = 28.5
e_Sub_bituminous = 21.9
e_Lignite = 17.0
e_Diesel = 45.3
e_Gasoline_car = 45.8
e_Gasoline_plane = 43.1
e_Jet_a = 43.3
e_Jet_b = 43.5
e_Kerosene = 46.3
#Foods:
e_Carbonhydrates = 17.2
e_Fats = 38.9
e_Proteins = 17.2
#Explosives:
e_ANFO = 6.3
e_C4 = 6.3
e_Dynamite = 7.5
e_Gunpowder = 3.0





print("What do you want to calculate")
print("Press 1 to calculate the nuclear energy")
print("2: for the kinetic energy")
print("3: for the energy form gravity")
print("4: for the energy delivered by a spring")
print("5: for the energy delivered by a windwill")
print("6: for the chemical energy")
#Room for more formulae

#The choice and its consequences
choice = input ("Choose the formula you need and fill in its corresponding number")

if choice == 1:
	m = input ("Fill in the mass in kilogram:")
	c = 299792458
	E = m * c ** 2
	re = 1

elif choice == 2:
	m = input ("Fill in the mass in kilograms:")
	v = input ("Fill in the speed in meters per second(If unknown type -1):")
	if v == -1:
		dx = input ("Fill in the change in distance in meters(If unknown type -1):")
		dt = input ("Fill in the change of time during the motion in seconds:")
		v = dx / dt 
		if dx == -1:
			a = input ("Fill in the acceleration:")
			dt = input ("Fill in the change of time during the motion in seconds:")
			v = a * dt
	E = 0.5 * m * v **2
	re = 1

elif choice == 3:
	m = input ("Fill in the mass in kilogram:")
	g = 9.86
	h = input ("Fill in the hight in meters:")
	E = m * g * h
	re = 1

elif choice == 4:
	C = input ("Fill in the spring constant:")
	u = input ("Fill in the distance of the spring's stretch in meters:")
	E = 0.5 * C * u ** 2

elif choice == 5:
	rho = 1.29
	A = input ("Fill in the area of the circle the rotors make in square meters (if unknown type -1):")
	v = input ("Fill in the speed of the wind in meters per second")
	if A == -1:
		r = input ("Fill in the radius/length of the rotors:")
		pi = 3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067982148086513282306647093844609550582231725359408128481117450284102701938521105559644622948954930381964428810975665933446128475648233
		A = pi * r ** 2
	P = 0.5 * rho * A * v ** 3
	re = 2

elif choice == 6:
	e = input ("Fill in the specific energy of the fuel in mega joules per kilogram:")
	m = input ("Fill in the mass of the fuel in kilograms:")
	E = e * m 
	re = 1

#Room for more formulae
else:
	print("Congrats, you have chrashed the program;")
	print("You should have filled in a number between one and six.") #Change if more formulae are added
	print("Bloody hell, it isn't that hard, is it?")
	re = 0

if re == 1:
	print (E)
elif re == 2:
	print (P)
	dt = input ("Fill in the change of time during the proces:")
	E = P * dt 
	print (E)