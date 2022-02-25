package vinamax

import (
	"fmt"
	"log"
	"math"
)

//adds a quantity to the output table
func Tableadd(a string) {
	switch a {
	case "B_ext":
		{
			b := output_B_ext{}
			outputList = append(outputList, &b)
		}
	case "B_ext_space":
		{
			b := output_B_ext_space{}
			outputList = append(outputList, &b)
		}
	case "Dt":
		{
			b := output_Dt{}
			outputList = append(outputList, &b)
		}
	case "NrMzPos":
		{
			b := output_NrMzPos{}
			outputList = append(outputList, &b)
		}
	case "AllMag":
		{
			b := output_AllMag{}
			outputList = append(outputList, &b)
		}
	case "AllB_Eff":
		{
			b := output_AllB_Eff{}
			outputList = append(outputList, &b)
		}
	case "AllB_Therm":
		{
			b := output_AllB_Therm{}
			outputList = append(outputList, &b)
		}
	case "AllM_Cross_B_Eff2":
		{
			b := output_AllM_Cross_B_eff2{}
			outputList = append(outputList, &b)
		}

	case "U_anis":
		{
			b := output_U_anis{}
			outputList = append(outputList, &b)
		}
	case "Energy":
		{
			b := output_Energy{}
			outputList = append(outputList, &b)
		}
	case "Heat":
		{
			b := output_Heat{}
			outputList = append(outputList, &b)
		}
	case "Detectorsignal":
		{
			b := output_Signal_detector{}
			outputList = append(outputList, &b)
		}
	case "FFP":
		{
			b := output_FFP{}
			outputList = append(outputList, &b)

		}
	default:
		{
			log.Fatal(a, " is currently not addable to table")
		}
	}
}

//OutputQuantity B_ext
type output_B_ext struct {
}

func (o output_B_ext) header() string {
	return "\tB_ext_x\tB_ext_y\tB_ext_z"
}

func (o output_B_ext) value() string {
	B_ext_x, B_ext_y, B_ext_z := B_ext(T.value)
	return fmt.Sprintf("\t%v\t%v\t%v", B_ext_x, B_ext_y, B_ext_z)
}

//OutputQuantity B_ext_space
type output_B_ext_space struct {
}

func (o output_B_ext_space) header() string {
	l := [3]float64{-X_scan, 0., X_scan}
	names := ""
	for i := 0; i < 3; i++ {
		names += fmt.Sprintf("\tB_ext_space_x_%v\tB_ext_space_y_%v\tB_ext_space_z_%v", l[i], l[i], l[i])
	}

	return names

}

func (o output_B_ext_space) value() string {
	l := [3]float64{-X_scan, 0., X_scan}
	values := ""
	for i := 0; i < 3; i++ {
		B_ext_space_x, B_ext_space_y, B_ext_space_z := B_ext_space(T.value, l[i], 0., 0.)
		values += fmt.Sprintf("\t%v\t%v\t%v", B_ext_space_x, B_ext_space_y, B_ext_space_z)
	}

	return values
}

//OutputQuantity Dt
type output_Dt struct {
}

func (o output_Dt) header() string {
	return "\tDt"
}
func (o output_Dt) value() string {
	return fmt.Sprintf("\t%v", Dt.value)
}

//OutputQuantity NrMzPos
type output_NrMzPos struct {
}

func (o output_NrMzPos) header() string {
	return "\tnrmzpos"
}

func (o output_NrMzPos) value() string {
	return fmt.Sprintf("\t%v", nrmzpositive())
}

//OutputQuantity AllMag
type output_AllMag struct {
}

func (o output_AllMag) header() string {
	header := ""
	for range lijst {
		header += fmt.Sprintf("\tm_x\tm_y\tm_z")
	}
	return header
}

func (o output_AllMag) value() string {
	string := ""
	for _, i := range lijst {
		string += fmt.Sprintf("\t%v\t%v\t%v", i.m[0], i.m[1], i.m[2])
	}
	return string
}

//OutputQuantity AllB_Eff
type output_AllB_Eff struct {
}

func (o output_AllB_Eff) header() string {
	header := ""
	for range lijst {
		header += fmt.Sprintf("\tB_Eff_x\tB_Eff_y\tB_eff_z")
	}
	return header
}

func (o output_AllB_Eff) value() string {
	string := ""
	for _, i := range lijst {
		string += fmt.Sprintf("\t%v\t%v\t%v", i.heff[0], i.heff[1], i.heff[2])
	}
	return string
}

//OutputQuantity AllB_therm
type output_AllB_Therm struct {
}

func (o output_AllB_Therm) header() string {
	header := ""
	for range lijst {
		header += fmt.Sprintf("\tB_Therm_x\tB_Therm_y\tB_Therm_z")
	}
	return header
}

func (o output_AllB_Therm) value() string {
	string := ""
	for _, i := range lijst {
		string += fmt.Sprintf("\t%v\t%v\t%v", i.thermField[0], i.thermField[1], i.thermField[2])
	}
	return string
}

//OutputQuantity AllM_Cross_B_eff2
type output_AllM_Cross_B_eff2 struct {
}

func (o output_AllM_Cross_B_eff2) header() string {
	header := ""
	for range lijst {
		header += fmt.Sprintf("\tM_Cross_B_eff2")
	}
	return header
}

func (o output_AllM_Cross_B_eff2) value() string {
	string := ""
	for _, i := range lijst {
		string += fmt.Sprintf("\t%v", i.m.cross(i.heff).dot(i.m.cross(i.heff)))
	}
	return string
}

//OutputQuantity U_anis
type output_U_anis struct {
}

func (o output_U_anis) header() string {
	return "\tu_x\tu_y\tu_z"
}

func (o output_U_anis) value() string {
	averaged_u := averages_u()
	return fmt.Sprintf("\t%v\t%v\t%v", averaged_u[0], averaged_u[1], averaged_u[2])
}

//OutputQuantity Energy
type output_Energy struct {
}

func (o output_Energy) header() string {
	return "\tE_zeeman\tE_demag\tE_anis\tE_therm\tE_total"
}

func (o output_Energy) value() string {
	return fmt.Sprintf("\t%v\t%v\t%v\t%v\t%v", E_zeeman(), E_demag(), E_anis(), E_therm(), E_total())
}

//OutputQuantity Heat
type output_Heat struct {
}

func (o output_Heat) header() string {
	header := ""
	for range lijst {
		header += fmt.Sprintf("\tHeat")
	}
	return header
}

func (o output_Heat) value() string {
	string := ""
	for _, i := range lijst {
		string += fmt.Sprintf("\t%v", i.heat)
	}
	return string
}

//OutputQuantity Signal in detector 6ch (SQUID 1)
type output_Signal_detector struct {
}

func (o output_Signal_detector) header() string {
	return "\tB_field_detector"
}

func (o output_Signal_detector) value() string {
	B_detector := 0.
	detectorcount := 0

	//loop over detector
	//for coil in Coil_location
	x_coord := Coil_Locations[0]
	y_coord := -7.5e-3
	for i := 0; y_coord <= 7.5e-3; i++ {
		z_coord := -7.5e-3
		for j := 0; z_coord <= 7.5e-3; j++ {
			//Bereken magnetic flux in detectorpoint: B_scalar
			B_detectorpoint_x, B_detectorpoint_y, B_detectorpoint_z := B_ext_space(T.value, x_coord, y_coord, z_coord) //magnetic induction
			//Flux_at_point(x_coord,y_coord,z_coord) flux vector at points
			B_scalar := B_detectorpoint_x + 0*(B_detectorpoint_y+B_detectorpoint_z) //flux at points in direction detector

			B_detector += B_scalar
			detectorcount += 1

			z_coord += 1.0e-3
			z_coord = math.Round(z_coord*10000) / 10000
		}
		y_coord += 1.0e-3
		y_coord = math.Round(y_coord*10000) / 10000
	}
	B_detector = B_detector / float64(detectorcount)
	return fmt.Sprintf("\t%v", B_detector)
}

//OutputQuantity FFP
type output_FFP struct {
}

func (o output_FFP) header() string {
	return "\tFFP_x"
}

func (o output_FFP) value() string {
	ffp :=  A/G*math.Cos(2*math.Pi*T.value*25e3)
	return fmt.Sprintf("\t%v", ffp)

}
