function [C, sigma] = dataset3Params(X, y, Xval, yval)
%EX6PARAMS returns your choice of C and sigma for Part 3 of the exercise
%where you select the optimal (C, sigma) learning parameters to use for SVM
%with RBF kernel
%   [C, sigma] = EX6PARAMS(X, y, Xval, yval) returns your choice of C and 
%   sigma. You should complete this function to return the optimal C and 
%   sigma based on a cross-validation set.
%

% You need to return the following variables correctly.
C = 1;
sigma = 0.1;

% ====================== YOUR CODE HERE ======================
% Instructions: Fill in this function to return the optimal C and sigma
%               learning parameters found using the cross validation set.
%               You can use svmPredict to predict the labels on the cross
%               validation set. For example, 
%                   predictions = svmPredict(model, Xval);
%               will return the predictions on the cross validation set.
%
%  Note: You can compute the prediction error using 
%        mean(double(predictions ~= yval))
%


% minVal = 1.0;
% C_set = [.01 .03 .1 .3 1 3 10 30];
% sigma_set = [.01 .03 .1 .3 1 3 10 30];

% for i=1:8
% 	C_cur = C_set(i);
% 	for j=1:8
% 		sigma_cur = sigma_set(j);
% 		model= svmTrain(X, y, C_cur, ...
% 			@(x1, x2) gaussianKernel(x1, x2, sigma_cur));
% 		predictions = svmPredict(model, Xval);
% 		err = mean(double(predictions ~= yval));
% 		fprintf('err = %.2f, minVal = %.2f\n', err, minVal);
% 		if err < minVal
% 			minVal = err;
% 			C = C_cur;
% 			sigma = sigma_cur;
% 		end
% 		fprintf('C = %.2f, sigma = %.2f\n', C, sigma);
% 	end
% end

% fprintf('C = %.2f, sigma = %.2f\n', C, sigma);




% =========================================================================

end
