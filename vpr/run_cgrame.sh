#set -e

GRAPH=(
    #nomem1
    sum
    mac
    simple
    simple2
    conv2
    two_loops1
    matrixmultiply
    accumulate
    two_loops2
    cap
    conv3
    mac2
    mults2
    mults1
)

M_PLACE=(
	"bounding_box" 
	#"net_timing_driven" 
	#"path_timing_driven"
)

for ((j=0; j < ${#M_PLACE[@]}; j++)) do
	echo "+ Place: ${M_PLACE[j]}"
	echo "bench, time, fifo, 1hop" > res_vpr.csv
	echo "" > results_vpr_time.csv
	for ((i=0; i < ${#GRAPH[@]}; i++)) do

		
		echo " - GRAPH: ${GRAPH[i]}"
		#PLACE="vpr/place/${GRAPH[i]}-${M_PLACE[j]}.out"
		BIN="./bin/vpr"
		PLACE="data/place/${GRAPH[i]}.place"
		ROUTE="data/route/${GRAPH[i]}.out"
		NET="data/net/${GRAPH[i]}.net"
		BLIF="data/blif/${GRAPH[i]}.blif"
		DOT="../bench/cgrame/${GRAPH[i]}.dot"
		RESULT="data/result/${GRAPH[i]}.out"
		GRID="data/grid/${GRAPH[i]}.grid"
		ARCH_vpr5="arch/k4-n1.xml"

		rm $RESULT
		rm $GRID

		python3 src/dot_to_net.py $DOT $NET

		#for ((k=0; k < 3; k++)) do
		#$BIN $NET $ARCH_vpr5 $PLACE $ROUTE -nodisp -place_algorithm ${M_PLACE[j]} -place_only > $RESULT
		$BIN $NET $ARCH_vpr5 $PLACE $ROUTE -nodisp -fast -place_only > $RESULT
		python3 src/create_list.py $PLACE $DOT

		python3 src/fifo.py $DOT $GRID >> res_vpr.csv

		#python3 vpr/src/create_grid_dac.py $PLACE $DOT >> res_vpr.csv
		python3 src/get_results.py ${GRAPH[i]} $RESULT >> results_vpr_time.csv
		#done
		#python3 vpr/src/get_time.py ${GRAPH[i]} results_vpr_time.csv >> time_${M_PLACE[j]}.csv
	done
done
