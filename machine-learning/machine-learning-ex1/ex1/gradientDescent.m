function [theta, J_history] = gradientDescent(X, y, theta, alpha, num_iters)

m = length(y); % number of training examples
J_history = zeros(num_iters, 1);

for iter = 1:num_iters

    theta = theta - alpha * X' * (X*theta-y) / m;
    J_history(iter) = computeCost(X, y, theta);

    % d = X*theta-y;
    % theta = theta - theta*alpha*(d'*d)/m;

    % theta(1) = theta(1) - alpha * X(:,1)' * (X*theta-y) / m;
    % theta(2) = theta(2) - alpha * X(:,2)' * (X*theta-y) /m;
end

end
