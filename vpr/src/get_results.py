import sys, os.path

if __name__ == "__main__":
    
    if len(sys.argv) > 2:
        name = sys.argv[1]
        info = sys.argv[2]
    else:
        print("python3 get_results.py <name> <info>\n")
        exit(0)
    
    info = open(info, "r")
    
    time=bb_cost=bb_scratch=t_routing_area=t_logic_tile=t_logic_area=cp=routed_nets=t_wirelength=avg_net_legth=max_net_length=wire_mesh=wire_1hop="0"
    
    for line in info:
        if line:
            line = line.strip()
            if "Time elapsed (PLACE&ROUTE)" in line: 
                time = line.replace("Time elapsed (PLACE&ROUTE): ","").replace(" ms","")
                #print(time)
            elif "BB estimate of min-dist (placement) wirelength is ;" in line:
                bb_cost = line.replace("BB estimate of min-dist (placement) wirelength is ;","")
                #print(bb_cost)
            elif "bb_cost recomputed from scratch is" in line:
                bb_scratch = line.replace("bb_cost recomputed from scratch is ","")[:-1]
                #print(bb_scratch)
            elif "Total Routing Area:" in line:
                t_routing_area = line.replace("Total Routing Area: ","").split(".")[0]
                #print(t_routing_area)
                t_logic_tile = line.split("Per logic tile: ")[1]
                #print(t_logic_tile)
            elif "Total Logic Area:" in line:
                t_logic_area = line.replace("Total Logic Area: ", "").split(" ")[0]
                #print(t_logic_area)
            elif "Critical Path:" in line:
                cp = line.replace("Critical Path: ", "").replace(" (s)","")
                #print(cp)
            elif "The number of routed nets (nonglobal):" in line:
                routed_nets = line.replace("The number of routed nets (nonglobal): ", "")
                #print(routed_nets)
            elif "Total wirelength:" in line:
                t_wirelength = line.replace("Total wirelength: ", "").split(" ")[0]
                #print(t_wirelength)
                avg_net_legth = line.split("Average net length: ")[1]
                #print(avg_net_legth)
            elif "Maximum net length:" in line:
                max_net_length = line.replace("Maximum net length: ","")
                #print(max_net_length)
            elif "wire mesh: " in line:
                wire_mesh = line.replace("wire mesh: ", "")
                #print(wire_mesh)
            elif "wire 1-hop: " in line:
                wire_1hop = line.replace("wire 1-hop: ", "")
                #print(wire_1hop)
    #print("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" %(name,bb_cost,bb_scratch,t_routing_area,t_logic_tile,t_logic_area,cp,routed_nets,t_wirelength,avg_net_legth,max_net_length,time,wire_mesh, wire_1hop))
    print("%s,%s,%s,%s,%s" %(name,wire_mesh,cp,avg_net_legth,time))
