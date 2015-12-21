clear ; close all; clc

load('ex6data3.mat');

% SVM Parameters
C_set = [.01 .03 .1 .3 1 3 10 30];
sigma_set = [.01 .03 .1 .3 1 3 10 30];

% We set the tolerance and max_passes lower here so that the code will run
% faster. However, in practice, you will want to run the training to
% convergence.
for i=1:8
	C = C_set(i);
	for j=1:8
		sigma = sigma_set(j);
		model= svmTrain(X, y, C, ...
			@(x1, x2) gaussianKernel(x1, x2, sigma)); 
		figure;
		visualizeBoundary(X, y, model);
		fprintf('C = %.2f, sigma = %.2f\n', C, sigma);
		% fprintf('Program paused. Press enter to continue.\n');
		% pause;
	end
end
