escalon.png : NV_graph.py advection.txt
	python3 NV_graph.py
advection.txt : step
	./step>advection.txt
step :NV_advection.cpp
	c++ NV_advection.cpp -o step

