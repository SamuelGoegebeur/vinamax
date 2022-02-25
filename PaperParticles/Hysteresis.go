package main

import (
	"math"
	"math/rand"
	. "vinamax"
)

var rng = rand.New(rand.NewSource(0))

func main() {
	Msat.Set(400e3)
	Alpha.Set(1.)
	M.Set(0.1, 0, 0)
	U_anis.Set(1, 0, 0)
	Viscosity.Set(1e-3)
	Ku1.Set(1e4)
	Temp.Set(310.)
	//for lognormal radius OR diameter
	for i := 0; i < 500; i++ {
		r := lognormal(20, 0.33)

		Rc.Set(r)
		Rh.Set(r)
		AddParticle(float64(i)*1.e7, 0., 0.)
	}
	Save("geometry")

	B_ext = func(t float64) (float64, float64, float64) {
		return 0.025 * math.Sin(2*math.Pi*t*25e3), 0., 0. //f = 25 kHz, T = 40 µs
	}

	BrownianRotation = true
	MagDynamics = true
	Demag = false
	T.Set(0.)
	SetSolver("dopri")
	Dt.Set(5e-10) //Solve in steps of 5 ns
	Errortolerance = 1e-3
	Adaptivestep = false
	//Tablename = "d20_µ033_B25"
	Tableadd("B_ext")

	Output(1e-7) //100 datapoints per cycle
	Run(200e-6)  //run 5 cycles

}

//returns a lognormally distributed number, to be used as radius
func lognormal(mu, sigma float64) float64 {
	result := 0.
	for result == 0. {
		x := rng.Float64() * 20. * mu
		if x > 8 {
			if x < 200 {
				f_x := 1. / (math.Sqrt(2*math.Pi) * sigma * x) * math.Exp(-1./(2.*sigma*sigma)*math.Pow(math.Log(x/mu), 2.))
				if rng.Float64() < f_x {
					result = x * 1e-9 / 2.
				}
			}

		}

	}
	return result
}
