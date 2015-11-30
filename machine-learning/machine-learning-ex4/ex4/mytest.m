%% mytest: function description
function [x] = mytest()
	x = 0;
	for i = 1:10
		% fprintf('%d\n', i);
		x = x + i;
	end
end