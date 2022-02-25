package main

import (
	"fmt"
	"math"
	. "vinamax"
)

func main() {
	Temp.Set(310.)
	//Define Particles
	Msat.Set(400e3)
	Alpha.Set(0.1)
	M.Set(1, 0, 0)
	U_anis.Set(1, 0.2, 0) //Small elevation to start torque along x-axis
	Viscosity.Set(1e-3)
	Ku1.Set(1e4)
	r := 30e-9
	Rc.Set(r)
	Rh.Set(r)

	G = 5
	A = 12e-3
	X_scan = 2.4e-3

	samplepoints := 50
	k := 1
	center := -X_scan + 2*float64(k)/float64(samplepoints)*X_scan
	fmt.Print(center)

	MNPs := 50 //add MNPS particles to the left and to the right of the center position
	//2*MNPs+1 particles along chain

	//ad particles along chain
	AddParticle(center, 0., 0.)
	for i := 1; i <= MNPs; i++ {
		AddParticle(center+float64(i)*61e-9, 0., 0.)
		AddParticle(center-float64(i)*61e-9, 0., 0.)
	}

	Runtime = 160e-6

	B_ext_space = func(t, x, y, z float64) (float64, float64, float64) {
		return G*x - A*math.Cos(2*math.Pi*t*25e3), 0., 0.
	}
	BrownianRotation = true
	MagDynamics = true
	Demag = false
	Errortolerance = 1e-3
	Adaptivestep = false
	SetSolver("dopri")
	T.Set(0.)
	Dt.Set(1.6e-10)

	Coil_Locations = append(Coil_Locations, 200e-3)
	Coil_Locations = append(Coil_Locations, -200e-3)
	Coil_Average = false

	//Tableadd("B_ext_space")
	//Tableadd("FFP")
	Tableadd("Dt")

	for i := range Coil_Locations {
		Tableadd_b_at_location(Coil_Locations[i], 0., 0.)
	}

	Tablename = fmt.Sprintf("%0.FMNPs_of_radius%.0f_@%.3fmm", 2*float64(MNPs)+1, r*1e9, center*1e3)
	Output(1.6e-7)
	Run(Runtime)
}
