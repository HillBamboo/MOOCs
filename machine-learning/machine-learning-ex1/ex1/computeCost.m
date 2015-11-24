function J = computeCost(X, y, theta)

m = length(y); 
J = 0;
J = (X*theta - y)'*(X*theta - y)/(2*m);

end
