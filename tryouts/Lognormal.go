package main

import (
	"math"
	"math/rand"
	. "vinamax"
)

var rng = rand.New(rand.NewSource(0))

func main() {
	Msat.Set(500e3)
	Alpha.Set(1.)
	M.Set(0.1, 1, 0)
	U_anis.Set(0, 1, 0)
	Viscosity.Set(1e-3)
	Ku1.Set(1e4)
	Temp.Set(310.)
	//for lognormal radius OR diameter
	for i := 0; i < 10; i++ {
		r := lognormal(50, 0.63)

		Rc.Set(r)
		Rh.Set(r)
		AddParticle(float64(i)*1.e7, 0., 0.)
	}

	//var f float64 = 25e3
	//var T float64 = 1 / f
	//var ppc int = 100
	//var cycles int = 10

	B_ext = func(t float64) (float64, float64, float64) {
		return 0.025 * math.Sin(2*math.Pi*t*25e3), 0., 0. //f = 25 kHz, T = 40 µs
	}

	BrownianRotation = true
	MagDynamics = true
	Demag = false
	T.Set(0.)
	SetSolver("dopri")
	Dt.Set(5e-9) //Solve in steps of 5 ns
	Adaptivestep = true
	Tableadd("B_ext")

	Output(1e-7) //100 datapoints per cycle
	Run(400e-6)  //run 125 cycles

}

//returns a lognormally distributed number, to be used as radius
func lognormal(mu, sigma float64) float64 {
	result := 0.
	for result == 0. {
		x := rng.Float64() * 20. * mu
		f_x := 1. / (math.Sqrt(2*math.Pi) * sigma * x) * math.Exp(-1./(2.*sigma*sigma)*math.Pow(math.Log(x/mu), 2.))
		if rng.Float64() < f_x {
			result = x * 1e-9 / 2.
			//fmt.Println(result)
		}
	}
	return result
}
