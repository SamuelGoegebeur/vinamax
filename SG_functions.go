package vinamax

import (
	"math"
	"math/rand"
)

var rng2 = rand.New(rand.NewSource(0))

//returns a lognormally distributed number, to be used as radius
func Lognormal(mu, sigma float64) float64 {
	result := 0.
	for result == 0. {
		x := rng2.Float64() * 20. * mu
		f_x := 1. / (math.Sqrt(2*math.Pi) * sigma * x) * math.Exp(-1./(2.*sigma*sigma)*math.Pow(math.Log(x/mu), 2.))
		if rng2.Float64() < f_x {
			result = x * 1e-9 / 2.
		}
	}
	return result
}

func Detection_Square(y, z float64) {
	x_coord := Coil_Locations[0]
	y_coord := -y
	for i := 0; y_coord <= y; i++ {
		z_coord := -z
		for j := 0; z_coord <= z; j++ {
			Tableadd_b_at_location(x_coord, y_coord, z_coord)
			z_coord += 1.0e-10
			z_coord = math.Round(z_coord*1e11) / 1e11
		}
		//fmt.Print(y_coord, "\n")
		y_coord += 1.0e-10
		y_coord = math.Round(y_coord*1e11) / 1e11
	}
}



