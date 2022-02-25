package main

import (
	"math"
	. "vinamax"
)

func main() {
	Msat.Set(400e3)
	Alpha.Set(1.)
	M.Set(0, 0, 0.1)
	U_anis.Set(0, 0, 1)
	Viscosity.Set(1e-3)
	Ku1.Set(1e4)
	Temp.Set(310.)
	//for lognormal radius OR diameter
	for i := 0; i < 30; i++ {
		Rc.Set(30e-9)
		Rh.Set(30e-9)
		AddParticle(float64(i)*1.e-6, 0., 0.)
	}
	//Save("geometry")

	B_ext = func(t float64) (float64, float64, float64) {
		return 0., 0., 0.025 * math.Sin(2*math.Pi*t*25e3) //f = 25 kHz, T = 40 µs
	}

	BrownianRotation = true
	MagDynamics = true
	Demag = true
	T.Set(0.)
	SetSolver("dopri")
	Dt.Set(2e-10) //Solve in steps of 5 ns
	Adaptivestep = false
	Tablename = "alongx"
	Tableadd("B_ext")

	Output(1e-7) //100 datapoints per cycle
	Run(120e-6)  //run 3 cycles

}
