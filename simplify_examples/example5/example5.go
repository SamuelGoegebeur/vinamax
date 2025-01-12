package main

import (
	"fmt"
	. "vinamax"
)

func main() {
	kb := 1.3806488e-23
	Clear()
	Rc.Set(6e-9)
	Rh.Set(6e-9)
	Msat.Set(400e3)
	M.Set(0, 0, 1) //orientatie deeltjes in cube
	Alpha.Set(1.)
	Ku1.Set(1.e7)
	U_anis.Set(0, 0, 1)
	Dt.Set(1e-10)
	MaxDt.Set(5e-9)
	T.Set(0.) //tijd
	Viscosity.Set(1e-3)
	Adaptivestep = true //zoekt zelf beste Dt
	Temp.Set(300.)
	BrownianRotation = true
	Demag = false

	geom := Cube{S: 2e-2}
	geom.AddParticles(10000)
	MagDynamics = false

	SetSolver("dopri")
	Tableadd("U_anis")
	tauB := 3 * Viscosity.Get() / Temp.Get() / kb * Volume(Rh.Get())
	fmt.Println(tauB)
	Output(tauB / 3000.)
	Run(tauB * 3)

}
