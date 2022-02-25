package main

import (
	//"bufio"
	"fmt"
	//"log"
	//"os"
	//"strings"
	//"strconv"
	"math"
	. "vinamax"
)

func main() {
	Simulation()

}

func Simulation() {

	Setorientrandomseed(0)
	Setgeorandomseed(0)
	Setrandomseed(0)

	kb := 1.3806488e-23
	Clear()
	Rc.Set(60.0e-9)
	Rh.Set(60.0e-9)
	Msat.Set(400e3)
	M.Set(0, 1, 0)
	Alpha.Set(1.)
	Ku1.Set(0.)
	U_anis.Set(0, 1, 0)
	//MaxDt.Set(5e-9)
	T.Set(0.)
	// An external field is applied that is a sine along the x-axis with amplitude 25 mT and frequency 25 kHz
	B_ext = func(t float64) (float64, float64, float64) { return 0.0025 * math.Sin(2*math.Pi*t*25.0e3), 0., 0. }
	Viscosity.Set(1e-3)
	Adaptivestep = false
	Temp.Set(300.)

	BrownianRotation = false
	Demag = false
	MagDynamics = true

	AddParticle(0., 1.0e-4, 0.)

	//geom := Cilinder{Radius: 0.5e-2, Height: 2.0e-2}
	//geom.Setorigin(0.0,1.0e-4,0.0)
	//geom.AddParticles_randor(100)

	//Tableadd("U_anis")
	Tableadd_b_at_location(0., 0., 0.)
	Tableadd("B_ext")

	tauB := 3 * Viscosity.Get() * Volume(Rh.Get()) / (Temp.Get() * kb)
	fmt.Println(tauB)

	Output(1e-6)
	Dt.Set(1e-8)
	SetSolver("dopri")
	T.Set(0.)

	Run(1e1)

}
