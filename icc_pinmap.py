import sys, os

if len(sys.argv) != 2:
    print("fail!\n")
    sys.exit()

side              = "0"
metal_layer       = "0"
offset_incr_size  = 0 
offset            = 0 
net_name          = ""

new_tdf = open("pinmap.tdf", "w")
netlist = open(os.path.abspath(sys.argv[1]),"r").readlines()

for line in netlist:
    if "side"   in line :
        line_side        = line.split(",")
        side             = line_side[1].replace("\n","")
    if "metal"  in line :
        line_layer       = line.split(",")
        metal_layer      = "M"+line_layer[1].replace("\n","")
    if "offset_start" in line :
        line_offset      = line.split(",")
        offset           = int(line_offset[1])
    if "offset_incr"  in line :
        line_offset      = line.split(",")
        offset_incr_size = int(line_offset[1])
    if "net"    in line :
        line_netname     = line.split(",")
        net_name         = line_netname[1].replace("\n","")
        basic_instruction = "set_pin_physical_constraints " \
                        + " -pin_name {" + net_name  + "}" \
                        + " -layers {"     + metal_layer + "}" \
                        + " -width 0.05 -depth 0.05" \
                        + " -side "   + side + " -offset " + str(offset)+"\n"

        new_tdf.writelines(basic_instruction)
        offset           = offset + offset_incr_size
    if "end"    in line :
        side              = "0"
        metal_layer       = "0"
        offset_incr_size  = 0 
        offset            = 0 
        net_name          = ""


new_tdf.close()