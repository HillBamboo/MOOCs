function J = computeCostMulti(X, y, theta)

m = length(y); % number of training examples
J = 0;
J = (X*theta - y)'*(X*theta - y)/(2*m);
end
