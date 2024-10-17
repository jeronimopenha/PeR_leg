import sys

if __name__ == "__main__":

    if len(sys.argv) > 2:
        name = sys.argv[1]
        csv = sys.argv[2]
    else:
        print("python3 get_time.py <name> <csv>\n")
        exit(0)
    
    data = open(csv, "r")

    time, mesh = [], []
    for line in data.readlines():
        if line != '':
            try:
                line = line.strip().split(",")
                mesh.append(float(line[1]))
                time.append(float(line[4]))
            except:
                continue
    mesh_avg = sum(mesh) / len(mesh)
    time_avg = sum(time) / len(time)

    mesh_dp, time_dp = 0, 0
    for i in range(len(mesh)):
        mesh_dp += (mesh[i]-mesh_avg)**2
        time_dp += (time[i]-time_avg)**2
    mesh_dp = (mesh_dp/len(mesh))**0.5
    time_dp = (time_dp/len(time))**0.5

    print("%s,%.2f,%.2f,%.2f,%.2f"%(name,mesh_avg,mesh_dp,time_avg,time_dp))
