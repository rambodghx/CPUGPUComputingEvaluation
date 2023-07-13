# CPU cores computing strength and GPU computing strength using Python
Repository Name: CPUGPUComputingEvaluation
## (1) Objective:
The objective of this project is to evaluate the CPU cores and GPU computing strengths in various scenarios using Python, considering different types of computational tasks.

## (2) Setup:
-> You must install CUDA
## (2.1) Cuda Installation:

https://developer.nvidia.com/cuda-downloads

## (2.2) OPENCV Cuda Build:

Download opencv source:

https://opencv.org/releases/

And then build via CMake with checked cuda flag:

https://cmake.org/

`pip install numpy`

`pip install cupy-cuda12x`

`pip install psutil`

`pip install gpustat`

`pip install opencv-python`
Ensure that your computer has a CPU with multiple cores and a dedicated GPU.
Install the necessary Python libraries for CPU and GPU computations, such as NumPy, TensorFlow, and PyTorch.
## (3) Scenarios:
### (3-1) Matrix Multiplication:
Write a Python function that performs matrix multiplication using CPU computation.
Utilize the NumPy library for efficient matrix operations.
Measure the execution time for matrix multiplication of various sizes using the time module or a performance profiling library.
Run the function multiple times and record the average execution time for each matrix size.
Repeat the same process for GPU computation using a GPU-accelerated library like TensorFlow or PyTorch.
Compare the average execution times between CPU and GPU for different matrix sizes.
### (3-2) Image Processing:

Write a Python function that performs image processing operations, such as image filtering or edge detection, using CPU computation.
Utilize libraries like OpenCV or PIL (Python Imaging Library) for image processing tasks.
Measure the execution time for image processing operations on various image sizes.
Repeat the process for GPU computation using GPU-accelerated libraries.
Compare the average execution times between CPU and GPU for different image sizes.

## (4)Comparative Analysis:

Analyze the performance differences between CPU and GPU in each scenario.
Consider factors such as the workload complexity, parallelization capabilities, and data sizes.
Identify scenarios where CPU outperforms GPU or vice versa.
Visualize the results using Python plotting libraries to present a clear comparison.
Conclusion:

Summarize the findings from the evaluation and analysis of different scenarios.
Discuss the strengths and limitations of CPU and GPU computing for each scenario.
Provide insights into the scenarios where each computing resource is more suitable based on performance considerations.
Remember to document your code, provide clear instructions, and make it easily reproducible for others to understand and replicate your project.


## (5) Expected Outputs:

Csv format file will be filled into `result.txt`.

Expected terminal output : 
`CPU Util : [CORE(0) 0.0%]       [CORE(1) 0.0%]  [CORE(2) 0.0%]  [CORE(3) 0.0%]  [CORE(4) 0.0%]  [CORE(5) 0.0%]  [CORE(6) 25.0%] [CORE(7) 0.0%]
CPU Temps :
NVIDIA GeForce GTX 1650 : 0Mb - 0% - 40C
Evaluating Scenario1...
0 of scenario 1...
1 of scenario 1...
2 of scenario 1...
3 of scenario 1...
4 of scenario 1...
Scenario 1 has been completed
PS C:\Users\Rambod Ghasemi\source\GitRepos\cpugpu\CPUGPUComputingEvaluation> py .\Evaluation.py
CPU Util : [CORE(0) 0.0%]       [CORE(1) 0.0%]  [CORE(2) 0.0%]  [CORE(3) 50.0%] [CORE(4) 0.0%]  [CORE(5) 25.0%] [CORE(6) 25.0%] [CORE(7) 0.0%]
CPU Temps :
NVIDIA GeForce GTX 1650 : 0Mb - 0% - 41C
Evaluating Scenario1...
0 of scenario 1...
1 of scenario 1...
2 of scenario 1...
3 of scenario 1...
4 of scenario 1...
Scenario 1 has been completed
Evaluating Scenario2...
0 of scenario 2...
1 of scenario 2...
2 of scenario 2...
3 of scenario 2...
4 of scenario 2...
Scenario 2 has been completed`
